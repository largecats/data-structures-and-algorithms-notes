# Array

**Referential array.** Array of object references.

<div style="text-align: center"><img src="./images/referential_array.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

E.g., Python lists, tuples.

**Compact array.** Array that store bits representing primary data.

<div style="text-align: center"><img src="./images/compact_array.png" width="300px" /></div>
<div align="center">
<sup></sup>
</div>

**Dynamic array.** Resizable array that grows or shrinks based on the number of items it contains, so that its operations can have amortized $O(1)$ runtime.

E.g., Python list is implemented using dynamic array.

| Operation                                   | Runtime                      |
| ------------------------------------------- | ---------------------------- |
| `data[j] = val`                             | $O(1)$                       |
| `data.append(value)`                        | $O(1)$*                      |
| `data.insert(k, value)`                     | $O(n-k+1)$* (element shifts) |
| `data.pop()`                                | $O(1)$*                      |
| `data.pop(k)`<br/> `del data[k]`            | $O(n-k)$* (element shifts)   |
| `data.remove(value)`                        | $O(n)$*                      |
| `data1.extend(data2)`<br/> `data1 += data2` | $O(n_2)$*                    |
| `data.reverse()`                            | $O(n)$                       |
| `data.sort()`                               | $O(n\log n)$                 |

* Amortized.

Reversing list:
```ocaml
# let rev list =
    let rec aux acc = function
      | [] -> acc
      | h::t -> aux (h::acc) t in
    aux [] list;;
```

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Stack

| Method         | Description                               | Runtime |
|----------------|-------------------------------------------|---------|
| `S.push(e)`    | Add e to top of stack.                    | $O(1)$* |
| `S.pop()`      | Remove and return item from top of stack. | $O(1)$* |
| `S.top()`      | Return reference to item at top of stack. | $O(1)$  |
| `S.is_empty()` | True if the stack is empty.               | $O(1)$  |
| `len(S)`       | Return the number of items in the stack.  | $O(1)$  |

*If implemented using a Python list, these operations are amortized.

Applications: 
1. Reverse a list (push all items in and pop them one by one, first in last out). 
2. Parenthesis matching.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Queue

| Method         | Description                                 | Runtime |
|----------------|---------------------------------------------|---------|
| `Q.enqueue(e)` | Add `e` to end of queue.                    | $O(1)$* |
| `Q.dequeue()`  | Remove and return item from front of queue. | $O(1)$* |
| `Q.first()`    | Return item at front of queue.              | $O(1)$  |
| `Q.is_empty()` | True if the queue is empty.                 | $O(1)$  |
| `len(Q)`       | Return the number of items in the queue.    | $O(1)$  |

*If implemented using a Python list (circular, wraps around when reaching end of list), these operations are amortized.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Deque

Double-ended queue. ADT that can add and remove elements from both ends of the queue.

| Method                                  | Description                                          | Runtime |
|-----------------------------------------|------------------------------------------------------|---------|
| `D.add_first(e)`, `D.add_last(e)`       | Add `e` to front/back of dequeue.                    | $O(1)$* |
| `D.delete_first(e)`, `D.delete_last(e)` | Remove and return item from front/back of dequeue.   | $O(1)$* |
| `D.first()`, `D.last()`                 | Return and return item at the front/back of dequeue. | $O(1)$  |
| `D.is_empty()`                          | True if the dequeue is empty.                        | $O(1)$  |
| `len(D)`                                | Return the number of items in the dequeue.           | $O(1)$  |

*If implemented using a Python list (circular, wraps around), these operations are amortized.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Linked List

## Singly Linked List

<div style="text-align: center"><img src="./images/singly_linked_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Applications:
1. Implement the Stack ADT, all operations are worst-case $O(1)$.
2. Implement the Queue ADT, all operations are worst-case $O(1)$.

## Circularly Linked List

<div style="text-align: center"><img src="./images/circularly_linked_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Applications:
1. Implement the Queue ADT, with more efficient method for wrapping around.

## Doubly Linked List

<div style="text-align: center"><img src="./images/doubly_linked_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Applications:
1. Implement the Deque ADT.
2. Implement the Positional List ADT.

## Positional List

<div style="text-align: center"><img src="./images/positional_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

| Method                                    | Description                                                |
|-------------------------------------------|------------------------------------------------------------|
| `L.first()`, `L.last()`                   | Return the position of the first/last item.                |
| `L.before(p)`, `L.after(p)`               | Return the position immediately before/after position `p`. |
| `L.is_empty()`                            | True if the positional list is empty.                      |
| `len(L)`                                  | Return the number of items in the positional list.         |
| `iter(L)`                                 | Return a forward iterator of items in the positional list. |
| `L.add_first(e)`, `L.add_last(e)`         | Add `e` to the front/back of the positional list.          |
| `L.add_before(p, e)`, `L.add_after(p, e)` | Add `e` before/after position `p`.                         |
| `L.replace(p, e)`                         | Replace the item at position `p` with `e`.                 |
| `L.delete(p)`                             | Remove and return the item at position `p`.                |

Applications:
1. Maintain access frequencies.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Array-based vs. Linked-based

| Metrics               | Array-based                                | Link-based                                                    |
|-----------------------|--------------------------------------------|---------------------------------------------------------------|
| access based on index | $O(1)$                                     | $O(n)$                                                        |
| search                | $O(\log n)$ if sorted (binary search)      | $O(n)$                                                        |
| insertion, deletion   | $O(n)$ worst case (need to shift elements) | $O(1)$ at arbitrary position                                  |
| memory usage          | $2n$ worst case (after resize)             | $2n$ for singly-linked lists<br/>$3n$ for doubly-linked lists |


Compromise between array-based and link-based structures: Skip lists achieve average $O(\log n)$ search and update operations via a probabilistic method.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Tree

## General Tree

**Tree.** A tree $T$ is set of nodes storing elements such that the nodes have a parent-child relationship that satisfies the following properties:

* If $T$ is nonempty, it has a special node, called the root of $T$ , that has no parent.
* Each node $v$ of $T$ different from the root has a unique parent node $w$; every node with parent $w$ is a child of $w$.

**Sibling.** Two nodes are siblings if they have the same parent node.

**External.** A node is external if it has no children. A.k.a leaves.

**Internal.** A node is internal if it has >= 1 children.

**Edge.** An edge of tree $T$ is a pair of nodes $(u,v)$ such that $u$ is the parent of $v$, or vice versa.

**Path.** A path of $T$ is a sequence of nodes such that any two consecutive nodes in the sequence form an edge.

**Ordered Tree.** A tree is ordered if there is a meaningful linear order among the children of each node.

**Depth of node.** The depth of a node is the number of its ancestors, excluding itself.

**Depth of node (recursive).** If $p$ is the root, then its depth is $0$. Otherwise, the depth of $p$ is $1 +$ depth of $p$'s parent.

**Height of node (recursive).** If $p$ is a leaf, then its height is $0$. Otherwise, the height of $p$ is $1 +$ the maximum of $p$'s children's heights.

**Height of tree.** The height of a tree is the height of its root.

**Proposition.** The height of a nonempty tree is the maximum of its leaves' depths.

**Proposition.** In a tree with $n$ nodes, the sum of the number of children of all nodes is $n-1$.

**Proof.** Every node except for the root is some other node's child.

| Method              | Description                                         | Runtime    |
|---------------------|-----------------------------------------------------|------------|
| `T.root()`          | Return the position of the tree's root.             |            |
| `T.is_root(p)`      | True if position `p` is the tree's root.            |            |
| `T.parent(p)`       | Return the position of `p`'s parent.                |            |
| `T.num children(p)` | Return the number of `p`'s children.                |            |
| `T.children(p)`     | Generate an iteration of position `p`'s children.   |            |
| `T.is leaf(p)`      | True if position `p` does not have any children.    |            |
| `len(T)`            | Return the number of positions in the tree.         |            |
| `T.is empty()`      | True if the tree does not contain any position.     |            |
| `T.positions()`     | Generate an iteration of the positions in the tree. |            |
| `iter(T)`           | Generate an iteration of the elements in the tree.  |            |
| `T.depth(p)`        | Return the depth of `p`.                            | $O(d_p+1)$ |
| `T.height()`        | Return the height of `T`.                           | $O(n)$*    |

*`T.height()` computes height recursively, and it takes $O(\sum_p (1+c_p)) = O(n + \sum_p c_p)$ ($c_p$ is number of `p`
s children), which is $O(n + (n - 1)) = O(n)$ time by the above proposition.

## Binary Tree

**Binary tree.** A binary tree is an ordered tree such that:
1. Every node has at most two children.
2. Each child node is either a left child or a right child.
3. A left child precedes a right child in the order of children of a node.

**Binary tree (recursive).** A binary tree is either empty or consists of:
* A node $r$, called the root of $T$, that stores an element.
* A binary tree (possibly empty), called the left subtree of $T$.
* A binary tree (possibly empty), called the right subtree of $T$.

| Method                    | Description                                    |
|---------------------------|------------------------------------------------|
| `T.left(p)`, `T.right(p)` | Return the position of `p`'s left/right child. |
| `T.sibling(p)`            | Return the position of `p`'s sibling.          |

**Proper/Full.** A binary tree is proper or full if each node has either zero or two children. That is, all its internal nodes have two children.

**Proposition.** In a nonempty proper binary tree $T$, with $n_E$ external nodes and $n_I$ internal nodes, we have $n_E = n_I +1$.

**Proof.** If $h$ is $T$'s height, then $n_E = 2^h$, $n_I = 2^0 + 2^1 + 2^2 + \cdots 2^h = 2^h-1$.

## Implementations

### Linked Binary Tree

<div style="text-align: center"><img src="./images/linked_binary_tree.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

| Method                                  | Description                                                         |
|-----------------------------------------|---------------------------------------------------------------------|
| `T.add_root(e)`                         | Add root `e` to an empty tree.                                      |
| `T.add_left(p, e)`, `T.add_right(p, e)` | Add `e` as left/right child to `p`.                                 |
| `T.replace(p, e)`                       | Replace element at position `p` with `e`.                           |
| `T.delete(p)`                           | Remove the node at position `p` and replace it with its only child. |
| `T.attach(p, T1, T2)`                   | Attach `T1`, `T2` as left and right subtress of the leaf `p`.       |

| Operation                                                                | Runtime    |
|--------------------------------------------------------------------------|------------|
| `len`, `is_empty`                                                        | $O(1)$     |
| `root`, `parent`, `left`, `right`, `sibling`, `children`, `num_children` | $O(1)$     |
| `is_root`, `is_leaf`                                                     | $O(1)$     |
| `depth(p)`                                                               | $O(d_p+1)$ |
| `height`                                                                 | $O(n)$     |
| `add_root`, `add_left`, `add_right`, `replace`, `delete`, `attach`       | $O(1)$     |

### Array-based Binary Tree

For every position $p$ of $T$ , let $f(p)$ be the integer defined as follows.
* If $p$ is the root of $T$, then $f(p) = 0$.
* If $p$ is the left child of position $q$, then $f(p) = 2f(q) + 1$.
* If $p$ is the right child of position $q$, then $f(p) = 2f(q) + 2$.

An array-based structure $A$ (such as a Python list) of capacity $N$, with the element at position $p$ of $T$ stored at $A[f(p)]$.

<div style="text-align: center"><img src="./images/array_based_binary_tree.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Drawbacks:
* Space usage depends on the binary tree's shape.
  * Worst case: All nodes in the right subtree of previous node, $N = 2^n-1$. 
  * Best case: Binary tree is complete (e.g., heap), $N=n$.
* `delete` is $O(n)$ as all the node's descendants need to be shifted in the array.

### Linked General Tree

<div style="text-align: center"><img src="./images/linked_general_tree.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

| Operation                              | Runtime    |
|----------------------------------------|------------|
| `len`, `is_empty`                      | $O(1)$     |
| `root`, `parent`, `is_root`, `is_leaf` | $O(1)$     |
| `children(p)`                          | $O(c_p+1)$ |
| `depth(p)`                             | $O(d_p+1)$ |
| `height`                               | $O(n)$     |

## Tree Traversal Algorithms

Traversals are $O(n)$ as they must visit every node in the tree.

Binary search is $O(\log n)$ in a proper binary tree.

### Preorder (General Tree)

Visit node, then visit node's children.

<div style="text-align: center"><img src="./images/preorder_traversal.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

### Postorder (General Tree)

Visit node's children, then visit node.

<div style="text-align: center"><img src="./images/postorder_traversal.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

### Breadth-first (General Tree)

Visit nodes level by level.

Not recursive.

<div style="text-align: center"><img src="./images/breadth_first_traversal.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Dequeue to get node. Visit node, then enqueue node's children.

<div style="text-align: center"><img src="./images/breadth_first_pseudo_code.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

### Inorder (Binary Tree)

Visit left subtree. Visit right subtree. Visit node.

<div style="text-align: center"><img src="./images/inorder_traversal.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Priority Queue

| Method           | Description                                                           |
|------------------|-----------------------------------------------------------------------|
| `P.add(k, v)`    | Add item with key `k` and value `v` into the priority queue.          |
| `P.min()`        | Return item with the minimum key in the priority queue.               |
| `P.remove_min()` | Remove and return an item with the minimum key in the priority queue. |
| `P.is_empty()`   | True if the priority queue is empty.                                  |
| `len(P)`         | Return the number of items in the priority queue.                     |

## Unsorted Priority Queue

Add item to the end of the priority queue, find minimum to remove in $O(n)$.

$O(1)$ insertions, $O(n)$ removals (best-case, because it always takes $O(n)$ to find the minimum).

| Method           | Runtime |
|------------------|---------|
| `P.add(k, v)`    | $O(1)$  |
| `P.min()`        | $O(n)$  |
| `P.remove_min()` | $O(n)$  |
| `P.is_empty()`   | $O(1)$  |
| `len(P)`         | $O(1)$  |

## Sorted Priority Queue

Maintain sortedness when inserting items, minimum is at front of the priority queue,

$O(n)$ insertions (best-case is $O(1)$, because the items may come in as sorted), $O(1)$ removals.

| Method           | Runtime |
|------------------|---------|
| `P.add(k, v)`    | $O(n)$  |
| `P.min()`        | $O(1)$  |
| `P.remove_min()` | $O(1)$  |
| `P.is_empty()`   | $O(1)$  |
| `len(P)`         | $O(1)$  |

## Sorting with Priority Queue

1. Add each item one by one to the priority queue.
2. Keep removing the minimum from the priority queue.

| Implementation/Operation | `add`                                                 | `remove_min`                                 |
|--------------------------|-------------------------------------------------------|----------------------------------------------|
| Unsorted List            | Add to the end of list in $O(1)$.                     | Find minimum to remove in best-case $O(n)$.  |
| Sorted List              | Insert into sorted list in $O(n)$ (best-case $O(1)$). | Remove minimum from front of list in $O(1)$. |

With unsorted list-based priority queue, this is selection-sort (best case $O(n^2)$). With sorted list-based priority queue, this is insertion-sort (best-case $O(n)$).

## Adaptable Priority Queue

Additional operations:
1. Remove arbitrary entry.
2. Update the key (priority) of exiting entry.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Heap

A heap is a binary tree $T$ that satisfies the following:

**Heap-Order Property.** (relational): In a heap $T$, for every position $p$ other than the root, the key stored at $p$ >= the key stored at $p$’s parent. (So the minimum is at the heap's root.)

**Complete Binary Tree Property.** (structural): A heap $T$ with height $h$ is a complete binary tree if levels $0,1,2, \ldots ,h− 1$ of $T$ have the maximum number of nodes possible and the remaining nodes at level $h$ reside in the leftmost positions.

<div style="text-align: center"><img src="./images/complete_binary_tree.png" width="400px" /></div>
<div align="center">
<sup></sup>
</div>

**Proposition.** A heap $T$ storing $n$ entries has height $h = \text{floor}(\log n)$.

## Heap-based Priority Queue

Add:
1. Add item to rightmost node at bottom level to maintain completeness.
2. Up-heap bubbling to swap the new node into correct position to maintain heap-order.

<div style="text-align: center"><img src="./images/upheap_bubbling.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Remove:
1. Remove minimum item from top of heap (root).
2. Copy item at rightmost node at bottom level to root.
3. Down-heap bubbling to swap the node into correct position to maintain heap order.

<div style="text-align: center"><img src="./images/downheap_bubbling.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

| Method           | Runtime      |
|------------------|--------------|
| `P.add(k, v)`    | $O(\log n)$* |
| `P.min()`        | $O(1)$       |
| `P.remove_min()` | $O(\log n)$* |
| `P.is_empty()`   | $O(1)$       |
| `len(P)`         | $O(1)$       |

*For array-based-tree-based heap, this is amortized, but array-based heap can locate last position in $O(1)$ via index access.

| Implementation/Operation | `add`                                                                         | `remove_min`                                                                                                                              |
|--------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Unsorted List            | Add to the end of list in $O(1)$.                                             | Insert into sorted list in $O(n)$.                                                                                                        |
| Sorted List              | Find minimum in $O(n)$ to remove.                                             | Remove minimum from front of list in $O(1)$.                                                                                              |
| Array-based Heap         | 1. Find last position in $O(1)$.<br/>2. Up-heap bubbling in $O(\log n)$.      | 1. Remove minimum at root in $O(1)$.<br/>2. Find last position and copy to root in $O(1)$.<br/>3. Down-heap bubbling in $O(\log n)$.      |
| Linked Heap              | 1. Find last position in $O(\log n)$.<br/>2. Up-heap bubbling in $O(\log n)$. | 1. Remove minimum at root in $O(1)$.<br/>2. Find last position and copy to root in $O(\log n)$.<br/>3. Down-heap bubbling in $O(\log n)$. |

## Heap-Sort

Since `add` and `remove_min` are both $O(\log n)$ for heap-based priority queue, heap-sort is $O(n\log n)$.

In-place heap-sort (can sort in-place because heap is complete binary tree which doesn't have gaps in array-based representation):

<div style="text-align: center"><img src="./images/heap_sort_in_place.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/heap_sort_in_place_phase_2.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Map

Python uses dictionary to represent namespace. Can assume $O(1)$ lookup time.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Hash Table

Hash table is a lookup table structure that supports $O(1)$ lookup when implementing maps. The fast lookup is made possible by directly computing the hash table index from the map's key $k$ via a hash function $h(k)$.

## Hash Functions

We store the item $(k,v)$ in the bucket $A[h(k)]$.

A hash function has two parts:
1. Hash code: keys $\to \mathbb{Z}$.
2. Compression function: $\mathbb{Z} \to [0, N-1]$ ($N$ is the number of entries in the hash table).

<div style="text-align: center"><img src="./images/hash_function.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

### Hash codes

1. Interpret keys as integers. If overflow, sum the upper and lower 32-bits, or take bitwise exclusive-or. Does not preserve meaningful order in the key's individual components (e.g., characters in strings), if any.
2. Polynomial in nonzero constant $a$.  $x_0a^{n-1} + x_1a^{n-2} + \cdots + x_{n-2}a + x_{n-1}$.
3. Cyclic shift. Sum each character in the key and shift the partial sum's bits cyclically in between.

### Compression functions

1. "Division Method": $x \to x\mod N$.
2. "MAD Method": $x \to [(ax + b) \mod p] \mod N$.

## Collision-handling schemes

### Separate Chaining

<div style="text-align: center"><img src="./images/separate_chaining.png" width="400px" /></div>
<div align="center">
<sup></sup>
</div>

### Open Addressing

#### Linear Probing

Iteratively tries the buckets $A[(h(k)+ i) \mod N]$, for $i = 0, 1, 2,\ldots$, until finding an empty bucket.

<div style="text-align: center"><img src="./images/linear_probing.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

#### Quadratic Probing

Iteratively tries the buckets $A[(h(k)+ f(i)) \mod N]$, for $i = 0, 1, 2,\ldots$, where $f(i)=i^2$, until finding
an empty bucket.

#### Double Hashing

For secondary hash function $h'(i)$, iteratively tries the buckets $A[(h(k)+ f(i)) \mod N]$, for $i = 0, 1, 2,\ldots$, where $f(i)=i\cdot h'(i)$, until finding an empty bucket.

## Rehashing

**Load factor.** If $n$ is the number of entries in a bucket array of capacity $N$, then the hash table's load factor is $\lambda = n/N$.

For each collision-handling scheme, there's a load factor threshold. If the load factor exceeds the threshold, the lookup efficiency starts degrading. For separate chaining, this is $0.9$, linear probing $0.5$, and Python dictionary's opening addressing $2/3$.

After the threshold is exceeded, the hash table is usually resized to twice the capacity (and all entries rehashed) to restore efficiency.

## Sorted Search Table

A hash table where keys are sorted. The sortedness of the keys support inexact search such as searching for a range of keys.

Array-based implementation of the sorted search table allows $O(\log n)$ search via binary search, though update operations are $O(n)$ because elements need to be shifted.

## Set

**Set.** An unordered collection of elements, without duplicates, that typically supports efficient membership tests (e.g., using hash tables). 

Sets are implemented using hash tables in Python. In fact, they are like maps with keys without values.

**Multiset.** A multiset is like a set but allows duplicates.

**Multimap.** A multimap is like a map but allows the same key to map to multiple values.

| Operation      | Description                                     |
|----------------|-------------------------------------------------|
| `S.add(e)`     | Add `e` to the set if it's not yet in the set.  |
| `S.discard(e)` | Remove `e` from the set if it's in the set.     |
| `e in S`       | True if `e` is in the set.                      |
| `len(S)`       | Return the number of elements in the set.       |
| `iter(S)`      | Return an iteration of the elements in the set. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Search Tree

## Binary Search Tree

**Binary search tree.** A binary tree $T$ with each position $p$ storing a key-value pair $(k,v)$ such that:
• Keys in $p$'s left subtree are $< k$.
• Keys in $p$'s right subtree are $> k$.

**Proposition.** An inorder traversal of a binary search tree visits positions in increasing order of their keys.

**Successor of node.** The successor of the node at position $p$ is the node with the smallest value that is $>= p$ (the next node to visit right after $p$ in an inorder traversal). 

* If $p$ has a right subtree, this is the leftmost node in its right subtree. 
* Else, this is the nearest ancestor such that $p$ is in its left subtree.

**Predecessor of node.** The predecessor of the node at position $p$ is the node with the largest value that is $<= p$ (the node visited right before $p$ in an inorder traversal). 

* If $p$ has a left subtree, this is the rightmost node in its left subtree. 
* Else, this is the nearest ancestor such that $p$ is in its right subtree.

### Deletion

If node to delete has only one child, replace it with its child:

<div style="text-align: center"><img src="./images/bst_deletion_one_child.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>
If node to delete has two children, 

1. replace it with its predecessor, and 
2. replace its predecessor with its predecessor's child (the case above):


<div style="text-align: center"><img src="./images/bst_deletion_two_children.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

### Efficiency

Efficiency of binary search in a binary search tree depends on its height.

<div style="text-align: center"><img src="./images/binary_search.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>
This motivates the following methods to balance a binary search tree.


## Balanced Search Tree

### Rotation

<div style="text-align: center"><img src="./images/single_rotation.png" width="600px" /></div>
<div align="center">
<sup>Rotating y above parent z, with x remaining as y's subtree.</sup>
</div>

<div style="text-align: center"><img src="./images/double_rotation.png" width="600px" /></div>
<div align="center">
<sup>Rotating x above parent y, then above grandparent z (with y remaining as x's subtree).</sup>
</div>

After the first rotation, the first tree becomes
```
a=z
    b=x
        c=y
```
And the second tree becomes
```
        c=z
    b=x
a=y
```
Rotating $x$ above $z$ gives the result (the relation between $x$ and $y$ remains unchanged in this rotation).

### AVL Tree

An AVL tree is a binary search that satisfies the following:

**Height balance property.** For every position $p$ of $T$, the heights* of the children of $p$ differ by at most $1$.

**\*Height of node (alternate definition).** Number of nodes (instead of edges) in a longest path from $p$ to a leaf. E.g., height of a leaf is $1$.

<div style="text-align: center"><img src="./images/avl_tree.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

**Proposition.** The height of an AVL tree storing $n$ entries is $O(\log n)$.

**Balanced node.** In a binary search tree $T$, a position is balanced if the absolute value of the difference between the heights of its children is at most $1$.

So the height balance property <=> every node is balanced.

<div style="text-align: center"><img src="./images/avl_tree_insertion.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/avl_tree_deletion.png" width="600px" /></div>
<div align="center">
<sup>For deletion, need to continue walking upward to repair further unbalances, until reaching the root. The number of operations is bounded by tree height O(log n).</sup>
</div>

So AVL tree guarantees $O(\log n)$ bound for binary search tree operations.

<div style="text-align: center"><img src="./images/avl_tree_performance.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

### Splay Tree

Moves more frequently accessed nodes closer to the root.

Amortized $O(\log n)$ for search, insertions, deletions.

### (2, 4) Tree

Particular case of a multiway search tree, where each node may have multiple children. Each internal node has 2, 3, or 4 children.

Operations' runtime is the same as AVL tree.

### Red-Black Tree

Only requires $O(1)$ structural operations for rebalancing (instead of $O(\log n)$ as in AVL tree).

A red-black tree is a binary search tree with nodes colored red and black such that:<br/>
**Root Property.** The root is black.<br/>
**Red Property.** The children of a red node (if any) are black.<br/>
**Depth Property.** All nodes with zero or one children have the same black depth, defined as the number of black ancestors. (Recall that a node is its own ancestor).

**Proposition.** The height of a red-black tree storing $n$ entries is $O(\log n)$.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Sorting

Runtime of sorting algorithms is bounded from above by $O(n!)$, because sorting produces a permutation of the original sequence, and there are $n!$ permutations.

Runtime of comparison-based sorting is bounded from below by $\Omega(n\log n)$.

<div style="text-align: center"><img src="./images/comparison_based_sorting_lower_bound.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

## Insertion-Sort

Maintain a sorted sub-list at the front, keep inserting the next element from the unsorted sub-list into the sorted sub-list to make sure it stays sorted.

| Scenario   | Runtime  | Description                      |
|------------|----------|----------------------------------|
| Worst case | $O(n^2)$ | When input is sorted in reverse. |
| Best case  | $O(n)$   | When input is sorted.            |
| Average    | $O(n^2)$ |                                  |

<div style="text-align: center"><img src="./images/insertion_sort_pseudo_code.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/insertion_sort_pic.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

## Selection-Sort

Maintain a sorted sub-list at the front, keep selecting the minimum from the unsorted sub-list and swapping it to the end of the sorted sub-list.

| Scenario   | Runtime  | Description                |
|------------|----------|----------------------------|
| Worst case | $O(n^2)$ |                            |
| Best case  | $O(n^2)$ | Even when input is sorted. |
| Average    | $O(n^2)$ |                            |

<div style="text-align: center"><img src="./images/selection_sort.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>


## Bubble-Sort

Make $n$ passes, swapping every two items into order in each pass.

| Scenario   | Runtime  | Description                      |
|------------|----------|----------------------------------|
| Worst case | $O(n^2)$ | When input is sorted in reverse. |
| Best case  | $O(n)$   | When input is sorted.            |
| Average    | $O(n^2)$ |                                  |

<div style="text-align: center"><img src="./images/bubble_sort.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

## Heap-Sort

First, add each item to heap. Then, keep popping the minimum from the heap.

With unsorted/sorted list-based heaps, this is selection/insertion-sort.

With linked/array-based binary tree-based heaps, this is heap-sort.
| Scenario   | Runtime      | Description                                                                                                                                 |
|------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Worst case | $O(n\log n)$ |                                                                                                                                             |
| Best case  | $O(n\log n)$ | If input is sorted, adding items to heap is $O(1)$ with array-based heaps, but down-heap bubbling when removing items is still $O(\log n)$. |
| Average    | $O(n\log n)$ |                                                                                                                                             |

## Merge-Sort

Divide and conquer.

1. Divide into two halves.
2. Recursively sort on each half.
3. Merge the sorted halves into a sorted list (where hard work is done).

| Scenario   | Runtime      | Description |
|------------|--------------|-------------|
| Worst case | $O(n\log n)$ |             |
| Best case  | $O(n\log n)$ |             |
| Average    | $O(n\log n)$ |             |

There are $\log n$ levels, and the merge step at each level is $O(n)$ ($O(n/2 * 2)$, $O(n/4 * 4)$, etc). So merge-sort is $O(n\log n)$.

<div style="text-align: center"><img src="./images/merge_sort_runtime.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

## Quick-Sort/Pivot-Sort

Divide and conquer.

1. Pick a pivot.
2. Divide into three parts: < pivot, = pivot, and > pivot (where hard work is done), can be done in-place to save space.
3. Recursively sort the < pivot part and the > pivot part.
4. Merge the sorted parts by concatenation (hard work is alrd done is step 2).

<div style="text-align: center"><img src="./images/in_place_quick_sort.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/in_place_quick_sort_pic.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

If pivot is randomized or divides the list into $1/2$, $1/2$ or $1/4$, $3/4$ at each step, the expected runtime is $O(n\log n)$. If pivot is badly chosen and the list is alrd sorted, runtime could be $O(n^2)$ (sub-list is $O(n)$ for each of the $n$ divisions).

<div style="text-align: center"><img src="./images/quick_sort_runtime.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Quick-Sort is not ideal for short sequences. Hybrid approach: Keep dividing and once the sub-problem size < some threshold, say, 50, switch to using insertion-sort, which is good on short sequences.

## Linear-Time Sorting

If the entries being sorted satisfy some additional constraints, we may avoid using comparisons and sort them in linear time.

Consider the problem of sorting a sequence of entries, each a key-value pair, where the keys have a restricted type.

### Bucket-Sort

If we know that the range of the keys is, say, $[0, N-1]$ where $N$ is a constant, then can sort in $O(n+N) = O(n)$ time.

Given a sequence $S$ with $n$ entries:

1. Create a bucket array $B$ with $N$ entries.
2. Remove each element $k$ from $S$ and insert it at the end of bucket $B[k]$ (stable sort) in case there are multiple entries with the same key ($O(n)$).
3. Iterate the bucket array $B$ from front to back (so that the elements come out sorted), iterate each bucket from front to back (stable sort), remove each entry and insert it at the end of $S$ ($O(N)$).

So if $N$ is $O(n)$ (e.g., a constant), this is linear time.

### Radix-Sort

Given a sequence $S$ with $n$ entries of key-value pairs, can sort in lexicographic order ($(k_1, v_1) < (k_2, v_2)$ if $k_1<k_2$ or $k_1=k_2$ and $v_1<v_2$) in $O(n)$ time.


1. Use stable bucket-sort to sort on the second component $v_i$.
2. Use stable bucket-sort to sort on the first component $k_i$ (stability here guarantees that the sorted second component remains sorted when the first component is the same).

## Comparing Sorting Algorithms

| Algorithm               | Runtime                                        | Stability      | Use case                       |
|-------------------------|------------------------------------------------|----------------|--------------------------------|
| Selection-Sort          | $O(n^2)$ best case                             | Can be stable. |                                |
| Insertion-Sort          | $O(n^2)$ worst/average case, $O(n)$ best case  | Stable.        | Small sequences (<50)          |
| Heap-Sort               | $O(n\log n)$                                   | Not stable.    | Small sequences                |
| Quick-Sort/Pivot-Sort   | $O(n^2)$ worst case, $O(n\log n)$ average case | Not stable.    | Large sequences                |
| Merge-Sort              | $O(n\log n)$ worst case                        | Stable.        | Difficult to do in-place.      |
| Bucket-Sort, Radix-Sort | $O(n)$                                         | Stable.        | Key range is known in advance. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Selection

The selection problem: Selecting the $k$th smallest element from an unsorted collection of $n$ comparable elements.

## Prune-and-Search/Decrease-and-Conquer

E.g., binary search.

### Randomized Quick-Select

Similar to randomized quick-sort.

<div style="text-align: center"><img src="./images/quick_select.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

$O(n)$ average case, $O(n^2)$ worst case.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Text-Processing

## Pattern-Matching

Given a text string $T$ of length $n$ and a pattern string $P$ of length $m$, find whether $P$ is a substring of $T$.

### Brute Force

For each of the $n-m+1$ possible starting index of $P$, try matching each of the $m$ characters in $P$.

$O(mn)$.

### Boyer-Moore

Like brute force, but skip over indices that can't possibly match.

Worst case $O(mn)$.

<div style="text-align: center"><img src="./images/boyer_moore.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/boyer_moore_2.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/boyer_moore_code.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/boyer_moore_example.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

### Knuth-Morris-Pratt (KMP)

Like Boyer-Moore, but use a failure table to make maximum skips upon mismatches.

$O(m+n)$.

<div style="text-align: center"><img src="./images/kmp_example.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/kmp_failure_function_example.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/kmp_code.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/kmp_failure_function.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
# Dynamic Programming

For finding optimal solutions.

## Knapsack Problem

Given $n$ items, their values `values` and weights `weights`, and a knapsack with weight capacity `W`, how to pick items to put in the knapsack such that their total value is highest?

### Brute Force

For each item, it is either included in the knapsack or excluded. $O(2^n)$.

```python
def knapSack(W, weights, values, n): 

    if n == 0 or W == 0: 
        return 0
    if (weights[n-1] > W): # item n is heavier than knapsack capacity, so can't include it
        return knapSack(W, weights, values, n-1) # exclude item n
    else: 
        return max( 
            values[n-1] + knapSack( 
                W-weights[n-1], weights, values, n-1), # include item n
            knapSack(W, weights, values, n-1) # exclude item n
            )
```

### Memoization

We implement memoization by computing, bottom-up, a table `M` as a two-dimensional array, where `M[i][w]` stores the maximal price achievable by taking only the first `i` items while not exceeding the weight `W`. This improves time complexity to $O(n\cdot W)$ by replacing the two recursive calls with two lookups in the memoization table.

```python
def knapSack(W, weights, values, n): 
    M = [[0 for x in range(W + 1)] for x in range(n + 1)] # initialize memoization table
  
    # build memoization table from bottom-up
    for i in range(n + 1): # row is the range of indices of items allowed to take (from 0 to n)
        for w in range(W + 1): # column is weight limit (from 0 to W)
            if i == 0 or w == 0: # if only the first 0 item is allowed to take or if weight limit is 0, maximal price is 0
                M[i][w] = 0
            elif weights[i-1] <= w: # if item's weight <= current weight limit
                M[i][w] = max( # recursive calls replaced by lookups in the memoization table M
                    		values[i-1] + M[i-1][w - weights[i-1]], # take this item
                    		M[i-1][w] # not taking this item
                			)
            else: # if item's weight > current weight limit, update the memoization table M[i][w] to be the same as M[i-1][w] because there's no improvement in price
                M[i][w] = M[i-1][w]
  
    return M[n][W] # return the maximal price achievable by taking all n items while not exceeding the weight limit W
```

Reconstructing the list of items from the memoization table (the first row is ignored as it's full of zeroes):

```
i  item    w  p |  0  1  2  3  4
--------------------------------
0  apple   1  1 |  0  1  1  1  1  
1  melon   2  2 |  0  1  2  3  3  
2  kiwi    1  2 |  0  2  3  4  5  
3  durian  2  3 |  0  2  3  5  6 
```

Let `sack = []` . We start from the rightmost, bottom-most cell: `weight=4` and `i=3`, with price `6`.

* The previous row has price `5`, less than `6` in current row, so durian was taken, and `sack = [3]`.
* We subtract Durian's weight `2` and go to column `4 - 2 = 2` in the same row, repeating the process. The previous row has price `2`, less than `3` in current row, so kiwi was taken, and `sack = [3, 2]`.
* We subtract Kiwi's weight `1` and go to column `2 - 1 = 1` in the same row. The previous row has price `1`, same as current row, so melon was not taken.
* Finally, apple was taken, so `sack = [3, 2, 0]`.

A similar improvement with Fibonacci:

```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```

This is slow because many subproblems are computed repeatedly. E.g.,

```
fib(5) = fib(4) + fib(3) = (fib(3) + fib(2)) + fib(3) = ...
```

Make it faster by "memorizing" the most immediate result:

```python
def fast_fib_helper(a, b, j):
    if j == 1:
        return b
    else:
        return fast_fib_helper(b, a + b, j - 1)
   
def fast_fib(n):
    if n == 0:
        return 1
    else:
        return fast_fib_helper(1, 1, n)
```





# Graph

**Graph.** A graph $G$ is a set $V$ of vertices and a collection $E$ of pairs of vertices from $V$, called edges. 

* A way of representing relations among objects in $V$.

**Path.** A path is a sequence of alternating vertices and edges that starts at a vertex and ends at a vertex such that each edge is incident to its predecessor and successor vertex.

**Cycle.** A cycle is a path that starts and ends at the same vertex, and that includes at least one edge. 

**Simple path.** A path is simple if each vertex in the path is distinct.

**Simple cycle.** A cycle is simple if each vertex in the cycle is distinct, except for the first and last one.  

**Spanning subgraph.** A spanning subgraph of $G$ is a subgraph of $G$ that contains all the vertices of the graph $G$. 

## Graph Traversal

### Depth-First Search

<div style="text-align: center"><img src="./images/graph_dfs_pseudo_code.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

<div style="text-align: center"><img src="./images/graph_dfs_code.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>