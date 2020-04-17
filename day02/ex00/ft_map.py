def ft_map(function_to_apply, list_of_inputs):
    return [function_to_apply(x) for x in list_of_inputs]

def addition(n): 
    return n + n 
  
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
result2 = ft_map(addition, numbers)
print(list(result)) 
print(list(result2))