#1 1부터 1000까지의 자연수 중 3의 배수의 합
number = 0
while number < 1001 :
    number = number + 1
    if number % 3 == 0:
        answer += number
        

print(answer)


#1-2 
star = 0
number = 10 - star
while star < 11 :
      star = star + 1
   
print('*' * number)


#1-3 
a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
a.sort()
a.pop(0)
a.pop(0)
a.pop(0)
a.pop(0)
result = a[0] + a[1] + a[2] + a[3] + a[4] + a[5] 
answer = result / 6

#연습문제(리스트 내장 함수)
b = ['Life', 'is', 'too', 'short']
' ' .join(b)

#2-1
for i in range(1. 101):
    print i

#2-2 
g = 0
c = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in c:
    g += i
want = g / len(c)
print(want)


#2-3
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]






