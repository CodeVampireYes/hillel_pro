import psutil
import subprocess

def get_rpi_metrics():
    """Получение метрик Raspberry Pi"""

    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # GPU temperature
    try:
        gpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True).decode().strip()
        gpu_temp = float(gpu_temp.replace("temp=", "").replace("'C", ""))
    except Exception:
        gpu_temp = 0.0  # Если ошибка, ставим 0

    # Memory usage
    memory_usage = psutil.virtual_memory().percent

    # CPU temperature
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            cpu_temp = int(f.read().strip()) / 1000.0
    except FileNotFoundError:
        cpu_temp = gpu_temp  # Используем GPU temp, если нет доступа

    # Disk usage
    disk_usage = psutil.disk_usage('/').percent

    # Number of running processes
    processes = len(psutil.pids())

    return {
        "cpu_usage": cpu_usage,
        "gpu_usage": 0.0,  # GPU usage измерить сложно
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "temperature": cpu_temp,
        "running_processes": processes
    }

# Проверка работы
if __name__ == "__main__":
    metrics = get_rpi_metrics()
    for key, value in metrics.items():
        print(f"{key}: {value}")
