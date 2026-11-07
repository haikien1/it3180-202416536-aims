def search_by_title(items, keyword):
    """Return the tasks whose title contains the keyword."""
    return [t for t in items if keyword in t.title]
