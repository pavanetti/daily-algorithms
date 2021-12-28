package main

import "testing"

func TestUniqueItem_Case1(t *testing.T) {
	input := []int32{13, 19, 13, 13}
	expected := int32(19)

	got := UniqueItem(input)
	if got != expected {
		t.Errorf("Expected %d, got %d", expected, got)
	}
}

func TestUniqueItem_Case2(t *testing.T) {
	input := []int32{6, 1, 3, 3, 3, 6, 6}
	expected := int32(1)

	got := UniqueItem(input)
	if got != expected {
		t.Errorf("Expected %d, got %d", expected, got)
	}
}

func TestUniqueItem_Case3(t *testing.T) {
	input := []int32{-6, -1, 3, 3, 3, -6, -6}
	expected := int32(-1)

	got := UniqueItem(input)
	if got != expected {
		t.Errorf("Expected %d, got %d", expected, got)
	}
}
