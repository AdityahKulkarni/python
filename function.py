def addition():
    sum = 0 
    for i in range(num):
        sum = sum + num_list[i]
        i = i+1
    print("Sum of array elements is: ",sum)

num_list = []
num = int(input("Please enter the number of array elements: "))
for i in range(int(num)):
    n = int(input())
    num_list.append(n)

addition()