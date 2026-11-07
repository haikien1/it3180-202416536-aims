class Task:
    def __init__(self, title, priority=1):
        self.title = title
        self.priority = priority
        self.done = False

    def __str__(self):
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title} (p{self.priority})"
