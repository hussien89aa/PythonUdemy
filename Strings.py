from django.template.defaultfilters import upper, lower

name="hussein alrubaye"
# find number of character in string
Strlen=len(name)
print(Strlen)
# upper case to string
print(upper(name))
#lower case to string
print(lower(name))
title="your grade is {}".format(79)
print(title)
# concat to string
str="San Fransisco{}".format(" is nice place")
print(str)
