n, m = map(int, input().split())

def next_elem(i):
    elem = 1 + (i + m - 2) % n
    return elem

i = 1
while True:
    print(i, end='')
    i = next_elem(i)
    if i == 1:
        break