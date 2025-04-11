## **Modeling with the Binomial Distribution**

---

### **1. What is the Binomial Distribution?**

A **discrete probability distribution** that models the number of **successes** in a fixed number of **independent Bernoulli trials**,
each with the same probability of success.

---

### **2. Conditions for a Binomial Experiment**

To use the binomial model, the following must hold:

1. **Fixed number of trials** $n$
2. **Only two outcomes**: success or failure
3. **Constant probability of success** $p$
4. **Independent trials**

---

### **3. Binomial Probability Formula**

The probability of getting exactly $k$ successes in $n$ trials:


$`P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}`$


Where:

- $`\binom{n}{k} = \frac{n!}{k!(n-k)!}`$
- $`p`$ = probability of success
- $`1 - p`$ = probability of failure
- $`k`$ = number of successes
- $`n`$ = total number of trials

---

### **4. Mean and Standard Deviation**

- **Mean (Expected Value)**:  
  
  $`\mu = np`$
  

- **Standard Deviation**:  
  
  $`\sigma = \sqrt{np(1 - p)}`$
  

---

### **5. Examples**

---

#### **Example 1: Biased Coin Toss**

A coin is tossed 5 times. Probability of heads (success) is 0.6. What is the probability of getting exactly 3 heads?


$`n = 5,\ k = 3,\ p = 0.6`$


$`P(X = 3) = \binom{5}{3} (0.6)^3 (0.4)^2 = 10 \cdot 0.216 \cdot 0.16 = 0.3456`$


---

#### **Example 2: Quality Control**

In a batch of 10 items, the chance an item is defective is 0.1. What is the probability that exactly 2 items are defective?


$`n = 10,\ k = 2,\ p = 0.1`$



$`P(X = 2) = \binom{10}{2} (0.1)^2 (0.9)^8 = 45 \cdot 0.01 \cdot 0.4305 \approx 0.1937`$


---

### **6. Cumulative Binomial Probabilities**

To compute \( P(X \leq k) \), sum individual probabilities from $`X = 0`$ to $`X = k`$:


$`P(X \leq 3) = P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3)`$


Or use a calculator or software function (e.g., `binom.cdf(k, n, p)` in SciPy).

---

### **7. Real-World Applications**

- **Manufacturing**: Estimating defective products in batches
- **Healthcare**: Modeling treatment success in trials
- **Finance**: Probability of defaults in portfolios
- **Elections**: Modeling polling results

---

### **8. Approximating Binomial with Normal Distribution**

When $n$ is large and $p$ is not too close to 0 or 1, the binomial distribution can be approximated by a normal distribution:

$`X \sim N(np, \sqrt{np(1-p)})`$


**Apply continuity correction**:  
To approximate $`P(X \leq k)`$, use $`P(Y \leq k + 0.5)`$

