#Assigntment
#   Take the following Python code that stores a string:
#
#   str = 'X-DSPAM-Confidence:0.8475'
#
#   Use find and string slicing to extract the portion of the string after the colon character
#   and then use the float function to convert the extracted string into a floating point number.
#
#   Solution

str = 'X-DSPAM-Confidence: 0.8475'
pos = str.find(':')
number=float(str[pos+2:])
print(number)
print(type(number))
