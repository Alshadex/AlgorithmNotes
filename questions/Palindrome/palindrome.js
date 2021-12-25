/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
    word = x.toString()
    mid = Math.floor(word.length / 2)
    for (let i = 0; i < word.length; i++){
	    j = word.length - 1 - i
	    
	    if (i > j){
		    break
	    }
	    if (word[i] !== word[j]){
		    return false
	    }
    }
    return true
};

console.log(isPalindrome(-121))
