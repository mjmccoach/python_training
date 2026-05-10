tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def get_incomplete_tasks(list):
    incomplete_tasks = []
    for item in list:
        if item["completed"] == False:
            incomplete_tasks.append(item)
    return incomplete_tasks

print(get_incomplete_tasks(tasks))

def get_complete_tasks(list):
    complete_tasks = []
    for item in list:
        if item["completed"] == True:
            complete_tasks.append(item)
    return complete_tasks

print(get_complete_tasks(tasks))

def get_task_descriptions(list):
    descriptions = []
    for item in list:
        descriptions.append(item["description"])
    return descriptions

print(get_task_descriptions(tasks))

def get_tasks_at_least_x_long(list, time):
    tasks = []

    for item in list:
        if item["time_taken"] >= time:
            tasks.append(item)
    return tasks

print(get_tasks_at_least_x_long(tasks, 60))

def get_tasks_by_description(list, description):
    tasks = []

    for item in list:
        if item["description"] == description:
            tasks.append(item)
    return tasks

print(get_tasks_by_description(tasks, "Feed Cat"))

def complete_task_by_description(list, description):
    for item in list:
        if item["description"] == description:
            item["completed"] == True

complete_task_by_description(tasks, "Feed Cat")
print(tasks)

def add_task_to_list(list, task):
    list.append(task)

golf_task = {"description": "Go to driving range", "completed": False, "time_taken": 120}

add_task_to_list(tasks, golf_task)

print(tasks)