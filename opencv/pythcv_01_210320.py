#變數型態
print('hello world')

x=3
print('x=',x)
print(type(x))
x=3.14
print('x=',x)
print(type(x))

#運算
x=10
y=3
#print('x^y=',x**y)
print('x^y='+x**y) no use
print('x/y=',x/y)
print('x//y=',x//y)

#x = x + 10
#x += 10

#文字 布林 迴圈
anser = input("使否要計算BMI(Y/N):").upper()
#while True:
while anser == 'Y':
    mheight = input("請輸入球員身(cm):")
    mweight = input("請輸入球體重(kg):")
    height = float(mheight)
    weight = float(mweight)
    bmi = weight / (height*0.01)**2
    print("bmi = ",bmi)

    if bmi < 18.5:
        print('過輕')
    elif 18.5 <= bmi < 24:
        print('正常')
    elif 24 <= bmi < 27:
        print('過重')
    else:
        print('體重過重')
    anser = input("使否要再計算BMI(Y/N):").upper()
    if anser == 'N':
        break
print('bye bye')
#迴圈 FOR each
mylist = ['A','B','C',1,2,3,3.14]
for d in mylist:
    print(d)
#break 中斷

#集合型
mylist = ['A','B','C',1,2,3,3.14]
print('mylist:',mylist)
print(type(mylist))
print('mylist[3]=',mylist[3])
mylist[3] = 'D'

mytuple= ('A','B','C',1,2,3,3.14)
print('mytuple:',mytuple)
print(type(mytuple))
print('mytuple[3]=',mytuple[3])
#mytuple[3] = 'D' 不可改值

#集合{} 不重覆 無順序
myset= {'A','B','C',1,2,3,3.14}
print('myset:',myset)
print(type(myset))
#print('myset[3]=',myset[3])
#myset[3] = 'D'

mydict = {1:'A',2:'B','3':'C','4':4,5:'KK'}
print('mydict:',mydict)
print(type(mydict))
print("mydict['3']=",mydict['3'])
mydict['3'] = 'D'
mydict[3] = 'D'
print('mydict:',mydict)

#二維
mylist2d = [['A','B','C'],[1,2,3]]
print('mylist2d:',mylist2d)
print(type(mylist2d))
print('mylist2d[1]=',mylist2d[1])
mylist2d[1][2] = 5
print('mylist2d:',mylist2d)


#range (包含,不包含,間隔)
print(list(range(20)))
print(list(range(0,20)))
print(list(range(10,30)))
print(list(range(10,30,5)))
print(list(range(1,30,2)))

#奇數
x = int(input('請輸入第一個數字:'))
y = int(input('請輸入第二個數字:'))
if x > y:
    x,y = y,x
if x % 2 == 0:
    x += 1
if y % 2 == 1:
    y += 1
print(list(range(x,y,2)))
print(sum(range(x,y,2)))
mysum = 0
for s in range(x,y,2):
    mysum += s
    print(mysum)
print(mysum)
#max min len

#質數
for s in range(2,101):
    i = 0
    #isprime = True
    for m in range(2,s):        
        if s % m == 0:
            #print(f'{s}被{m}整除了')
            i += 1
            #isprime = False
            #print('非質數:',s)
            break
    else:   #for else
        print(s)    #搭配break
    if i == 0:
    #if isprime:
        print('質數:  ',s)
    else:
        print('非質數:',s)
#print(list(range(2,2)))

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

#import

#索引子
data = [1,2,3,4,5,6]

print(data[0])
print(data[-2])
print(data[1:5])
print(data[1:-1])
print(data[-4:-1])
#print(data[-2:-6]) no use
print(data[-4:5])
print(data[0:4])
print(data[0:])
print(data[0:len(data)])
print(data[:])
print(data[::-1])

#串列解析 list comprehensions
#mylist = [i for i in range(10)]
#mylist = [i for i in range(3,10,2)]
mylist = [i for i in range(3,10) if i % 2 == 0]
print(mylist)

#讀寫檔案
import os 
if os.path.isfile('test.txt'):
    mfile = open('test.txt','r',encoding='UTF-8')
    mline = mfile.read()
    while mline != '':
        print(mline)
        mline = mfile.read()
else:
    print('檔案不存在')
mfile.close()

mfile = open('test.txt','a',encoding='UTF-8')
mfile.write('\n多加一行在後面\n')
mfile.close()