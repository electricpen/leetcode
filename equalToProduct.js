const equalToProduct = (product, list) => {
  let hash = {};
  let found = false;
  list.map(x => (hash[x] = x));
  list.forEach(number => {
    const target = product / number;
    if (product % number === 0) {
      for (key in hash) {
        if (parseInt(key) === target) {
          found = true;
        }
      }
    }
  });
  return found;
};

console.log(equalToProduct(2, [1, 2, 3, 4, 5]));
