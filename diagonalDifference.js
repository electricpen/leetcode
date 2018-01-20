function diagonalDifference(a) {
  // Complete this function
  const n = a[0, 0][0];
  const sumMajorDiagonal = matrix => {
    let sum = 0;
    let row = 1;
    let col = 0;
    // 1,0 --> n, n - 1
    for (let i = 0; i < n; i++) {
      sum += matrix[row + i][col + i];
    }
    return sum;
  };
  const sumMinorDiagonal = matrix => {
    let sum = 0;
    let row = 1;
    let col = n - 1;
    // 1, n-1 -> n, 0
    for (let i = 0; i < n; i++) {
      sum += matrix[row + i][col - i];
    }
    return sum;
  };
  return Math.abs(sumMajorDiagonal(a) - sumMinorDiagonal(a));
}

console.log(diagonalDifference([
  [3],
  [11, 2, 4],
  [4, 5, 6],
  [10, 8, -12]
]));
console.log(diagonalDifference([
  [2],
  [1, 3],
  [3, 4]
]));

