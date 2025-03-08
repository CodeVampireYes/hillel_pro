from django.db import models


class SystemMetrics(models.Model):
    id = models.AutoField(primary_key=True)  # Добавляем первичный ключ
    cpu_usage = models.FloatField(blank=True, null=True)
    memory_usage = models.FloatField(blank=True, null=True)
    disk_usage = models.FloatField(blank=True, null=True)
    running_processes = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)  # Время создания записи

    class Meta:
        db_table = 'system_metrics'  # Название таблицы


class Users(models.Model):
    user_id = models.BigIntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=255)
    discord_on = models.IntegerField()  # Оставляем как IntegerField
    discord_link = models.CharField(max_length=512, blank=True, null=True)
    list_weekend = models.IntegerField()  # Оставляем как IntegerField

    class Meta:
        db_table = 'users'  # Название таблицы

