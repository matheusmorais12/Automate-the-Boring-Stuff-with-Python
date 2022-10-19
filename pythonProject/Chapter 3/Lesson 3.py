


def spam2(divdeby):
    try:
        return 42/ divdeby
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam2(2))
print(spam2(12))
print(spam2(0))
print(spam2(1))
print('\n')


def spam(divdeby):
    return 42/ divdeby

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

