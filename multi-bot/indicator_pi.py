import psutil
import subprocess
import asyncio

async def get_rpi_metrics():
    """Получение метрик Raspberry Pi асинхронно"""

    # CPU usage (вызываем в отдельном потоке, чтобы не блокировать asyncio)
    cpu_usage = await asyncio.to_thread(psutil.cpu_percent, interval=1)

    # GPU temperature
    gpu_temp = 0.0  # Значение по умолчанию
    try:
        output = await asyncio.to_thread(subprocess.check_output, "vcgencmd measure_temp", shell=True)
        gpu_temp = float(output.decode().strip().replace("temp=", "").replace("'C", ""))
    except Exception:
        pass  # Оставляем gpu_temp равным 0.0 при ошибке

    # Memory usage
    memory_usage = psutil.virtual_memory().percent

    # Disk usage
    disk_usage = psutil.disk_usage('/').percent

    # Running processes
    running_processes = len(psutil.pids())

    # CPU temperature (если не удалось взять CPU temp, используем GPU temp)
    cpu_temp = gpu_temp
    try:
        async with asyncio.to_thread(open, "/sys/class/thermal/thermal_zone0/temp", "r") as f:
            cpu_temp = int(await asyncio.to_thread(f.read)) / 1000.0
    except (FileNotFoundError, ValueError):
        pass  # Оставляем значение из GPU temp

    return {
        "cpu_usage": cpu_usage,
        "gpu_usage": 0.0,  # GPU usage измерить сложно
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "running_processes": running_processes,
        "temperature": cpu_temp
    }
