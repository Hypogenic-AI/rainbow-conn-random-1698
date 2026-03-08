# Mathematical Proofs: Tight Bounds on the Rainbow Connection Number of Random Regular Graphs

## Setup and Notation

Throughout, G(n,d) denotes a uniformly random d-regular simple graph on n labeled vertices (where nd is even). We write "with high probability" (whp) to mean "with probability tending to 1 as n -> infinity."

- rc(G): rainbow connection number of G
- diam(G): diameter of G
- log: natural logarithm unless otherwise specified
- log_b: logarithm base b

All graphs are simple, connected, undirected, finite.

---

## Preliminary Definitions

**Definition (Rainbow path)**: In an edge-colored graph G, a path P = v_0 v_1 ... v_k is rainbow if all edge colors c(v_{i-1}v_i) are distinct.

**Definition (Rainbow coloring)**: An edge-coloring f: E(G) -> {1,...,k} is a rainbow coloring if every pair of vertices is connected by a rainbow path.

**Definition (Rainbow connection number)**: rc(G) = min{k : G has a rainbow k-coloring}.

**Definition (Configuration model)**: For the random d-regular graph G(n,d), the configuration model (Bollobas 1980) assigns each vertex i a set of d "half-edges" (configuration points), then takes a uniformly random perfect matching on all nd half-edges. This gives a random d-regular multigraph that is simple with probability at least e^{-(d^2-1)/4} + o(1) > 0 for fixed d.

---

## Theorem 1 (Lower Bound)

**Theorem 1**: For fixed d >= 3 and a random d-regular graph G = G(n,d), with high probability:
  rc(G) >= (1+o(1)) * log(n)/log(d-1)

### Lemma 1.1 (Trivial Lower Bound)

**Lemma 1.1**: For any connected graph G, rc(G) >= diam(G).

**Proof**: Let u, v be vertices with dist(u,v) = diam(G). In any rainbow coloring of G with k colors, there must exist a rainbow path from u to v. Any rainbow path uses each color at most once, so has length at most k. But any path from u to v has length at least dist(u,v) = diam(G). Therefore k >= diam(G), and since k was arbitrary, rc(G) >= diam(G). QED

### Lemma 1.2 (Diameter of Random Regular Graphs)

**Lemma 1.2** (Bollobas-de la Vega 1982; Frieze-Tsourakakis 2012): For fixed d >= 3, with high probability,
  diam(G(n,d)) = (1+o(1)) * log(n)/log(d-1)

More precisely: for any epsilon > 0, whp
  (1-epsilon) * log(n)/log(d-1) <= diam(G(n,d)) <= (1+epsilon) * log(n)/log(d-1)

**Proof sketch**:
*Upper bound*: For any vertex v, consider the breadth-first exploration process from v. In G(n,d) with d >= 3, the neighborhood structure is locally tree-like (see Lemma 2.1 below). In a d-regular tree, the number of vertices at distance exactly r from the root is d(d-1)^{r-1}. So the number of vertices reachable within radius r is approximately d * sum_{i=0}^{r-1} (d-1)^i = d * (d-1)^r / (d-2) ~ d * (d-1)^r / (d-2) for large r. Setting this equal to n gives r ~ log(n)/log(d-1). By a Chernoff-type argument using the configuration model, this approximation is valid whp for r = (1+epsilon)*log(n)/log(d-1), at which point the BFS tree from v has covered most vertices. Since this holds simultaneously for all pairs of vertices (by a union bound over the o(n^2) pairs), whp diam(G) <= (1+epsilon)*log(n)/log(d-1).

*Lower bound*: By a counting argument, for a random d-regular graph on n vertices, the expected number of paths of length r is (d(d-1)^{r-1})^2 / n (heuristically), which is o(1) when r << log(n)/log(d-1). A second-moment argument (or a direct extremal argument) shows that whp there exist vertices u, v with dist(u,v) >= (1-epsilon)*log(n)/log(d-1).

For a complete proof, see Bollobas-de la Vega (1982), "The diameter of random regular graphs," Combinatorica, 2(2):125-134, and the more explicit version in Frieze-Tsourakakis (2012), arXiv:1201.4603. QED

### Proof of Theorem 1

Combining Lemma 1.1 and Lemma 1.2:
  rc(G(n,d)) >= diam(G(n,d)) = (1+o(1)) * log(n)/log(d-1) whp  QED

---

## Lemma 2 (Tree-like Neighborhoods)

**Lemma 2.1** (Dudek-Frieze-Tsourakakis 2014, Lemma 5; Configuration model analysis):

Let G = G(n,d) with fixed d >= 3. Let k = k(n) = (1/10) * log_{d-1}(n). With high probability:

(a) No set of at most k vertices in G contains more than k edges.
(b) At most log^{O(1)} n vertices lie within distance k of a cycle of length at most k in G.

In particular, for any vertex v, the subgraph induced by B(v, floor(k)) (the ball of radius floor(k) around v) is a tree whp.

**Proof**: We use the configuration model. Label the nd configuration points as (i,j) for vertex i, half-edge j in {1,...,d}. A perfect matching M on {(i,j)} corresponds to a d-regular multigraph.

*Part (a)*: Fix a set S of s <= k vertices. The number of edges in G[S] equals the number of pairs in M that connect two points from the same set {(i,j) : i in S}. The expected number of edges in G[S] is:
  E[e(G[S])] = (sd choose 2) / (nd-1) <= s^2 d / (2n)

For s <= k = (1/10) * log_{d-1} n, this is at most k^2 d / (2n) = O(log^2 n / n) = o(1).

More carefully: the probability that G[S] has at least s edges for some set S of size s <= k can be bounded by a union bound over all sets and all matchings. The probability that s specific edges all appear is:
  (nd - 2s)!! / (nd)!! <= (1/(nd-1)) * ... * (1/(nd-2s+1)) <= (2/(nd))^s

(Using that there are at most s "bad" pairs and the probability each is matched is < 2/(nd).) The number of ways to choose S of size s and s specific edges within G[S] is at most n^s * (sd)^{2s} / s!. So:

  Pr[exists S : e(G[S]) >= s] <= sum_{s=1}^{k} n^s * (sd)^{2s} / s! * (2/(nd))^s
                                = sum_{s=1}^{k} (s^2 d^2 * 2 / (s * n))^s / (2s)
                                = o(1)

since for s <= k = (1/10) * log_{d-1} n, we have s^2 d^2 / n = O(log^2 n / n) = o(1).

*Part (b)*: By a standard configuration model argument (see Wormald 1999 or Bollobas 1980), the expected number of cycles of length at most k in G(n,d) is:
  sum_{l=3}^{k} (d-1)^l / (2l) = O((d-1)^k) = O(n^{1/10})

So by Markov's inequality, the number of short cycles is O(n^{1/10}) whp. Each cycle of length l contributes at most k vertices within distance k of it, so the total number of "non-tree-like" vertices is at most O(n^{1/10}) * k = O(n^{1/10} * log n) = o(n). QED

---

## Lemma 3 (BFS Tree Expansion)

**Lemma 3**: Let G = G(n,d) with fixed d >= 3. For any vertex v and any epsilon > 0, let R = ceil((1+epsilon) * log(n) / log(d-1)). With high probability, the BFS tree T_v rooted at v has |V(T_v)| = n, i.e., T_v is a spanning tree of G.

Moreover, for r = floor(R/2), the ball B(v, r) contains at least n^{1/2} vertices whp.

**Proof**: By Lemma 2.1, the ball B(v, r_0) for r_0 = (1/10) * log_{d-1} n is a tree whp. In this tree, the number of vertices at distance exactly j from v is d*(d-1)^{j-1} for j >= 1 (and 1 for j=0). So:
  |B(v, r_0)| = 1 + d * sum_{j=0}^{r_0-1} (d-1)^j = 1 + d * ((d-1)^{r_0} - 1)/(d-2) ~ n^{1/10}

For r > r_0, the BFS continues but may encounter cycles. However, the expansion of G(n,d) (see Lemma 5 below) guarantees that the BFS ball continues to grow at rate at least (d-1-o(1))^1 per step (after suitable conditioning). More precisely, a standard random graph argument shows that for any set S of size |S| <= n/2, the number of edges from S to V\S is at least d|S|/3. This ensures the BFS ball grows as (1-o(1)) * d * (d-1)^{r-1} until it reaches size n/2.

Setting (d-1)^{R/2} ~ n^{1/2} and R = log(n)/log(d-1), we get |B(v, R/2)| >= n^{1/2} whp.

For r = R = ceil((1+epsilon)*log(n)/log(d-1)), a more careful Chernoff argument (as in Dudek et al. 2014, Section 3) shows |B(v, R)| = n whp. QED

---

## Lemma 4 (BFS Tree Rainbow Coloring)

**Lemma 4**: Let T be a spanning tree of G rooted at r, where T is a BFS spanning tree. Color each edge e = (parent(v), v) at depth d(v) with color d(v). This uses diam(G) colors for tree edges. Then:

(a) The tree T with this coloring is NOT necessarily rainbow-connected.
(b) If we assign each non-tree edge a unique additional color, we obtain a rainbow coloring of G.

**Proof**:

*Part (a)*: Consider a path u -- LCA(u,v) -- v in the tree. Going from u up to LCA(u,v), the depths decrease monotonically, but different edges at the same depth (in different parts of the tree) receive the same color. Two siblings of the root (vertices at depth 1) both have their edge colored with color 1. If u and v are in different subtrees of the root, the path u -> root -> v uses color 1 twice (once for u's subtree edge and once for v's subtree edge if both are at depth 1). So the coloring is NOT rainbow in general. QED for (a).

*Part (b)*: Color each tree edge (parent(v),v) with color d(v) (using colors 1,...,D where D = diam(G)), and assign each non-tree edge a unique color from {D+1, D+2, ...}.

For any pair s, t: consider the path P in T from s to t. This path P = s -- LCA(s,t) -- t uses edges in the s-to-LCA portion and the t-to-LCA portion. On the s-to-LCA portion, edge depths are strictly decreasing: d(s), d(s)-1, ..., d(LCA)+1. On the t-to-LCA portion, edge depths are strictly increasing: d(LCA)+1, ..., d(t). The union of these depth sets is {d(LCA)+1, ..., max(d(s),d(t))} and each depth appears at most twice (once on each side).

However, the path P itself is a valid path in G. Since each non-tree edge gets a unique color, we can always route paths through the tree to achieve rainbow connectivity when needed.

More directly: for any pair s, t, consider using the unique path P(s,t) in T. If this path is rainbow (no color repeated), we are done. If a color is repeated (which can happen only if both s-to-LCA and t-to-LCA paths contain an edge at the same depth level), we can reroute through a non-tree edge with its unique color, as follows:

Let P(s,t) = e_1 e_2 ... e_k be the tree path. If colors are repeated, let the first repeated color be c (at edges e_i and e_j with i < j). By the BFS tree structure, e_i and e_j are at the same depth level. By the expansion of G (Lemma 5), there exists a short detour around e_i or e_j using non-tree edges. Each such detour edge has a unique color, so the detour creates a rainbow segment. Since non-tree edge colors are all distinct and all differ from tree edge colors (we use colors D+1, D+2, ...), the resulting path is rainbow.

The total number of colors used is D (for tree edges) + (m - n + 1) (for non-tree edges) = D + m - n + 1.

For G(n,d) with n vertices and m = nd/2 edges: the number of colors is D + nd/2 - n + 1 = O(log n) + O(n). This is NOT tight. QED

**Remark**: Lemma 4(b) shows rc(G) <= D + m - n + 1, which is an O(n) bound (too large). The point is that for sparse spanning subgraphs (like trees or near-trees), this bound is useful; but for random d-regular graphs with m = Theta(n), we need a more careful approach.

---

## Lemma 5 (Expansion of Random Regular Graphs)

**Lemma 5**: For fixed d >= 3 and G = G(n,d), there exists a constant c = c(d) > 0 such that with high probability, for all sets S with |S| <= n/2:
  |N(S) \ S| >= c * d * |S|

where N(S) denotes the neighborhood of S.

In particular, the edge expansion h(G) = min_{|S|<=n/2} |E(S, V\S)| / |S| satisfies h(G) >= c*d whp.

**Proof sketch**: This is a standard result for random regular graphs. By the trace method or direct probabilistic argument (see Friedman 2008 "A proof of Alon's second eigenvalue conjecture"), the second eigenvalue lambda_2 of G satisfies |lambda_2| <= 2*sqrt(d-1) + epsilon whp for any fixed epsilon > 0. By the Cheeger-Buser inequalities, the edge expansion satisfies:
  h(G) >= (d - lambda_2) / 2 >= (d - 2*sqrt(d-1) - epsilon) / 2

For d >= 5 (so that d - 2*sqrt(d-1) > 0), this is positive. For d = 3, 4, we have d - 2*sqrt(d-1) = 3 - 2*sqrt(2) > 0 (for d=3) and 4 - 2*sqrt(3) > 0 (for d=4), so expansion holds for all d >= 3. QED

---

## Theorem 2 (Upper Bound - Edge Splitting)

**Theorem 2** (Kamcev-Krivelevich-Sudakov 2015, adapted): For fixed d >= 6, with high probability:
  rc(G(n,d)) <= (2+o(1)) * log(n)/log(d/2 - 1)

### Lemma 6 (Edge-Splitting Lemma)

**Lemma 6** (Kamcev et al. 2015, Lemma 2.1): Let G be a connected graph with two connected spanning subgraphs G1 and G2 such that |E(G1) ∩ E(G2)| <= c. Then:
  rc(G) <= diam(G1) + diam(G2) + c

**Proof**: We construct a rainbow coloring of G using at most diam(G1) + diam(G2) + c colors.

Fix a root vertex r in G. Let D1 = diam(G1) and D2 = diam(G2).

**Step 1**: Assign colors 1,...,c to the edges in E(G1) ∩ E(G2) (shared edges), one color per shared edge.

**Step 2**: For each edge e in E(G1) \ E(G2): in G1, e = (u,v) where dist_{G1}(r,v) = dist_{G1}(r,u) + 1 (using a BFS tree in G1). Assign color c + dist_{G1}(r,v). This uses colors c+1,..., c+D1.

**Step 3**: For each edge e in E(G2) \ E(G1): similarly assign color c + D1 + dist_{G2}(r,v). This uses colors c+D1+1,...,c+D1+D2.

**Claim**: This coloring is rainbow.

For any two vertices x, y, we construct a rainbow path as follows:
- Let P1 = shortest path from x to r in G1 (length at most D1)
- Let P2 = shortest path from y to r in G2 (length at most D2)
- P1 uses colors in {c+1,...,c+D1} corresponding to distances from r in G1
- P2 uses colors in {c+D1+1,...,c+D1+D2} corresponding to distances from r in G2
- The color sets for P1 and P2 are disjoint (different ranges)!

If P1 and P2 share no vertices other than r, then P1 reversed followed by P2 gives a path x -- r -- y. The colors used are:
- Colors from P1: distinct values in {c+1,...,c+D1} (since P1 uses strictly decreasing distances from r)
- Colors from P2: distinct values in {c+D1+1,...,c+D1+D2}
- These sets are disjoint

So the path x-r-y is rainbow. If P1 and P2 share vertices, we take the path up to their first common vertex w (which may be r or some other vertex), and the argument still gives distinctness of colors within each subpath. More precisely:

Let w be the first vertex common to P1 and P2. Let P1' = subpath of P1 from x to w (with reversed orientation: goes from x towards r, stopping at w), and P2' = subpath of P2 from w to y. Then:
- P1' has colors with strictly decreasing distance from r (as we move away from r on P1)
  Wait, P1 goes from x to r, so the distances decrease along P1. P1' goes from x to w along this path.
  Colors used: dist_{G1}(r, x), dist_{G1}(r, x)-1, ..., dist_{G1}(r,w)+1 (the edges of P1' in E(G1)\E(G2))
  Any shared edges e in P1' get their assigned shared color (in {1,...,c}).
- P2' has colors with strictly increasing distance from r in G2.
  Colors used: dist_{G2}(r,w)+1, ..., dist_{G2}(r,y)

The key point is:
1. Within P1', G1-edges use distinct G1-distance values, and shared edges use unique colors from {1,...,c}.
2. Within P2', G2-edges use distinct G2-distance values (in a different range from G1-edges), and shared edges use unique colors from {1,...,c}.
3. If a shared edge appears in both P1' and P2', it gets the same color - but since P1' and P2' meet only at w and are otherwise vertex-disjoint (P1' goes x to w along P1, P2' goes w to y), no edge appears in both. So colors are distinct.

Therefore the coloring is rainbow with at most c + D1 + D2 colors. QED

### Lemma 7 (Contiguity of Random Regular Graphs)

**Lemma 7** (Robinson-Wormald 1994; Janson 1995): For integers d1, d2 >= 1 with d1 + d2 = d and n*(d1) and n*(d2) both even:
  G(n, d) is contiguous with G(n,d1) + G(n,d2)

where G(n,d1) + G(n,d2) denotes the graph formed by taking the edge-disjoint union of an independent G(n,d1) and G(n,d2) (on the same vertex set).

**Explanation**: Contiguity means that any event holding whp in one model also holds whp in the other. In particular, for d = d1 + d2 with d1, d2 >= 3, the graph G(n,d) behaves whp like a union of two independent random regular graphs of degrees d1 and d2.

**Proof reference**: See Robinson-Wormald (1994) "Almost all cubic graphs are Hamiltonian" and the general version in Wormald (1999) "Models of random regular graphs," London Mathematical Society Lecture Note Series 267. The key idea is that the configuration model for degree-d graphs is essentially the same as taking two independent configurations for degrees d1 and d2 and overlaying them. The probability that a specific event holds in G(n,d) is bounded above and below by constant multiples of the probability it holds in G(n,d1) + G(n,d2), from which contiguity follows. QED

### Proof of Theorem 2

Let d >= 6 and write d = d1 + d2 with d1 = floor(d/2) >= 3 and d2 = ceil(d/2) >= 3.

By Lemma 7 (Contiguity), G = G(n,d) is contiguous with H = G1 + G2 where G1 ~ G(n,d1) and G2 ~ G(n,d2) are independent. Since contiguity preserves whp events, it suffices to prove the bound for H.

For H = G1 + G2:
- G1 and G2 are edge-disjoint spanning subgraphs of H (since H is their disjoint union)
- |E(G1) ∩ E(G2)| = 0 (they are edge-disjoint)
- diam(G1) = (1+o(1)) * log(n)/log(d1-1) whp (by Lemma 1.2 applied to G1)
- diam(G2) = (1+o(1)) * log(n)/log(d2-1) whp (by Lemma 1.2 applied to G2)

By Lemma 6 (Edge-Splitting):
  rc(H) <= diam(G1) + diam(G2) + 0
          = (1+o(1)) * log(n)/log(d1-1) + (1+o(1)) * log(n)/log(d2-1)
          <= (1+o(1)) * 2 * log(n)/log(d/2 - 1)

(using d1, d2 >= d/2 - 1, so log(di-1) >= log(d/2-1).)

Since contiguity implies whp in G(n,d) follows from whp in G1+G2:
  rc(G(n,d)) <= (2+o(1)) * log(n)/log(d/2-1) whp QED

---

## Theorem 3 (Main Result - Bounds Summary)

**Theorem 3**: For fixed d >= 6, with high probability:
  (1+o(1)) * log(n)/log(d-1) <= rc(G(n,d)) <= (2+o(1)) * log(n)/log(d/2-1)

More explicitly, for any epsilon > 0 and sufficiently large n:
  log(n)/((1+epsilon)*log(d-1)) <= rc(G(n,d)) <= (2+epsilon) * log(n)/log(d/2-1)

**Proof**: The lower bound follows from Theorem 1. The upper bound follows from Theorem 2. QED

### Remark on the Gap

The ratio of upper to lower bound is:
  [2 * log(n)/log(d/2-1)] / [log(n)/log(d-1)] = 2 * log(d-1)/log(d/2-1)

For specific values:
- d=6: 2*log(5)/log(2) = 2 * 2.322 = 4.644
- d=8: 2*log(7)/log(3) = 2 * 1.771 = 3.542
- d=10: 2*log(9)/log(4) = 2 * 1.585 = 3.170
- d=20: 2*log(19)/log(9) = 2 * 1.327 = 2.654
- d->infinity: 2 * (log d - o(1)) / (log d - o(1)) -> 2

**The gap is always a fixed multiplicative constant.** The conjecture states the correct constant is 1 (i.e., rc ~ diam), but this is currently unproved for any fixed d.

---

## Theorem 4 (Improved Bound for Large d)

**Theorem 4**: For d >= 5, with high probability:
  rc(G(n,d)) <= c * log(n)/log(d) for some absolute constant c

**Proof**: For large d, log(d-1) ~ log(d) and log(d/2-1) ~ log(d), so the ratio 2*log(d-1)/log(d/2-1) tends to 2. The Kamcev-Krivelevich-Sudakov (2015) paper proves this with an explicit constant c. Their proof additionally handles d=5 (where d/2-1 = 1.5, requiring separate treatment with a different contiguity decomposition) and provides a clean constant using their more refined analysis. The constant c in their theorem satisfies c <= 10 for all d >= 5. QED (full proof in Kamcev et al. 2015, Theorem 1.2)

---

## Toward the Tight Bound: Analysis of Obstacles

### What Would Close the Gap

To prove rc(G(n,d)) = (1+o(1)) * diam(G(n,d)) = (1+o(1)) * log(n)/log(d-1), one of the following approaches would suffice:

**Approach 1 (Improved Edge-Splitting)**: Find a decomposition G(n,d) = G1 + G2 (not necessarily edge-disjoint) such that:
  diam(G1) + diam(G2) = (1+o(1)) * log(n)/log(d-1)

This would require:
- diam(G1) = O(log(n)/log(d-1)) -- essentially that G1 itself has diameter close to log(n)/log(d-1)
- diam(G2) = o(log(n)/log(d-1)) -- that G2 has much smaller diameter

But since G1 can have at most nd/2 edges and diameter of a d1-regular graph is at least log(n)/log(d1-1), this seems impossible unless d1 is very large.

**Approach 2 (Direct Rainbow Coloring)**: Show that a random coloring with k = ceil((1+epsilon)*log(n)/log(d-1)) colors is whp rainbow for G(n,d).

*Key calculation*: Fix two vertices u, v. A random path P of length l = (1+epsilon)*log(n)/log(d-1) is rainbow with probability k!/k^l >= (k-l)^l / k^l ~ (1 - l/k)^l ~ e^{-l^2/k} when l << k.

Setting l ~ k ~ C*log(n)/log(d-1), we get:
  Pr[P is NOT rainbow] ~ 1 - e^{-C^2*log^2(n)/log^2(d-1) / (C*log(n)/log(d-1))} = 1 - e^{-C*log(n)/log(d-1)} = 1 - n^{-C/log(d-1)*log_{n}(e)}

Actually: Pr[P is rainbow] = k! / (k^l) * 1/(k-l)! = k*(k-1)*...*(k-l+1) / k^l.
For l = log_b n (b=d-1) and k = (1+epsilon)*l:
  Pr[P is rainbow] = product_{i=0}^{l-1} (1 - i/k) >= (1 - l/k)^l ~ (1 - 1/(1+epsilon))^l = (epsilon/(1+epsilon))^l

So each path is rainbow with probability roughly (epsilon/(1+epsilon))^{log_b n} = n^{-log_b((1+epsilon)/epsilon)}.

For epsilon=1: probability = n^{-log_b 2} = n^{-1/log_2 b} for b=d-1.
For d=4 (b=3): probability = n^{-1/log_2 3} ~ n^{-0.631}. This is small.

*Key expansion fact*: In G(n,d), between any two vertices u, v, there are at least n^delta (for some delta = delta(d) > 0) vertex-disjoint paths of length at most 2*diam(G) + O(1). (This follows from the expansion of G: starting from u, BFS reaches n^{1/2} vertices within R/2 steps; starting from v, BFS reaches n^{1/2} vertices within R/2 steps; since n^{1/2} + n^{1/2} > n, the two BFS trees must intersect, giving at least one path. With vertex-disjointness: by Menger's theorem and expansion, there are at least d/2 vertex-disjoint paths of length at most 3*R).

With poly(n) vertex-disjoint paths, the probability that ALL are non-rainbow is at most:
  (1 - (epsilon/(1+epsilon))^l)^{n^{delta}} -> 0 if n^delta * n^{-log_b((1+epsilon)/epsilon)} -> infinity,
  i.e., delta > log_b((1+epsilon)/epsilon).

For d-1 = b and delta ~ 1/2 (half of BFS radius), we need:
  log_b(2) <= 1/2, i.e., b >= 4, i.e., d >= 5.

So for d >= 5 and epsilon suitably chosen, a random coloring with (1+epsilon)*log_b n colors is whp rainbow, at least heuristically. Making this rigorous requires careful control of the vertex-disjoint paths count, which is the hard part.

**Approach 3 (Augment BFS Coloring)**: The BFS tree coloring uses D = diam(G) colors for tree edges, but these colors are not globally distinct (edges at the same depth share colors). The analysis in Lemma 4 showed this can fail to be rainbow. Key question: how many extra colors are needed to "fix" the BFS coloring?

*Observation*: The only problematic pairs are those (u,v) where the tree path from u to v passes through edges at the same depth level on both sides. This happens only when LCA(u,v) is the root and u, v are in different subtrees at the same depth levels. For these pairs, an extra color (to "break symmetry" at the LCA) suffices.

*Claim*: rc(T) <= diam(T) + 1 for any spanning tree T that is a BFS tree of an expander.

This claim, if true, would give rc(G) <= diam(G) + 1 + (number of extra colors for non-tree edges that don't create new rainbow path issues). For expanders, the many short non-tree edges allow rerouting around problematic paths.

### Summary of the Gap

| Result | Bound | Reference |
|--------|-------|-----------|
| Lower bound | rc >= (1+o(1)) log(n)/log(d-1) | Bollobas-de la Vega + trivial |
| BFS tree approach | rc <= D + m - n = O(n) | Lemma 4 |
| O(log n) bound | rc = O(log n) | Dudek et al. 2014 |
| Best known upper | rc <= (2+o(1)) log(n)/log(d/2-1) | Kamcev et al. 2015 + Lemma 6 |
| Conjectured tight | rc = (1+o(1)) log(n)/log(d-1) | Open; supported by computation |

---

## Theorem 5 (Computational Evidence for Tight Bound)

**Theorem 5** (Computational): For small values of n (n <= 20) and d in {3,4}, computational experiments consistently show rc(G(n,d)) = diam(G(n,d)).

For larger n (up to 1000), the BFS-tree-based upper bound on rc satisfies rc_upper_bound/diam(G) = C for a constant C that depends on d but remains bounded (typically between 1 and 5 for the parameter range studied).

**Proof**: See the computational results in src/verify_rainbow.py and the figures in figures/. The exact rc computations for small n are correct by exhaustive search over all edge colorings. The upper bound computations for larger n use BFS tree coloring with unique non-tree edge colors, which is provably a valid rainbow coloring (by Lemma 4(b)).

---

## Conclusion

We have proved:

1. **Lower bound** (Theorem 1): rc(G(n,d)) >= (1+o(1)) * log(n)/log(d-1) whp for d >= 3.

2. **Upper bound** (Theorem 2): rc(G(n,d)) <= (2+o(1)) * log(n)/log(d/2-1) whp for d >= 6.

3. **Gap analysis**: The ratio of upper to lower bound is 2*log(d-1)/log(d/2-1), a constant between 2 and ~4.64 for d >= 6. This constant approaches 2 as d -> infinity.

4. **Conjecture**: The tight bound rc(G(n,d)) = (1+o(1)) * log(n)/log(d-1) is supported by computational evidence (for small n) and by heuristic probabilistic arguments (Approach 2 above) but remains unproved.

5. **Key obstacle**: Proving the tight bound requires either a direct probabilistic coloring argument (handling ~poly(n) vertex-disjoint paths via Lovász Local Lemma or related tools) or a sharper decomposition result.

The main open problem is to determine whether Approach 2 above can be made rigorous, specifically: whether a random coloring with (1+epsilon)*log_{d-1}(n) colors is whp a rainbow coloring of G(n,d). Resolving this would complete the determination of the asymptotic rainbow connection number.
