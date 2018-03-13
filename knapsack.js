const knapsack = (bagSize, lootList) => {
  // I think a reasonable starting point is to order the list by value per weight. You would want to fill the bag with the most valuable items by weight
  let results = [];
  let carryWeight = 0;
  const appraise = function(a, b) {
    return a.value / a.weight - b.value / b.weight;
  };

  lootList.sort(appraise);

  lootList.forEach(item => {
    console.log(item);
  });
};

// Edge Cases: Most valuable item takes up entire bag but the sum of all the other items would be more?
const testCase1 = [
  { value: 10, weight: 5, name: "fancy pot" },
  { value: 1000, weight: 23, name: "large TV" },
  { value: 50, weight: 1, name: "gold watch" },
  { value: 25, weight: 3, name: "silver ornament" },
  { value: 40, weight: 9, name: "stereo receiver" },
  { value: 15, weight: 4, name: "piggy bank" },
  { value: 80, weight: 12, name: "electronics" }
];

const testCase2 = [
  { value: 10, weight: 5, name: "fancy pot" },
  { value: 1000, weight: 23, name: "large TV" },
  { value: 50, weight: 1, name: "gold watch" },
  { value: 25, weight: 3, name: "silver ornament" },
  { value: 100, weight: 10, name: "stereo receiver" },
  { value: 15, weight: 4, name: "piggy bank" },
  { value: 80, weight: 12, name: "electronics" }
];

knapsack(10, testCase2);
