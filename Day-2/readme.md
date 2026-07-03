# Python DSA Practice – Real World Searching & Sorting

This repository contains beginner-friendly Python programs that explain common Data Structures and Algorithms (DSA) concepts using real-world examples.

The programs are written in simple Python with functions so that students can easily understand the logic.

---

## 📚 Programs Included

### 1. Spam Detector (Linear Search)

**Problem**
A cybersecurity system checks whether an incoming sender ID is present in a blacklist of spam senders.

**Algorithm Used**
- Linear Search

**Concept**
- Search each element one by one.
- If the sender ID is found, return its position.
- Otherwise, return `-1`.

**Time Complexity**
- **O(n)**

---

### 2. E-Commerce Price Filter (Binary Search - Lower Bound)

**Problem**
Find the first product whose price is greater than or equal to the target price.

Example:
```
Prices:
25000 32000 45000 50000 55000 70000

Target:
50000

Output:
50000
```

**Algorithm Used**
- Binary Search (Lower Bound)

**Concept**
- Products are already sorted.
- Binary Search reduces the search space by half.
- Find the first value that is greater than or equal to the target.

**Time Complexity**
- **O(log n)**

---

### 3. IRCTC Waitlist Merger (Merge Step of Merge Sort)

**Problem**
Merge two sorted waitlists into one sorted waitlist.

Example:
```
List 1:
2 5 8 12

List 2:
1 4 7 10

Output:
1 2 4 5 7 8 10 12
```


**Time Complexity**
- **O(n + m)**


## 💻 Technologies Used

- Python 3

---

