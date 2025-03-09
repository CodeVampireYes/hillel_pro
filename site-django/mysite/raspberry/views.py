from django.shortcuts import render

from app1.models import SystemMetrics  # Правильный путь
from app1.models import Users


def raspberry(request):
    db_users = Users.objects.all()
    db_system_metrics = SystemMetrics.objects.all()

    my_id = []
    cpu_usage = []
    memory_usage = []
    disk_usage = []
    running_processes = []
    temperature = []
    timestamp = []

    for item in db_system_metrics:
        my_id.append(item.id)
        cpu_usage.append(item.cpu_usage)
        memory_usage.append(item.memory_usage)
        disk_usage.append(item.disk_usage)
        running_processes.append(item.running_processes)
        temperature.append(item.temperature)
        timestamp.append(item.timestamp)



    return render(request, 'raspberry/raspberry.html', {"my_id": my_id[0],
                                                        'cpu_usage': cpu_usage[0],
                                                        'memory_usage': memory_usage[0],
                                                        'disk_usage': disk_usage[0],
                                                        'running_processes': running_processes[0],
                                                        'temperature': temperature[0],
                                                        'timestamp': timestamp[0] })
