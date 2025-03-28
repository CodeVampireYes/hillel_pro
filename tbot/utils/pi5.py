import subprocess


async def cpu_temp():
    result = subprocess.run(['vcgencmd', 'measure_temp'])
    print(result)


