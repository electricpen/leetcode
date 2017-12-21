var smallestDistancePair = function(nums, k) {
  var sum = (acc, val) => {
    return Math.abs(acc - val);
  };
  let results = {};
  let diff = [];
  const numericSort = (a, b) => {
    return a - b;
  };
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
  let list = Array.from(diff);
  list.sort(numericSort);
  k = (k - 1) % list.length;
  return list[k];
};

console.log(smallestDistancePair([62, 100, 4], 2));
