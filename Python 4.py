#Q4)program to accept n numbers and store them in array and sort them using function?
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
lst.sort()
print(lst)