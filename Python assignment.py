"""Challenge 1"""
my_list = []
print(my_list)

"""Challenge 2"""
my_list= [10, 40, 30, 20]
print(my_list)

"""Challenge 3"""
my_list[1]= 15
print(my_list)

"""Challenge 4"""
listTwo= [50,60,70]
my_list.extend(listTwo)
print(my_list)

"""Challenge 5"""
del my_list[-1]
print(f'When the last numerical value is removed, the list becomes:\n {my_list}')

"""Challenge 6"""
my_list.sort()
print(my_list)

"""Challenge 7"""
indexOfThirty= my_list.index(30)
print(f'The index of 30 is: {indexOfThirty}')