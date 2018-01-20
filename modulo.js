// Subtract Y from X until X is less than Y

const modulo = (x, y) => {
  // edge case
  // if y = 0 return NaN
  if (y === 0) {
    return NaN;
  }
  y = Math.abs(y);
  // base case
  // Check if x is less than y
  if (Math.abs(x) < y) {
    return x;
  }

  // recursive case
  // modulo(x - y, y)
  if (x < 0) {
    return modulo(x + y, y);
  } else {
    return modulo(x - y, y);
  }
};

console.log(modulo(-5, 2), "should equal", -1);
console.log(modulo(-10, 2), "should equal", 0);
console.log(modulo(-14, 3), "should equal", -2);
console.log(modulo(-2, 2), "should equal", 0);
console.log(modulo(5, 0), "should equal", "NaN");
console.log(modulo(5, 1), "should equal", 0);
console.log(modulo(5, 7), "should equal", 5);
