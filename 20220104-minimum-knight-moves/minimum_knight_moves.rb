require "set"

def minimum_knight_moves(size, start, finish)
  breadth_first_search(
    KnightPosition.new(*start, size),
    KnightPosition.new(*finish, size)
  )
end

def breadth_first_search(start, finish)
  queue = [start]
  visited = Set.new [start]
  until queue.empty?
    current = queue.shift
    return current.steps if current == finish

    current.next_positions.each do |adj|
      unless visited.include?(adj)
        visited.add adj
        queue << adj
      end
    end
  end
  -1
end

class KnightPosition
  attr_reader :row, :col, :steps

  def initialize(row, col, board_size, steps = 0)
    @row, @col = row, col
    @board_size = board_size
    @steps = steps
  end

  def next_positions
    [
      [+2, +1], [+2, -1],
      [-2, +1], [-2, -1],
      [+1, +2], [+1, -2],
      [-1, +2], [-1, -2],
    ].map do |dx, dy|
      KnightPosition.new(@row + dx, @col + dy, @board_size, @steps + 1)
    end.filter { |position| position.valid? }
  end

  def valid?
    @row >= 0 && @row < @board_size &&
    @col >= 0 && @col < @board_size
  end

  def eql?(other)
    self.class == other.class &&
    @row == other.row && @col == other.col
  end

  alias :== eql?

  def hash
    [@row, @col].hash
  end
end
