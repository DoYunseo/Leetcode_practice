# Find the town judge

In a town, there are n people labeled from `1 to n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.

2. Everybody (except for the town judge) trusts the town judge.

3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust [i] = [ai, bi] representing that the person labeled ai trusts the person
labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

# Savio's Solution Complexity Analysis

First off, I start by making constructing the indegree and outdegree dictionarys which costs `O(n)` each

Then we loop through the array trust which takes `O(len(trust))` to populate the indegree and outdegree dictionaries.

Then we finally iterage once again from 1 to n, which takes `O(n)` to find the judge.

Adding everything up: `O(n) + O(n) + O(len(trust)) + O(n) = O(3n + len(trust))`

Dropping the constants, we have that the time complexity is

`T(n) = O(n + len(trust))`
