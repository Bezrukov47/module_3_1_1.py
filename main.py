# ПРОСТРАНСТВО ИМЁН
calls = 0 # Переменная, которая отслеживает звонки, она вне функций.
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()  # счетчик вызовов
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()  #  счетчик вызовов
    return string.lower() in (item.lower() for item in list_to_search)
# Примеры вызовов функций
result1 = string_info("Hello Konstantin")
result2 = is_contains("urban", ["Urban", "City", "town"])
# Выводим результаты
print(result1)
print(result2)
# Выводим количество вызовов
print(calls)
# Пример результата выполнения программы:(
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)