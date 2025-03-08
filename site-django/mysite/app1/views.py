from django.shortcuts import render
from .models import SystemMetrics
from .models import Users


def home(request):
    db_users = Users.objects.all()
    db_system_metrics = SystemMetrics.objects.all()
    return render(request, 'app1/home.html', {'db_users': db_users,
                                                                "db_system_metrics": db_system_metrics})
