def count_calls():
    global calls
    calls += 1
    return 0


def string_info(string):
    count_calls()
    tuple_ = (len(string), str(string).upper(), str(string).lower())
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for element in list_to_search:
        if str(string).lower() == str(element).lower():
            flag = True
            return True

    if not flag:
        return False


calls = 0

print(string_info("Swiat"))
print(string_info("Alex"))
print(is_contains(1, [1, 2, 3, 4, 5]))
print(is_contains("Swiat", ["Alex", "Max", 3]))

print(calls)
