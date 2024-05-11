arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


add_2_array = [x + 2 for x in arr]


multiply_2_array = [x * 2 for x in arr]


shifted_2_array = arr[2:] + arr[:2]

print("Mảng cộng 2:", add_2_array)
print("Mảng nhân 2:", multiply_2_array)
print("Mảng dịch 2:", shifted_2_array)