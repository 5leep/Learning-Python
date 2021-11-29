# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# My solution...

n = 5
n_compute = n + (n**2 + n**3)

print(n_compute)

# Eeehhhhhh


# Example solution...

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


# My amended solution...

x = int(input("Please enter an integer: "))
x1 = int("%s" % x)
x2 = int("%s%s" % (x,x))
x3 = int("%s%s%s" % (x,x,x))
print(x1 + x2 + x3)

