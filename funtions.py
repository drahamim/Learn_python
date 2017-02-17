# Convert C to F 

def celToF(tempurature):
    f = tempurature*9/5 + 32
    print f
    return f, tempurature

faren = celToF(12) #caller of the function
print "test"
print faren

print celToF(13)

x,y = celToF(14)
print x,y