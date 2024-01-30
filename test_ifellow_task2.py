
def get_repeating_symbol(string='Hello'):
    prev_char = string[0]
    for i in string[1:]:
        if i == prev_char:
            print(f'Повторяющийся символ: {prev_char}')
        else:
            prev_char = i

get_repeating_symbol()

