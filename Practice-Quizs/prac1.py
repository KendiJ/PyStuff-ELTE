# Write a function called sum_only_evens(numbers) that takes a list of integers as input. 
# The function should loop through the list and return the sum of only the even numbers.

def sum_only_evens(numbers):
    
        if not isinstance(numbers, list):
            return "Must be list of integers"
        
        total_sum = 0
        
        for num in numbers:
            if not isinstance(num, int):
                continue
            if num % 2 == 0:
                total_sum += num
        return total_sum
my_list = [1, 4, 5, 11, 12, 20]
result = sum_only_evens(my_list)
    
print(f"The list is: {my_list}")
print(f"the sum of evens is: {result}")