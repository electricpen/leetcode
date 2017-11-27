function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

var mergeTrees = function (t1, t2) {
  if (t1 && t2) {
    t1.val += t2.val;
  } else if (!t1 && t2) {
    t1 = t2;
  }
  if (t1.left && t2.left) {
    mergeTrees(t1.left, t2.left);
  } else if (!t1.left && t2.left) {
    t1.left = t2.left;
  }
  if (t1.right && t2.right) {
    mergeTrees(t1.right, t2.right);
  } else if (!t1.right && t2.right) {
    t1.right = t2.right;
  }
  return t1;
};

var tree1 = new TreeNode(1);
tree1.left = new TreeNode(2);
tree1.right = new TreeNode(3);
var tree2 = new TreeNode(5);
tree2.left = new TreeNode(2);

console.log(mergeTrees(tree1, tree2));