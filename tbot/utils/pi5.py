import subprocess


def get_metrics_pi5():
    def cpu_temp():
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        return result.stdout.strip().replace('temp=', '')

    return str(f"""
    CPU: {cpu_temp()}
    """)



