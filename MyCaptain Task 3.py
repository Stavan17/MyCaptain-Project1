list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
num = 0
sum = 0
while(num < len(list1)):
    if list1[num] >= 0:
        print(list1[num], end = " ")
    num += 1 
print()
while(sum < len(list2)):
    if list2[sum] >= 0:
        print(list2[sum], end = " ")
    sum += 1