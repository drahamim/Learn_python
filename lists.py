#list: is a collection of "items"

list1 = [100, 21, 32, 4]
#        0    1   2   3
print list1
print type(list1) 
print list1[2]  # print specific element

print list1[0], list1[1]
print list1[0:2]   # prints range index 0 to -1
print list1[1:2]   # prints range index 1 and -1
print list1[-1]    # print counting backwards (last one)
print list1[-2:-1]   # print counting backwards
print list1[-3:-1]  #print 3rd last and the second last

list1.append(1200)
print list1
print len(list1)
print "Length of list:",len(list1)
del list1[0]  # Delete element at index 0
print list1

list1.remove(21) # Delete specific value in list
print list1
