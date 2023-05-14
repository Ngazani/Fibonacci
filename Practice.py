fibonacci = [] #initial List
#first 2 numbers
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
#add the first 2 numbers to the list
fibonacci.append(a)
fibonacci.append(b)
#Define the length of the sequence
defineLen = int(input("Length of sequence: "))

#for loop that iterates through the length of the sequence, but starts at the second index of the list
for x in range(1,defineLen):
    #determine the next number of the sequence by adding the number at the current index (1) to the number at the previous index (0)
    next = fibonacci[x] + fibonacci[x-1]
    #add the number to the list and repeat the process till you exhaust the length
    fibonacci.append(next)

print(fibonacci)#print the complete list
