#math.ceil(x) - return the ceiling value of x - the smallest integer not less  than or equal to x.
import math #this imports the math module
print "math.ceil(-45.17): ", math.ceil(-45.17)
print "math.ceil(100.12): ", math.ceil(100.12)
print "math.ceil(119L): ", math.ceil(119L)
print "math.ceil(math.pi): ", math.ceil(math.pi)

#math.floor returns the floor of x - the largest integer less than or equal to x.
print "math.floor(-45.17): ", math.floor(-45.17)
print "math.floor(100.12): ", math.floor(100.12)
print "math.floor(119L): ", math.floor(119L)
print "math.floor(math.pi): ", math.floor(math.pi)

#math.fabs(x) returns the absolute value of x.
print "math.fabs(-45.17): ", math.fabs(-45.17)
print "math.fabs(119L): ", math.fabs(119L)
print "math.fabs(math.pi): ", math.fabs(math.pi)

#math.factorial - returns x factorial
print "math.factorial(9): ", math.factorial(9)

#math.fmod - return fmod(x, y) return mod as defined by the platform C.  It may not return the same as x % y, and fmod is generally preferred when working with floats, and % when working with integers.
print math.fmod(5.3, 2.2)
print 5.3 % 2.2

#math.isnan(x) return True is x is a NaN (not a number), and False otherwise
print "math.isnan(-1): ", math.isnan(-1)
print "math.isnan(9): ", math.isnan(9)

#math.trunc(x) return the real value x truncated to an Integral
print "math.trunc(5.55555555): ", math.trunc(5.55555555)

#math.modf(x) - returns the fractional and integer part of x in a two-item tuple
print "math.modf(100.12): ", math.modf(100.12)
print "math.modf(math.pi): ", math.modf(math.pi)

#math.exp(x) - returns the returns exponential of x
print "math.exp(-45.17): ", math.exp(-45.17)
print "math.exp(100.12): ", math.exp(100.12)
print "math.exp(119L): ", math.exp(119L)
print "math.exp(math.pi): ", math.exp(math.pi)

#math.pow(x, y) return x raised to the power of y.
print "math.pow(-45.17, 2): ", math.pow(-45.17, 2)
print "math.pow(100.12, 5): ", math.pow(100.12, 5)
print "math.pow(math.pi, 4): ", math.pow(math.pi, 4)

#math.sqrt(x) - return the square root of x
print "math.sqrt(45.17): ", math.sqrt(45.17)
print "math.sqrt(100.0): ", math.sqrt(100.0)
print "math.sqrt(math.pi): ", math.sqrt(math.pi)
