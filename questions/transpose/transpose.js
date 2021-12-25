/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    res = [...matrix]
    console.log(res)
    for (i = 0; i<matrix.length; i++){
        for (j = 0; j < matrix[i].length; j++){
	    console.log(i,j)
	    console.log(res[j][i])
	//console.log(matrix[i][j])
            res[j][i] = matrix[i][j]
        }
    }
	console.log(res)
    return res
};

transpose([[2,4,-1],[-10,5,11],[18,-7,6]])
