- [Data Structures and Algorithms](#data-structures-and-algorithms)
  - [Array](#array)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Deque](#deque)
  - [Linked List](#linked-list)
    - [Singly Linked List](#singly-linked-list)
    - [Circularly Linked List](#circularly-linked-list)
    - [Doubly Linked List](#doubly-linked-list)
    - [Positional List](#positional-list)
  - [Array-based vs. Linked-based](#array-based-vs-linked-based)
  - [Tree](#tree)

# Data Structures and Algorithms

## Array

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

## Stack

| Method       | Description                               | Runtime |
|--------------|-------------------------------------------|---------|
| S.push(e)    | Add e to top of stack.                    | $O(1)$* |
| S.pop()      | Remove and return item from top of stack. | $O(1)$* |
| S.top(）     | Return reference to item at top of stack. | $O(1)$  |
| S.is_empty() | Whether the stack is empty.               | $O(1)$  |
| len(S)       | Return the number of items in the stack.  | $O(1)$  |

*If implemented using a Python list, these operations are amortized.

Applications: 
1. Reverse a list (push all items in and pop them one by one, first in last out). 
2. Parenthesis matching.

## Queue

| Method       | Description                                 | Runtime |
|--------------|---------------------------------------------|---------|
| Q.enqueue(e) | Add e to end of queue.                      | $O(1)$* |
| Q.dequeue()  | Remove and return item from front of queue. | $O(1)$* |
| Q.first()    | Return item at front of queue.              | $O(1)$  |
| Q.is_empty() | Whether the queue is empty.                 | $O(1)$  |
| len(Q)       | Return the number of items in the queue.    | $O(1)$  |

*If implemented using a Python list (circular, wraps around when reaching end of list), these operations are amortized.

## Deque

Double-ended queue. ADT that can add and remove elements from both ends of the queue.

| Method            | Description                                     | Runtime |
|-------------------|-------------------------------------------------|---------|
| D.add_first(e)    | Add e to front of dequeue.                      | $O(1)$* |
| D.add_last(e)     | Add e to end of dequeue.                        | $O(1)$* |
| D.delete_first(e) | Remove and return item from front of dequeue.   | $O(1)$* |
| D.delete_last(e)  | Remove and return item from end of dequeue.     | $O(1)$* |
| D.first()         | Return and return item at the front of dequeue. | $O(1)$  |
| D.last()          | Return and return item at the end of dequeue.   | $O(1)$  |
| D.is_empty()      | Whether the dequeue is empty.                   | $O(1)$  |
| len(D)            | Return the number of items in the dequeue.      | $O(1)$  |

*If implemented using a Python list (circular, wraps around), these operations are amortized.

## Linked List

### Singly Linked List

<div style="text-align: center"><img src="./images/singly_linked_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Applications:
1. Implement the Stack ADT, all operations are worst-case $O(1)$.
2. Implement the Queue ADT, all operations are worst-case $O(1)$.

### Circularly Linked List

<div style="text-align: center"><img src="./images/circularly_linked_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Applications:
1. Implement the Queue ADT, with more efficient method for wrapping around.

### Doubly Linked List

<div style="text-align: center"><img src="./images/doubly_linked_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

Applications:
1. Implement the Deque ADT.
2. Implement the Positional List ADT.

### Positional List

<div style="text-align: center"><img src="./images/positional_list.png" width="600px" /></div>
<div align="center">
<sup></sup>
</div>

| Method             | Description                                                |
|--------------------|------------------------------------------------------------|
| L.first()          | Return the position of the first item.                     |
| L.last()           | Return the position of the last item.                      |
| L.before(p)        | Return the position immediately before position p.         |
| L.after(p)         | Return the position immediately after position p.          |
| L.is_empty()       | Whether the positional list is empty.                      |
| len(L)             | Return the number of items in the positional list.         |
| iter(L)            | Return a forward iterator of items in the positional list. |
| L.add_first(e)     | Add e to the front of the positional list.                 |
| L.add_last(e)      | Add e to the back of the positional list.                  |
| L.add_before(p, e) | Add e before position p.                                   |
| L.add_after(p, e)  | Add e after position p.                                    |
| L.replace(p, e)    | Replace the item at position p with e.                     |
| L.delete(p)        | Remove and return the item at position p.                  |

Applications:
1. Maintain access frequencies.

## Array-based vs. Linked-based

| Metrics               | Array-based                    | Linked-based                                              |
|-----------------------|--------------------------------|-----------------------------------------------------------|
| access based on index | $O(1)$                         | $O(n)$                                                    |
| insertion, deletion   | $O(n)$ worst case              | $O(1)$ at arbitrary position                              |
| memory usage          | $2n$ worst case (after resize) | $2n$ for singly-linked lists $3n$ for doubly-linked lists |

## Tree

A tree $T$ is set of nodes storing elements such that the nodes have a parent-child relationship that satisfies the following properties:
* If $T$ is nonempty, it has a special node, called the root of $T$ , that has no parent.
* Each node $v$ of $T$ different from the root has a unique parent node $w$; every node with parent $w$ is a child of $w$.

**Sibling.** Two nodes are siblings if they have the same parent node.

**External.** A node is external if it has no children. A.k.a leaves.

**Internal.** A node is internal if it has >= 1 children.

**Edge.** An edge of tree $T$ is a pair of nodes $(u,v)$ such that $u$ is the parent of $v$, or vice versa.

**Path.** A path of $T$ is a sequence of nodes such that any two consecutive nodes in the sequence form an edge.

**Ordered Tree.** A tree is ordered if there is a meaningful linear order among the children of each node.

| Method       | Description                             |
|--------------|-----------------------------------------|
| T.root()     | Return the position of the tree's root. |
| T.is_root(p) | Whether position p is the tree's root.  |
| T.parent(p)  | Return the position of p's parent.  |