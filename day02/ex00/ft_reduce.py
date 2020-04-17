from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
    first = list_of_inputs[0]
    for i in list_of_inputs[1:]:
        first = function_to_apply(first, i)
    return first

def do_sum(x1, x2): 
    return x1 + x2

print(ft_reduce(do_sum, [1, 2, 3, 4]))
print(reduce(do_sum, [1, 2, 3, 4]))
