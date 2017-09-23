## DICTIONARY

d1 = { 1: 'rajesh',
       2: 'nitin',
       3: ['prashant','abhijit']
     }

print d1
print type(d1)
print "First Value of Dictionary: " + str(d1[1])

d1[2]='sachin'
print d1

d1[4]=['sinrin','sinntk']
print d1

d1['r']=['sinrin','sinntk']
print d1

print "Length: " + str(len(d1))
print "Max: " + str(max(d1))
print "Min: " + str(min(d1))

print sorted(d1)

print d1.keys()
print d1.values()
print d1.items()
print d1.get(6,'Raj')
d1.setdefault(6,'SAS')
print d1
d2 = {3: 'x', 6: 'y'}
d1.update(d2)
print d1

print cmp(d1,d2)



s = '{3 : "x", 6: "y", "sinrin" : 31005}'

print s
print eval(s)
print type(s)
print type(eval(s))
















