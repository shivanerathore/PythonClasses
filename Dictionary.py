# 1.Write a Python program to sum all the items in a dictionary.
print('This part of the program sum all the items in a dictionary')
first = {'1':10, '2':20, '3':30}
print(sum(first.values()))

print(" ")
# 2.Write a Python program to multiply all the items in a dictionary.
print('This part of the program multiply all the items in a dictionary')
second = {'id1':10, 'id2':5, 'id3': 4}
answer = 1
for key in second:
    answer *= second[key]
print(answer)

print(" ")
# 3.Write a Python program to remove a key from a dictionary.
print('This part of the program remove a key from a dictionary')
my_dict = {'a':1,'b':2,'c':3,'d':4}
print(my_dict)
if 'a' in my_dict:
    del my_dict['a']
print(my_dict)

print(" ")
# 4.Write a Python program to sort a dictionary by key.
print('This part of the program prints sorted dictionary by key')
my_dict = {'c':3,'d':4,'b':2,'a':1}
print("Unsorted",my_dict)
for key in sorted(my_dict):
    print(key, my_dict[key])

print(" ")
# 5. Write a Python program to sort(ascending and descending) a dictionary by value.
print('This part of the program prints sorted dictionary by value')
import operator
my_dict = {'c':3,'d':4,'b':2,'a':1}
print('Original dictionary : ',my_dict)
sorted_d = sorted(my_dict.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
