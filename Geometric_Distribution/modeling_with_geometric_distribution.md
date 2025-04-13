## **Modeling with the Geometric Distribution**

---

### **Overview**

The **geometric distribution** models the number of **Bernoulli trials** needed to get 
the **first success**, where each trial is independent and has a constant success 
probability $p$. This distribution answers: *"How many trials until the first success?"*

---

### **Definition**

Let $X$ be a discrete random variable representing the number of trials until the first success. 
Then:

$`P(X = k) = (1 - p)^{k - 1} p, \quad k = 1, 2, 3, \dots`$


- $p$: probability of success on each trial  
- $`(1 - p)^{k - 1}`$: probability of $k - 1$ failures before the first success

---

### **Key Properties**

- **Support**: $`X \in \{1, 2, 3, \dots\}`$


- **Mean (Expected Value)**:
  
  $`\mathbb{E}[X] = \frac{1}{p}`$
  

- **Variance**:
  
  $`\text{Var}(X) = \frac{1 - p}{p^2}`$
  

- **Memoryless Property**:
  
  $`P(X > m + n \mid X > m) = P(X > n)`$
  

  The geometric distribution is the **only discrete distribution** with this property.

---

### **Use Cases**

1. **Call centers**: How many calls until someone answers "Yes" to a product?
2. **Quality control**: Number of items tested before finding the first defective.
3. **Clinical trials**: Number of patients treated before the first shows side effects.

---

### **Modeling Steps**

1. **Check for Bernoulli trials**: Each trial is independent, binary outcome (success/failure), and success probability is constant.
2. **Identify what you are measuring**: Number of trials *until* first success.
3. **Use PMF** to compute probabilities for specific outcomes.
4. **Use expected value** if looking for average performance over time.

---

### **Example Problem**

> A machine has a 20% chance of producing a defective item. What is the probability the first defective is the 4th item?


$`P(X = 4) = (1 - 0.2)^{3} \cdot 0.2 = (0.8)^3 \cdot 0.2 = 0.1024`$









