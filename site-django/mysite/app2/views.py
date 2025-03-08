from django.shortcuts import render

def about(request):
    return render(request, 'app2/about.html')

