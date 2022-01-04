require "minitest/autorun"
require_relative "pivot_index"

class TestPivotIndex < Minitest::Test
  def test_than_can_find_pivot_index
    got = pivot_index([1, 7, 3, 6, 5, 6])
    assert_equal 3, got
  end

  def test_than_cannot_find_pivot_index
    got = pivot_index([1, 2, 3])
    assert_equal -1, got
  end

  def test_that_pivot_can_be_on_the_edges
    got = pivot_index([2, 1, -1])
    assert_equal 0, got
  end
end
