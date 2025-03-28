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

    def ssd_temp():
        result = subprocess.run(['sudo', 'nvme', 'smart-log', '/dev/nvme0', '|', 'grep temperature'], capture_output=True, text=True)
        return result.stdout.strip().replace("""Smart Log for NVME device:nvme0 namespace-id:ffffffff
                                                        critical_warning   : 0
                                                        temperature    : 34°C (307 Kelvin)
                                                        available_spare    : 100%
                                                        available_spare_threshold  : 10%
                                                        percentage_used    : 0%
                                                        endurance group critical warning summary: 0
                                                        Data Units Read    : 44,083 (22.57 GB)
                                                        Data Units Written   : 593,884 (304.07 GB)
                                                        host_read_commands   : 433,287
                                                        host_write_commands   : 1,859,842
                                                        controller_busy_time   : 13
                                                        power_cycles    : 67
                                                        power_on_hours    : 3
                                                        unsafe_shutdowns   : 44
                                                        media_errors    : 0
                                                        num_err_log_entries   : 0
                                                        Warning Temperature Time  : 0
                                                        Critical Composite Temperature Time : 0""", '')

    return str(f"""
    CPU: {cpu_temp()}°C | {cpu_usage()}%
    RAM: {ram_usage():.2f} MB
    SSD: {ssd_temp()}
    """)



