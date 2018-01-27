const spiralTraversal = n => {
  // Check for bad inputs
  if (n < 1) {
    return null;
  }
  // Initialize array
  let matrix = [];
  for (let i = 0; i < n; i++) {
    matrix.push([]);
    for (let j = 0; j < n; j++) {
      matrix[i].push(0);
    }
  }
  // Initialize edges
  let border = {
    top: 0,
    right: n - 1,
    bottom: n - 1,
    left: 0
  };

  // Initialize counter
  let steps = 1;
  // Do one Lap
  while (steps <= n * n) {
    // Fill top row
    for (let i = border.left; i <= border.right; i++) {
      matrix[border.top][i] = steps;
      steps++;
    }
    // Fill right row
    for (let j = border.top + 1; j <= border.bottom; j++) {
      matrix[j][border.right] = steps;
      steps++;
    }
    // Fill bottom row
    for (let k = border.right - 1; k >= border.left + 1; k--) {
      matrix[border.bottom][k] = steps;
      steps++;
    }
    //Fill left row
    for (let l = border.bottom; l >= border.top + 1; l--) {
      matrix[l][border.left] = steps;
      steps++;
    }

    // Adjust borders
    border.top++;
    border.right--;
    border.bottom--;
    border.left++;
  }

  // Testing area
  matrix.forEach(row => {
    console.log(row);
  });
};

spiralTraversal(4);
