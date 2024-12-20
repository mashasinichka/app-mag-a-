print('task 1')
def is_even(number: int) -> int:
    """
    Функция должна проверять число на четность/нечетность
    number - аргумент вводимый пользователем
    Функция должна выводить True/False 
    """
    return "четное (True)" if number % 2 == 0 else "нечетное (False)"
print(is_even(6))
print(is_even(9))
print(is_even.__doc__)


def test_is_even():
    t_number = 2 
    is_even(t_number)
    if t_number % 2 == 0:
        print('#test1 - success')
    else:
        print('#test1 - failed')

test_is_even()

print('task 2')
def age_category(voz: int) -> int:
    """
    ТРАМП ВЫИГРАЛ!!!!
    """
    if voz <= 8:
        return "Детский"
    if 18 >= voz >= 14:
        return "Подростковый"
    if voz >= 18:
        return "Взрослый"
print(age_category(8)) 
print(age_category(15))
print(age_category(19))
print(age_category.__doc__)  

print('task 3')
def check_sign(yui: int) -> int:
    if yui > 0:
        return "Положительное"
    if yui < 0:
        return "Отрицательное"
    if yui == 0:
        return "Ноль"
print(check_sign(-1))
print(check_sign(4))
print(check_sign(0))

print('task 4')
def grade_evaluation(trump: int) -> int:
    if -1 < trump <= 30:
        return "Ужасно"
    if -1 < trump <= 60:
        return "Хорошо"
    if -1 < trump <= 80:
        return "Отлично"
    if -1 < trump <= 90:
        return "Нужно научиться"
print(age_category(8)) 
print(age_category(15))
print(age_category(19))
