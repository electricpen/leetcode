var smallestDistancePair = function(nums, k) {
  const numericSort = (a, b) => {
    return a - b;
  };
  nums.sort();
  if (k < nums.length - 2) {
    return Math.abs(nums[0] - nums[k]);
  } else {
    return Math.abs(nums[0] - nums[nums.length - 1]);
  }
};

console.log(smallestDistancePair([1, 6, 1], 3));
