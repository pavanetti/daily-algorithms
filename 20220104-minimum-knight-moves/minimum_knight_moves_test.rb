require "minitest/autorun"
require_relative "minimum_knight_moves"

class TestMinimumKnightMoves < Minitest::Test
  test_cases = [
    { size: 10, start: [0, 0], finish: [0, 2], expected: 2 },
    { size: 6, start: [5, 1], finish: [0, 5], expected: 3 },
    { size: 3, start: [0, 0], finish: [1, 1], expected: -1 },
  ]

  test_cases.each_with_index do |test_case, index|
    define_method "test_that_it_works_for_case_#{index + 1}" do
      got = minimum_knight_moves(test_case[:size], test_case[:start], test_case[:finish])
      assert_equal test_case[:expected], got
    end
  end
end
