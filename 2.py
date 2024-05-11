arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l', 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']

decoded_string = ''
is_reverse = False

for char in arr:
    if char.isalpha():
        if is_reverse:
            decoded_string = char + decoded_string
        else:
            decoded_string += char
        is_reverse = not is_reverse
    else:
        decoded_string += char

print("Chuỗi giải mã:", decoded_string)
