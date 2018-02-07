const reversalArray = (list, d) => {
  return list.slice(d).concat(list.slice(0, d));
};

console.log(reversalArray([1, 2, 3, 4, 5], 5));
