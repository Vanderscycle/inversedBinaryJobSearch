/*

Have the function LongestIncreasingSequence(arr) take the array of positive integers stored in arr and return the length of the longest increasing subsequence (LIS). A LIS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in increasing order. The sequence does not need to be contiguous or unique, and there can be several different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], and another is [1, 6]. For this input, your program should return 3 because that is the length of the longest increasing subsequence.

*/
function LongestIncreasingSequence(arr) {

  // code goes here  

  //returned value 
  var longestSub = 1
  //temp values to calculate the  returned value
  var tempLongestSub = 1
  var largestValue = 0

  // I am sorry for the o(n**2) dimension
  for (let [i, v] of arr.entries()) {
    largestValue = v

    //we navigate each subslices
    for (var seq of arr.slice(i)) {

      // Must be increasing
      if (largestValue < seq) {
        // we must keep track of the largest value in the substring and compare it to subsequent values
        largestValue = seq
        tempLongestSub += 1
      }
    }
    // if we found that the substring is the largest one
    if (tempLongestSub > longestSub) {
      longestSub = tempLongestSub
    }
    //reset the counter
    tempLongestSub = 1

  }

  return longestSub; 

}
   
// keep this function call here 
console.log(LongestIncreasingSequence(readline()));
