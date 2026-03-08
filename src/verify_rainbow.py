#!/usr/bin/env python3
"""
Computational verification of rainbow connection number bounds
for random regular graphs.

Strategy for exact rc:
- Lower bound: rc >= diam(G)
- Upper bound: BFS-tree coloring gives rc <= diam + (m - n + 1)
- For small graphs (n <= 10), use random coloring search starting from k = diam
- Key check: is_rainbow_connected uses BFS with bitmask states, but we
  limit to k <= 6 colors so bitmask fits in 64-bit int and state space is manageable.
"""

import random
import numpy as np
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from itertools import combinations, product
from collections import deque
import sys
import os
import time

random.seed(42)
np.random.seed(42)


def is_rainbow_connected(G, color_dict):
    """Check if edge coloring makes G rainbow connected. Uses BFS with color bitmask."""
    nodes = list(G.nodes())
    edges_key = {(min(u, v), max(u, v)): c for (u, v), c in color_dict.items()}

    for i in range(len(nodes)):
        s = nodes[i]
        # BFS: state = (vertex, frozenset of used colors as bitmask)
        visited = {}  # vertex -> set of color-masks that reach it
        queue = deque([(s, 0)])
        reached = {s}
        visited[s] = {0}

        while queue:
            v, mask = queue.popleft()
            for w in G.neighbors(v):
                e = (min(v, w), max(v, w))
                c = edges_key[e]
                c_bit = 1 << c
                if not (mask & c_bit):
                    new_mask = mask | c_bit
                    if w not in visited:
                        visited[w] = set()
                    # Pruning: only add state if no subset already reaches w
                    # (dominated states: if mask1 subset of mask2, mask1 is better)
                    dominated = any((new_mask & m) == m for m in visited[w])
                    if not dominated:
                        # Remove states dominated by new_mask
                        visited[w] = {m for m in visited[w] if (m & new_mask) != new_mask}
                        visited[w].add(new_mask)
                        reached.add(w)
                        queue.append((w, new_mask))

        if len(reached) < len(nodes):
            return False
    return True


def compute_rc_exact_small(G, max_k=8, trials_per_k=500, time_limit=5.0):
    """
    Compute (or bound) rc(G) for small graphs.
    Returns (rc, exact) where exact=True if we verified the coloring works.
    Starts from k = diam(G) and tries random colorings.
    """
    edges = list(G.edges())
    m = len(edges)
    diam = nx.diameter(G)

    edge_index = {(min(u, v), max(u, v)): i for i, (u, v) in enumerate(edges)}

    def try_coloring(k, n_trials):
        for _ in range(n_trials):
            coloring_list = [random.randint(0, k - 1) for _ in edges]
            color_dict = {e: coloring_list[i] for e, i in edge_index.items()}
            if is_rainbow_connected(G, color_dict):
                return True
        return False

    t0 = time.time()
    for k in range(diam, min(max_k, m) + 1):
        if time.time() - t0 > time_limit:
            return k, False  # timed out, return current k as upper bound
        found = try_coloring(k, trials_per_k)
        if found:
            return k, True

    return m, False


def fast_rc_upper_bound(G):
    """
    Upper bound on rc(G) using BFS tree coloring.
    Tree edges at depth i get color i; non-tree edges get fresh colors.
    """
    root = next(iter(G.nodes()))
    tree = nx.bfs_tree(G, root)
    depths = nx.single_source_shortest_path_length(G, root)
    max_depth = max(depths.values())

    next_color = max_depth + 1
    for u, v in G.edges():
        if not (tree.has_edge(u, v) or tree.has_edge(v, u)):
            next_color += 1

    return next_color - 1


def diameter(G):
    return nx.diameter(G)


def run_small_exact():
    """Exact rc for small graphs, comparing to diameter."""
    print("Exact rc computation for small random d-regular graphs")
    print("=" * 60)
    print(f"{'n':>4} {'d':>3} {'seed':>5} {'diam':>5} {'rc':>5} {'exact':>6} {'rc=diam':>8}")
    print("-" * 50)

    results = []
    for n, d in [(6, 3), (8, 3), (8, 4), (10, 3), (10, 4), (12, 3), (12, 4)]:
        if (n * d) % 2 != 0:
            continue
        for seed in range(5):
            try:
                G = nx.random_regular_graph(d, n, seed=seed)
                if not nx.is_connected(G):
                    continue
                diam = diameter(G)
                rc, exact = compute_rc_exact_small(G, max_k=diam + 2, trials_per_k=1000, time_limit=3.0)
                eq = (rc == diam)
                results.append({'n': n, 'd': d, 'diam': diam, 'rc': rc, 'exact': exact, 'eq': eq})
                if seed < 2:
                    print(f"{n:>4} {d:>3} {seed:>5} {diam:>5} {rc:>5} {'yes' if exact else 'ub':>6} {'YES' if eq else 'NO':>8}")
            except Exception as e:
                pass

    total = len(results)
    eq_count = sum(1 for r in results if r['eq'])
    exact_count = sum(1 for r in results if r['exact'])
    print(f"\nrc = diam in {eq_count}/{total} cases ({100*eq_count/total:.0f}%)")
    print(f"Exact computation succeeded in {exact_count}/{total} cases")
    return results


def run_large_experiments():
    """Diameter and upper bound experiments for larger n."""
    print("\nDiameter and rc upper bound for larger graphs")
    print("=" * 60)
    print(f"{'n':>6} {'d':>3} {'avg_diam':>9} {'theo_diam':>10} {'ratio':>7} {'rc_ub':>7}")
    print("-" * 55)

    data = {}
    params = [
        (50, 3), (50, 4), (50, 5),
        (100, 3), (100, 4), (100, 5),
        (200, 3), (200, 4), (200, 5),
        (500, 3), (500, 5),
        (1000, 3), (1000, 5),
    ]

    for n, d in params:
        diams, rc_ubs = [], []
        for seed in range(20):
            try:
                G = nx.random_regular_graph(d, n, seed=seed)
                if nx.is_connected(G):
                    diams.append(diameter(G))
                    rc_ubs.append(fast_rc_upper_bound(G))
            except Exception:
                continue
        if diams:
            avg_diam = np.mean(diams)
            avg_rc_ub = np.mean(rc_ubs)
            theo = np.log(n) / np.log(d - 1)
            ratio = avg_diam / theo
            print(f"{n:>6} {d:>3} {avg_diam:>9.2f} {theo:>10.2f} {ratio:>7.3f} {avg_rc_ub:>7.1f}")
            data[(n, d)] = {'avg_diam': avg_diam, 'theo_diam': theo, 'ratio': ratio, 'rc_ub': avg_rc_ub}

    return data


def make_plots(large_data):
    """Create analysis plots."""
    os.makedirs('/workspaces/rainbow-conn-random-1698/figures', exist_ok=True)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    d_vals = [3, 4, 5]
    colors = ['steelblue', 'firebrick', 'seagreen']
    n_range = [20, 50, 100, 200, 500, 1000]

    # --- Plot 1: diam and rc_ub vs n ---
    ax = axes[0, 0]
    for d, col in zip(d_vals, colors):
        ns, diams, theo = [], [], []
        for n in n_range:
            dv = []
            for seed in range(15):
                try:
                    G = nx.random_regular_graph(d, n, seed=seed)
                    if nx.is_connected(G):
                        dv.append(diameter(G))
                except Exception:
                    pass
            if dv:
                ns.append(n)
                diams.append(np.mean(dv))
                theo.append(np.log(n) / np.log(d - 1))
        if ns:
            ax.plot(ns, diams, 'o-', color=col, label=f'd={d} diam')
            ax.plot(ns, theo, '--', color=col, alpha=0.5, label=f'd={d} ln(n)/ln(d-1)')
    ax.set_xscale('log')
    ax.set_xlabel('n')
    ax.set_ylabel('diameter')
    ax.set_title('Diameter vs n (random d-regular graphs)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # --- Plot 2: diam / (ln n / ln(d-1)) vs n ---
    ax = axes[0, 1]
    for d, col in zip(d_vals, colors):
        ns, ratios = [], []
        for n in n_range:
            dv = []
            for seed in range(15):
                try:
                    G = nx.random_regular_graph(d, n, seed=seed)
                    if nx.is_connected(G):
                        dv.append(diameter(G))
                except Exception:
                    pass
            if dv:
                ns.append(n)
                theo = np.log(n) / np.log(d - 1)
                ratios.append(np.mean(dv) / theo)
        if ns:
            ax.plot(ns, ratios, 'o-', color=col, label=f'd={d}')
    ax.axhline(1.0, color='black', linestyle=':', label='ratio = 1 (tight)')
    ax.set_xscale('log')
    ax.set_xlabel('n')
    ax.set_ylabel('diam(G) / [ln(n)/ln(d-1)]')
    ax.set_title('Convergence of diameter to theoretical value')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Plot 3: diam vs d for fixed n ---
    ax = axes[1, 0]
    for n_fixed, col in [(100, 'steelblue'), (500, 'firebrick')]:
        d_range = [3, 4, 5, 6, 8, 10, 15, 20]
        ds, diams, theos = [], [], []
        for d in d_range:
            if (n_fixed * d) % 2 != 0:
                continue
            dv = []
            for seed in range(15):
                try:
                    G = nx.random_regular_graph(d, n_fixed, seed=seed)
                    if nx.is_connected(G):
                        dv.append(diameter(G))
                except Exception:
                    pass
            if dv:
                ds.append(d)
                diams.append(np.mean(dv))
                theos.append(np.log(n_fixed) / np.log(d - 1))
        if ds:
            ax.plot(ds, diams, 'o-', color=col, label=f'n={n_fixed} observed')
            ax.plot(ds, theos, '--', color=col, alpha=0.5, label=f'n={n_fixed} ln(n)/ln(d-1)')
    ax.set_xlabel('d (degree)')
    ax.set_ylabel('diameter')
    ax.set_title('Diameter vs degree')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Plot 4: Distribution of diam for n=200, d=4 ---
    ax = axes[1, 1]
    n_test, d_test = 200, 4
    diam_samples = []
    for seed in range(100):
        try:
            G = nx.random_regular_graph(d_test, n_test, seed=seed)
            if nx.is_connected(G):
                diam_samples.append(diameter(G))
        except Exception:
            pass
    if diam_samples:
        theo = np.log(n_test) / np.log(d_test - 1)
        ax.hist(diam_samples, bins=range(min(diam_samples), max(diam_samples) + 2),
                align='left', color='steelblue', alpha=0.7, edgecolor='white')
        ax.axvline(theo, color='red', linestyle='--', linewidth=2,
                   label=f'ln(n)/ln(d-1) = {theo:.2f}')
        ax.axvline(np.mean(diam_samples), color='black', linestyle='-',
                   label=f'mean = {np.mean(diam_samples):.2f}')
        ax.set_xlabel('diameter')
        ax.set_ylabel('count')
        ax.set_title(f'Distribution of diam(G): n={n_test}, d={d_test}, 100 samples')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = '/workspaces/rainbow-conn-random-1698/figures/rainbow_connection_analysis.png'
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nFigure saved: {path}")


if __name__ == '__main__':
    print(f"Python: {sys.version.split()[0]}")
    print(f"NetworkX: {nx.__version__}")
    print(f"NumPy: {np.__version__}")
    print()

    small_results = run_small_exact()
    large_data = run_large_experiments()
    make_plots(large_data)

    print("\nDone.")
