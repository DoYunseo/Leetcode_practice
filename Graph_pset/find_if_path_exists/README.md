# Leetcode Problem 1971- Find if path exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from `0` to `n - 1` (inclusive). The edges in the graph are represented as a 2D integer array edges , where each edges `[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination

Given edges and the integers `n`, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

# Savio's Complexity Analysis

Let `N` be the number of nodes (`n` in the code) and `M` be the number of edges (`len(edges)`).

1.  **Building the Adjacency List:**

    - First up, I create the basic structure of my `adj_list`:
      ```python
      adj_list = {i: [] for i in range(n)}
      ```
      This is a loop that runs `N` times (for `n` nodes). So, that's  **`O(N)`**.
    - Next, I go through all the `edges` to actually fill in the connections:
      ```python
      for u, v in edges:
          adj_list[u].append(v)
          adj_list[v].append(u)
      ```
      If there are `M` edges, this loop runs `M` times. Appending to a list is usually `O(1)` on average. So, this part costs **`O(M)`**.

    _So, for the whole adjacency list setup, we have `O(N) + O(M)` which simplifies to **`O(N + M)`**._

2.  ** Evaluating the Depth First Search (DFS):**

    - Initializing my `visited` set:
      ```python
      visited = set()
      ```
      That's just **`O(1)`**.
    - Now for the `dfs_helper` function. 
      - The check `if node in visited:`: costs  **`O(1)`**.
      - Adding to the set `visited.add(node)`: Also averages **`O(1)`**.
      - Looping through neighbors `for neighbor in adj_list[node]:`:
         For _one_ node, I look at all its direct neighbors. If a node has `k` neighbors, that's `k` operations for that specific call.
        However, because of my `visited` set, I only fully process each node (and its neighbors) _once_.
        - Each node will be added to `visited` at most once. That's `N` operations in total for all node visits (`N` calls to `dfs_helper` where the node isn't yet visited).
        - Over the entire DFS, every edge `(u,v)` in the `adj_list` will be considered twice (once when visiting `u` and looking at `v`, and once when visiting `v` and looking at `u`, if the graph is connected and undirected). So, if there are `M` edges, the sum of degrees is `2M`. This means all the "looping through neighbors" across all `dfs_helper` calls sums up to about **`O(M)`** work.

    _Combining these, the DFS itself visits each node and each edge (in its component) roughly once. So, the DFS part costs **`O(N + M)`** (in the worst case, where all nodes and edges are part of the traversal from the source)._

3.  **Adding It All Up (Total Time Complexity):**

    - Adjacency List: `O(N + M)`
    - DFS (initialization `O(1)` + actual traversal `O(N+M)`): `O(N + M)`

    So, T(N, M) = `O(N + M)` (for adj list) + `O(N + M)` (for DFS)
    Which gives us a grand total time complexity of **`O(N + M)`**.

    This means the time it takes grows linearly with the number of nodes _and_ the number of edges.
