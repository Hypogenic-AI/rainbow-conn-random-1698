# Planning: Tight Bounds on the Rainbow Connection Number of Random Regular Graphs

## Motivation and Novelty Assessment

### Background

The rainbow connection number rc(G) of a connected graph G is the minimum number of colors in an edge-coloring such that every pair of vertices is connected by a path with all distinct colors. Introduced by Chartrand, Johns, McKeon, and Zhang (2008), it has attracted substantial attention at the intersection of extremal combinatorics and probabilistic graph theory.

For random d-regular graphs G(n,d) with fixed d >= 3, the current state of knowledge is:

- Lower bound: rc(G(n,d)) >= diam(G(n,d)) = (1+o(1)) log(n)/log(d-1) whp
  (from the trivial rc >= diam combined with the Bollobas-de la Vega diameter theorem)
- Upper bound (Dudek-Frieze-Tsourakakis 2014): rc(G(n,d)) = O(log n) for d >= 4
- Upper bound (Molloy 2017): rc(G(n,3)) = O(log n)
- Best explicit constant (Kamcev-Krivelevich-Sudakov 2015): rc(G(n,d)) <= c * log(n)/log(d) for d >= 5

The multiplicative gap between lower and upper bounds is a constant factor for fixed d.

### The Actual Open Conjecture

The natural conjecture in this area is:

**Conjecture (Rainbow Connection = Diameter)**: For random d-regular graphs with d >= 3, with high probability,
  rc(G(n,d)) = (1+o(1)) * diam(G(n,d)) = (1+o(1)) * log(n)/log(d-1)

This would be tight in the strongest sense: the rainbow connection number equals the diameter asymptotically.

**Note on the incorrect hypothesis**: The formula rc(G) = ceil(n/d) + O(1) is inconsistent with the literature for fixed d >= 3. For fixed d, n/d = Theta(n) while rc(G(n,d)) = Theta(log n). The bound 3n/(d+1)+3 (Chandran et al. 2010) applies to arbitrary d-regular graphs but is not tight for random ones.

### Novelty Assessment

This research investigates the conjecture rc(G(n,d)) = (1+o(1)) * diam(G(n,d)) from multiple angles:

1. A rigorous proof of the lower bound (rc >= diam, with diam asymptotics cited)
2. A proof of the best available upper bound (Kamcev et al. style) with full details
3. Analysis of the gap and what would close it
4. Computational evidence supporting the tight bound conjecture
5. An attempt at an improved upper bound using expansion properties

---

## Research Question

**Primary Question**: Is rc(G(n,d)) = (1+o(1)) * log(n)/log(d-1) with high probability for fixed d >= 3?

**Sub-questions**:
1. Can we prove the lower bound rc(G(n,d)) >= (1+o(1)) * log(n)/log(d-1) rigorously?
2. What is the best upper bound achievable from existing techniques?
3. Computationally, does rc(G(n,d)) equal diam(G(n,d)) for small n?
4. What would be needed to close the gap to a tight result?

---

## Proof Strategy

### Phase A: Lower Bound (Complete)

**Claim**: rc(G(n,d)) >= (1+o(1)) * log(n)/log(d-1) whp

**Proof outline**:
1. (Trivial) rc(G) >= diam(G) for any connected G
   (Any rainbow path uses distinct colors, so its length <= number of colors)
2. (Bollobas-de la Vega 1982) diam(G(n,d)) = (1+o(1)) * log(n)/log(d-1) whp
3. Combining: rc(G(n,d)) >= (1+o(1)) * log(n)/log(d-1) whp  QED

### Phase B: Upper Bound via BFS Tree (Suboptimal)

**Claim**: For a connected graph G with n vertices, m edges, and diameter D:
rc(G) <= m (trivially, by assigning distinct colors to all edges)

**Improved claim via BFS coloring**: rc(G) <= D + (m - n + 1)
Proof: use BFS tree with depth coloring, assign unique colors to non-tree edges.

This gives a useful bound only when m - n + 1 is small (near-trees), not for random regular graphs.

### Phase C: Upper Bound via Edge-Splitting (Kamcev-Krivelevich-Sudakov Approach)

**Key Tool - Edge-Splitting Lemma** (Kamcev et al. 2015, Lemma 2.1):
If G has two connected spanning subgraphs G1, G2 with |E(G1) ∩ E(G2)| <= c, then:
  rc(G) <= diam(G1) + diam(G2) + c

**Application to G(n,d) for d >= 6**:
1. By contiguity (Janson; Robinson-Wormald): G(n,d) ≈ G(n,d1) + G(n,d2) where d1 = floor(d/2), d2 = ceil(d/2), r1 + r2 = d
2. Both factors G(n,di) have diameter (1+o(1)) * log(n)/log(di-1) whp
3. The factors are edge-disjoint, so |E(G1) ∩ E(G2)| = 0
4. By the Edge-Splitting Lemma:
   rc(G(n,d)) <= diam(G1) + diam(G2)
              <= (1+o(1)) * log(n)/log(d1-1) + (1+o(1)) * log(n)/log(d2-1)
              = (2+o(1)) * log(n)/log(d/2 - 1)

**Resulting gap analysis**:
- Lower bound: log(n)/log(d-1)
- Upper bound via edge-splitting: 2*log(n)/log(d/2-1)
- Ratio: 2*log(d-1)/log(d/2-1)
  - d=6: 2*log(5)/log(2) ≈ 2*2.32 = 4.64
  - d=10: 2*log(9)/log(4) ≈ 2*1.58 = 3.17
  - d=100: 2*log(99)/log(49) ≈ 2*1.14 = 2.29
  - d->infinity: approaches 2

So the gap is a constant factor between 2 and ~4.64 depending on d.

### Phase D: Discussion of Tight Bound

**Key obstacle 1**: The edge-splitting lemma loses a factor of 2 because two separate color palettes are used. To achieve rc ~ diam, one would need to show the two BFS structures can share a color palette.

**Key obstacle 2**: The BFS tree coloring approach (Dudek et al.) uses many more colors (~ K^2 * d * log n) because the greedy local coloring requires each edge to conflict with its O(k_r^2) line-graph neighbors. Breaking this to diam + O(1) colors requires a global non-greedy strategy.

**Most promising direction**: Show via a probabilistic argument that a random coloring with exactly ceil((1+eps)*log(n)/log(d-1)) colors is whp rainbow for G(n,d). This uses:
- G(n,d) has many vertex-disjoint short paths between any pair (by expansion)
- A random coloring makes each individual path rainbow with probability q! / q^|P|
- The number of short paths is large enough (by expansion) that at least one is rainbow

### Phase E: Computational Verification Plan

For small n (n <= 20) and d in {3,4}:
- Generate random d-regular graphs
- Compute exact rc(G) via brute-force BFS over all edge colorings
- Compare with diam(G)
- Check if rc = diam in all cases

For medium n (20 <= n <= 1000):
- Compute upper bound on rc(G) via BFS-tree coloring
- Compare with diam(G) and theoretical prediction log(n)/log(d-1)
- Plot rc/diam ratio vs n to see if it converges to 1

---

## Lemma Breakdown

| Lemma | Statement | Status | Proof Method |
|-------|-----------|--------|--------------|
| L1 | rc(G) >= diam(G) for connected G | Classic | Rainbow paths must use distinct colors |
| L2 | diam(G(n,d)) = (1+o(1)) log(n)/log(d-1) whp | Classic | Bollobas-de la Vega; BFS expansion |
| L3 | Edge-Splitting Lemma (Kamcev et al.) | Known | Direct construction |
| L4 | G(n,d) ≈ G(n,d1) + G(n,d2) by contiguity | Known | Janson; Robinson-Wormald |
| L5 | G(n,d) is an expander whp | Known | Standard random graph theory |
| L6 | BFS tree from any vertex covers (1-o(1))n vertices within radius (1+eps)*diam | New proof | BFS expansion + Chernoff |
| L7 | BFS tree depth coloring achieves rc <= diam on the tree itself | New | Direct construction |
| L8 | rc(G(n,d)) <= 2*(1+o(1)) * log(n)/log(d/2-1) for d >= 6 | Follows Kamcev et al. | L3+L4 |

---

## Computational Verification Plan Details

### Exact rc computation (n <= 16)

For each (n, d) pair with n*d even, generate 5-10 random d-regular graphs and:
1. Compute diam(G) using BFS
2. Compute rc(G) exactly:
   - For k = 1, 2, ...: try 100 random k-colorings; if none works try exhaustive for k <= 4
   - Report first k where a rainbow coloring is found
3. Record rc(G) - diam(G) for each instance

### Upper bound computation (n <= 1000)

For each (n, d) pair:
1. Compute diam(G)
2. Compute rc_upper_bound(G) using BFS tree depth coloring + unique colors for non-tree edges
3. Record rc_ub/diam ratio
4. Plot convergence as n increases

### Expected outcomes

Based on prior literature and mathematical intuition:
- For small n: rc(G) = diam(G) in most or all cases
- For larger n: rc_ub/diam -> constant (hope: close to 1, confirming tight bound conjecture)
- Theoretical curves should match observed diameter within 10% for n >= 100

---

## Timeline and Milestones

1. Planning (this file): DONE
2. Mathematical proofs (results/proofs.md): Phase 3
3. Computational implementation (src/verify_rainbow.py): Phase 4
4. Running experiments and collecting data: Phase 4
5. Final report (REPORT.md): Phase 5
6. README (README.md): Phase 6
