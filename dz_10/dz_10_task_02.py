import sys


list = [1, 2, 5, 4, 10, 12]
list1 = [1, 2, 5, 4, 5, 1, 1]
list2 = [1, 2, 5, 4, '5', 12]
list3 = [1, 2, 5, 4, 5, 'xdg']
def uniq_num(list):


    if type(list) == list :
        raise TypeError ("Неправильний тип списка")


    if len(list) == 0:
        raise Exception('Список не може бути пустим, додайте занчення до списку')

    for i in list:
        try:
            if i != int(i):
                raise ValueError ("В списку знаходяться некоректні елементи")
        except ValueError as err:
            print(err, file=sys.stderr)
        if list.count(i) > 1:
            print(f' Елемент {i} зустрічається в списку {list.count(i)} раз')
            break
    else:
        print('Список є унікальним')


uniq_num(list)
print("*" * 35)
uniq_num(list1)
print("*" * 35)
uniq_num(list2)
print("*" * 35)
uniq_num(list3)
print("*" * 35)
