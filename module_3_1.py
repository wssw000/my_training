calls = 0
list = ['hello', 'Goodbye']


def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    strinfo = (len(string), string.upper(), string.lower())
    count_calls()
    return strinfo

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            is_cont = True
            break
        else:
            is_cont = False
            continue

    return is_cont


print(is_contains('goOdbye', list))
print(is_contains('house', list))
print(string_info('Hello'))
print(calls)