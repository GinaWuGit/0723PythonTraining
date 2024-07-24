#判斷一數是否為質數
def if_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True 

sum = 0
x = int(input("Please enter a number: "))
for i in range(2, x+1):
    answer = if_prime(i)
    if answer:
        print(i)
        sum += 1
print("此數所含的質數總數:", sum)
