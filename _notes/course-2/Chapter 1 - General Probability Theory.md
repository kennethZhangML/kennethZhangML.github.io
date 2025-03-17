---
layout: page
title: Chapter 1 - General Probability Theory
description: Notes on general probability theory and foundational concepts.
parent: course-2
importance: 1
permalink: /notes/course-2/chapter-1-general-probability/
nav: false
---


### **Infinite Probability Spaces**
We want t model a situation in which a random experiment with infinitely many possible outcomes is conducted. Problem: uncountably infinite samples spaces.

Let $\Omega$ be a sample spaces with $\Omega_{\infty}$ denoting the infinite sample space

Not possible to list elements in sequence, probability of any outcome is 0. 
- Cannot determine probability of $A$ summing up probabilities of the elements in $A \subseteq \Omega$ 
- **Must** define probabilities of the events directly. 
------------------------------------------------------------------------
**Definition**: $\sigma$-algebra of $\Omega$ and $F \subseteq \Omega$ collection of subsets of $\Omega$
1. $\emptyset$ belongs to $F$
2. when $A \in F$ then $A^c \in F$ as well
3. $A_1, A_2, \dots$ in $F$ then $\cup_{n = 1}^\infty A_n$ also belongs to $F$
Operations done to the elements of a $\sigma$-algebra give us other sets in the $\sigma$-algebra.
For example, the intersection of a finite number of sets in a $\sigma$-algebra results in a set in the $\sigma$-algebra, if $F$ is a $\sigma$-algebra, then the whole space $\Omega$ must be one of the sets in $F$ because $\Omega = F^c$.

------------------------------------------------------------------------
**Definition**: A probability measure $\mathbb{P}$ is a function that maps every $A \in F$ to a number in $[0, 1]$.
We call this the probability of $A$ written as $\mathbb{P}(A)$. 
1. $\mathbb{P}(A)$
2. Countable Additivity: when a sequence of events $A_1, A_2, \dots$ of disjoint sets is in $F$ then,
$$
\mathbb{P} \left(\cup_{n = 1}^\infty A_n \right) = \sum_{n = 1}^\infty \mathbb{P}(A_n)
$$
We denote $(\Omega, F, \mathbb{P})$ as our probability space. 

**Examples**
Take $A_1, A_2, \dots$ as our sequence of events in $F$ which is in the sample space $\Omega$. Then, to be sure that $\mathbb{P}(\emptyset) = 0$, we have that:
$$
A_1 = A_2 = A_3 = \dots = \emptyset
$$
Then it is the case that
$$
\mathbb{P}(\emptyset) = \sum_{n = 1}^\infty \mathbb{P}(\emptyset)
$$
Thus we have that, $\mathbb{P} = \emptyset$. 
Let's say that our previous sequence is finitely additive, and that our sequence is finitely many disjoint sets in $F$, then we have:
$$
\mathbb{P}\left(\cup_{n = 1}^N A_n \right) = \sum_{n = 1}^N \mathbb{P}(A_n)
$$
use, $A_{N + 1} = A_{N + 2} = \dots = \emptyset$ to get the result above. It follows by transitivity. 


**Lebesgue Measure**: usually denoted $\mathcal{L}$, is the probability measure that the number chosen is between $a$ and $b$ which is $b - a$, that is:
$$
\mathbb{P}[a, b] = b - a,\quad, 0\le a \le b \le 1
$$
The Lebesgue measure of a subset of $\mathbb{R}$ is its length, so, if $b = a$, then naturally,
$$
\mathbb{P}[a, b] = \mathbb{P}[a, a] = a - a = 0
$$
Single points have zero probability, thus, the probability of an open interval $(a, b)$ has the same probability as a closed interval $[a, b]$. We can also write an open interval as the union of a sequence of closed intervals:
$$
(a, b) = \cup_{n = 1}^\infty \left[a + \frac{1}{n}, b - \frac{1}{n} \right]
$$
which is a $\sigma$-algebra that contains all open intervals. 

------------------------------------------------------------------------
**Borel $\sigma$-algebra**: A $\sigma$-algebra obtained by starting with closed intervals, and adding everything else necessary in order to have a $\sigma$ algebra. i.e., the borel sigma algebra of subsets of $[0, 1]$ is denoted by $\mathcal{B}[0, 1]$ which contain **Borel Sets**

e.g., Take an independent coin space, starting with $\mathbb{P}(\emptyset) = 0$ and $\mathbb{P}(\Omega) = 1$, then we start with:
$$
2^{(2^0)} = 2 \text{ sets} \implies \mathcal{F} = \{\emptyset, \Omega \}
$$
For which $A_H$ is the set with sequences starting with $H$, and $A_T$ starting with $T$. We continue to carry out these tosses to get $2^{(2^1)} = 4$ sets for $\mathcal{F_1}$ and $2^{(2^2)} = 16$ sets for $\mathcal{F_2}$ and so on. Once the probabilities for these sets are defined, then other, non-describable sets are also determined. 

We can expand this to $F_\infty$ where we can take the limit:
$$
\lim_{n \rightarrow \infty} = \frac{H_n(\omega_1 \dots \omega_n)}{n} = \frac{1}{2}
$$
where the numerator of the limit denotes the number of heads in the first $n$ tosses. Thus, by the definition of this limit, and the coin toss sequences $\omega = \omega_1 \omega_2 \dots$, is satisfied if and only if for every integer $m$ there is a positive integer $N$ such that for all $n \ge N$ we have $\omega \in S_{n, m}$
$$
S_{n, m} = \left\{\omega; \left|\frac{H_n(\omega_1 \dots \omega_n)}{n} - \frac{1}{2} \right| \le \frac{1}{m} \right\}
$$
Set $A$ in $F_\infty$ because it is described in terms of the unions and intersections of a sequence of sets that are in $\mathcal{F}_\infty$, thus tells us that $\mathbb{P}(A)$ is somehow determined. 

We say that an event with $\mathbb{P}(A) = 1$ occurs almost surely. That is, if a set $A \in \mathcal{F}$ satisfies $\mathbb{P} = 1$ we that the event $A$ occurs almost surely. 


------------------------------------------------------------------------

### **Random Variables and Distributions**
$X$ is a random variable (i.e. a real-valued function) defined on our sample space $\Omega$ that for every Borel subset $B \subseteq \mathbb{R}$ the subset of $\Omega$ is given by:
$$
\{X \in B\} = \{\omega \in \Omega; X(\omega) \in B\}
$$
is in the $\sigma$-algebra $\mathcal{F}$. Start with closed intervals $[a, b] \subset \mathbb{R}$ and add all other sets that are necessary in order to have a $\sigma$-algebra. We determine the value via a random experiment of choosing $\omega \in \Omega$, i.e., the probability that $X$ takes some value in some set. 
$$
\mathbb{P}\{X \in B\} \implies \{X \in B\} \in \mathcal{F} \implies B \in B(\mathbb{R})
$$
Think of random variables $S_0, S_1, S_2, \dots$ that have distribution.
$$
\mathbb{P}(S_0 = 4) = 1
$$
We can say that $S_0$ puts a unit of mass on the number $4$. So for random variables, with multiple possible outcomes, let's say 3 different scenarios, we can say that the distribution of this random variable puts three lumps of mass of different sizes (probabilities) on each possibility. 

We need to allow the possibility that the random variables we consider don't assign lumps of mass but spread a unit of mass continuously over the real line (i.e., tells us how much mass is in a set rather than how much mass is at a point). 

**Distribution** of a random variable itself is a probability measure, but is a measure on subsets of $\mathbb{R}$ rather than the subsets of $\Omega$. 

------------------------------------------------------------------------
**Definition**: The distribution measure of random variable $X$ is the probability measure $\mu_X$ that assigns each Borel subset $B$ of $\mathbb{R}$ the mass:
$$
\mu_X (B) = \mathbb{P} \{X \in B\}
$$
e.g., Uniform measure on $[0, 1]$ and define $X(\omega) = \omega$ and $Y(\omega) = 1- \omega$, then
$$
\mu_X [a, b] = \mathbb{P}\{\omega; a \le X(\omega) \le b\} = \mathbb{P}[a, b] = b - a,\quad 0\le a \le b \le 1
$$
we use the same technique to define $\mu_Y$:
$$
\mu_Y[a, b] = \mathbb{P}\{\omega; a \le Y(\omega) \le b\} = \mathbb{P}\{\omega; a \le 1 - \omega \le b\} = \mathbb{P}[1 - b, 1 - a] = b - a = \mu_X[a, b]
$$
Suppose we define $\tilde{\mathbb{P}}$ on $[0, 1]$ and specify that:
$$
\tilde{\mathbb{P}}[a, b] = \int_a^b 2 \omega d \omega = b^2 - a^2,\quad 0 \le a \le b \le 1
$$
then $\tilde{\mu}_X[a, b]$ is equal to the above and the random variable $X$ no long has the uniform distribution as defined previously. 

------------------------------------------------------------------------

**Cumulative Distribution Function (cdf) of a random variable**
$$
F(x) = \mathbb{P}\{X \le x\},\quad x \in \mathbb{R}
$$
We know the distribution measure $\mu_X$ then we know cdf $F$ because
$$
F(x) = \mu_X (-\infty, x]
$$
- If we know cdf $F$, then we can compute $\mu_X(x, y] = F(y) - F(x)$ so for $a \le b$:
$$
[a, b] = \cap_{n = 1}^\infty \left(a - \frac{1}{n}, b\right]
$$
- Thus we get that:
$$
\mu_X[x, b] = \lim_{n \rightarrow \infty} \mu_X \left(a - \frac{1}{n}, b \right] = F(b) - \lim_{n \rightarrow \infty} F(a - 1/n)
$$
Thus, knowing the cdf $F$ for a random variable is the same as knowing its distribution measure $\mu_X$. In other cases, we can record a random variable using:

1. a density function $f(x)$,
$$
\mu_X[a, b] = \mathbb{P}\{a \le X \le b\} = \int_a^b f(x) dx,\quad -\infty < a \le b < \infty
$$
$$
\int_{-\infty}^\infty f(x)dx = \lim_{n \rightarrow \infty} \int_{-\infty}^\infty f(x) dx = \lim_{n \rightarrow \infty} \mathbb{P}\{-n \le X \le n\} = \mathbb{P}\{X \in \mathbb{R}\} = \mathbb{P}(\Omega) = 1
$$
2. a probability mass function, given sequence of numbers $x_1, \dots, x_N$ or infinite sequence, we can define $p_i = \mathbb{P}\{X = x_i\}$ so that $\sum p_i = 1$ for all $i$. Then the mass assigned to a Borel set $B \subset \mathbb{R}$ by the distribution measure of $X$ is:
$$
\mu_X(B) = \sum_{i, x_i \in B} p_i,\quad B \in B(\mathbb{R})
$$

------------------------------------------------------------------------
### Expectations 
We want to compute the average value of a random variable $X$. If $\Omega$ is finite, then we define:
$$
\mathbb{E} X = \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\omega)
$$
For an infinite sequence, we can define this as the infinite sum:
$$
\mathbb{E} X = \sum_{k = 1}^\infty X(\omega_k) \mathbb{P}(\omega_k)
$$
For uncountably infinite sample spaces $\Omega$, then:
Partition the interval $[a, b]$ into subintervals $[x_0, x_1], [x_1, x_2], \dots, [x_{n - 1}, x_n]$ such that we have $a = x_1 < x_1 < \dots < x_n = b$ where our partition is $\Pi = \{x_0, x_1, x_2, \dots, x_n \}$ is the set of partition points and by:
$$
||\Pi|| = \max_{1 \le k \le n} \{x_k - x_{k - 1} \}
$$
we take the length of the longest subinterval in the partition. For each subinterval in this partition, we take $M_k$ and $m_k$ as the largest subinterval defined on the function $f(x)$ as:
$$
M_k = \max_{x_{k - 1} \le x \le x_k} f(x), \quad m_k = \min_{x_{k - 1} \le x \le x_k} f(x)
$$
The **Upper Riemann Sum**:
$$
RS^+_\Pi (f) = \sum_{k = 1}^n M_k(x_k - x_{k - 1})
$$
The **Lower Riemann Sum**:
$$
RS^-_\Pi (f) = \sum_{k = 1}^n m_k (x_k - x_{k - 1})
$$
as we take more and more partition points and the subintervals, we take, get smaller and smaller, the upper and lower Riemann sums converge to the same limit. 

**We cannot do this for random variables**, since they are a function of $\omega \in \Omega$, which is often not a subset of $\mathbb{R}$. Thus, we take $0 \le X(\omega) < \infty$, and let $\Pi = \{y_0, y_1, \dots\}$ where $0 = y_0 < y_1 <\dots$. For each subinterval $[y_k, y_{k + 1}]$, we set:
$$
A_k = \{\omega \in \Omega; y_k \le X(\omega) < y_{k + 1}\}
$$
The **Lower Lebesgue Sum**
$$
LS^-_\Pi (X) = \sum_{k = 1}^\infty y_k \mathbb{P}(A_k)
$$
As this lower sum converges as $|| \Pi ||$ approaches (i.e., the maximal distance between $y_k$ partition points approaches 0), we define this limit as the Lebesgue Integral:
$$
\int_\Omega X(\omega) d \mathbb{P}(\omega) \quad\text{or}\quad \int_\Omega X d\mathbb{P}
$$
- If $\mathbb{P}\{\omega; X(\omega) \ge 0\} = 1$ but $\mathbb{P}\{\omega; X(\omega) = \infty\} > 0$ then we define:
$$
\int_\Omega X(\omega) d \mathbb{P}(\omega) = \infty
$$


We also must consider that $X$ can take positive and negative values, thus we define positive and negative parts of $X$ by:
$$
X^+ (\omega) = \max \{X(\omega), 0\} \quad\text{and}\quad X^-(\omega) = \max\{- X(\omega), 0\}
$$
Note, the following remarks
- $X^+$ and $X^-$ are both non-negative random variables
- $X = X^+ - X^-$
- $|X| = X^+ + X^-$ 
Finally,
$$
\int_\Omega X^+(\omega) d \mathbb{P}(\omega) = \int_\Omega X^+ (\omega) d \mathbb{P}(\omega) - \int_\Omega X^-(\omega) d \mathbb{P}(\omega)
$$
where the two integrals on the RHS, are both finite, and thus $X$ is said to be integrable and finite.


**Theorem**: Expectation properties
1. $X$ takes finitely many values $y_0, y_1, y_2, \dots, y_n$ then
$$
\int_\Omega X(\omega) d \mathbb{P}(\omega) = \sum_{k = 0}^n y_k \mathbb{P}\{X = y_k\}
$$
2. R.v. $X$ is integrable if and only if
$$
\int_\Omega |X(\omega)| d \mathbb{P}(\omega) < \infty
$$
3. Take $X \le Y$, $\mathbb{P}\{X \le Y\} = 1$, then:
$$
\int_\Omega X(\omega) d \mathbb{P}(\omega) \le \int_\Omega Y(\omega) d \mathbb{P}(\omega)
$$
	For the case that $X = Y$ then we have:
$$
\int_\Omega X(\omega) d \mathbb{P}(\omega) = \int_\Omega Y(\omega) d \mathbb{P}(\omega)
$$
4. Linearity of Expectation of integrable random variables
$$
\int_\Omega (\alpha X(\omega) + \beta Y(\omega)) d \mathbb{P}(\omega) = \alpha \int_\Omega X(\omega) d \mathbb{P}(\omega) + \beta \int_\Omega Y(\omega) d \mathbb{P}(\omega)
$$

Take $X \le Y$ almost surely, so that $X^+ \le Y^+$ and $X^- \ge Y^-$ almost surely, then, 
$$
LS^-_\Pi (X^+) \le LS^-_\Pi (Y^+)
$$
so that we have,
$$
\int_\Omega X^+(\omega) d \mathbb{P}(\omega) \le \int_\Omega Y^+(\omega) d\mathbb{P}(\omega)
$$
A similarly formulation with the $\ge$ applies for $X^-$ and $Y^-$. 


Let's say we want to integrate a random variable $X$ over a subset of $A$ of $\Omega$ rather than over all $\Omega$ then for this reason, we can use an indicator random variable, for $\omega$ when it is in $A$ and when it is not. i.e., thus we can get that if $A$ and $B$ are disjoint sets in $\mathcal{F}$ then we can write that:
$$
\mathbb{I}_A + \mathbb{I}_B = \mathbb{I}_{A \cup B}
$$
Then, by the linearity property we can get that:
$$
\mathbb{E} X = \int_\Omega X(\omega) d \mathbb{P}(\omega)
$$
where at least one of $\mathbb{E} X^+$ or $\mathbb{E}X^-$ is finite. 


**Theorem**: $X$ is a random variable on some probability space,
1. $X$ takes finitely many values, then
$$
\mathbb{E} X = \sum_{k = 0}^n x_k \mathbb{P}\{X = x_k\}
$$
	If $\Omega$ is finite, then
$$
\mathbb{E} X = \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\omega)
$$
2. Integrability, $X$ is integrable if and only if
$$
\mathbb{E}|X| < \infty
$$
3. Comparison, if $X \le Y$ then
$$
\mathbb{E}X \le \mathbb{E} Y
$$
	if $X = Y$ then
$$
\mathbb{E} X = \mathbb{E} Y
$$
4. Linearity and Jensen's inequality hold for expectation, trivially. 


However, no matter how small we take the subintervals in the partition, the upper Riemann sum is always 1 and the lower is always 0, so the sums do not converge. Thus, because the Riemann sum discretizes the x-axis, the function is too discontinuous to handle, thus we use the Lebesgue integral which discretizes the y-axis. 

**Definition**: Take $B(\mathbb{R})$ the sigma-algebra of Borel subsets of $\mathbb{R}$. The Lebesgue measure on $\mathbb{R}$ which we denote by $\mathcal{L}$ assigns to each Borel set $B \in B(\mathbb{R})$ a number in $[0, \infty)$ or $\infty$ such that:
1. $\mathcal{L}[a, b] = b - a$ when $a \le b$
2. If $B_1, B_2, \dots$ is a sequence of disjoint Real-Borel sets, then we have the countable additivity property that tells us that:
$$
\mathcal{L} \left(\cup_{n = 1}^\infty B_n \right) = \sum_{n = 1}^\infty \mathcal{L}(B_n)
$$
which also holds for non-$\infty$, so the finite additivity property for $N$ also holds for the above. 
For $f(x)$, a real-valued function, we assume that for every Borel subset $B$ of $\mathbb{R}$, the set $\{x; f(x) \in B\}$ is also a Borel subset of $\mathbb{R}$. We define the Lebesgue integral as:
$$
\int_\mathbb{R} f(x) d \mathcal{L}(x)
$$
of $f$ over $\mathbb{R}$. Again, we define $\Pi$ as we did before and for each subinterval, we define:
$$
B_k = \{x \in \mathbb{R}; y_k \le f(x) < y_{k + 1}\}
$$
$f$ is Borel measurable, then similarly, the following hold:
- As the $|| \Pi||$ converges to zero, the lower Lebesgue sums converge to a limit, which we define $\int_\mathbb{R} f(x) d \mathcal{L} (x)$ which could give value $\infty$ 
- For some $B \in B(\mathbb{R})$ we compute the Lebesgue integral over only part of $\mathbb{R}$, as indicated by our indicator function, so the product $f(x) \mathbb{I}_B(x)$ agrees with $f(x)$ when $x \in B$
$$
\int_B f(x) d \mathcal{L}(x) = \int_B \mathbb{I}_B f(x) d \mathcal{L}(x)
$$


**Theorem**: $f$ is bounded and $a < b$
1. Riemann integral is defined for $f(x)$ on the reals, if and only if the set of points $x$ in $[a, b]$ where $f(x)$ is not continuous has Lebesgue measure 0.
2. Riemann integral is defined, then $f$ is Borel measurable (so the Lebesgue integral is also defined) and the Riemann and Lebesgue integrals agree, trivially, 

**Definition**: If the set of numbers in $\mathbb{R}$ fails to have some property is a set with Lebesgue measure 0, we say that the property holds almost everywhere. 

------------------------------------------------------------------------

### Convergence of Integrals

**Definition**: Let $X$ be an r.v., and the sequence $X_1, X_2, \dots$ converges to $X$ almost surely, then
$$
\lim_{n \rightarrow \infty} X_n = X \quad \text{almost surely}
$$
if the set $\omega \in \Omega$ where $X_1(\omega), X_2(\omega), \dots$ has limit $X(\omega)$ with proba. 1. Conversely, if they do not converge to $X(\omega)$, then it has proba. 0. 

**Definition**: Let $f_1, f_2, \dots$ be a sequence of real-valued Borel-measurable functions defined on $\mathbb{R}$. Then $f$ is another real-valued, Borel-measurable function, we say that $f_1, f_2, \dots$ converges to $f$ almost everywhere and write,
$$
\lim_{n \rightarrow \infty} f_n = f \quad\text{almost everywhere}
$$
if the set of $x \in \mathbb{R}$ for which the sequence of numbers $f_1(x), f_2(x), f_3(x), \dots$ does not have limit $f(x)$ is a set with Lebesgue measure 0. 
- when functions converge almost everywhere, their expected values converge to the expected value of the limit random variable 
- Lebesgue integrals converge to the Lebesgue integral of the limiting function, but not always, in particular, when the everywhere-limit function $f$ is identically 0. 
- To get the integrals of a sequence of functions to converge to the integral of the limiting function, we impose that, all the functions are non-negative and they converge to their limit from below

**Theorem**: Monotone Convergence theorem
$X_1, X_2, \dots$ is a sequence of random variables converging almost surely to another random variable $X$, so, if $0 \le X_1 \le X_2 \le \dots$ almost surely, we have that,
$$
\lim_{n \rightarrow \infty} \mathbb{E}X_n = \mathbb{E} X
$$
Let $f_1, f_2, f_3, \dots$ be a sequence of Borel-measurable functions on $\mathbb{R}$ converging almost everywhere to a function $f$, if $0 \le f_1 \le f_2 \le f_3 \le \dots$ almost everywhere, then
$$
\lim_{n \rightarrow \infty} \int_{-\infty}^\infty f_n(x)dx = \int_{-\infty}^\infty f(x) dx
$$

**Corollary**: Suppose the non-negative random variable $X$ takes countably many values, then
$$
\mathbb{E}X = \sum_{k = 0}^\infty x_k \mathbb{P}\{X = x_k\}
$$
Let $A_k = \{X = x_k\}$ so that $X$ can be written as:
$$
X = \sum_{k = 0}^\infty = x_k \mathbb{I}_{A_k}
$$
Then, we can define $X_n = \sum_{k = 0}^n x_k \mathbb{I}_{A_k}$ for $0 \le X_1 \le X_2 \le X_3 \le \dots$ and $\lim_{n \rightarrow \infty} X_n = X$ almost surely. Thus, the proof follows by taking the limit on both sides and using the MCT to justify the first equality to get our definition for $\mathbb{E}X$ above. 


**Theorem**: Dominated Convergence 
Let $X_1, X_2, \dots$ be a sequence of random variable converging almost surely to a random variable $X$. If there is another random variable $Y$ such that $\mathbb{E}Y < \infty$ and $|X_n| \le Y$ almost surely, then
$$
\lim_{n \rightarrow \infty} \mathbb{E} X_n = \mathbb{E} X
$$
$f_1, f_2, \dots$ is a sequence of Borel-measurable functions on $\mathbb{R}$ converging almost everywhere to a function $f$. If there is another function $g$ such that $\int_{-\infty}^{\infty} g(x) dx < \infty$ and $|f_n| \le g$ almost everywhere, then we can write,
$$
\lim_{n \rightarrow \infty} \int_{-\infty}^{\infty} f_n(x) dx = \int_{-\infty}^{\infty} f(x) dx
$$
------------------------------------------------------------------------

### Computation of Expectations 
Using the definition of the expectation of r.v., X, to be the Lebesgue integral, we need to rely on densities of the random variables to compute the expectation under $\Omega$. 

$\mu_X$ is a probability measure on $\mathbb{R}$ so we can use it to integrate functions over $\mathbb{R}$. 

**Theorem**: $X$ is a random variable, on a probability space defined by the triple, let $g$ be a Borel-measurable function on $R$, then,
$$
\mathbb{E} |g(X)| = \int_\mathbb{R} |g(x)| d \mu_X(x)
$$
if this quantity, above, is finite, then,
$$
\mathbb{E} g(X) = \int_\mathbb{R} g(x) d \mu_X (x)
$$
The proof follows by using an indicator random variable that takes values to compute the expectation of $\mathbb{I}_B(X)$ and use properties of non-negative simple functions as a finite sum of indicator functions times some constant(s). Then, we achieve something of the form of a non-negative Borel-measurable function which we assume to be arbitrary. Taking the limit, using the MCT, we obtain the integral over $g(x)$ over the reals. We can then compute the Lebesgue integral over the abstract space $\Omega$ so it suffices to compute the integral over the set of real numbers. Since $X$ only takes finitely many values, $\mu_X$ places a mass of size $p_k = \mathbb{P}\{X = x_k\}$ at each number $x_k$. Then we can get something like,
$$
\mathbb{E}g(X) = \int_\mathbb{R} g(x) \mu_X dx = \sum_{k = 0}^n g(x_k) p_k
$$

**Theorem** Let $g$ be a Borel-measurable function on $\mathbb{R}$ and suppose $X$ has density $f$, then:
$$
\mathbb{E} |g(X)| = \int_{-\infty}^\infty |g(x)| f(x) dx
$$
if the quantity above is finite, then we can write 
$$
\mathbb{E} g(X) = \int_{-\infty}^\infty g(x) f(x) dx
$$

------------------------------------------------------------------------

### Change of Measure 
We had previously used $Z$ to change probability measures on $\Omega$. When $\Omega$ is uncountably infinite, and $\mathbb{P}(\omega) = \tilde{\mathbb{P}}(\omega) = 0$ for every $\omega \in \Omega$, there is no use to write it as:
$$
Z(\omega) = \frac{\tilde{\mathbb{P}(\omega)} }{\mathbb{P}(\omega)} \implies Z(\omega) \mathbb{P}(\omega) = \tilde{\mathbb{P}}(\omega)
$$
We re-assign probabilities in $\Omega$ using $Z$ to tell us where in $\Omega$ we should revise the probability upward where $Z > 1$ and revise the probability downward $Z < 1$. 

**Theorem**: Let $Z$ be an almost surely non-negative random variable with $\mathbb{E}Z = 1$ and, for $A \in F$,
$$
\tilde{\mathbb{P}}(A) = \int_A Z(\omega) d \mathbb{P}(\omega)
$$
Then, $\tilde{\mathbb{P}}$ is a probability measure. If $X$ is a non-negative random variable, then,
$$
\tilde{\mathbb{E}}X = \mathbb{E}[XZ]
$$
If $Z$ is almost surely strictly positive, then,
$$
\mathbb{E} Y = \tilde{\mathbb{E}} \left[\frac{Y}{Z} \right]
$$
for every non-negative random variable $Y$. 
Suppose $X$ is a r.v., that can take both positive and negative values, and apply $\tilde{\mathbb{E}}X$ to the negative and positive parts of $X$ then subtract the resulting equations to see that $\mathbb{E}Y$ holds well. 
Given by assumption,
$$
\tilde{\mathbb{P}}(\Omega) = \int_\Omega Z(\omega) d \mathbb{P}(\omega) = \mathbb{E}Z = 1
$$
For countable additivity, let $A_1, A_2, \dots$ be a sequence of disjoint sets in $F$ and define $B_n = \cup_{k = 1}^n A_k, B_\infty = \cup_{k = 1}^\infty A_k$. Thus:
$$
\mathbb{I}_{B_1} \le \mathbb{I}_{B_2} \le \dots \implies \lim_{n \rightarrow \infty} \mathbb{I}_{B_n} = \mathbb{I}_{B_\infty}
$$
$$
\begin{align*}
\tilde{\mathbb{P}}(B_\infty) = \int_\Omega \mathbb{I}_{B_\infty} (\omega) Z(\omega) d \mathbb{P}(\omega) = \lim_{n \rightarrow \infty} \int_\Omega \mathbb{I}_{B_n} (\omega) Z(\omega) d \mathbb{P}(\omega)\\
\int_\Omega \mathbb{I}_{B_n}(\omega) Z(\omega) d \mathbb{P}(\omega) = \sum_{k = 1}^n \int_\Omega \mathbb{I}_{A_k}(\omega) Z(\omega) d \mathbb{P}(\omega) = \sum_{k = 1}^n \tilde{\mathbb{P}}(A_k)\\
\end{align*}
$$
We get, through combining the equations, to get:
$$
\tilde{\mathbb{P}} \left(\cup_{k = 1}^\infty A_k \right) = \lim_{n \rightarrow \infty} \sum_{k = 1}^n \tilde{\mathbb{P}}(A_k) = \sum_{k = 1}^\infty \tilde{\mathbb{P}}(A_k)
$$
Suppose $X$ is a non-negative random variable, if $X$ is an indicator function, then we get;
$$
\tilde{\mathbb{E}}(X) = \tilde{\mathbb{P}}(A) = \int_\Omega \mathbb{I}_A (\omega) Z(\omega) d \mathbb{P}(\omega) = \mathbb{E}[\mathbb{I}_A Z] = \mathbb{E}[X Z]
$$

**Definition**: Let $\Omega$ be a non-empty set and $\mathcal{F}$ be a sigma-algebra of subsets of $\Omega$. Two probability measure $\mathbb{P}$ and $\tilde{\mathbb{P}}$ on $(\Omega, \mathcal{F})$ are said to be equivalent if they agree on which sets in $\mathcal{F}$ have probability zero. 

**Definition**: Let a probability space defined by it's probability triple, and have $\tilde{\mathbb{P}}$ and $\mathbb{P}$ be the risk-neutral and real-world probability measures. Then $Z$ is called the Radon-Nikodym derivative of $\tilde{\mathbb{P}}$ with respect to $\mathbb{P}$ and we can write:
$$
Z = \frac{d \tilde{\mathbb{P}}}{d \mathbb{P}}
$$
**Definition**: Let $\mathbb{P}$ and $\tilde{\mathbb{P}}$ be equivalent probability measures defined on $(\Omega, \mathcal{F})$. Then there exists an almost surely positive random variable $Z$ such that $\mathbb{E}Z = 1$, and
$$
\tilde{\mathbb{P}}(A) = \int_A Z(\omega) d \mathbb{P}(\omega) \quad \text{for every } A \in \mathcal{F}
$$


