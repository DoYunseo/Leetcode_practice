class MyPair {
    private int node;
    private long cost;

    public MyPair(int node, long cost) {
        this.node = node;
        this.cost = cost;
    }

    public int getNode() {
        return this.node;
    }

    public long getCost() {
        return this.cost;
    }
}

class Solution {
    private boolean check(int limit, int n, long k, Map<Integer, List<int[]>> adj) {
        long[] cost_matrix = new long[n];

        PriorityQueue<MyPair> pq = new PriorityQueue<>(new Comparator<>() {
            @Override
            public int compare(MyPair p1, MyPair p2) {
                return Long.compare(p1.getCost(), p2.getCost());
            }
        });

        for (int i = 0; i < n; i++) {
            cost_matrix[i] = k + 1;
        }
        cost_matrix[0] = 0;

        pq.add(new MyPair(0, 0));

        while (!pq.isEmpty()) {

            MyPair pair = pq.poll();
            int node = pair.getNode();
            long cost = pair.getCost();

            if (node == n - 1)
                return true;
            if (cost > cost_matrix[node])
                continue;

            for (int[] neighbor : adj.get(node)) {
                int new_node = neighbor[0];
                int new_cost = neighbor[1];

                if (new_cost < limit)
                    continue;
                long r_sum = cost + new_cost;
                if (r_sum < cost_matrix[new_node]) {
                    cost_matrix[new_node] = r_sum;
                    pq.add(new MyPair(new_node, r_sum));
                }
            }

        }
        return false;
    }

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n = online.length;
        int left = Integer.MAX_VALUE;
        int right = 0;
        int result = -1;

        Map<Integer, List<int[]>> adj = new HashMap<>();

        for (int i = 0; i < n; i++) {
            adj.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], cost = edge[2];
            if (!online[u] || !online[v])
                continue;
            adj.get(u).add(new int[] { v, cost });
            left = Math.min(left, cost);
            right = Math.max(right, cost);
        }

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid, n, k, adj)) {
                result = mid;
                left = mid + 1;
            } else
                right = mid - 1;
        }

        return result;
    }
}