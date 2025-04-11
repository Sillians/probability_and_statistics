## **The Standard Normal Distribution**

---

#### **Definition**:

The **standard normal distribution** is a special case of the normal distribution with:

- **Mean $(μ) = 0$**
- **Standard Deviation $(σ) = 1$**

It is a **bell-shaped**, **symmetric** probability distribution used to model standardized values.

---

### **Probability Density Function (PDF)**


$`f(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}`$


Where:
- $`z \in (-\infty, \infty)`$ is the standardized variable (z-score)
- The total area under the curve is **1**

---

### **Standardization (Z-score)**

To transform a normally distributed random variable $`X \sim N(\mu, \sigma^2)`$ into a standard normal variable:


$`z = \frac{x - \mu}{\sigma}`$


This allows comparison across different normal distributions.

---

### **Cumulative Distribution Function (CDF)**


$`\Phi(z) = P(Z \leq z) = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-t^2/2} \, dt`$


- There's **no closed-form** for $`\Phi(z)`$; we use **tables** or numerical tools.

---

### **Properties**

- Symmetric about 0
- Mean = 0, Median = 0, Mode = 0
- 68% of values lie within 1 standard deviation: $`P(-1 \leq Z \leq 1) \approx 0.68`$
- 95% within 2 standard deviations: $`P(-2 \leq Z \leq 2) \approx 0.95`$
- 99.7% within 3 standard deviations: $`P(-3 \leq Z \leq 3) \approx 0.997`$

---

### **Using Z-tables**

Z-tables give the area under the curve to the **left** of a z-value.

#### Example 1:  
**What is $`P(Z \leq 1.25)`$?**

From the Z-table:  

$`P(Z \leq 1.25) = \Phi(1.25) \approx 0.8944`$


#### Example 2:  
**What is $`P(Z > 1.25)`$?**


$`P(Z > 1.25) = 1 - \Phi(1.25) = 1 - 0.8944 = 0.1056`$


---

### **Applications**

- Standardizing scores (test scores, measurements)
- Hypothesis testing (z-tests)
- Confidence intervals

---

### **Example Problem:**

Let $`X \sim N(100, 15^2)`$. Find:

#### (a) $P(X < 120)$

1. Standardize:  
   
   $`z = \frac{120 - 100}{15} = \frac{20}{15} = 1.33`$
   

2. Look up $\Phi(1.33) \approx 0.9082$

#### Answer:  

$`P(X < 120) = 0.9082`$
