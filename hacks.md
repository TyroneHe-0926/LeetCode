```(From LC #50) if n & 1 same as if n % 2```

```n >> 1 same as n //= 2```

```(From LC #69) x << y same as x * (2^y)```

```x >> y same as x/(2^y)```

```mySqrt(x)=mySqrt(x>>2)<<1```

#### --------------------------------------------------------------------------------------------------
#### (From LC #108) Here is the funny thing about BST. Inorder traversal is not a unique identifier of BST. At the same time both preorder and postorder traversals are unique identifiers of BST. From these traversals one could restore the inorder one: inorder = sorted(postorder) = sorted(preorder), and inorder + postorder or inorder + preorder are both unique identifiers of whatever binary tree.
#### --------------------------------------------------------------------------------------------------
```
"""(From LC #59) Rotating a matrix clockwise in python could be as simple as"""
rotated = list(zip(*original[::-1])

"""Assuming we had"""
og_arr = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

"""After reversing"""
reversed_arr = [[7, 8, 9],
                [4, 5, 6],
                [1, 2, 3]]

"""Next each of the sublists is unpacked and passed as an argument to zip"""
zip([7, 8, 9], [4, 5, 6], [1, 2, 3])

"""Rotated and covert it back to list"""
rotated = [(7, 4, 1), 
           (8, 5, 2), 
           (9, 6, 3)]
```
#### --------------------------------------------------------------------------------------------------
