dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#accessing values in dictionary
print "dict['Name']: ", dict['Name']

#updating dictionary by adding a new entry or a key-value pair, modifying and existing entry, or deleting and existing entry
dict['Age'] = 8 #updating existing entry
dict['School'] = 'DPS School'; # Add new entry

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

#Delete Dictionary Elements - remove individual dictionary elements  or clear the entire contents of a dictionary.

#del dict['Name']; #remove entry with key 'Name'
#dict.clear(); # remove all entries in dict
#del dict;

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']


#len(dict) gives the total length of the dictionary.  This would be equal to the number of items in the dictionary(dict)
print "length: %d" % len(dict)

#str(dict) produces a printable string representation of a dictionary(dict).
print "Equivalent String: %s" % str(dict)

#type(dict) method returns the variable type.
print "Variable Type: %s" % type(dict)

#dict.copy returns a shallow copy of dictionary(dict)
dict2 = dict.copy()
print "New Dictionary: %s" % str(dict2)

#fromkeys() creates a new dictionary with keys from seq and values set to value.
#seq = ('name', 'age', 'sex')
#dict = dict.fromkeys(seq, 10)
#print "New Dictionary: %s" % str(dict)

#get(dict) method returns a value for the given key. If key in not available then returns default value None.
print "Value: %s" % dict.get('Age')
print "Value: %s" % dict.get('Education')

#dict.items() returns a list of dict's (key, value) tuple pairs
print "Value: %s" % dict.items()

#dict.keys returns lists of dictionary dict's keys
print "Value: %s" % dict.keys()

#dict.update(dict2) adds dictionary dict2's key-values pairs to dict
dict2 = {'Sex': 'female'}
dict.update(dict2)
print "Value: %s" % dict

#dict.values() returns a list of all values available in a given dictionary.
print "Value: %s" % dict.values()