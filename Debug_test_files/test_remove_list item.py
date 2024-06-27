int_list = list(range(1, 51))

if len(int_list) > 25:
    for i in int_list:
        int_list.pop(len(int_list))
        print(i)
else:
    print(int_list)