str = "this a string example...wow!!";

#str.capitalized() returns a copyy of th string with only its first character capitalized.
print "str.capitalized(): ", str.capitalize()

#count() returns the number of occurrences of substring sub in the range[start, end]. str.count(sub, start = 0, end=len(str))
sub = 'i';
print 'str.count(sub, 4, len(str)): ', str.count(sub, 4, len(str))

sub = 'wow';
print "str.count(sub): ", str.count(sub)

#endswith() - it returns True if the string ends with the specified suffix, otherwise False.  str.endswith(suffix[, start[, end]]). suffix could be a string or could also be a tuple of suffixes to look for. start - the slice begins from here, end - the slice ends here.
suffix = 'wow!!';
print 'str.endswith(suffix): ', str.endswith(suffix)
print 'str.endswith(suffix, 20): ', str.endswith(suffix, 20)

suffix = 'is';
print 'str.endswith(suffix, 2, 4): ', str.endswith(suffix, 2, 4)
print 'str.endswith(suffix, 2, 6): ', str.endswith(suffix, 2, 6)

#find(str, beg=0, end=len(string)) - determin if str occurs in string, or in a substring if starting index beg and ending index end are given. returns index if found and -1 otherwise.
str2 = 'exam';

print 'str.find(str2): ', str.find(str2)
print 'str.find(str2, 10): ', str.find(str2, 10)
print 'str.find(str2, 40): ', str.find(str2, 40)

#isalnum() - returns true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
str1 = 'this2009' #No space in this string
print 'str1.isalnum(): ', str1.isalnum()
print 'str.isalnum(): ', str.isalnum()

#isalpha() - returns true if string has at least 1 character and all characters are alphabetic, false otherwise.
str2 = 'this'; #No space & digit in this string
print 'str2.isalpha(): ', str2.isalpha()

print 'str.isalpha(): ', str.isalpha()

#isdigit() - retruns true if string contains only digits and false otherwise.
print 'str.isdigit(): ', str.isdigit()

#join() - returns a string in which the string elements of sequence have been joined by str seperator. str.join(seq) seq - is a sequence of the elements to be joined.
s = "-";
seq = ('a', 'b', 'c'); # This is seq of strings.
print 's.join(seq): ', s.join(seq)
print 's.join(str): ', s.join(str)

#lower() - returns a copy of the string in which all case-based characters have been lowercased.
str2 = 'THIS IS STRING EXAMPLE...WOW!!'
print 'str2.lower(): ', str2.lower()

#upper() - returns a copy of the string in which all cased-based characters have been uppercased.
print 'str.upper(): ', str.upper()

#max() - returns the max alphabetical character from the string str.
print "Max character: " + max(str)

#min() - returns the min alphabetical character from the string str.
print "Min character of str: " + min(str) #has spaces
str2 = 'this-is-string-example'
print "Min character of str2: " + min(str2) #has no spaces

#replace(old, new [, max]) - replaces all occurances of old in string with new or at most max occurrences if max given. max - if this optional argument max given, only the first count occurences are replaced.
str1 = 'this is string example...wow!! this is really string'

print "str1.replace('is', 'was'): ", str1.replace("is", "was")
print  "str1.replace('is', 'was', 3): ", str1.replace("is","was", 3)

#split() - returns a list of all the words in the string, using str as the seperator(splits on all whitespace if left unspecified)
print 'str.split(): ', str.split()


