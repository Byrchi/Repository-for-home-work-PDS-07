def print_hi(name):
       print(f'Hi, {name}')
def mane_function():
    x = input("Введіть довільне чмсло: ")
    s = 0
    list_of_number = list(x)
    for i in list_of_number:
        r = int(i)
        s += r
    return print("Сумма всіх цифр в числі дорівнює", s)

def test_function():
    pass

print_hi(name="Oleh")
mane_function()



