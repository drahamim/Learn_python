list1 = [21, 'stringword', True, 32.0, 4, [1, 2, 4, 5]]
print list1[1], type(list1[1])
print list1[4]
print list1[5]
print list1[5][1]  # prints list at 5 and index 2
# strings are implimented as lists thus 
print list1[1][1]  # prints list1 index 1, sub index 1

#range(0,10) = [0,1,2,......9]
for i in list1:
    print i

print range(0,10)

tup = (1,2,3,4)

print tup

#tup[0] = 12

for i in tup[3:1:-1]:
 print i