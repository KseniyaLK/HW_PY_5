# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]

my_list = [1, 5, 2, 3, 4, 6, 1, 7]


#1________________________________
# def rost (my_list):
#     new_list = [my_list[0]]

#     for i in range(1, len(my_list)):
#         if new_list[-1] < my_list[i]:
#             new_list.append(my_list[i])

#     return (new_list)     

# print (rost(my_list))     

#2________________________________ через включения

new_list = [my_list[0]]
[new_list.append(my_list[i]) for i in range(1, len(my_list)) if new_list[-1] < my_list[i]]
print(new_list)