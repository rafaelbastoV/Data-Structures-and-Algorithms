def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        middle = (left + right) // 2
        print(middle)
        guess = arr[middle]
        
        if guess == target:
            return middle 
        elif guess < target:
            left = middle+1
        else:
            right = middle-1
    
    return -1 

arr = [1,5,8,10,20,22,30,31,32,43,49]
target = 31

result = binary_search(arr, target)

if result != -1:
    print(f"Value {target} found at index {result}.")
else:
    print(f"Valor {target} não encontrado.")

