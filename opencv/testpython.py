#自訂函式
def checkPrime(n):
    for m in range(2,n):        
        if n % m == 0:
            return False
    return True
print('3 ->',checkPrime(3))
for s in range(2,101):
    if checkPrime(s):
        print('質數:',s)
    