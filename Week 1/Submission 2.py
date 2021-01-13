l = [-10,2,3,4,-10] #change the list as per wish

neg = [] #negative integers
posi = [] #positive integers

answer = 0

for i in range(len(l)):
    if l[i] < 0:
        neg.append(l[i])
        i+=1
    elif l[i] == 0:
        posi.append(l[i])
        i+=1
    else:
        posi.append(l[i])
        i+=1

print(posi,neg)

if len(l) == 3:
    answer == (l[0])*(l[1])*(l[2])
elif len(neg) == len(l):
    neg.sort()
    answer = (neg[-3])*(neg[-2])*(neg[-1])
elif len(posi) == len(l):
    posi.sort()
    answer = (posi[-1])*(posi[-2])*(posi[-3])
elif len(neg) > 2 and len(posi) == 1:
    neg.sort()
    if posi[0] == 0:
        answer = 0
    else:
        answer = (neg[0])*(neg[1])*(posi[0])
elif len(neg) == 1 and len(posi) > 2:
    posi.sort()
    answer = (posi[-1])*(posi[-2])*(posi[-3])
elif len(neg) == 2 and len(posi) == 2:
    neg.sort()
    posi.sort()
    if posi[-1] == 0:
        answer = 0
    else:
        answer = (neg[0])*(neg[1])*(posi[-1])
elif len(neg) >= 2 and len(posi) >= 2:
    neg.sort()
    posi.sort()
    if len(posi) == 3:
        if 0 in posi:
            answer = (neg[0])*(neg[1])*(posi[-1])
        else:
            check1 = (posi[-3])*(posi[-2])*(posi[-1])
            check2 = (neg[0])*(neg[1])*(posi[-1])
            answer = max(check1,check2)
    elif len(posi) == 2:
        answer = (neg[0])*(neg[1])*(posi[-1])
    else:
        check1 = (posi[-3])*(posi[-2])*(posi[-1])
        check2 = (neg[0])*(neg[1])*(posi[-1])
        answer = max(check1,check2)
print(posi,neg)
print(answer)
