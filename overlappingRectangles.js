const overlappingRectangles = (rect1, rect2) => {
  const r1 = {
    top: rect1[1],
    left: rect1[0],
    bottom: rect1[3],
    right: rect1[2]
  };
  const r2 = {
    top: rect2[1],
    left: rect2[0],
    bottom: rect2[3],
    right: rect2[2]
  };

  const inside = (bound1, bound2, target) => {
    return target >= bound1 && target <= bound2;
  };

  if (
    inside(r1.top, r1.bottom, r2.top) ||
    inside(r1.top, r1.bottom, r2.bottom) ||
    inside(r1.left, r1.right, r2.left) ||
    inside(r1.left, r1.right, r2.right) ||
    inside(r2.top, r2.bottom, r1.top) ||
    inside(r2.top, r2.bottom, r1.bottom) ||
    inside(r2.left, r2.right, r1.left) ||
    inside(r2.left, r2.right, r1.right)
  ) {
    return true;
  }
  return false;
};

console.log(overlappingRectangles([0, 0, 4, 4], [4, 6, 10, 5]));
