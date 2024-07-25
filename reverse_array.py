a = [1, 4, 3, 2]


def reverseArray(a) -> list:
    return a[::1]

def reverseArrayWithCode(a) -> list:
    new_a = []
    for i in range(len(a) - 1, -1, -1):
        new_a.append(a[i])
    return new_a

print(reverseArrayWithCode(a))