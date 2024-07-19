list = []
num_per_list = int(input("enter number of list: "))
list_num = int(input("enter number per list: "))

for i in range (num_per_list):
    list1 = []
    for j in range(list_num):
        x= (input(f"enter [{i},{j}]: "))
        list1.append(x)
    list.append(list1)

print(list)
print(list[0][0])