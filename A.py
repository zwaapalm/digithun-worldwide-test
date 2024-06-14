def max(inputs):
    try:
        max_value = inputs[0]
        for num in inputs:
            if num > max_value:
                max_value = num
        return max_value
    except Exception as e:
        print(f"An error: {e}")


print(max([ -1, 4, 30, 2, -4 ]))  #Output: 30
print(max([ 3, 4, 5, 6, 7 ]))  #Output: 7
