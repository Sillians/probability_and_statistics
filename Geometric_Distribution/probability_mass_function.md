## **The Geometric Distribution**

---

### **1. Overview**

The **Geometric Distribution** models the number of **Bernoulli trials** until the **first success**. 
It answers the question:

> "What is the probability that the first success occurs on the \( k \)-th trial?"

---

### **2. Assumptions**

- Trials are **independent**.
- Each trial results in **success (with probability \( p \))** or **failure (with probability \( 1 - p \))**.
- Trials are repeated **until the first success occurs**.

---

### **3. Probability Mass Function (PMF)**

\[
P(X = k) = (1 - p)^{k - 1}p
\]
- \( X \): the trial number of the first success
- \( k \in \{1, 2, 3, \dots\} \)

🧠 **Interpretation**: \( k - 1 \) failures followed by a success.

---

### **4. Cumulative Distribution Function (CDF)**

\[
P(X \leq k) = 1 - (1 - p)^k
\]

---

### **5. Mean and Variance**

- **Expected Value (Mean)**:  
  \[
  \mathbb{E}[X] = \frac{1}{p}
  \]
- **Variance**:  
  \[
  \text{Var}(X) = \frac{1 - p}{p^2}
  \]

---

### **6. Memoryless Property**

\[
P(X > m + n \mid X > m) = P(X > n)
\]

The future doesn’t depend on the past: the geometric distribution “resets” after each failure.

---

## **Probability Computations**

---

### **A. Computing a Probability at a Point**

Use the **PMF** to compute the probability of the first success occurring exactly on the \( k \)-th trial:

\[
P(X = k) = (1 - p)^{k - 1}p
\]

**Example**:  
If \( p = 0.3 \), find \( P(X = 4) \):

\[
P(X = 4) = (1 - 0.3)^3 \cdot 0.3 = 0.343 \cdot 0.3 = 0.1029
\]

---

### **B. Computing a Probability Over a Bounded Interval: Lower Bound is Zero**

This corresponds to:
\[
P(X \leq k) = 1 - (1 - p)^k
\]

**Example**:  
For \( p = 0.25 \), compute the probability that the first success happens within the first 3 trials:

\[
P(X \leq 3) = 1 - (1 - 0.25)^3 = 1 - (0.75)^3 = 1 - 0.4219 = 0.5781
\]

---

### **C. Computing a Probability Over a Bounded Interval: Lower Bound is Not Zero**

This corresponds to:
\[
P(a \leq X \leq b) = P(X \leq b) - P(X < a) = P(X \leq b) - P(X \leq a - 1)
\]

**Example**:  
Let \( p = 0.2 \). What’s the probability that the first success occurs between the 4th and 6th trial?

\[
P(4 \leq X \leq 6) = P(X \leq 6) - P(X \leq 3) = [1 - (0.8)^6] - [1 - (0.8)^3]
\]
\[
= (1 - 0.262144) - (1 - 0.512) = 0.737856 - 0.488 = 0.249856
\]

---

### **D. Computing a Probability Over an Interval Using the Complement**

When it's easier to calculate the complement of the interval and subtract from 1:

\[
P(X > k) = (1 - p)^k
\]
\[
P(X \leq k) = 1 - (1 - p)^k
\]

**Example**:  
What’s the probability the first success **takes more than 5 trials**, with \( p = 0.1 \)?

\[
P(X > 5) = (1 - 0.1)^5 = 0.9^5 = 0.59049
\]

So, the complement is:
\[
P(X \leq 5) = 1 - 0.59049 = 0.40951
\]

---

## ✅ Summary Table

| Task | Formula | Example |
|------|---------|---------|
| PMF \( P(X = k) \) | \( (1 - p)^{k-1}p \) | \( P(X = 4) = 0.1029 \) |
| \( P(X \leq k) \) | \( 1 - (1 - p)^k \) | \( P(X \leq 3) = 0.5781 \) |
| \( P(a \leq X \leq b) \) | \( P(X \leq b) - P(X \leq a - 1) \) | \( P(4 \leq X \leq 6) = 0.249856 \) |
| \( P(X > k) \) | \( (1 - p)^k \) | \( P(X > 5) = 0.59049 \) |

---
