user_list = range(1,1000if )

def multiples_of_3_or_5(a_list):
    v_sum = 0
    for number in a_list:
        if number%3 == 0 or number%5 == 0:
            v_sum += number
    return v_sum

print(multiples_of_3_or_5(user_list))