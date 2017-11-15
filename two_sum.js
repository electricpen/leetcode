var twoSum = function(nums, target) {
  // Given an array of numbers find two elements that add up to the target number
  var result = [];
  for (var i = 0; i < nums.length; i++) {
    for (var j = 0; j < nums.length; j++) {
      if (i !== j) {
        if (nums[i] + nums[j] === target) {
          result = [j, i];
        }
      }
    }
  }
  return result;
};

// testing area
var assert = function(expected, actual) {
  if (expected === actual) {
    console.log("Test passed! (", expected, " = ", actual);
  } else {
    console.log("Expected", actual, "to equal", expected);
  }
};

assert([0, 1], twoSum([2, 7, 11, 15], 9));

/*

  Post Solution Notes:
  The solution I came up was the brute force solution. The time complexity is O(n^2)
  You can reduce time complexity by iterating through the array and placing each item in a hash table with index as value
    You can then iterate through the array one more time and check if the target value exists in the hash table
      Further optimization would be to check if the item's target complement exists in the hash table every time you insert an item.

*/
