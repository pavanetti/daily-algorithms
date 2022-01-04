def minimum_window_substring(string, target)
  window = ""
  wc = Hash.new
  tc = Hash.new
  target.split("").each do |k|
    tc[k] = tc[k].to_i + 1
  end

  i, j = 0, 0
  while j <= string.size
    if tc.all? { |k, v| wc[k].to_i >= v }
      window = string[i, j - i] if window.empty? || string[i, j - i].size < window.size

      c = string[i]
      wc[c] = wc[c] - 1 if tc.key? c
      i += 1
    else
      c = string[j]
      wc[c] = wc[c].to_i + 1 if tc.key? c
      j += 1
    end
  end

  window
end
