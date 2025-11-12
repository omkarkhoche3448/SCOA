import numpy as np

# ----- Fuzzy Sets -----
X = [1, 2, 3, 4, 5]
A = {1: 0.2, 2: 0.7, 3: 1.0, 4: 0.4, 5: 0.1}
B = {1: 0.6, 2: 0.2, 3: 0.9, 4: 0.3, 5: 0.5}

# ----- Basic Operations -----
union = {x: max(A[x], B[x]) for x in X}
intersection = {x: min(A[x], B[x]) for x in X}
complement_A = {x: 1 - A[x] for x in X}

print("Union:", union)
print("Intersection:", intersection)
print("Complement of A:", complement_A)

# ----- Cartesian Product (Fuzzy Relation) -----
R1 = {(x, y): min(A[x], B[y]) for x in X for y in X}
R2 = {(x, y): min(B[x], A[y]) for x in X for y in X}

print("\nFuzzy Relation R1 (A x B):")
[print(f"{p}: {v}") for p, v in R1.items()]

print("\nFuzzy Relation R2 (B x A):")
[print(f"{p}: {v}") for p, v in R2.items()]

# ----- Max–Min Composition -----
Comp = {(x, z): max(min(R1[(x, y)], R2[(y, z)]) for y in X) for x in X for z in X}

print("\nMax–Min Composition (R1 ∘ R2):")
[print(f"{p}: {v}") for p, v in Comp.items()]

"""
===== EXPLANATION =====

PART 1: Fuzzy Sets
- Universe X = {1, 2, 3, 4, 5} contains all possible elements
- Fuzzy set A: Each element has membership degree [0, 1]
  Example: Element 3 belongs to A with degree 1.0 (full membership)
- Fuzzy set B: Similar representation with different membership values

PART 2: Basic Fuzzy Operations
1. Union (A ∪ B): Take MAX membership value
   - Element is in union if in A OR B → choose stronger membership
   - Example: For element 1, max(0.2, 0.6) = 0.6

2. Intersection (A ∩ B): Take MIN membership value
   - Element is in intersection if in A AND B → choose weaker membership
   - Example: For element 1, min(0.2, 0.6) = 0.2

3. Complement (A'): 1 - membership value
   - Opposite of set A
   - Example: For element 1, 1 - 0.2 = 0.8

PART 3: Fuzzy Relations (Cartesian Product)
- Creates all possible pairs (x,y) from two sets
- Membership of pair = min(membership of x, membership of y)
- R1 = A × B: For pair (1,1), membership = min(0.2, 0.6) = 0.2
- R2 = B × A: Reversed order, for (1,1), membership = min(0.6, 0.2) = 0.2

PART 4: Max-Min Composition (R1 ∘ R2)
- Combines two relations through intermediate elements
- For each pair (x,z):
  1. Find all intermediate y values
  2. Take min(R1(x,y), R2(y,z)) for each y
  3. Take max across all y values
- Example: (1,1) = max{min(R1(1,1),R2(1,1)), min(R1(1,2),R2(2,1)), ...}
- This finds the "best path" from x to z through any intermediate y
"""
