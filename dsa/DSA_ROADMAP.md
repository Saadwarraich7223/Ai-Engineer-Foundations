# ⚡ 30-Minute Daily DSA — ML/AI Engineer Edition

> You don't need to be a LeetCode god. You need to think algorithmically enough to write efficient data pipelines, debug performance issues, and pass ML engineer interviews.

---

## 🎯 The Minimal Viable DSA for ML/AI Engineers

| Topic | ML Relevance | Interview Weight |
|-------|-------------|------------------|
| Arrays & Strings | Data preprocessing, feature vectors, sequence data | 🔴 High (every interview) |
| Hashing | Frequency counts, feature encoding, grouping | 🔴 High |
| Stack / Queue | BFS for graphs, tree traversal, sequence processing | 🟡 Medium |
| Recursion | Tree models (decision trees), divide & conquer | 🟡 Medium |
| Sorting + Binary Search | Search algorithms, data cleaning, efficient lookups | 🟡 Medium |
| Linked Lists | Optional — LRU cache, memory management concepts | 🟢 Low |

---

## ⏱️ Daily Routine (30 Minutes)

```
5 min   → Review pattern from yesterday
15 min  → Learn a new pattern + trace it on paper
10 min  → Solve one LeetCode problem
```

**Weekly cadence**: 6 days DSA, 1 day rest/revision.

---

## 📅 6-Week DSA Plan

### Week 1 — Arrays & Two Pointers

| Day | Topic | Pattern | LeetCode |
|-----|-------|---------|----------|
| 1 | Array basics, traversal, in-place modification | Loop, swap | [27. Remove Element](https://leetcode.com/problems/remove-element/) |
| 2 | Two pointers (sorted) | `i=0, j=n-1`, move inward | [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| 3 | Two pointers (unsorted) | `slow, fast` pointer | [26. Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |
| 4 | Two pointers (partition) | Dutch flag, 3-way partition | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) |
| 5 | Sliding window (fixed size) | Window sum, max/min | [643. Max Avg Subarray](https://leetcode.com/problems/maximum-average-subarray-i/) |
| 6 | Sliding window (variable size) | Expand/contract with condition | [3. Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |

**Python Pattern** — Two Pointers:
```python
def two_sum_sorted(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        curr = numbers[i] + numbers[j]
        if curr == target:
            return [i + 1, j + 1]
        elif curr < target:
            i += 1
        else:
            j -= 1
    return []
```

---

### Week 2 — Hashing & Prefix Sum

| Day | Topic | Pattern | LeetCode |
|-----|-------|---------|----------|
| 7 | Frequency maps | `collections.Counter` | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) |
| 8 | Dictionary for lookups | `dict` as cache | [1. Two Sum](https://leetcode.com/problems/two-sum/) |
| 9 | Prefix sum basics | Running total array | [1480. Running Sum](https://leetcode.com/problems/running-sum-of-1d-array/) |
| 10 | Prefix sum with hashmap | Subarray sums | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 11 | Set operations | Deduplication, intersection | [349. Intersection of Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) |
| 12 | Review + mixed problems | All week 1–2 patterns | Solve any 2 unseen easys |

**Python Pattern** — Prefix Sum + HashMap:
```python
def subarray_sum(nums, k):
    prefix = {0: 1}  # sum -> count
    curr_sum = count = 0
    for n in nums:
        curr_sum += n
        count += prefix.get(curr_sum - k, 0)
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
    return count
```

---

### Week 3 — Recursion

| Day | Topic | Pattern | LeetCode |
|-----|-------|---------|----------|
| 13 | Call stack visualization | Trace on paper | [509. Fibonacci](https://leetcode.com/problems/fibonacci-number/) |
| 14 | Tree recursion | Multiple branches | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |
| 15 | Divide & conquer | Split then combine | [104. Max Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| 16 | Backtracking basics | Explore + un-choose | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) |
| 17 | Memoization | Top-down DP | [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) |
| 18 | Review | Recursion tree drill | Fibonacci with and without memo |

**Python Pattern** — Recursion + Memo:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

---

### Week 4 — Stack & Queue

| Day | Topic | Pattern | LeetCode |
|-----|-------|---------|----------|
| 19 | Stack basics (LIFO) | `list` as stack | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |
| 20 | Stack for parsing | String processing | [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) |
| 21 | Monotonic stack | Next greater/smaller | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) |
| 22 | Queue basics (FIFO) | `collections.deque` | [933. Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) |
| 23 | Deque as sliding window | Max/min in window | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| 24 | Review | Stack + queue patterns | Valid parentheses, daily temps |

**Python Pattern** — Monotonic Stack:
```python
def daily_temperatures(temps):
    stack = []
    result = [0] * len(temps)
    for i, t in enumerate(temps):
        while stack and t > temps[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result
```

---

### Week 5 — Sorting, Binary Search & Linked Lists

| Day | Topic | Pattern | LeetCode |
|-----|-------|---------|----------|
| 25 | Binary search basics | Halve the search space | [704. Binary Search](https://leetcode.com/problems/binary-search/) |
| 26 | Binary search variants | Bound finding | [34. First/Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 27 | Sorting logic | Sort + two pointers | [977. Squares of Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) |
| 28 | Linked list basics | Traversal, insertion | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |
| 29 | Linked list two pointers | `slow, fast` | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) |
| 30 | Linked list merge | Merge sorted lists | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) |

**Python Pattern** — Binary Search:
```python
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
```

---

### Week 6 — Review & Mixed Practice

| Day | Topic | Focus |
|-----|-------|-------|
| 31 | Arrays + Two Pointers | Solve 3 unseen easys |
| 32 | Hashing + Prefix Sum | Solve 3 unseen easys |
| 33 | Recursion + DP | Solve 2 mediums |
| 34 | Stack + Queue | Solve 2 mid-range |
| 35 | Binary Search + Sort | Solve 3 problems |
| 36 | **Final assessment** | Solve 5 problems in 50 min (any topic) |

---

## 📊 LeetCode Difficulty Progression

```
Week 1-2: Easy     → 15-20 min each
Week 3-4: Easy     → 10-15 min each
Week 5:   Easy+    → add 1-2 Medium
Week 6:   Medium   → 25-35 min each
```

**Target by end of 6 weeks**: Comfortably solve LeetCode Easy in 15 min, Medium with hints in 30 min.

---

## 🧠 Problem-Solving Framework

For every problem, follow this script:

```
1. BRUTE FORCE   → Naive solution (say it out loud)
2. BETTER        → What's wasteful? (time/space)
3. OPTIMAL       → Apply pattern (hashmap? two pointers? binary search?)
4. DRY RUN       → Trace on small example
5. EDGE CASES    → Empty input, single element, negatives, duplicates
6. CODE          → Write clean, named variables
```

---

## 🐍 Python Cheat Sheet for DSA

| Operation | Code | Complexity |
|-----------|------|------------|
| List append | `arr.append(x)` | O(1) |
| List pop end | `arr.pop()` | O(1) |
| List pop index | `arr.pop(i)` | O(n) |
| Dict get/set | `d[k]`, `d[k] = v` | O(1) avg |
| Dict safe get | `d.get(k, default)` | O(1) |
| Counter | `from collections import Counter` | O(n) |
| Deque append/pop | `dq.append()`, `dq.popleft()` | O(1) |
| Stack (list) | `stack.append()`, `stack.pop()` | O(1) |
| Min/Max of list | `min(arr)`, `max(arr)` | O(n) |
| Sort | `sorted(arr)` or `arr.sort()` | O(n log n) |
| Reverse | `arr[::-1]` or `arr.reverse()` | O(n) |
| Set membership | `x in my_set` | O(1) avg |

---

## 🚀 When DSA Meets ML — Real Connections

| DSA Concept | Where It Shows Up in ML/AI |
|-------------|---------------------------|
| **Sliding window** | Time-series rolling averages, convolution, sequence batching |
| **Prefix sum** | Cumulative distribution functions, feature normalization |
| **Hashmap / Counter** | One-hot encoding, vocabulary building, feature hashing |
| **Stack** | Tree traversal for decision trees, expression parsing |
| **Binary search** | Hyperparameter tuning (learning rate search), threshold optimization |
| **Sorting** | Ranking metrics (NDCG), k-NN neighbors, priority queues |
| **Recursion** | Decision tree induction, recursive feature elimination |
| **Two pointers** | Merge sorted feature sets, array intersection |

---

## 📚 Resources (Curated, Minimal)

| Resource | Best For | Time |
|----------|----------|------|
| [NeetCode Roadmap](https://neetcode.io/roadmap) | Structured DSA path | 30 min/day |
| [LeetCode Explore Cards](https://leetcode.com/explore/) | Topic deep dives | 20 min/card |
| [Cracking the Coding Interview (book)](https://www.crackingthecodinginterview.com/) | Interview prep | Chapter per week |
| [Visualgo.net](https://visualgo.net/) | Visualizing algorithms | 5 min glance |
| [Python `collections` docs](https://docs.python.org/3/library/collections.html) | Data structure reference | As needed |

---

## ✅ Weekly Check-in Template

```
Week ___

Patterns covered:
  □ Two pointers     □ Sliding window     □ Prefix sum
  □ Hashing          □ Recursion          □ Stack/Queue
  □ Binary search    □ Linked list

Problems solved this week: ___
Total problems so far: ___

Be honest — which pattern still feels shaky? _______________

Next week's focus: _______________
```

---

> **30 minutes a day > 5 hours on Saturday.**
>
> Consistency compounds. You're not trying to win LeetCode — you're building algorithmic intuition that makes you a better engineer.
