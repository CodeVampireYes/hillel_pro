import psutil
import subprocess
import asyncio
from database import db

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
    except Exception as e:
        print(f"Ошибка при получении температуры GPU: {e}")
        pass  # Если ошибка — оставляем 0.0

    # CPU температура
    cpu_temp = gpu_temp
    try:
        temp_raw = await asyncio.to_thread(lambda: open("/sys/class/thermal/thermal_zone0/temp", "r").read().strip())
        cpu_temp = int(temp_raw) / 1000.0
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка при получении температуры CPU: {e}")
        pass  # Если ошибка — оставляем GPU temp

    # Обновляем данные в базе данных (используем UPDATE, чтобы обновить последние метрики)
    async with db.pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("""
                UPDATE system_metrics
                SET cpu_usage = %s, memory_usage = %s, disk_usage = %s, 
                    running_processes = %s, temperature = %s, timestamp = NOW()
                WHERE id = 1  -- Обновляем строку с id = 1 (или используйте свой идентификатор)
            """, (cpu_usage, memory_usage, disk_usage, running_processes, cpu_temp))
            await conn.commit()

    # Возвращаем собранные метрики
    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "running_processes": running_processes,
        "temperature": cpu_temp
    }

async def periodic_task():
    while True:
        # Вызываем функцию для получения метрик
        metrics = await get_rpi_metrics()

        # Логируем или выводим метрики
        print(f"Метрики Raspberry Pi: {metrics}")

        # Задержка в 20 секунд перед следующим запуском
        await asyncio.sleep(20)  # Задержка 20 секунд между выполнениями

