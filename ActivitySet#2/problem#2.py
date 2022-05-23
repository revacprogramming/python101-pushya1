
def add(a, b):
    sum = a+b
    return sum


def output(a, b, sum):
    print(a,"+",b,'is',sum)


def main():
    a, b = input('input_two_numbers')
    a = int(a)
    b = int(b)
    sum = add(a, b)

    output(a, b, sum)


main()
