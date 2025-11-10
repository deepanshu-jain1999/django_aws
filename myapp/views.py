from django.shortcuts import render
from django.http import JsonResponse
import socket
import os


def home(request):
    """Simple homepage view"""
    context = {
        'title': 'Django CI/CD Demo',
        'message': 'Welcome to your containerized Django app!',
        'hostname': socket.gethostname(),
        'environment': os.environ.get('ENVIRONMENT', 'development')
    }
    return render(request, 'home.html', context)


def health_check(request):
    """Health check endpoint for monitoring"""
    return JsonResponse({
        'status': 'healthy',
        'hostname': socket.gethostname()
    })
