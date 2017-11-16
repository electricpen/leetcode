function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

var mergeTrees = function(t1, t2) {
  let result = new TreeNode(0);
  /*
  traverse three trees simultaneously(t1, t2, result)
    if both nodes exist, result node equals sum of values
    if both have left, traverse(left)
    if one has left, append that child to result.left
    if both have right, traverse(right)
    if one has right, append that child to result.right
  */
  var traverse = function(t1, t2, r1) {
    if (t1 !== null && t2 !== null) {
      r1.val = t1.val + t2.val;
    } else if (t1.left === null && t2.left !== null) {
      r1.left = t2.left;
    } else if (t1.left !== null && t2.left === null) {
      r1.left = t1.left;
    } else if (t1.right === null && t2.right !== null) {
      r1.right = t2.right;
    } else if (t1.right !== null && t2.right === null) {
      r1.right = t1.right;
    } else if (t1.left !== null && t2.left !== null) {
      r1.left = new TreeNode(0);
      traverse(t1.left, t2.left, r1.left);
    } else if (t1.right !== null && t2.right !== null) {
      r1.right = new TreeNode(0);
      traverse(t1.right, t2.right, r1.right);
    }
  };

  return result;
};

console.log(mergeTrees());
