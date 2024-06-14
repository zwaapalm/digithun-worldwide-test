def secondMax(inputs):
    try:
        max_value = second_max = float('-inf')
        for num in inputs:
            if num > max_value:
                second_max = max_value
                max_value = num               
            elif num == max_value:
                return  max_value
            elif max_value > num > second_max:
                second_max = num              
        return second_max if second_max != float('-inf') else None
    except Exception as e:
        print(f"An error: {e}")

print(secondMax([ -1, 4, 30, 2, -4 ]))  #Output: 4
print(secondMax([ 3, 4, 5, 6, 7 ]))  #Output: 6
print(secondMax([ 3, 4, 5, 6, 7, 7 ]))  #Output: 7
