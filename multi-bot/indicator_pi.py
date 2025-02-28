import psutil
import subprocess

def get_rpi_metrics():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # GPU usage (нет прямого способа, но можно использовать vcgencmd для проверки температуры GPU)
    gpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True).decode("utf-8")
    gpu_temp = float(gpu_temp.replace("temp=", "").replace("'C\n", ""))

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

    return {
        "cpu_usage": cpu_usage,
        "gpu_usage": 0.0,  # GPU usage сложно измерить, ставим 0
        "memory_usage": memory_usage,
        "temperature": cpu_temp
    }

