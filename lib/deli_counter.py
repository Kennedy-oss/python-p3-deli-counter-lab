def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: "
        line_status += " ".join([f"{index + 1}. {name}" for index, name in enumerate(queue)])
        print(line_status)

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")
    return queue

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {queue.pop(0)}.")
        return queue


