START = 1
STOP = 101

def fizzbuzz():
    for i in range(START, STOP):
        ans = ''
        if i % 3 == 0:
            ans += 'Fizz'
        if i % 5 == 0:
            ans += 'Buzz'

        print_solution(ans, i)


def print_solution(ans, i):
    if len(ans) > 0:
        print(ans)
    else:
        print(i)


fizzbuzz()
