## 9/3/19 Day 4 Afternoon Python Exercises

#title = "Green"
#STOP = 10
#counter = 0
#while counter < STOP:
#    print(counter)
#    counter = counter + 1

#title = "Green"
#counter = 0
#
#while counter < len(title):
#    print(counter)
#    counter = counter + 1

#title = "Green"
#counter = 0
#
#while counter < len(title):
#    print(title[counter])
#    counter = counter + 1

#title = "Green"
#counter = 0
#
#while counter < len(title):
#    if (counter % 2) == 0: 
#       print(counter)
#       print(title[counter])
#    counter = counter + 1
 
#--Lists

#power_rangers = ['Jason','Trini','Billy','Zach','Kim']
#
#power_rangers.append ('Chris')
#print(power_rangers)
#
#test_list = []
#print(test_list)
#test_list.append('Test List Item')
#print(test_list)
#
#index = 0
#while index < len(test_list):
#    print(test_list[index])
#    index = index + 1
#
#test_list.append('Item 2 for list')
#print(test_list)
#
#while index < len(test_list):
#    print(test_list[index])
#    index = index + 1
#
#test_list.remove(test_list[0])

#test='here is my test string'
#print(test)
#print(test.upper())
#print(test.capitalize())
#reversed=''.join(reversed(test))
#print(reversed)
#
#index = (len(test) - 1)
#print(index)
#while index > -1:
#    print(test[index]) 
#    index = index - 1

#str = 'Python'
#reversed=''.join(reversed(str))
#print(reversed)

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

#str = 'This is my absolute test string to see if my Leet cipher is working'
#
#def my_function_a(x):
#  strA = x.replace('a','4')
#  return strA
#
#strA = my_function_a(str)
#
##print(my_function_a(str))
#
#def my_function_e(x):
#  strE = x.replace('e','3')
#  return strE 
#
#strE = my_function_e(strA)
#
##print(my_function_e(strA))
#  
#def my_function_g(x):
#  strG = x.replace('g','6')
#  return strG 
#
#strG = my_function_g(strE)
#
##print(my_function_g(strE))
#
#def my_function_g(x):
#  strI = x.replace('I','1')
#  return strI 
#
#strI = my_function_g(strG)
#
##print(my_function_g(strG)


# S => 5
# T => 7


#
#def my_function_g(x):
#  strO = x.replace('o','0')
#  return strO 
#
#strO = my_function_g(strI)
#
##print(my_function_g(strI))
#
#def my_function_g(x):
#  strS = x.replace('s','5')
#  return strS 
#
#strS = my_function_g(strO)
#
##print(my_function_g(strO))
#
#def my_function_g(x):
#  strT = x.replace('t','7')
#  return strT 
#
#strT = my_function_g(strS)
#
#print(my_function_g(strS))


# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

str = 'This is my absolute test string to see if my Leet cipher is working'
#original_character = ['A','a','E','e','G','g','I','i','O','o','S','s','T','t']
#new_character = ['4','4','3','3','6','6','1','1','0','0','5','5','7','7']
#
#index = 0
#
#while str[index] < len(str):
#    while str[index] == str[original_character]
#    return index
#    print(str[index])
#    index = index + 1

str = 'This is my absolute test string to see if my Leet cipher is working'
#original_character = ['A','a','E','e','G','g','I','i','O','o','S','s','T','t']
#new_character = ['4','4','3','3','6','6','1','1','0','0','5','5','7','7']
#
#index = 0
#
#while str[index] < len(str):
#    while str[index] == str[original_character]
#    return index
#    print(str[index])
#    index = index + 1



# def my_function_a(x):
#  str1 = x.replace('a','4')
#  str1 = str1.replace('e','3')
#  str1 = str1.replace('g','6')
#  str1 = str1.replace('I','1')
#  str1 = str1.replace('o','0')
#  str1 = str1.replace('s','5')
#  str1 = str1.replace('t','7')
#  print(str1)
# my_function_a(str)

## List Exercises

list_to_sum = ['4','4','3','3','6','6','1','1','0','0','5','5','7','7']

index = 0
sum = 0

while index < len(list_to_sum):
    sum =+ list_to_sum([index])
    