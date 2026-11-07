MAX_TASKS = 20


class TodoList:
    def __init__(self):
        self.items = []

    def add(self, task):
        if len(self.items) > MAX_TASKS:
            return False
        self.items.append(task)
        return True

    def complete(self, title):
        for t in self.items:
            if t.title == title:
                t.done = True
                return True
        return False

    def pending_count(self):
        return sum(1 for t in self.items if not t.done)

    def print_list(self):
        if not self.items:
            print("The list is empty")
            return
        for t in self.items:
            print(t)
