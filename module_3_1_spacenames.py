calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(enter_word): #Функция вывода строки в малом и большом регистре и ее длины
    count_calls()
    all_str_num = len(enter_word)
    result_l = enter_word.lower()
    result_u = enter_word.upper()
    information_of_word = (all_str_num, result_l, result_u)
    return information_of_word

def is_contains(default_str, list_to_search): #Функция проверки на наличие строки в списке
    count_calls()
    for i in list_to_search:
        if i == default_str:
            return True
        else:
            return False

first_test = 'Разработчик'
second_test = 'Арбуз'
print(string_info(first_test))
print(string_info(second_test))

list_to_search_test = ['first', 'main_elem', 'apple', 'pen']
word_for_test = 'first'
word_for_two_test = 'second'
word_for_third_test = 'third'

print(is_contains(word_for_test, list_to_search_test))
print(is_contains(word_for_two_test, list_to_search_test))
print(is_contains(word_for_third_test, list_to_search_test))
print('Функции вызваны всего раз: ', calls)