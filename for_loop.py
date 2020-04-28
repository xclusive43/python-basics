#for loop
prices=[10,20,30]
sum=0
for i in prices:
    sum +=i

print(f'total price is:{sum}')

#example 2
#nested for loop
for x in range(4):
    for y in range(3):
     print(f'({x},{y})')

 #exapmle 3
 #XXXXXXX
 #XX
 #XXXXX
 #XX
 #XX
 # this pattern
num = [8, 2, 6, 2, 2]
for i in num:
    out = ''
    for j in range(i):
        out += 'x'
    print(out)
