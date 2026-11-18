
a = 0
b = 1

while a <= 12586269025:

    if a == 12586269025:
        print(a)
    else:
        print(a, end=", ")

    c = a + b
    a = b
    b = c
