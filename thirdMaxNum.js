const thirdMaxNumber = list => {
  let results = [];
  for (let i = 0; i < list.length; i++) {
    if (results.length < 3) {
      if (!results.includes(list[i])) {
        results.push(list[i]);
        results.sort();
      }
    } else {
      if (list[i] > results[0]) {
        results.push(list[i]);
        results.sort();
        results = results.slice(1);
      }
    }
  }
  return results[0];
};
// const add = (list, num) => {
//   if (list.length === 0) {
//     list.push(num);
//   } else {
//     for (let i = list.length; i >= 0; i--) {
//       if (num > list[i]) {
//         list.splice(i, 0, num);
//       }
//     }
//   }
//   return list;
// };

// const thirdMaxNumber = list => {
//   let results = [];
//   for (let i = 0; i < list.length; i++) {
//     if (results.length < 3) {
//       if (!results.includes(list[i])) {
//         add(results, list[i]);
//       }
//     } else if (list[i] > results[0]) {
//       add(results, list[i]);
//       results.splice(1);
//     }
//   }
//   return results[0];
// };

console.log(thirdMaxNumber([3, 2, 1]), " should equal ", "1");
console.log(thirdMaxNumber([3, 2, 2, 1]), " should equal ", "1");
console.log(thirdMaxNumber([3, 2]), " should equal ", "2");
