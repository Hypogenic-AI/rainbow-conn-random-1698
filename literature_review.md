# Literature Review: Tight Bounds on the Rainbow Connection Number of Random Regular Graphs

## Research Area Overview

The rainbow connection number rc(G) of a connected graph G is a graph coloring parameter introduced by Chartrand, Johns, McKeon, and Zhang in 2008. It sits at the intersection of extremal graph theory, probabilistic combinatorics, and random graph theory. For random d-regular graphs G(n,d), the central question is: what is the minimum number of colors needed to edge-color G so that every pair of vertices is connected by a path whose edges all have distinct colors?

The current state of knowledge shows that for a random d-regular graph on n vertices with fixed d ≥ 3:
- The lower bound from the diameter gives rc(G) ≥ (1+o(1)) log n / log(d-1) w.h.p.
- The best upper bound (Kamcev-Krivelevich-Sudakov 2015) gives rc(G) ≤ c·log n / log d for r ≥ 5 w.h.p.

The multiplicative constant between these bounds is the main open problem. There is no known graph-theoretic obstruction preventing rc(G(n,d)) from equaling (1+o(1))·diam(G(n,d)) = (1+o(1)) log n / log(d-1) w.h.p.

**Note on the Research Hypothesis**: The stated hypothesis rc(G) = ⌈n/d⌉ + O(1) appears to conflict with known results. For fixed d ≥ 3, the diameter (and hence rc) is Θ(log n), while n/d = Θ(n). The bound n/d applies to *worst-case* d-regular graphs (via the Chandran et al. upper bound), but random regular graphs are much better connected. The actual open problem is to determine whether rc(G(n,d)) = (1 + o(1)) · log n / log(d-1) (i.e., whether rc matches the diameter asymptotically). See Section "Gaps and Opportunities" for discussion.

---

## Key Definitions

**Definition 1 (Rainbow Path)**: In an edge-colored graph G, a path is *rainbow* if all its edges have distinct colors.

**Definition 2 (Rainbow Connection Number)**: The *rainbow connection number* rc(G) of a connected graph G is the minimum number of colors in an edge-coloring such that every pair of vertices is connected by a rainbow path.

**Definition 3 (Strong Rainbow Connection Number)**: src(G) is the minimum number of colors needed so that every pair of vertices is connected by a *shortest* rainbow path.

**Definition 4 (Rainbow Vertex Connection Number)**: rvc(G) is the minimum number of colors needed for a vertex-coloring so that every pair of vertices is connected by a path whose *internal vertices* all have distinct colors.

**Definition 5 (Random Regular Graph G(n,r))**: The uniform probability distribution on all r-regular simple graphs on n labeled vertices (where rn is even).

**Definition 6 (Configuration Model)**: A standard model for random regular graphs (Bollobas 1980). Let W = [rn] be a set of configuration points, with Wi = [(i-1)r+1, ir] for vertex i. A uniform random pairing of W gives a random r-regular multigraph; it is simple with positive probability for fixed r.

**Definition 7 (Diameter)**: diam(G) = max_{u,v} dist(u,v). Always a lower bound: rc(G) ≥ diam(G).

**Definition 8 (Radius)**: rad(G) = min_v max_u dist(u,v). Related bound: rc(G) ≤ 3·rad(G) for bridgeless graphs.

**Definition 9 (Connected Dominating Set)**: A set S ⊆ V(G) is a connected dominating set if G[S] is connected and every vertex not in S has a neighbor in S.

**Definition 10 (Tree-like neighborhood)**: In G(n,r), a vertex x is *tree-like* if the subgraph induced by all vertices within distance k of x is a tree.

---

## Key Papers

### Paper 1: Rainbow Connection of Random Regular Graphs
- **Authors**: Andrzej Dudek, Alan Frieze, Charalampos E. Tsourakakis
- **Year**: 2014 (arXiv:1311.2299)
- **Main Result**:

  **Theorem 1 (Dudek-Frieze-Tsourakakis)**: Let r ≥ 4 be a constant. Then w.h.p. rc(G(n,r)) = O(log n).

  The diameter of G(n,r) is w.h.p. asymptotically log_{r-1} n, so this is best possible up to a hidden constant.

- **Proof Techniques**:
  1. **Greedy random coloring**: Order the edges e_1, e_2, ..., e_m. Use q = ⌈K₁²r log n⌉ colors; assign each edge a random color from those not used by edges within distance k_r = log_{r-1}(K₁ log n) of it in the line graph. By definition, this ensures each root-to-leaf path in the breadth-first tree T_x is rainbow.

  2. **Tree-like structure (Lemma 5)**: w.h.p. in G(n,r), (a) no set of s ≤ t₀ = (1/10)log_{r-1} n vertices contains more than s edges, and (b) at most log^{O(1)} n vertices lie within distance k_r of a short cycle. Hence almost all vertices are tree-like.

  3. **Rainbow tree matching (Lemma 2/3/Corollary 4)**: For two vertex-disjoint complete d-ary trees (d ≥ 3) with L levels whose edges are colored such that edges within distance L of each other have distinct colors, there exist subsets S₁ ⊆ L(T₁), S₂ ⊆ L(T₂) with |Sᵢ| ≥ d^{L/10} and a bijection f: S₁ → S₂ such that P(x, T₁) ∪ P(f(x), T₂) is rainbow for all x ∈ S₁.

  **Key Lemma 2**: κ_{ℓ,d} ≥ d^{2ℓ}/4 for d ≥ 3, where κ_{ℓ,d} is the minimum over all pairs of vertex-disjoint rainbow d-ary trees of height ℓ of the number of leaf-pairs with jointly rainbow root-to-leaf paths. This fails for d = 2 (binary trees), which is why r = 3 required separate treatment.

  4. **BFS tree expansion**: Grow trees from T_x and T_y until they have n^{1/20} leaves, controlling color conflicts via binomial tail bounds (Chernoff). Then grow n^{3/5} leaf subtrees from these and find edges connecting them.

  5. **Non-tree-like cases**: Handled separately; non-tree-like vertices that are near short cycles are o(n) and get O(1) additional colors each.

- **Open problems stated**: (a) Determine the hidden constant. (b) Case r = 3 was conjectured to hold but proved separately by Molloy 2017.

---

### Paper 2: Rainbow Connection of Sparse Random Graphs
- **Authors**: Alan Frieze, Charalampos E. Tsourakakis
- **Year**: 2012 (arXiv:1201.4603)
- **Main Results**:

  **Theorem 1 (Frieze-Tsourakakis, G(n,p))**: Let G ~ G(n,p) with p = (log n + ω)/n, ω → ∞, ω = o(log n). Let Z₁ = number of degree-1 vertices. Then w.h.p. rc(G) ~ max{Z₁, log n / log log n}.

  **Theorem 2 (Frieze-Tsourakakis, G(n,r))**: For G(n,r) with fixed r ≥ 3, w.h.p.:
  - rc(G) = O(log^4 n) when r = 3
  - rc(G) = O(log^{2θ_r} n) when r ≥ 4, where θ_r = log(r-1)/log(r-2)

  This was the *first* result for rainbow connection of random regular graphs.

- **Proof Techniques**: Random coloring of edges using MCMC (Markov Chain Monte Carlo). The approach is weaker than Dudek et al. because it does not achieve O(log n) for r ≥ 4.

---

### Paper 3: Some Remarks on Rainbow Connectivity
- **Authors**: Nina Kamcev, Michael Krivelevich, Benny Sudakov
- **Year**: 2015 (arXiv:1501.00821)
- **Main Results**:

  **Theorem 1.2 (Kamcev-Krivelevich-Sudakov)**: There exists an absolute constant c such that for r ≥ 5, rc(G_{n,r}) ≤ c·log n / log r w.h.p.

  **Theorem 1.3**: Let G be n-vertex r-regular with edge expansion ≥ εr. If r ≥ max{64ε⁻¹ log(64ε⁻¹), 324}, then rc(G) = O(ε⁻¹ log n).

  **Theorem 1.1**: For connected n-vertex G with min degree δ ≥ 4, rc(G) ≤ 16n/δ.

- **Key Technical Tool: Edge-Splitting Lemma**:

  **Lemma 2.1**: Let G have two connected spanning subgraphs G₁, G₂ with |E(G₁) ∩ E(G₂)| ≤ c. Then rc(G) ≤ diam(G₁) + diam(G₂) + c.

  *Proof*: Color E(G₁) ∩ E(G₂) with c distinct colors. Color remaining edges of Gᵢ by distance levels from a root in Gᵢ. Any two vertices x₁, x₂ are connected by concatenating their shortest paths in G₁ and G₂ to the root (switching at the first shared edge).

- **Application to G(n,r) (r ≥ 6)**: Use contiguity G_{n,r} ≈ G_{n,r₁} ⊕ G_{n,r₂} (Janson, Robinson-Wormald). Each G_{n,rᵢ} has diameter ≤ (1+o(1)) log n / log(rᵢ-1). Splitting lemma gives rc ≤ 2·(1+o(1)) log n / log(r/2 - 1) = O(log n / log r).

- **Significance**: This is the *best known upper bound*, and matches the diameter up to a constant factor. The bound c·log n / log r vs. the lower bound log n / log(r-1) ~ log n / log r shows the multiplicative constant is between 1 and c.

---

### Paper 4: Rainbow Connection Number and Connected Dominating Sets
- **Authors**: L. Sunil Chandran, Anita Das, Deepak Rajendraprasad, Nithin M. Varma
- **Year**: 2010 (arXiv:1010.2296)
- **Main Result**:

  **Theorem (Chandran et al.)**: For every connected graph G on n vertices with minimum degree δ, rc(G) ≤ 3n/(δ+1) + 3.

  This is the best known general bound and is tight up to additive factors.

- **Key Technique**: Construct a connected two-step dominating set of size at most n/(δ+1) - 1. Color the induced subgraph rainbow (at most n/(δ+1) - 1 + 3 colors). The key lemma: rc(G) ≤ γ_c(G) + 2 where γ_c(G) is the connected domination number.

- **Lower bound**: Caro et al. 2008 gave a construction of graphs with min degree δ and rc(G) ≥ 3n/(δ+1) - (δ+7)/(δ+1), showing the bound is essentially tight.

- **Corollaries**:
  - rc(G) ≤ diam(G) + c for c ≤ 4 for many graph classes (interval graphs, AT-free graphs, threshold graphs, chordal graphs when bridgeless)
  - rc(G) ≤ 3·rad(G) for bridgeless graphs

---

### Paper 5: The Rainbow Connection of a Graph is (at most) Reciprocal to its Minimum Degree
- **Authors**: Michael Krivelevich, Raphael Yuster
- **Year**: 2010
- **Main Result**: rc(G) ≤ 20n/δ for connected graphs with min degree δ.
- **Significance**: First result removing the logarithmic factor from the Caro et al. bound. Later improved to 16n/δ (Kamcev et al.) and 3n/(δ+1)+3 (Chandran et al.).

---

### Paper 6: Rainbow Connection in Graphs
- **Authors**: Gary Chartrand, Garry L. Johns, Kathleen A. McKeon, Ping Zhang
- **Year**: 2008
- **Significance**: Foundational paper introducing the rainbow connection concept. Proved basic facts, determined rc for complete graphs, trees, cycles, complete multipartite graphs, the Petersen graph, and wheels.
- **Key facts**:
  - rc(G) = 1 iff G is complete
  - rc(G) = n-1 iff G is a tree
  - rc(G) ≥ diam(G) (always)
  - p = √(log n/n) is the sharp threshold for rc(G(n,p)) ≤ 2

---

### Paper 7: On the Threshold for Rainbow Connection Number r in Random Graphs
- **Authors**: Annika Heckel, Oliver Riordan
- **Year**: 2013 (arXiv:1307.7747)
- **Main Result**: Proves sharp thresholds for the property rc(G(n,p)) ≤ r for fixed r. For r = 2, the threshold coincides with the diameter-2 threshold. For r ≥ 3, the threshold is conjectured to differ from the diameter-r threshold, and they prove partial results.
- **Relevance**: Establishes the precise threshold for constant rc in Erdos-Renyi random graphs; methodologically relevant for tight constant determination.

---

### Paper 8: Rainbow Hamilton Cycles in Random Regular Graphs
- **Authors**: Svante Janson, Nicholas Wormald
- **Year**: 2005 (arXiv:math/0508145)
- **Main Result**: For r ≥ 3 and fixed r, a random r-regular graph on n vertices contains a rainbow Hamilton cycle when edges are colored uniformly at random with r colors.
- **Relevance**: Uses contiguity of random regular graph models; the MCMC/contiguity techniques used here are related to approaches in Kamcev et al.

---

## Known Results: Prerequisite Theorems

### Diameter of Random Regular Graphs

**Theorem (Bollobas-de la Vega 1982)**: For fixed r ≥ 3, the diameter of G(n,r) is w.h.p. asymptotically log_{r-1} n. More precisely, diam(G(n,r)) = (1+o(1)) log n / log(r-1) w.h.p.

Used for: Lower bound rc(G(n,r)) ≥ diam(G) = (1+o(1)) log n / log(r-1).

### Tree-like Neighborhoods in Random Regular Graphs

**Lemma (Dudek et al., Lemma 5)**: For G = G(n,r) w.h.p.:
- (a) No set of s ≤ t₀ = (1/10) log_{r-1} n vertices contains more than s edges (so the s-neighborhood of any vertex is a tree for s ≤ t₀).
- (b) At most log^{O(1)} n vertices lie within distance k_r = log_{r-1}(K₁ log n) of a cycle of length ≤ k_r.

Proved using the configuration model; key probability estimate: Pr[given k disjoint pairs are in a random configuration] ≤ 1/(r^k (n-k)^k).

Used for: Showing almost all vertices are tree-like, enabling the rainbow coloring argument.

### Configuration Model (Bollobas 1980)

Provides a uniform model for random r-regular multigraphs. Any event occurring w.h.p. in the configuration model also occurs w.h.p. in G(n,r) for fixed r (since GF is simple with positive probability).

### Expansion of Random Regular Graphs

G(n,r) for fixed r ≥ 3 is an expander w.h.p. Edge expansion Φ(G) ≥ c·r for some absolute constant c > 0. This underpins the Kamcev et al. approach (Theorem 1.3 applies to G(n,r)).

### Contiguity of Random Regular Graph Models

For r = r₁ + r₂ (with rᵢ ≥ 3), G_{n,r} ≈ G_{n,r₁} ⊕ G_{n,r₂} (Janson; Robinson-Wormald). This allows decomposing a random r-regular graph into two edge-disjoint random regular graphs each of smaller degree, which is the key tool in Kamcev et al.

### Chernoff Bounds

Standard: Pr(Bin(n,p) ≤ αnp) ≤ e^{-(1-α)²np/2} for 0 ≤ α ≤ 1, and Pr(Bin(n,p) ≥ αnp) ≤ (e/α)^{αnp} for α ≥ 1. Used in the BFS expansion arguments throughout.

---

## Proof Techniques in the Literature

### 1. BFS Tree / Local Tree Expansion (Dudek-Frieze-Tsourakakis)
- Grow breadth-first trees from source and target vertices.
- Most vertices are tree-like (neighborhood is an actual tree up to radius ~ (1/10) log n).
- Key insight: the greedy random coloring assigns distinct colors to edges within distance k_r, ensuring root-to-leaf paths in BFS trees are rainbow.
- Then match leaves of the two BFS trees and find a connecting rainbow path through random structure.

**Applicable to**: Random regular graphs with expansion, where BFS trees are actual trees for many rounds.

### 2. Edge-Splitting (Kamcev-Krivelevich-Sudakov)
- Decompose G into two spanning subgraphs G₁, G₂ with small intersection and small diameters.
- Color each Gᵢ using a different palette based on distances from a common root.
- rc(G) ≤ diam(G₁) + diam(G₂) + |E(G₁) ∩ E(G₂)|.

**Applicable to**: Dense regular graphs, expanders, graphs that can be decomposed into two sparse graphs with small diameter. Particularly powerful when G decomposes via contiguity arguments into two random graphs each with logarithmic diameter.

### 3. MCMC Random Coloring (Frieze-Tsourakakis)
- Use a Markov chain to sample a random proper coloring of the line graph's power, ensuring local rainbow paths.
- Weaker approach, gives polynomial powers of log n instead of O(log n).

**Applicable to**: Random regular graphs but gives suboptimal bounds; only needed before better techniques were found.

### 4. Connected Dominating Set Method (Chandran et al.)
- Find a small connected two-step dominating set S.
- Color G[S] rainbow.
- Every vertex not in S is within 2 steps of S, so paths can be extended.
- Gives rc(G) ≤ γ₂_c(G) + 3 ≤ 3n/(δ+1) + 3 via a greedy domination bound.

**Applicable to**: General graphs with minimum degree δ. Not directly useful for random regular graphs since this bound (3n/(δ+1)) >> diam = Θ(log n).

---

## Related Open Problems

1. **Exact constant for rc(G(n,r))**: Is it the case that rc(G(n,r)) = (1+o(1)) log n / log(r-1) w.h.p.? This would mean rc equals the diameter asymptotically. The lower bound is (1+o(1)) log n/log(r-1); the upper bound is c·log n/log r. For large r both are ~ log n / log r. For fixed r the gap is a fixed multiplicative constant that is currently unknown.

2. **The case r = 3 (resolved by Molloy 2017)**: Molloy proved rc(G(n,3)) = O(log n) using a separate argument, since the Dudek et al. approach based on d ≥ 3 ary trees fails for binary trees (r-1 = 2). Molloy used Noga Alon's probabilistic argument on the matching within binary trees.

3. **Rainbow vertex connection for random regular graphs**: Kamcev et al. showed rvc(G_{n,r}) ≤ c·log n / log r for r ≥ 28. Tighter bounds are open.

4. **Behavior when r grows with n**: The case r = r(n) → ∞ with n is mentioned as open by Dudek et al.

5. **Sharp constant determination**: For fixed r ≥ 5, the constant c such that rc(G(n,r)) = (c + o(1)) log n / log(r-1) is unknown. The lower bound gives c ≥ 1.

---

## Gaps and Opportunities

**Gap 1: The O(1) multiplicative constant**

The most important gap: is rc(G(n,r)) = (1+o(1)) diam(G(n,r))? The diameter is the natural lower bound and equals (1+o(1)) log n / log(r-1). Proving that rc equals this asymptotically would be a tight result. This appears accessible given the strong expansion properties of G(n,r) and the fact that very few paths are needed.

**Gap 2: Understanding when rc > diameter**

For special graphs, rc can be much larger than the diameter. For paths, rc = n-1 while diam = n-1 (so rc = diam). For cycles, rc = diam or diam + 1. For random regular graphs, the diameter is O(log n) and so is rc, but it's not known whether they are equal or if there is a gap of, say, 2 or 3 in the additive constant.

**Gap 3: The additive constant**

A cleaner but potentially harder question: is rc(G(n,r)) ≤ diam(G(n,r)) + O(1) for r ≥ 5? This additive form of the question, analogous to known results for special graph families (interval graphs, chordal graphs, etc.), is the version closest to the stated research hypothesis but should be interpreted as rc ~ diam (asymptotically), not rc ~ n/d.

**On the stated hypothesis**:

The hypothesis rc(G) = ⌈n/d⌉ + O(1) does not align with the known literature for random d-regular graphs with fixed d. For fixed d, n/d = Θ(n) while rc = Θ(log n). The bound 3n/(δ+1) + 3 ≤ 3n/d + 3 from Chandran et al. applies to all d-regular graphs including random ones, but this is a very loose upper bound for random regular graphs. The actual natural conjecture in the area is whether rc(G(n,d)) = (1+o(1)) · log n / log(d-1).

If d = d(n) grows with n, say d = n/c for some constant c, then n/d = c = O(1) and the graph is dense. In that regime, Kamcev et al.'s Theorem 1.3 would give rc = O(log n) since edge expansion of G(n,d) with d = Θ(n) is Θ(n). The bound n/d in this regime is a constant and rc would indeed be O(1). So the conjecture could potentially make sense only for very dense regular graphs (d = Θ(n)), where both rc and n/d are O(1).

---

## Recommendations for Proof Strategy

**Recommended approach for proving tight bounds**:

1. **Lower bound path**: rc(G(n,r)) ≥ diam(G(n,r)) = (1+o(1)) log n / log(r-1). This is immediate from known diameter results.

2. **Upper bound via edge-splitting (Kamcev et al. style)**: Use contiguity G_{n,r} ≈ G_{n,⌊r/2⌋} ⊕ G_{n,⌈r/2⌉} and the fact that each factor has diameter (1+o(1)) log n / log(⌊r/2⌋ - 1). The splitting lemma gives rc(G(n,r)) ≤ 2·(1+o(1)) log n / log(r/2 - 1) ~ 2 log n / log r. This is approximately 2 diam(G). To get rc = (1+o(1)) diam, a recursive or more careful splitting is needed.

3. **Key lemma to establish**: Show that G(n,r) can be decomposed into two spanning trees T₁, T₂ such that |diam(T₁) + diam(T₂)| ≤ (1+o(1)) log n / log(r-1) and E(T₁) ∩ E(T₂) = O(1). This would give rc ≤ (1+o(1)) diam via the edge-splitting lemma with no shared edges.

4. **Alternative: Direct probabilistic argument**: Use the BFS tree approach from Dudek et al. but with a more refined random coloring that uses exactly diam(G) + O(1) colors. This requires a more careful analysis of color conflicts.

**Key obstacles**:
- The BFS expansion approach (Dudek et al.) uses K₁² r log n >> log n colors because the greedy coloring assigns a fresh color to each edge based on local neighborhood conflicts. Reducing this to diam(G) + O(1) colors requires either a global coloring strategy or a very different approach.
- The edge-splitting lemma (Kamcev et al.) inherently loses a factor of 2 because it uses two separate palettes for T₁ and T₂. To achieve tight bounds, one would need a way to "reuse" colors between the two trees.

**Most promising new direction**: Investigate whether a *random proper edge coloring* with ⌈(1+ε) log n / log(r-1)⌉ colors is w.h.p. a rainbow coloring for G(n,r). This would use the expansion properties of G(n,r) to show that any pair of vertices finds a rainbow path among the many short paths available.

**Computational support**: Use NetworkX to generate small random regular graphs and verify empirically what rc(G(n,r)) is for small n and r. This could inform the exact additive constant conjecture.
