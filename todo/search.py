def search_by_priority(items, priority):
    """Return the tasks with exactly the given priority."""
    return [t for t in items if t.priority == priority]


def search_by_title(items, keyword):
    """Return the tasks whose title contains the keyword."""
    return [t for t in items if keyword.lower() in t.title.lower()]
