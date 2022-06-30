# in this program we will use the break keyword
# Break keyword is used if we want to hault the execution of while loop.

k = 10
while k > 1:
    if k == 5:
        k = k - 1
        continue
    if k == 3:
        break
    print(k)
    k = k - 1