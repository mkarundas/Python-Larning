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

esult_22 = my_string[:3:-1]
print(esult_22) #Output: gnimmar