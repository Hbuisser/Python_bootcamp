def ft_filter(function_to_apply, list_of_inputs):
    lst_result = []
    for x in list_of_inputs:
        if function_to_apply(x) is True:
            lst_result.append(x)
    return lst_result
  

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
less_than_zero2 = list(ft_filter(lambda x: x < 0, number_list))
print(less_than_zero)
print(less_than_zero2)
