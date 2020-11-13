
def print_result(task):
    print((task.id, task.result))
    print()
    print(task.attempt_count)
    print()
    print(task.get_result(task.id))
    return True


# def print_result(task):
#     print(task.id, task.result)
#     return True