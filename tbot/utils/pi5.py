import subprocess
import psutil

def get_metrics_pi5():
    def cpu_temp():
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        return result.stdout.strip().replace('temp=', '').replace("'C", "")

    def cpu_usage():
        return psutil.cpu_percent(interval=1)

    def ram_usage():
        mem = psutil.virtual_memory()
        return mem.used / (1024 ** 2)

    return str(f"""
    CPU: {cpu_temp()}°C | {cpu_usage()}%
    """)



