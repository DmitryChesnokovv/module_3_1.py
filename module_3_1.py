calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    return string in list_to_search

print(string_info('PythonProgrammig'))
print(string_info('DataScience'))
print(is_contains('apple', ['Banana', 'Orange', 'apple', 'Grapes']))
print(is_contains('watermelon', ['melon', 'WATER', 'cantaloupe']))
print(calls)