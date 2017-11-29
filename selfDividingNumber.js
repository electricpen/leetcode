const selfDividingNumber = num => {
  if (num === 0) {
    return false;
  }
  let digits = num.toString().split("");
  for (digit of digits) {
    if (num % parseInt(digit) !== 0) {
      return false;
    }
  }
  return true;
};

const selfDividingNumbers = num => {
  let results = [];
  for (var i = 1; i <= num; i++) {
    if (selfDividingNumber(i)) {
      results.push(i);
    }
  }
  return results;
};

const assert = (expected, actual) => {
  if (expected === actual) {
    console.log("Test passed!");
  } else {
    console.log("Expected:", expected, ",but result was:", actual);
  }
};

let test = selfDividingNumbers(128);
for (num of test) {
  console.log(num);
}
