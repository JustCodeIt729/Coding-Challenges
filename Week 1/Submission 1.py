def product(lst):
    if len(lst) < 3:
        return -1
    
    lst = sorted(set(lst))
    lst.sort()

    list2 = []
    for x in lst:
        if x > 0:
            list2.append(x)
    
    if len(list2) >= 3:
        if -(lst[0]) * -(lst[1]) > lst[-1] * lst[-2]:
            t = lst[0] * lst[1] * lst[-1]
            return t
        else:
            total2 = lst[-1] * lst[-2] * lst[-3]
            return total2
    elif len(list2) == 2:
        total1 = lst[0] * lst[1] * lst[-1]
        return total1
    elif len(list2) == 1:
        total3 = lst[0] * lst[1] * lst[-1]
        return total3
    else:
        if 0 in lst:
            return 0
        else:
            return lst[-1] * lst[-2] * lst[-3]
    

arr = [-1,-1,-1,-1,-2] #change the list as per you like

r = product(arr)
if r == -1:
    print("No triplet!")
else:
    print(r)
