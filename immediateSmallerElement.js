const immediateSmallerElement = list => {
  const result = [];
  for (var i = 0; i < list.length; i++) {
    if (i === list.length - 1) {
      result.push(-1);
    } else {
      if (list[i] >= list[i + 1]) {
        result.push(list[i + 1]);
      } else {
        result.push(-1);
      }
    }
  }
  return result;
};

console.log(immediateSmallerElement([5, 6, 2, 3, 1, 7]));
