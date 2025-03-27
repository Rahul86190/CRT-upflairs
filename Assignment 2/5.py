def modify_list(lst, item):
    lst.append(item)

my_list = [1, 2, 3]
print("Before function call:", my_list)
modify_list(my_list, 4)
print("After function call:", my_list)