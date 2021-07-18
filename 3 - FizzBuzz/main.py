START = 1
STOP = 100

def fizzbuzz():
    for i in range(START, STOP + 1):
        ans = ''
        if i % 3 == 0:
            ans += 'Fizz'
        if i % 5 == 0:
            ans += 'Buzz'
        if len(ans) > 0:
            print(ans)
        else:
            print(i)
            
fizzbuzz()
