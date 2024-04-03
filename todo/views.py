from django.shortcuts import render, redirect
from .models import Task

def home(request):
    """
    Home view.

    It renders the index.html template with all tasks and
    the current URL as a parameter.
    """
    tasks = Task.objects.all()

    return render(request, 'index.html', {
        'tasks': tasks,
        'current_url': 'home',
    })


def completed(request):
    """
    Completed view.

    It renders the completed.html template with all completed tasks and
    the current URL as a parameter.
    """
    completed_tasks = Task.objects.filter(completed=True)

    return render(request, 'completed.html', {
        'tasks': completed_tasks,
        'current_url': 'completed',
    })


def remaining(request):
    """
    Remaining view.

    It renders the remaining.html template with all remaining tasks and
    the current URL as a parameter.
    """
    remaining_tasks = Task.objects.filter(completed=False)

    return render(request, 'remaining.html', {
        'tasks': remaining_tasks,
        'current_url': 'remaining',
    })


def add_task(request):
    """
    Add task view.

    It renders the add_task.html template with the current URL as a parameter
    if the request method is GET.

    If the request method is POST, it creates a new task with the given
    title, description, due date and due time and redirects to the home
    view with the current URL as a parameter.
    """
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        completed = False

        # Check if all fields have been filled
        if title != "" and due_date != "" and due_time != "":
            task = Task(
                title=title,
                description=description,
                due_date=due_date,
                due_time=due_time,
                completed=completed
            )
            task.save()
            return redirect('home')
    else:
        return render(request, 'add_task.html', {
            'current_url': 'add_task'
        })

    # If the request method is not POST, render the add_task.html template
    # with the current URL as a parameter.
    return render(request, 'add_task.html', {
        'current_url': 'add_task'
    })


def delete_task(request, task_id):
    """
    Delete task view.

    It renders the delete.html template with the task to delete as a parameter.
    """
    task = Task.objects.get(id=task_id)
    return render(request, 'delete.html', {
        "task": task,
        'current_url': 'delete_task',
    })


def task_detail(request, task_id):
    """
    View to render the task_detail.html template with the task to display as a parameter.

    The function receives the task id as a parameter and retrieves the task
    object from the database using the Django ORM.

    The function renders the task_detail.html template with the task object as a
    parameter, and the current URL as a parameter.
    """
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html', {
        "task": task,
        'current_url': 'task_detail',
    })


def toggle_complete(request, task_id):
    """
    Toggle complete task view.

    It retrieves the task object from the database using the Django ORM
    and sets the completed attribute to the opposite of its current value.
    Then it saves the task object and redirects to the home view with the
    current URL as a parameter.
    """
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')


def remove_task(request, task_id):
    """
    Remove task view.

    It retrieves the task object from the database using the Django ORM
    and deletes it. Then it redirects to the home view with the
    current URL as a parameter.
    """
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')
