def pivot_index(arr)
  i, j = 0, arr.size - 1
  left_sum, right_sum = 0, 0

  while i < j
    if left_sum < right_sum
      left_sum += arr[i]
      i += 1
    else
      right_sum += arr[j]
      j -= 1
    end
  end

  if left_sum == right_sum
    i or j
  else
    -1
  end
end

# 1, 7, 3, 6, 5, 6
# i              j
# l = 0, r = 0
