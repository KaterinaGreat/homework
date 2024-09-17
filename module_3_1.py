calls = 0
def count_calls(calls):
    print(calls)
def string_info(string):
    global calls
    calls += 1
    new_string = (len(string), string.upper(), string.lower())
    return new_string
def is_contains(string, list_to_search):
    global calls
    calls += 1
    for i in list_to_search:
        new_list = []
        new_list.append(i.lower())
        if string.lower() in new_list:
            return False
    return True

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)