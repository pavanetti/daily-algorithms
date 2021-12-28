package main

func UniqueItem(input []int32) int32 {
	var count [32]uint8

	for _, v := range input {
		for i := range count {
			count[i] += uint8(v>>uint(i)) & 1
			count[i] %= 3
		}
	}

	return numberFromBits(count)
}

func numberFromBits(bits [32]uint8) int32 {
	sum := int32(0)
	for i := range bits {
		sum += int32(bits[i]) << uint(i)
	}
	return sum
}
