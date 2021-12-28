package main

func Rotate(matrix [][]int) {
	Transpose(matrix)
	ReverseRows(matrix)
}

func Transpose(matrix [][]int) {
	for i := range matrix {
		for j := range matrix[i] {
			if i < j {
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
			}
		}
	}
}

func ReverseRows(matrix [][]int) {
	for i := range matrix {
		for j := range matrix[i] {
			if j < len(matrix)/2 {
				j_ := len(matrix) - j - 1
				matrix[i][j], matrix[i][j_] = matrix[i][j_], matrix[i][j]
			}
		}
	}
}
