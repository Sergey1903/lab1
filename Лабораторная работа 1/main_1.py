numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
valid_numbers = [number for number in numbers if number is not None]
mean = sum(valid_numbers)/len(numbers)
for i in range(len(numbers)):
    if numbers[i]is None:
        numbers[i] = mean
print("Измененный список:",numbers)