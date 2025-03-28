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
        return result.stdout.strip().replace("""CompletedProcess(args=['sudo', 'nvme', 'smart-log', '/dev/nvme0', '|',
         'grep temperature'], returncode=0, stdout='Smart Log for NVME device:nvme0 
         namespace-id:ffffffff\ncritical_warning\t\t\t: 0\ntemperature\t\t\t\t: 33°C (306 Kelvin)\navailable_spare\t\t\t\t:
          100%\navailable_spare_threshold\t\t: 10%\npercentage_used\t\t\t\t: 0%\nendurance group critical warning
           summary: 0\nData Units Read\t\t\t\t: 44,083 (22.57 GB)\nData Units Written\t\t\t:
            593,883 (304.07 GB)\nhost_read_commands\t\t\t: 433,287\nhost_write_commands\t\t\t:
             1,859,791\ncontroller_busy_time\t\t\t: 13\npower_cycles\t\t\t\t: 67\npower_on_hours\t\t\t\t:
              3\nunsafe_shutdowns\t\t\t: 44\nmedia_errors\t\t\t\t: 0\nnum_err_log_entries\t\t\t: 0\nWarning Temperature
               Time\t\t: 0\nCritical Composite Temperature Time\t: 0\n""", '')

    return str(f"""
    CPU: {cpu_temp()}°C | {cpu_usage()}%
    RAM: {ram_usage():.2f} MB
    SSD: {ssd_temp()}
    """)



