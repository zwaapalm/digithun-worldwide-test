def max_sum(inputs, k):
    try:
        if len(inputs) < k:
            return "Invalid input. Array length is less than k"
        max_sum = current_sum = sum(inputs[:k])
        for i in range(k, len(inputs)):
            current_sum = current_sum - inputs[i - k] + inputs[i]
            max_sum = max(max_sum, current_sum)
        return max_sum
    except Exception as e:
        print(f"An error: {e}")

print(max_sum([1, 4, -1, 2, 3], 3))  #Output: 5
print(max_sum([1, 4, -1, 2, 3], 2))  #Output: 5
