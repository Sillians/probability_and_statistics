## **Mean and Variance of the Normal Distribution**

---

### **1. Definition of the Normal Distribution**

The **Normal distribution** (also known as Gaussian distribution) is a continuous probability distribution 
characterized by its **bell-shaped curve**. Its probability density function (PDF) is given by:


$`f(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)`$


- $\mu$ = **mean** (location parameter)
- $\sigma^2$ = **variance** (scale parameter)
- $\sigma$ = **standard deviation**

---

### **2. Mean of the Normal Distribution**

The **mean** of a distribution gives the expected value or the center of mass of the distribution. 
For the normal distribution:


$`\mathbb{E}[X] = \mu`$


#### **Derivation of the Mean:**

Using the definition of expected value:


$`\mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x)\, dx`$


Substitute the PDF:

$`\mathbb{E}[X] = \int_{-\infty}^{\infty} x \cdot \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right) dx`$


Use the substitution $`z = \frac{x - \mu}{\sigma}`$, so $`x = \sigma z + \mu`$, $`dx = \sigma dz`$:


$`\mathbb{E}[X] = \int_{-\infty}^{\infty} (\sigma z + \mu) \cdot \frac{1}{\sqrt{2\pi}} e^{-z^2/2} dz`$


Split the integral:


$`\mathbb{E}[X] = \mu \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-z^2/2} dz + \sigma \int_{-\infty}^{\infty} z \cdot \frac{1}{\sqrt{2\pi}} e^{-z^2/2} dz`$


- The first integral is 1 (PDF of standard normal integrates to 1)
- The second integral is 0 (since $`z \cdot e^{-z^2/2}`$ is an **odd function**)


$`\Rightarrow \mathbb{E}[X] = \mu`$


### **Finding the Mean**

For a continuous random variable $`X \sim \mathcal{N}(\mu, \sigma^2)`$, the **mean** $\mu$ is defined as:


$`\mathbb{E}[X] = \int_{-\infty}^{\infty} x \cdot f(x) \, dx`$


Where the PDF is:


$`f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)`$


By change of variables $`z = \frac{x - \mu}{\sigma}`$, we reduce the integral to that of a standard normal, yielding:


$`\mathbb{E}[X] = \mu`$


#### **Key Insight:**
The mean $\mu$ is the **center of symmetry** of the bell curve.

---


### **3. Variance of the Normal Distribution**

The **variance** measures the spread of the distribution:


$`\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = \sigma^2`$


#### **Derivation of the Variance:**

Use the substitution from above. First, compute $`\mathbb{E}[X^2]`$:


$`\mathbb{E}[X^2] = \int_{-\infty}^{\infty} x^2 f(x)\, dx`$


Using the same substitution $`x = \sigma z + \mu`$, $`dx = \sigma dz`$:


$`\mathbb{E}[X^2] = \int_{-\infty}^{\infty} (\sigma z + \mu)^2 \cdot \frac{1}{\sqrt{2\pi}} e^{-z^2/2} dz`$


Expand the square:


$`(\sigma z + \mu)^2 = \sigma^2 z^2 + 2\sigma\mu z + \mu^2`$


Now split into three terms:


$`\mathbb{E}[X^2] = \sigma^2 \int z^2 \phi(z) dz + 2\sigma\mu \int z \phi(z) dz + \mu^2 \int \phi(z) dz`$


Where $`\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}`$

- $`\int z \phi(z) dz = 0`$ (odd function)
- $`\int z^2 \phi(z) dz = 1`$
- $`\int \phi(z) dz = 1`$

Thus:


$`\mathbb{E}[X^2] = \sigma^2 \cdot 1 + 0 + \mu^2 = \sigma^2 + \mu^2`$


Now compute variance:


$`\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \sigma^2 + \mu^2 - \mu^2 = \sigma^2`$


### **Finding the Variance or Standard Deviation**

Variance is defined as:


$`\text{Var}(X) = \mathbb{E}[(X - \mu)^2]`$


Using the same PDF and substitution:


$`\text{Var}(X) = \sigma^2 \quad \Rightarrow \quad \text{Standard Deviation } \sigma = \sqrt{\text{Var}(X)}`$


---


### **3. Finding a Missing Parameter Using Symmetry When the Mean Is Zero**

Let $`X \sim \mathcal{N}(0, \sigma^2)`$, and suppose:

- $`P(-a \leq X \leq a) = 0.95`$
- This implies \( a \) is the **symmetric bound** capturing 95% of the data.

Use Z-tables:

- $`P(-1.96 \leq Z \leq 1.96) = 0.95`$
- So if $`X = \sigma Z`$, then:
  
  $`a = 1.96\sigma \quad \Rightarrow \quad \sigma = \frac{a}{1.96}`$
  

#### **Example:**
Given $`P(-4 \leq X \leq 4) = 0.95`$, find $\sigma$:


$`4 = 1.96\sigma \quad \Rightarrow \quad \sigma \approx \frac{4}{1.96} \approx 2.04`$


---

### **4. Finding a Missing Parameter Using Symmetry When the Mean Is Nonzero**

Let $`X \sim \mathcal{N}(\mu, \sigma^2)`$ and suppose:

- $`P(\mu - a \leq X \leq \mu + a) = 0.99`$

From the Z-table:
- $`P(-2.58 \leq Z \leq 2.58) = 0.99`$
- So:
  
  $`a = 2.58\sigma \quad \Rightarrow \quad \sigma = \frac{a}{2.58}`$
  

#### **Example:**
Given $`X \sim \mathcal{N}(5, \sigma^2)`$ and: 
$`$P(2 \leq X \leq 8) = 0.99`$


This is symmetric around 5 (since $8 - 5 = 3$ and $5 - 2 = 3$), so:


$`a = 3 \quad \Rightarrow \quad \sigma = \frac{3}{2.58} \approx 1.16`$

---


### **4. Summary**

- **Mean (Expected Value):** $\mu$
- **Variance:** $\sigma^2$

These two parameters fully define a normal distribution. The mean sets the location (center), and the variance controls the spread (width) of the bell curve.









