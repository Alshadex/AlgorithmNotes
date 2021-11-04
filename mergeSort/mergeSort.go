package main

import (
    "fmt"
    "os"
	"strconv"
)


/*
Run this go file by doing:
$ go run mergeSort.go 4 3 2 1
Array to sort: [4 3 2 1]
Sorted Array: [1 2 3 4]
*/


func mergeSort(lst []int) []int {
	if len(lst) <= 1 {
		return lst
	}
	mid := len(lst) / 2
	left := lst[:mid]
	right := lst[mid:]
	left_s := mergeSort(left)
	right_s := mergeSort(right)
	result := merge(left_s, right_s)
	return result
}


func merge(lst1 []int, lst2 []int ) []int {
	lst := []int{}
	i, j := 0, 0

	for (i < len(lst1) && j < len(lst2)) {
		if lst1[i] < lst2[j] {
			lst = append(lst, lst1[i])
			i++
		} else {
			lst = append(lst, lst2[j])
			j++
		}
	}
	result := append(lst, lst1[i:]...)
	result = append(result, lst2[j:]...)
	return result
}


func main() {

    argsWithoutProg := os.Args[1:]
    fmt.Println("Array to sort:", argsWithoutProg)

	// Convert string array to int array
	var toSort = []int{}
	for _, i := range argsWithoutProg {
        j, err := strconv.Atoi(i)
        if err != nil {
            panic(err)
        }
        toSort = append(toSort, j)
    }
	fmt.Println("Sorted Array:", mergeSort(toSort))
}
