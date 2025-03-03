import psutil
import subprocess
import shlex
from database import db


async def get_rpi_metrics():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # GPU temperature (Raspberry Pi)
    try:
        gpu_temp_output = subprocess.check_output(shlex.split("vcgencmd measure_temp")).decode("utf-8")
        gpu_temp = float(gpu_temp_output.replace("temp=", "").replace("'C\n", ""))
    except Exception:
        gpu_temp = None  # Если команда не выполняется, установим значение в None

    # Memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # CPU temperature
    cpu_temp = None
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            cpu_temp = int(f.read().strip()) / 1000.0  # Преобразование в градусы Цельсия
    except FileNotFoundError:
        cpu_temp = gpu_temp  # Если нет доступа к файлу, используем GPU temp

    # Запись в базу данных
    async with db.pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                """
                INSERT INTO metrics (cpu_usage, gpu_temp, memory_usage, temperature, timestamp)
                VALUES (%s, %s, %s, %s, NOW())
                """,
                (cpu_usage, gpu_temp, memory_usage, cpu_temp)
            )
            await conn.commit()  # Сохраняем изменения

    return {
        "cpu_usage": cpu_usage,
        "gpu_usage": None,  # GPU usage сложно измерить, поэтому убрал 0.0
        "memory_usage": memory_usage,
        "temperature": cpu_temp
    }
