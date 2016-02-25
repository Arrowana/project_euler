def match_pattern(number):
    number_str = str(number)
    selected_digits = [int(number_str[i]) for i in range(0, len(number_str), 2)]

    for i, digit in zip(range(1, len(selected_digits))+ [0], selected_digits):
        if i == int(digit):
            continue
        else:
            return False

    return True
