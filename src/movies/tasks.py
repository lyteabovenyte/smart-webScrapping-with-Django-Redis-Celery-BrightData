from celery import shared_task
import random

# do not use django model instances
# as function arguments
# it should be json-ready arguments
@shared_task
def add(x, y):
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # celery will recognize this as 'multiply_two_numbers'
    return x * (y * random.randint(3, 100))

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)