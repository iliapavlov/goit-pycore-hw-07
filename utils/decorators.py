def input_error_add(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Add me name and <value> please. Error: {e}"
        # except IndexError:
        #     return "Add <name> after 'phone' command"
    return inner

def input_error_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Add me <old_value> and <new_value>, please. Error: {e}"
    return inner

def input_error_search(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Add <name> after command, please. Error: {e}"
        except AttributeError as e:
            return f"There is no birthday data for some contact. Error: {e}"
    return inner