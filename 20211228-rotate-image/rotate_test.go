package main

import (
	"reflect"
	"testing"
)

func TestRotate_1x1(t *testing.T) {
	matrix := [][]int{{1}}
	Rotate(matrix)
	expected := [][]int{{1}}

	if !reflect.DeepEqual(matrix, expected) {
		t.Errorf("Expected %v, got %v", expected, matrix)
	}
}

func TestRotate_2x2(t *testing.T) {
	matrix := [][]int{{1, 2}, {3, 4}}
	Rotate(matrix)
	expected := [][]int{{3, 1}, {4, 2}}

	if !reflect.DeepEqual(matrix, expected) {
		t.Errorf("Expected %v, got %v", expected, matrix)
	}
}

func TestRotate_3x3(t *testing.T) {
	matrix := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	Rotate(matrix)
	expected := [][]int{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}

	if !reflect.DeepEqual(matrix, expected) {
		t.Errorf("Expected %v, got %v", expected, matrix)
	}
}
