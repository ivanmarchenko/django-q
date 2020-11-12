from django.shortcuts import render
from django.http import JsonResponse
from time import sleep
from django_q.tasks import async_task

def index(request):
    json_context = {
        'message': 'Hello world!'
    }
    async_task('async_test.func.sleep_and_print', 10)
    return JsonResponse(json_context)