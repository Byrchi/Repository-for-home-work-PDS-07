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
a = 9
b = 10
print(f"{a+b}")

def test_function():
    s = 'випив'
    pr = list(s)
    pp = list(s[::-1])
    if pr == pp:
        return True
    else:
        return False

print_hi(name="Oleh")
mane_function()

print_hi(name="Oleh")
mane_function()



