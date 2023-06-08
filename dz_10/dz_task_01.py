import sys
def number_mounth(x):
    month_dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    try:
        x = int(x)
    except ValueError as ex:
            print("Не правильний тип значення, введіть числове значення.", file= sys.stderr)
            return ex

    print( month_dict.get(x))
    if x <= 0 or x >= 13:
        raise ValueError("Ви ввели некоректне значення, значення має бути від 1 до 12")



    for i in month_dict:
        if x == i :
            return month_dict.get(x)

number_mounth("13")

