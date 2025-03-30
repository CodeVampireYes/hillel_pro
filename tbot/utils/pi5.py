import subprocess
import psutil
import os


def get_metrics_pi5():
    def cpu_temp():
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        return result.stdout.strip().replace('temp=', '').replace("'C", "")

    def cpu_usage():
        return psutil.cpu_percent(interval=1)

    def ram_usage():
        mem = psutil.virtual_memory()
        return mem.used / (1024 ** 2)

    def ssd_temp():
        result = subprocess.run(['sudo', 'nvme', 'smart-log', '/dev/nvme0', '|', 'grep temperature'], capture_output=True, text=True)
        for line in result.stdout.split("\n"):
            if "temperature" in line.lower() and "sensor" not in line:  # Ищем общую температуру, без сенсоров
                temp_value = line.split(":")[1].strip().split("°")[0]  # Извлекаем число
                return int(temp_value)

    def ssd_usage(mount_point="/mnt/ssd2"):
        if os.path.ismount(mount_point):  # Проверяем, смонтирован ли SSD
            usage = psutil.disk_usage(mount_point)
            return usage.percent
        else:
            return "SSD не подключен"

    return str(f"""
    🤖 CPU: {cpu_temp()}°C | {cpu_usage()}%
    ⚡ RAM: {ram_usage():.2f} MB
    💾 SSD: {ssd_temp()}°C | {ssd_usage()}%
    """)



