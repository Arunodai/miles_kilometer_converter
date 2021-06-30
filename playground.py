def add(*agrgs):
    sum = 0
    for n in agrgs:
        sum += n
    return sum

p = add(5, 4, 5)
print(p)