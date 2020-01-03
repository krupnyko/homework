
###########################
a = int(input())
 
suma = 0
mult = 1
 
while a > 0:
    digit = a % 10
    suma += digit
    mult *= digit
    a = a // 10
 
print("Сума:", suma)
print("Добуток", mult)

###########################
n1 = int(input("Введіть ціле число: "))
n2 = 0
 
while n1 > 0:
    number = n1 % 10; 
    n1 = n1 // 10; 
    n2 = n2 * 10 
    n2 = n2 + number 
 
print('Реверсне число',n2)

##################################

a = [5, 2, 3, 1, 4]
a.sort()
print("Sorted: ",a)
