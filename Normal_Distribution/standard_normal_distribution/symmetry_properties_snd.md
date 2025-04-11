## **Symmetry Properties of the Standard Normal Distribution**

---

#### **1. Symmetric About the Mean**

- The standard normal distribution is **perfectly symmetric** about the mean $\mu = 0$.

This means:

$`f(z) = f(-z)`$

for all values of $z$.  
So, the **height** of the curve at $z = 1$ is the same as at $z = -1$.

---

#### **2. Cumulative Distribution Function (CDF) Symmetry**

The cumulative probability to the left of $-z$ is equal to the probability to the right of $z$:

$`P(Z \leq -z) = P(Z \geq z)`$

Equivalently:

$`\Phi(-z) = 1 - \Phi(z)`$


This identity is fundamental in computing tail probabilities using the Z-table.

---

#### **3. Two-Tailed Probabilities**

For values symmetric around the mean (e.g., between $-z$ and $z$):


$`P(-z \leq Z \leq z) = 2\Phi(z) - 1`$


This helps compute confidence intervals and central probabilities.

---

### **Illustrative Examples**

---

#### **Example 1: Left and Right Tail Equality**

Find:  

$`P(Z \leq -1.5) \quad \text{and} \quad P(Z \geq 1.5)`$


From Z-table:

$`\Phi(1.5) = 0.9332`$


Then:

$`P(Z \leq -1.5) = 1 - 0.9332 = 0.0668`$


$`P(Z \geq 1.5) = 1 - \Phi(1.5) = 0.0668`$


Both tails are equal: **symmetry confirmed.**

---

#### **Example 2: Two-Tailed Probability**

Find:

$`P(-2 < Z < 2)`$



$`\Phi(2) \approx 0.9772`$



$`P(-2 < Z < 2) = \Phi(2) - \Phi(-2) = 0.9772 - (1 - 0.9772) = 0.9544`$


So, about 95.44% of values lie within two standard deviations.

---

#### **Example 3: Using Symmetry to Avoid Negative Z-table Values**

Suppose we need:


$`P(Z < -1.24)`$


Instead of using a negative z-value:


$`P(Z < -1.24) = 1 - \Phi(1.24) = 1 - 0.8925 = 0.1075`$


---

### **Why This Matters**

- **Saves time**: Use symmetry to avoid negative z-values in tables.
- **Simplifies calculation**: Easily compute tail and interval probabilities.
- **Important in hypothesis testing**: Especially for **two-tailed tests**.

---

