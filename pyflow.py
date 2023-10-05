x = 0


def func1():
    global x
    x = 10


def func2(x, y, z):
    return x + y + z


def func3(x, y):
    return x * y


def func4(a, b, c):
    global x
    x = func5(a, b, c)
    return x


def func5(x, y, z):
    x = func7(func6(x + y, z), func6(x + y, z))
    return x


def func6(x, y):
    return func8(x * y)


def func7(x, y):
    x = x * y
    return x


def func8(y):
    global x
    return x + y


def main():
    global x
    func1()
    y = func2(x, x, x)
    z = func3(x, y)
    print(func4(x, y, z))


if __name__ == "__main__":
    main()
