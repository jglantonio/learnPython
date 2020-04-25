num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69,
            113, 166]
list_ood_nubers = [];
count = 0
for num in num_list:
    if len(list_ood_nubers) == 5:
        break
    odd = count % 5
    count = count + 1
    if odd == 0:
        list_ood_nubers.append(num)
        num_list.append(num)
        print(num)
print(num_list)