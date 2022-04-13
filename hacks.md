```if n & 1``` same as ```if n % 2```
```n >> 1``` same as ```n //= 2```
```x << y``` same as ```x * (2^y)```
```x >> y``` same as ```x/(2^y)```
```mySqrt(x)=mySqrt(x>>2)<<1```
## ------------------------------------------------
## Here is the funny thing about BST. Inorder traversal is not a unique identifier of BST. At the same time both preorder and postorder traversals are unique identifiers of BST. From these traversals one could restore the inorder one: inorder = sorted(postorder) = sorted(preorder), and inorder + postorder or inorder + preorder are both unique identifiers of whatever binary tree.
## ------------------------------------------------