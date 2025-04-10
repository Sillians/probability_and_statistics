# The Binomial Distribution

### **1. Definition**

The **binomial distribution** applies when we perform a fixed number of independent trials, each with only two possible outcomes (success or failure)
and with the same probability of success on each trial.

If a random variable $X$ represents the number of successes in $n$ trials, and the probability of success on each trial is $p$, then:


$`X \sim \operatorname{Bin}(n, p)`$

where:
- **$n$** is the number of trials.
- **$p$** is the probability of a success in a single trial.
- **$X$** is the total number of successes out of $n$ trials.

---

### **Probability Mass Function (PMF)**

$`P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}`$

Where:
- $`\binom{n}{k} = \frac{n!}{k!(n-k)!}`$ is the number of ways to choose $k$ successes from $n$ trials.
- $`p^k`$: probability of $k$ successes.
- $`(1 - p)^{n - k}`$: probability of $n - k$ failures.

---

**Example (PMF at a point):**

*Scenario:* A fair coin is tossed 5 times. What is the probability of getting exactly 2 heads?

*Solution:*

- $n = 5$
- $p = 0.5$ (coin is fair)
- $k = 2$

Applying the PMF:

$`P(X = 2) = \binom{5}{2} (0.5)^2 (1 - 0.5)^{5 - 2}`$

Calculate each component:
- $`\binom{5}{2} = \frac{5 \times 4}{2 \times 1} = 10`$
- $`(0.5)^2 = 0.25`$
- $`(0.5)^3 = 0.125`$

Thus,

$`P(X = 2) = 10 \times 0.25 \times 0.125 = 0.3125.`$
So there is a **31.25%** chance of getting exactly 2 heads in 5 tosses.

---

### **3. Expected Value and Variance**

For $`X \sim \operatorname{Bin}(n, p)`$

- **Expected Value (Mean):**
  $`\mathbb{E}[X] = np`$

- **Variance:**
  $`\operatorname{Var}(X) = np(1 - p)`$

---

### **4. Computing Probabilities Over Intervals**

The binomial distribution enables calculations for a variety of probability questions. 
Here are three common cases with examples:

#### **A. Probability Over an Unbounded Interval**

This is used to compute the probability of obtaining at least $k$ successes:

$`P(X \geq k) = \sum_{x=k}^{n} P(X = x)`$

**Example:**

*Scenario:* A basketball player has a 70% chance of making a free throw. 
If they take 10 free throws, what is the probability of making at least 8 shots?

*Solution:*

- $n = 10$
- $p = 0.7$
- Compute for $k = 8, 9, 10$

Calculate each term:
- $`P(X = 8) = \binom{10}{8} (0.7)^8 (0.3)^2 \approx 0.2335`$
- $`P(X = 9) = \binom{10}{9} (0.7)^9 (0.3)^1 \approx 0.1211`$
- $`P(X = 10) = \binom{10}{10} (0.7)^{10} (0.3)^0 \approx 0.0282`$


Summing these:

$`P(X \geq 8) \approx 0.2335 + 0.1211 + 0.0282 = 0.3828.`$

Thus, there is approximately a **38.28%** chance the player makes at least 8 shots.

---

#### **B. Probability Over a Bounded Interval**

This computes the probability that the number of successes falls between two values 
$a$ and $b$ (inclusive):

$`P(a \leq X \leq b) = \sum_{x=a}^{b} P(X = x)`$


**Example:**

*Scenario:* A quality inspector examines 15 items, each with a 95% chance of being 
non-defective. What is the probability that between 12 and 14 items (inclusive) 
are non-defective?

*Solution:*

- $n = 15$
- $p = 0.95$
- We want $`P(12 \leq X \leq 14)`$

Calculate:

$`P(12 \leq X \leq 14) = P(X = 12) + P(X = 13) + P(X = 14)`$

Assuming calculations (or a software/computation aid) yield:
- $`P(X = 12) \approx 0.1974`$
- $`P(X = 13) \approx 0.3552`$
- $`P(X = 14) \approx 0.3552`$


Then,
$`P(12 \leq X \leq 14) \approx 0.1974 + 0.3552 + 0.3552 = 0.9078.`$

Hence, there is about a **90.78%** chance that between 12 and 14 items are non-defective.

---

#### **C. Computing a Probability Using the Complement**

For many binomial problems, especially when dealing with tail probabilities, 
it's easier to work with the complement:

$`P(X \geq k) = 1 - P(X < k) = 1 - \sum_{x=0}^{k-1} P(X = x)`$


**Example:**

*Scenario:* In a multiple-choice quiz with 10 questions (each with 4 options and one 
correct answer), a student guesses all answers at random. What is the probability that 
the student gets at least 8 questions correct?

*Solution:*

- $n = 10$
- $p = 0.25$ (chance of guessing correctly)
- We need $`P(X \geq 8)`$.

Using the complement rule:

$`P(X \geq 8) = 1 - P(X \leq 7).`$

First, compute the cumulative probability:

$`P(X \leq 7) = \sum_{x=0}^{7} P(X = x).`$

Assume (via computation or a binomial table) we obtain:

$`P(X \leq 7) \approx 0.9453.`$

Then:

$`P(X \geq 8) = 1 - 0.9453 = 0.0547.`$

So, there is about a **5.47%** chance the student gets at least 8 correct answers.

---

### **Summary**

- **PMF at a Point:** $`P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}`$  
  *Example:* $`P(\text{2 heads in 5 tosses}) = 0.3125`$.


- **Unbounded Interval:** $`P(X \geq k) = \sum_{x=k}^{n} P(X = x)`$  
  *Example:* $`P(\text{at least 8 free throws out of 10, } p=0.7) \approx 0.3828`$.


- **Bounded Interval:** $`P(a \leq X \leq b) = \sum_{x=a}^{b} P(X = x)`$  
  *Example:* $`P(12 \leq X \leq 14 \text{ non-defective items out of 15, } p=0.95) \approx 0.9078`$.


- **Complement Rule:** $`P(X \geq k) = 1 - P(X \leq k-1)`$  
  *Example:* $`P(\text{at least 8 correct answers out of 10, } p=0.25) \approx 0.0547`$.

 