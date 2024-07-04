fruit_list = ["banana", "orange", "apple", "papaya"]
for fruit in fruit_list:
    if fruit != "apple":
        print("can't get ")
    else:
        print(f"I gat it in {fruit_list.index(fruit)}")
        break