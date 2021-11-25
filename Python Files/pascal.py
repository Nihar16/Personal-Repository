n=int(input("Enter the no of ros in pascal trainagle : "))
list=[1]

for i in range(n):
    for j in range(i):
        list.append(list[j-1]+list[j])
        print(list)
