import ast

def get_products_of_all_ints_except_at_index(arr):
    result_list = []
    for x in arr:
        result = 1
        for i in arr:
            if arr.index(i) == arr.index(x):
                continue
            else:
                result *= i
        result_list.append(result)
    
    return result_list

input = input("Enter list: ")
input = ast.literal_eval(input)
result = get_products_of_all_ints_except_at_index(input)
print(result)
