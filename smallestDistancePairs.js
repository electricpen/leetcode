var smallestDistancePair = function(nums, k) {
  var sum = (acc, val) => {
    return Math.abs(acc - val);
  };
  let results = {};
  let diff = [];
  // k =
  const numericSort = (a, b) => {
    return a - b;
  };
  nums.sort(numericSort);
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (i !== j) {
        results[nums[i] + " " + nums[j]] = true;
      }
    }
  }
  for (pair in results) {
    diff.push(pair.split(" ").reduce(sum));
  }
  diff.sort(numericSort);
  return diff[k - 1] === undefined ? diff[diff.length - 1] : diff[k - 1];
};

console.log(smallestDistancePair([1, 6, 1], 3));
