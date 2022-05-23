# Random array of numbers
array = [40, 45, 50, 55, 80, 85, 90, 95, 100]

# start at 0 to get the largest number
largest_num = array[0]
# loop through the array 
for i in range(0, len(array)):
    #compare against each number
    if (array[i] > largest_num):

        largest_num = array[i]


print(largest_num)



# Defined a function to get odd numbers
def get_odd_num(array):

# empty list for the odd numbers found
    odd_num = []
# A for loop to loop through the array of numbers with a sum to find the odd numbers
    for num in array:
        if num % 2 == 1:
            odd_num.append(num)
    return odd_num


print(get_odd_num(array))


def get_even_num(array):
    even_num = []

    for num in array:
        if num % 2 == 0:
            even_num.append(num)
    return even_num


print(get_even_num(array))


def main(array):
    even = []
    odd = []

    for num in array:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

print(main(array))
