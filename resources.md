# Resources Catalog

## Summary

This document catalogs all resources gathered for the mathematics research project on tight bounds for the rainbow connection number of random regular graphs.

---

## Papers

Total papers downloaded: 9

| Title | Authors | Year | File | Key Results |
|-------|---------|------|------|-------------|
| Rainbow Connection of Random Regular Graphs | Dudek, Frieze, Tsourakakis | 2014 | papers/1311.2299_dudek_frieze_tsourakakis_rainbow_regular.pdf | rc(G(n,r)) = O(log n) for r ≥ 4 w.h.p. |
| Rainbow Connection of Sparse Random Graphs | Frieze, Tsourakakis | 2012 | papers/1201.4603_frieze_tsourakakis_rainbow_sparse_random.pdf | rc = O(log^{2θ_r} n) for r ≥ 4; rc ~ max{Z₁, diam} for G(n,p) |
| Some Remarks on Rainbow Connectivity | Kamcev, Krivelevich, Sudakov | 2015 | papers/1501.00821_kamcev_krivelevich_sudakov_rainbow_remarks.pdf | rc(G_{n,r}) ≤ c log n / log r for r ≥ 5 (asymptotically tight) |
| Rainbow Connection Number and Connected Dominating Sets | Chandran, Das, Rajendraprasad, Varma | 2010 | papers/1010.2296_chandran_das_rainbow_domsets.pdf | rc(G) ≤ 3n/(δ+1) + 3; essentially optimal for general graphs |
| Hardness and Algorithms for Rainbow Connection | Chakraborty, Fischer, Matsliah, Yuster | 2009 | papers/0809.2493_chakraborty_rainbow_hardness.pdf | rc(G) is NP-Hard to compute; NP-Complete to decide rc = 2 |
| On the Threshold for Rainbow Connection Number r in Random Graphs | Heckel, Riordan | 2013 | papers/1307.7747_heckel_riordan_rainbow_threshold.pdf | Sharp threshold for rc(G(n,p)) ≤ r (fixed r) |
| Rainbow Hamilton Cycles in Random Regular Graphs | Janson, Wormald | 2005 | papers/math_0508145_janson_wormald_rainbow_hamilton.pdf | Random r-regular graphs contain rainbow Hamilton cycles; contiguity methods |
| On Rainbow Connection Number and Connectivity | Chandran, Mathew, Rajendraprasad | 2011 | papers/1105.5704_chandran_mathew_rainbow_connectivity.pdf | Relationship between rc and connectivity |
| On Rainbow Thresholds | Han, Yuan | 2024 | papers/2310.03974_han_yuan_rainbow_thresholds.pdf | Rainbow threshold results using FKNP framework |

See papers/README.md for detailed descriptions.

---

## Prior Results Catalog

Key theorems and lemmas available for our proofs:

| Result | Source | Statement Summary | Used For |
|--------|--------|-------------------|----------|
| rc(G) ≥ diam(G) | Chartrand et al. 2008 | rc is at least the diameter | Lower bound for rc(G(n,r)) |
| diam(G(n,r)) ~ log n / log(r-1) | Bollobas-de la Vega 1982 | Random r-regular diameter | Lower bound rc(G(n,r)) ≥ (1+o(1)) log n/log(r-1) |
| rc(G) ≤ 3n/(δ+1) + 3 | Chandran et al. 2010 | General min-degree bound | Upper bound for general graphs; NOT tight for random graphs |
| rc(G(n,r)) = O(log n), r ≥ 4 | Dudek et al. 2014 | Upper bound for r ≥ 4 | Best O(log n) upper bound; proof technique reference |
| rc(G(n,3)) = O(log n) | Molloy 2017 | Completes r = 3 case | Shows r = 3 also has O(log n) bound |
| rc(G_{n,r}) ≤ c log n / log r, r ≥ 5 | Kamcev et al. 2015 | Tight upper bound | Best explicit constant; proof uses edge-splitting + contiguity |
| Edge-Splitting Lemma | Kamcev et al. 2015 | rc(G) ≤ diam(G₁) + diam(G₂) + \|E(G₁) ∩ E(G₂)\| | Core tool for upper bounds via graph decomposition |
| Configuration model probability | Bollobas 1980 | Pr[k disjoint pairs in random conf.] ≤ 1/(r^k (n-k)^k) | Used in tree-like neighborhood proofs |
| G_{n,r} ≈ G_{n,r₁} ⊕ G_{n,r₂} | Janson; Robinson-Wormald | Contiguity of random regular models | Edge-splitting for random regular graphs |
| Tree-like neighborhoods | Dudek et al. 2014, Lemma 5 | G(n,r) is locally tree-like w.h.p. | Enables BFS tree expansion argument |
| κ_{ℓ,d} ≥ d^{2ℓ}/4 (Lemma 2) | Dudek et al. 2014 | d-ary tree rainbow matching bound | Core to proving O(log n) upper bound for r ≥ 4 |
| Chernoff bounds | Standard | Bin(n,p) tail bounds | BFS expansion probability estimates |

---

## Computational Tools

| Tool | Purpose | Location | Notes |
|------|---------|----------|-------|
| NetworkX | Graph generation and computation | pip package (installed) | Generate G(n,r), compute diameters, verify small cases |
| Python arxiv | Literature search | pip package (installed) | Used for paper discovery |
| pypdf | PDF reading | pip package (installed) | Used for paper reading via chunker |

### Notes on Computational Setup
- Virtual environment: `.venv/` (Python 3.12.8)
- Packages installed: networkx, pypdf, requests, arxiv, httpx
- For small computational verification, NetworkX can generate random regular graphs and compute rc numerically.

---

## Resource Gathering Notes

### Search Strategy

1. Used the paper-finder service with query "rainbow connection number random regular graphs" (diligent mode) returning 135 papers from Semantic Scholar.
2. Identified top-relevance papers (score 3): Dudek et al. 2013, Kamcev et al. 2015, Frieze-Tsourakakis 2012, Molloy 2017.
3. Used the Python arxiv API to find correct arXiv IDs (the URLs provided in the research spec 1005.1665 and 1101.5428 are NOT the rainbow connection papers; actual IDs are 1201.4603 and 1311.2299).
4. Downloaded papers via arxiv API download method.
5. Used PDF chunker to read papers 3 pages at a time.

### Selection Criteria

Prioritized papers that:
- Directly study rc(G(n,r)) for random regular graphs (primary)
- Contain proof techniques applicable to tight bound analysis
- Establish foundational results (diameter, tree-like structure)
- Provide general bounds that illuminate what is special about random graphs

### Key Note on User-Specified arXiv IDs

The research specification provided URLs https://arxiv.org/abs/1005.1665 and https://arxiv.org/abs/1101.5428 which correspond to completely different papers (non-classicality estimation and digital ecosystems respectively). The correct arXiv IDs for the rainbow connection papers cited are:
- Frieze-Tsourakakis 2012 sparse random graphs: **arXiv:1201.4603**
- Dudek-Frieze-Tsourakakis 2014 random regular: **arXiv:1311.2299**

---

## Recommendations for Proof Construction

### 1. Correct the Research Hypothesis

The stated hypothesis rc(G(n,d)) = ⌈n/d⌉ + O(1) is likely incorrect for fixed constant d ≥ 3. For fixed d:
- n/d = Θ(n) grows linearly
- rc(G(n,d)) = Θ(log n) as shown by multiple papers

The natural conjecture in this area is:

**Conjecture**: rc(G(n,r)) = (1+o(1)) · diam(G(n,r)) = (1+o(1)) · log n / log(r-1) w.h.p.

The current best bounds give a gap of only a multiplicative constant factor for r ≥ 5.

### 2. Proof Strategy

**Lower bound** (already known): rc(G(n,r)) ≥ diam(G(n,r)) ~ log n / log(r-1).

**Upper bound approaches** (in order of promise):

(a) *Improve the edge-splitting lemma*: Show G(n,r) can be split into two spanning subgraphs G₁, G₂ with |E(G₁) ∩ E(G₂)| = O(1) and diam(G₁) + diam(G₂) = (1+o(1)) log n / log(r-1). This would give rc ≤ (1+o(1)) diam + O(1).

(b) *Random proper coloring approach*: Show that a random proper edge coloring with exactly ⌈(1+ε) log n / log(r-1)⌉ colors is w.h.p. a rainbow coloring. Uses the expansion of G(n,r): any two vertices have many vertex-disjoint short paths, so one is likely to be rainbow.

(c) *Strengthen Dudek et al.*: The current proof uses q = K₁²r log n colors, far more than the diameter. Analyzing whether q = C · log n / log(r-1) suffices for some explicit constant C.

### 3. Key Prerequisites to Establish

- Precise diameter distribution of G(n,r) (not just asymptotics; need to know diam ≤ (1+ε)log_{r-1} n for explicit ε)
- Number of vertex-disjoint paths of length ≤ (1+ε)diam between any pair of vertices in G(n,r)
- Mixing time of random walks on G(n,r) (relevant for random coloring approaches)

### 4. Potential Difficulties

- The BFS tree approach in Dudek et al. fundamentally requires many more colors than the diameter because of the greedy coloring step. Breaking this barrier requires a global (non-greedy) coloring strategy.
- The edge-splitting lemma (Kamcev et al.) is tight for bipartite graphs but may lose a constant factor for random graphs. Proving O(1) overlap in the split requires careful analysis.

### 5. Computational Verification

Before attempting proofs, verify computationally for small n (n ≤ 100) and r = 3, 4, 5:
1. What is rc(G(n,r)) vs. diam(G(n,r)) for random instances?
2. Does rc(G(n,r)) = diam(G(n,r)) always hold, or are there instances with rc > diam?
3. What is the distribution of rc - diam?

NetworkX can compute exact rc via BFS, though this is O(n^3) so limited to small graphs.
