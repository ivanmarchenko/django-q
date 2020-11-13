import json
from django.http import JsonResponse
from django.shortcuts import render
from django_q.tasks import async_task, result_group, Chain
from .services import sleep_and_print


# def testredisview(request):
#     # async_task(sleep_and_print, 1, hook='djangoq.hooks.print_result')
#     context = {}
#     for i in range(4):
#         async_task('math.modf', i, group='modf')
#         # wait until the group has 4 results
#         result = result_group('modf', count=4)
#         print(result)
#     return render(request, 'index.html', context)

def testredisview(request):
    json_payload = {"message": "hello world!"}
    # async_task('async_test.func.sleep_and_print', 10)
    # for i in range(4):
    # async_task(sleep_and_print, i, group='xxx', hook='djangoq.hooks.print_result')
    chain = Chain(group='chain')
    chain.append(sleep_and_print, 5)
    chain.append(sleep_and_print, 4)
    chain.append(sleep_and_print, 3)
    chain.run()
    return JsonResponse(json_payload)


# from django.shortcuts import render
# from django.http import JsonResponse
# from time import sleep
# from django_q.tasks import async_task, result
# from .services import sleep_and_print

# def index(request):
    
#     # async_task('async_test.func.sleep_and_print', 10)
#     # task_id = async_task(sleep_and_print, 10)
#     # task_result = result(task_id, 20)
#     context = {
#         'message': 'Hello world!',
#         # 'task_id': task_id,
#         # 'task_result': task_result,
#     }
#     async_task (sleep_and_print, 3, hook='hooks.print_result')
#     return render(request, 'index.html', context)
