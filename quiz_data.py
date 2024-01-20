
quiz_data = [
     {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Какой оператор используется для выполнения целочисленного деления в Python?',
        'options': ['/', '//', '%', '**'],
        'correct_option': 1
    },
    {
        'question': 'Как создать список, содержащий числа от 1 до 5 (включительно) в одной строке кода?',
        'options': ['list(1, 2, 3, 4, 5)', '[1, 2, 3, 4, 5]', 'range(1, 6)', '{1, 2, 3, 4, 5}'],
        'correct_option': 1
    },
    {
        'question': 'Как получить количество элементов в списке `my_list`?',
        'options': ['count(my_list)', 'len(my_list)', 'size(my_list)', 'total(my_list)'],
        'correct_option': 1
    },
    {
        'question': 'Какой метод используется для добавления элемента в конец списка?',
        'options': ['add()', 'append()', 'extend()', 'insert()'],
        'correct_option': 1
    },
    {
        'question': 'Как объявить функцию с параметром по умолчанию в Python?',
        'options': ['def my_function(param=default_value):', 'def my_function(param, default_value):', 'def my_function(param = default_value):', 'def my_function(default_value, param):'],
        'correct_option': 2
    },
    {
        'question': 'Какой тип данных представляет собой неизменяемую последовательность элементов?',
        'options': ['list', 'tuple', 'set', 'dictionary'],
        'correct_option': 1
    },
    {
        'question': 'Какой оператор используется для проверки равенства значений и типов переменных?',
        'options': ['==', '=', '!=', 'is'],
        'correct_option': 3
    },
    {
        'question': 'Какая функция используется для чтения данных с клавиатуры в Python?',
        'options': ['input()', 'read()', 'get_input()', 'keyboard_input()'],
        'correct_option': 0
    },
    # Добавьте другие вопросы
]
print(quiz_data[1]['correct_option'])