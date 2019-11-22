# Matthew Brause
# CSCI102 - Section C
# Git Workshop 2

fib = [0,1]
for i in range(100):
    fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    print(fib[i])
