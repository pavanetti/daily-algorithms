require "minitest/autorun"
require_relative "minimum_window_substring"

class TestMinimumWindowSubstring < Minitest::Test
  def test_than_can_find_minimum_window_substring
    got = minimum_window_substring("ADOBECODEBANC", "ABC")
    assert_equal "BANC", got
  end

  def test_than_cannot_find_minimum_window_substring
    got = minimum_window_substring("ADOBECODEBANC", "ABZ")
    assert_equal "", got
  end
end
