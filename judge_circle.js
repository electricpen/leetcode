var judgeCircle = function(moves) {
  /*
  Input parameter moves is a string
  Output boolean - true if the move list ends with the "robot" in the same place, false if it does not    
*/
  const interpreter = {
    L: -1,
    R: 1,
    U: 1,
    D: -1
  };

  let coords = {
    x: 0,
    y: 0
  };
  moves = moves.toUpperCase();

  for (var i = 0; i < moves.length; i++) {
    if (moves[i] === "L" || moves[i] === "R") {
      coords.x += interpreter[moves[i]];
    } else {
      coords.y += interpreter[moves[i]];
    }
  }
  return coords.x === 0 && coords.y === 0;
};

// Testing area
const assert = (expected, actual) => {
  if (expected === actual) {
    console.log("Test passed!");
  } else {
    console.log("Expected", actual, "to equal", expected);
  }
};

assert(true, judgeCircle("LR"));
assert(true, judgeCircle(""));
assert(true, judgeCircle("lrud"));
assert(false, judgeCircle("L"));
assert(false, judgeCircle("uuddllrrr"));
