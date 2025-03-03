import psutil
import subprocess
import asyncio

async def get_rpi_metrics():
    """Получение метрик Raspberry Pi (асинхронно)"""

    # Получаем данные асинхронно
    cpu_usage = await asyncio.to_thread(psutil.cpu_percent, interval=1)
    memory_usage = await asyncio.to_thread(lambda: psutil.virtual_memory().percent)
    disk_usage = await asyncio.to_thread(lambda: psutil.disk_usage('/').percent)
    running_processes = await asyncio.to_thread(lambda: len(psutil.pids()))

    # GPU температура (vcgencmd)
    gpu_temp = 0.0
    try:
        output = await asyncio.to_thread(subprocess.check_output, "vcgencmd measure_temp", shell=True)
        gpu_temp = float(output.decode().strip().replace("temp=", "").replace("'C", ""))
    except Exception:
        pass  # Если ошибка — оставляем 0.0

    # CPU температура
    cpu_temp = gpu_temp
    try:
        temp_raw = await asyncio.to_thread(lambda: open("/sys/class/thermal/thermal_zone0/temp", "r").read().strip())
        cpu_temp = int(temp_raw) / 1000.0
    except (FileNotFoundError, ValueError):
        pass  # Если ошибка — оставляем GPU temp

    return {
        "cpu_usage": cpu_usage,
        "gpu_usage": 0.0,  # GPU usage измерить сложно
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "running_processes": running_processes,
        "temperature": cpu_temp
    }
