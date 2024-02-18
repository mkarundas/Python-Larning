greeting = "Hello Wordld!"
morning_greeting = 'Good morning'

patrick_address = """"Patrick A Parry
2316 Jim Rosa Lane
San Francisco, California(CA), 94118"""

brian_address = '''Brian A Ledesma
464 Pine Street
Crafton, Pennsylvania(PA), 15205'''

# greeting = "Hello World!"
# greeting[3] = "p" # Output: TypeError: 'str' object does not support item assignment

greeting = "Hello World!"
length_of_greeting = len(greeting)
print(length_of_greeting) # Output: 12

greeting = "Hello World!"
print(type(greeting)) # Output: <class 'str'>

my_string = "programming"

result_1 = my_string[:]
print(result_1) #Output: programming

result_2 = my_string[::]
print(result_2) #Output: programming

result_3 = my_string[0]
print(result_3) #Output: p

result_4 = my_string[4]
print(result_4) #Output: r

result_5 = my_string[:4]
print(result_5) #Output: prog

result_6 = my_string[0:4]
print(result_6) #Output: prog

result_7 = my_string[1:4]
print(result_7) #Output: rog

result_8 = my_string[4:]
print(result_8) #Output: ramming

result_9 = my_string[4:9]
print(result_9) #Output: rammi

result_10 = my_string[4:9:2]
print(result_10) #Output: rmi

result_11 = my_string[-1]
print(result_11) #Output: g

result_12 = my_string[-2]
print(result_12) #Output: n

result_13 = my_string[:-4]
print(result_13) #Output: program

result_14 = my_string[-10:-4]
print(result_14) #Output: rogram

result_15 = my_string[-10:]
print(result_15) #Output: rogramming

result_16 = my_string[-10:-4:2]
print(result_16) #Output: rga

result_17 = my_string[-4:-10:-2]
print(result_17) #Output: mag

result_18 = my_string[::-1]
print(result_18) #Output: gnimmargorp

result_19 = my_string[::-2]
print(result_19) #Output: gimrop

result_20 = my_string[:-5:-1]
print(result_20) #Output: gnim

result_21 = my_string[3::-1]
print(result_21) #Output: gorp

result_22 = my_string[:3:-1]
print(result_22) #Output: gnimmar

###String Methods

##1. capitalize()
# This method returns a string where the first character is upper case, and the rest is lower case.

string_1 = 'python is fun.'
result_23 = string_1.capitalize()
print(result_23) # Output: Python is fun.

##2. casefold()
# This method returns a string where all the characters are lower case.

string_2 = 'Python Is FUN.'
result_24 = string_2.casefold()
print(result_24) # Output: python is fun.

##3. center()
# This method allows us to 'center' a string within a specific width, padding it with a specified character.

string_3 = 'Python'
result_25 = string_3.center(0)
result_26 = string_3.center(1)
result_27 = string_3.center(2)
result_28 = string_3.center(3)
result_29 = string_3.center(4)
result_30 = string_3.center(5)
result_31 = string_3.center(6)
result_32 = string_3.center(7)
result_33 = string_3.center(8)
result_34 = string_3.center(9)
result_35 = string_3.center(10)
result_36 = string_3.center(11)
result_37 = string_3.center(11, "*")
result_38 = string_3.center(12, "*")
result_39 = string_3.center(13, "*")
result_40 = string_3.center(14, "*")
result_41 = string_3.center(14, "#")

print(result_25) # Output: Python
print(result_26) # Output: Python
print(result_27) # Output: Python
print(result_28) # Output: Python
print(result_29) # Output: Python
print(result_30) # Output: Python
print(result_31) # Output: Python
print(result_32) # Output:  Python
print(result_33) # Output:  Python 
print(result_34) # Output:   Python 
print(result_35) # Output:   Python  
print(result_36) # Output:    Python  
print(result_37) # Output: ***Python**
print(result_38) # Output: ***Python***
print(result_39) # Output: ****Python***
print(result_40) # Output: ****Python****
print(result_41) # Output: ####Python####

##4. count()
# This method returns the number of times a specified value appears in the string.

string_4 = 'Python is a popular programming language. Python works on different platforms. Python has a simple syntax.'
result_42 = string_4.count('Python')
print(result_42) # Output: 3

result_43 = string_4.count('Python', 10, 50)
print(result_43) # Output: 1 :- Search from position 10 to 50

##5. encode()
# This method returns an encoded version of the given string.
# If no encoding is specified, UTF-8 will be used.

string_5 = 'python is fun.'
result_44 = string_5.encode()
print(result_44) # Output: b'python is fun.' :- default encoding to utf-8

string_6 = 'pythön! is fun.'
result_45 = string_6.encode("ascii", "ignore")
print(result_45) # Output: b'pythn! is fun.' :- ignore error

string_7 = 'pythön! is fun.'
result_46 = string_7.encode("ascii", "replace")
print(result_46) # Output: b'pyth?n! is fun.' :- replace error