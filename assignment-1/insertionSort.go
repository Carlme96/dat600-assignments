package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

func insertionSort(input []int) []int {
	for j := 1; j < len(input); j++ {
		key := input[j]
		i := j - 1
		for i >= 0 && input[i] > key {
			input[i+1] = input[i]
			i = i - 1
		}
		input[i+1] = key
	}
	return input
}

func mergeSort(input []int) []int {
	if len(input) > 1 {
		mid := len(input) / 2
		left := make([]int, mid)
		right := make([]int, len(input)-mid)
		copy(left, input[:mid])
		copy(right, input[mid:])
		left = mergeSort(left)
		right = mergeSort(right)
		return merge(left, right)
	}
	return input
}

func merge(left []int, right []int) []int {
	merged := make([]int, len(left)+len(right))
	left = append(left, 1e12)
	right = append(right, 1e12)
	i := 0
	j := 0
	for k := 0; k < len(left)+len(right)-2; k++ {
		if left[i] < right[j] {
			merged[k] = left[i]
			i++
		} else {
			merged[k] = right[j]
			j++
		}
	}
	return merged
}

func time_insertion() {
	points := 13
	var arr []int
	f, _ := os.Create("result_insertion.txt")
	x := 6
	for i := 0; i <= points; i++ {

		arr = rand.Perm(x)

		start := time.Now()
		insertionSort(arr)

		elapsed := time.Since(start).Nanoseconds()
		result := fmt.Sprintf("%d %d\n", x, elapsed)
		f.WriteString(result)
		x = x * 2
	}
}

func time_merge() {
	points := 13
	var arr []int
	f, _ := os.Create("result_merge.txt")
	x := 6
	for i := 0; i <= points; i++ {

		arr = rand.Perm(x)

		start := time.Now()
		mergeSort(arr)

		elapsed := time.Since(start).Nanoseconds()
		result := fmt.Sprintf("%d %d\n", x, elapsed)
		f.WriteString(result)
		x = x * 2
	}
}

func main() {
	time_insertion()
	time_merge()
}
