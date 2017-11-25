const balanced_parens = parens => {
  // Takes a string of parentheses and returns index of unmatched parentheses or -1 if string is balanced
  // Iterate through parens
  // record index of each open paren
  // when a close paren is found, pop the most recent index from the open paren list
  // return -1 if parenlist === 0 otherwise return the earliest index
  let parenList = [];
  for (let i = 0; i < parens.length; i++) {
    if (parens[i] === "(") {
      parenList.push(i);
    } else if (parens[i] === ")") {
      if (parenList.length > 0) {
        parenList.pop();
      } else {
        return i;
      }
    }
  }
  return parenList.length === 0 ? -1 : parenList[0];
};

const assert = (expected, actual) => {
  if (JSON.stringify(expected) === JSON.stringify(actual)) {
    console.log("Expected", expected, " is TRUE");
  } else {
    console.log("Expected:", expected, "but instead received:", actual);
  }
};

assert(-1, balanced_parens("()"));
assert(0, balanced_parens(")"));
assert(2, balanced_parens("())"));
assert(0, balanced_parens("(()"));
assert(0, balanced_parens("((())"));
assert(0, balanced_parens("(()()()()"));
