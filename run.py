# Random array of numbers
array = [40, 45, 50, 55, 80, 85, 90, 95, 100]

# Using the built in max function to get the largest number
largest_num = max(array)

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
