---
layout: page
title: Chapter 2 Exercises
description: Exercises for Chapter 2 - Probability Theory on Coin Toss Space.
parent: course-1
importance: 4
permalink: /notes/course-1/chapter-2-exercises/
nav: false
---


**Exercise**: Using Definition 2.1.1 show the following:
**(i)** If 
$$A$$
 is an event and $A^c$ denotes its complement, then $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$

**Solution**
Using the fact that $A^c$ is the event complement of $A$, we can say that:

$$
A^c = \Omega \backslash A \implies A \cap B = \emptyset 
$$

Equivalently, we have that:

$$
A \cup A^c = \Omega
$$

Thus, we can express the probabilities under the probability measure $\mathbb{P}$:

$$
\begin{align*}
\mathbb{P}(A \cup A^c) &= \mathbb{P}(A) + \mathbb{P}(A^c)\\
\implies 1 &= \mathbb{P}(A) + \mathbb{P}(A^c)\\
\text{Since we have: } \mathbb{P}(\Omega) &= 1\\
\mathbb{P}(A^c) &= \mathbb{P}(A) + \mathbb{P}(A^c)
\end{align*}
$$

as required.

**(ii)** If $A_1, A_2, \dots, A_N$ is a finite set of events, then:

$$
\mathbb{P}\left(\bigcup_{n = 1}^N A_n \right) \le \sum_{n = 1}^N \mathbb{P}(A_n)
$$

If the events $A_1, A_2, \dots, A_N$ are disjoint, then equality holds in (2.8.1).

**Solution**

$$
\bigcup_{n = 1}^N A_n = A_1 \cup A_2 \cup \cdots \cup A_N
$$

For our disjoint case, where $A_1, \dots, A_N$ for $A_i \hat A_j = \emptyset$ for $i \neq j$

$$
\mathbb{P} \left(\bigcup_{n = 1}^N A_n \right) = \sum_{n = 1}^N \mathbb{P}(A_n)
$$

Generally, for $A_1, \dots, A_N$ is not disjoint, we apply the inclusion-exclusion principle, to prevent overlapping events:

$$
\begin{align*}
\mathbb{P} \left(\bigcup_{n = 1}^N A_n \right) &= \sum_{n = 1}^N \mathbb{P}(A_n) - \sum_{1 \le i \le j \le N} \mathbb{P}(A_i \hat A_j)) + \cdots\\
\mathbb{P} \left(\bigcup_{n = 1}^N A_n \right) &\le \sum_{n = 1}^N \mathbb{P}(A_n)
\end{align*}
$$

Thus, all the probabilities are non-negative, and the sum of the higher order intersections is subtracted in the inclusion-exclusion principle. 


**Exercise**
Consider the stock price $S_3$ in Figure 2.3.1.
**(i)** What is the distribution of $S_3$ under the risk-neutral probabilities $\tilde{p} = \frac{1}{2}, \tilde{q} = \frac{1}{2}$?

**Solution**

$$
\begin{align*}
&\text{Step 1: Possible values of } S_3 \\
&\quad S_3(HHH) = 32, \quad S_3(HHT) = 8, \quad S_3(HTH) = 8, \\
&\quad S_3(HTT) = 2, \quad S_3(THH) = 8, \quad S_3(THT) = 2, \quad S_3(TTT) = 0.50.\\
\\
&\text{Step 2: Probability of each path} \\
&\quad P(\text{sequence}) = (\tilde{p})^h (\tilde{q})^t \quad \text{where } \tilde{p} = \frac{1}{2}, \, \tilde{q} = \frac{1}{2}, \, h = \text{\# heads}, \, t = \text{\# tails}, \\
&\quad P(HHH) = \left(\frac{1}{2}\right)^3 = \frac{1}{8}, \\
&\quad P(HHT) = P(HTH) = P(THH) = \left(\frac{1}{2}\right)^3 = \frac{1}{8}, \\
&\quad P(HTT) = P(THT) = \left(\frac{1}{2}\right)^3 = \frac{1}{8}, \\
&\quad P(TTT) = \left(\frac{1}{2}\right)^3 = \frac{1}{8}.\\
\\
&\text{Step 3: Group identical values of } S_3 \\
&\quad S_3 = 32 \quad \text{occurs for } HHH: \quad P = \frac{1}{8}, \\
&\quad S_3 = 8 \quad \text{occurs for } HHT, HTH, THH: \quad P = \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{3}{8}, \\
&\quad S_3 = 2 \quad \text{occurs for } HTT, THT: \quad P = \frac{1}{8} + \frac{1}{8} = \frac{2}{8} = \frac{1}{4}, \\
&\quad S_3 = 0.50 \quad \text{occurs for } TTT: \quad P = \frac{1}{8}.\\
\\
&\text{Step 4: Final distribution of } S_3 \\
&\quad P(S_3 = 32) = \frac{1}{8}, \quad P(S_3 = 8) = \frac{3}{8}, \quad P(S_3 = 2) = \frac{1}{4}, \quad P(S_3 = 0.50) = \frac{1}{8}.
\end{align*}
$$


**(ii)** Compute $\tilde{\mathbb{E}}S_1, \tilde{\mathbb{E}}S_2, \tilde{\mathbb{E}}S_3$. What is the average rate of growth of the stock price under $\tilde{P}$?

$$
\begin{align*}
&\text{Step 1: Compute } \tilde{\mathbb{E}}S_1 \\
&\tilde{\mathbb{E}}S_1 = \tilde{p} S_1(H) + \tilde{q} S_1(T) \\
&= \frac{1}{2}(8) + \frac{1}{2}(2) \\
&= 4 + 1 = 5.\\
\\
&\text{Step 2: Compute } \tilde{\mathbb{E}}S_2 \\
&\tilde{\mathbb{E}}S_2 = \tilde{p} \tilde{\mathbb{E}}[S_2 \mid S_1 = H] + \tilde{q} \tilde{\mathbb{E}}[S_2 \mid S_1 = T] \\
&= \frac{1}{2}\left(\frac{1}{2}(16) + \frac{1}{2}(4)\right) + \frac{1}{2}\left(\frac{1}{2}(4) + \frac{1}{2}(1)\right) \\
&= \frac{1}{2}\left(8 + 2\right) + \frac{1}{2}\left(2 + 0.5\right) \\
&= \frac{1}{2}(10) + \frac{1}{2}(2.5) \\
&= 5 + 1.25 = 6.25.\\
\\
&\text{Step 3: Compute } \tilde{\mathbb{E}}S_3 \\
&\tilde{\mathbb{E}}S_3 = \sum_{i=1}^{7} P(S_3 = s_i) \cdot s_i, \quad \text{where } s_i \text{ are the possible values of } S_3. \\
&\tilde{\mathbb{E}}S_3 = \frac{1}{8}(32) + \frac{3}{8}(8) + \frac{1}{4}(2) + \frac{1}{8}(0.5) \\
&= 4 + 3 + 0.5 + 0.0625 \\
&= 7.5625.
\end{align*}
$$

Thus, we get that the average rate of growth is:

$$
\frac{\tilde{E} S_3}{S_0}^{\frac{1}{3}} = \left(\frac{7.5625}{4} \right)^{\frac{1}{3}} = 1.25
$$


**Exercise**
Show that a convex function of a martingale is a submartingale. In other words, let $M_1, \dots, M_N$ be a martingale and let $\phi$ be a convex function. Show that $\phi(M_0), \phi(M_1), \dots, \phi(M_N)$ is a submartingale. 

**Solution**
To show that if $M_1, M_2, \dots, M_N$ is a martingale and $\phi$ is a convex function, then the sequence $\phi(M_0), \dots, \phi(M_N)$ is a submartingale, we proceed as follows:

Again, we define a martingale, $M_1, M_2, \dots$, as one that satisfies the property:

$$
\mathbb{E}[M_{n + 1}] = M_n \quad\text{ for all } n
$$

We want to show that:

$$
\mathbb{E}[\phi(M_{n + 1})] \ge \phi(M_n)
$$

Using convexity of $\phi$, we can apply Jensen's inequality, which states that for any convex function $\phi$ and a random variable $X$, we have the following:

$$
\begin{align*}
\phi(\mathbb{E}[X]) &\le \mathbb{E}[\phi(X)]\\
\mathbb{E}[M_{n +1}] &= M_n\\
\phi(M_n) = \phi(\mathbb{E}[M_{n + 1}]) &\le \mathbb{E}[\phi(M_{n+1})]\\
\mathbb{E}[\phi(M_{n + 1})] &\ge \phi(M_n)
\end{align*}
$$

which mean that $\phi(M_0), \phi(M_1), \dots, \phi(M_N)$ is a submartingale. Thus, a convex function of a martingale is indeed a submartingale. 


**Exercise**: Toss a coin repeatedly. Assume the probability of head on each toss is $\frac{1}{2}$, as is the probability of tail. Let $X_j = 1$ if the $j$th toss results in a head and $X_j = -1$ if the $j$th toss results in a tail. Consider the stochastic process $M_0, M_1, M_2, \dots$ defined by $M_0 = 0$ and:

$$
M_n = \sum_{j = 1}^n X_j,\quad n \ge 1
$$

This is called a symmetric random walk; with each head, it steps up one, and with each tail, it steps down one. 
**(i)** Using the properties of Theorem 2.3.2, show that $M_0, M_1, M_2, \dots$ is a martingale.

**Solution**
Each $X_j$ is a random variable taking values $1$ and $-1$ with equal probability, so it had finite expectation:

$$
\mathbb{E}[X_j] = \frac{1}{2}(1) + \frac{1}{2}(-1) = 0
$$

Since we have that:

$$
M_n = \sum_{j = 1}^n X_j \implies \mathbb{E}[M_n] = \mathbb{E} \left[\sum_{j = 1}^n X_j \right] = \sum_{j = 1}^n \mathbb{E}[X_j] = 0
$$

Thus we have that $M_n$ has finite expectation and is integrable. Now, we just want to use the definition of $M_{n + 1}$ as well as $\mathbb{E}[M_{n + 1} | F_n] = M_n$ to show that $M_n$ is $F$-measurable and $M_n$ satisfies the conditions for martingales:

$$
\begin{align*}
\mathbb{E}[M_{n + 1} | F_n] &= M_n\\
M_{n + 1} &= \sum_{j = 1}^{n + 1} X_j = M_n + X_{n + 1}\\
\mathbb{E}[M_{n + 1} | F_n] &= \mathbb{E}[M_n + X_{n + 1} | F_n] = \mathbb{E}[M_n | F_n] + \mathbb{E}[X_{n + 1} | F_n]\\
\\
\mathbb{E}[M_n | F_n] = M_n &\implies \mathbb{E}[X_{n + 1} | F_n] = \mathbb{E}[X_{n + 1}] = 0\\
\implies \mathbb{E}[M_{n + 1} | F_n] &= M_n + 0 = M_n
\end{align*}
$$

Thus, we see that $M_n$ is a martingale, and satisfies all conditions such that $M_0, M_1, M_2, \dots$ is a martingale by definition of conditional expectation. Simply put, we pulled out what was know, in this case it was the $X_{n + 1}$ in the final two steps of the proof above, and computed directly to get $M_n$, giving, by definition, the required equation for a martingale. 

**(ii)** Let $\sigma$ be a positive constant and for $n \ge 0$ define:

$$
S_n = \exp{(\sigma M_n)} \left(\frac{2}{e^\sigma + e^{-\sigma}} \right)^n
$$

Show that $S_0, S_1, S_2, \dots$ is a martingale. Note that even though the symmetric random walk $M_n$ has no tendency to grow, the geometric symmetric random walk $\exp{\sigma M_n}$ does have a tendency to grow. This is the result of putting a martingale into the convex exponential function. In order to again have a martingale, we must discount the geometric symmetric random walk, using the term $\frac{2}{e^\sigma + e^{-\sigma}}$ as the discount rate. This term is strictly less than one unless $\sigma = 0$. 

**Solution**

$$
\begin{align*}
  S_n &= \exp(\sigma M_n) \left( \frac{2}{e^\sigma + e^{-\sigma}} \right)^n, \\
  S_{n+1} &= \exp(\sigma (M_n + X_{n+1})) \left( \frac{2}{e^\sigma + e^{-\sigma}} \right)^{n+1}, \\
          &= \exp(\sigma M_n) \exp(\sigma X_{n+1}) \left( \frac{2}{e^\sigma + e^{-\sigma}} \right)^{n+1}, \\
  \mathbb{E}[S_{n+1} | \mathcal{F}_n] &= \exp(\sigma M_n) \left( \frac{2}{e^\sigma + e^{-\sigma}} \right)^{n+1} \mathbb{E}[\exp(\sigma X_{n+1})], \\
  \mathbb{E}[\exp(\sigma X_{n+1})] &= \frac{1}{2} \left( \exp(\sigma) + \exp(-\sigma) \right), \\
                                      &= \cosh(\sigma), \\
  \mathbb{E}[S_{n+1} | \mathcal{F}_n] &= \exp(\sigma M_n) \left( \frac{2}{e^\sigma + e^{-\sigma}} \right)^{n+1} \cdot \cosh(\sigma), \\
  \cosh(\sigma) &= \frac{e^\sigma + e^{-\sigma}}{2}, \\
  \mathbb{E}[S_{n+1} | \mathcal{F}_n] &= \exp(\sigma M_n) \left( \frac{2}{e^\sigma + e^{-\sigma}} \right)^n, \\
                                       &= S_n.
\end{align*}
$$



**Exercise** 
Let $M_0, M_1, M_2, \dots$ be the symmetric random walk of the previous exercise and we define a new variable $I_0 = 0$ and:

$$
I_n = \sum_{j = 0}^{n - 1} M_j(M_{j + 1} - M_j),\quad n = 1, 2, \dots
$$

**(i)** Show that:

$$
I_n = \frac{1}{2} M_n^2 - \frac{n}{2}
$$

**Solution**
We start with the definition of $I_n$:

$$
\begin{align} 
I_n &= \sum_{j=0}^{n-1} M_j (M_{j+1} - M_j)
\end{align}
$$

We can use the relationship $M_{j+1} - M_j = X_{j+1}$, since $M_n = \sum_{i=1}^n X_i$, to rewrite:

$$
\begin{align} 
I_n &= \sum_{j=0}^{n-1} M_j X_{j+1}
\end{align}
$$

Now consider $M_n^2$:

$$
\begin{align} 
M_n^2 &= \left( \sum_{j=1}^n X_j \right)^2, \\ 
&= \sum_{j=1}^n X_j^2 + 2 \sum_{1 \leq i < j \leq n} X_i X_j.\\
\\
\sum_{j=1}^n X_j^2 &= n.\\
\\
M_n^2 &= n + 2 \sum_{1 \leq i < j \leq n} X_i X_j.\\
2 \sum_{1 \leq i < j \leq n} X_i X_j &= 2 \sum_{j=1}^{n-1} M_j X_{j+1}
\end{align}
$$

Since each $M_j = \sum_{i=1}^j X_i$ represents the accumulated sum of $X_i$ terms up to step $j$ this is exactly the definition of $2 I_n$, which, after substituting back, gives:

$$
M_n^2 = n + 2 I_n \implies I_n = \frac{1}{2} M_n^2 - \frac{n}{2}
$$

**(ii)** Let $n$ be an arbitrary non-negative integer, and let $f(i)$ be an arbitrary function of a variable $i$. In terms of $n$ and $f$, define another function $g(i)$ satisfying:

$$
\mathbb{E}_n [f(I_{n + 1})] = g(I_n)
$$

Note that although the function $g(I_n)$ on the right-hand side of this equation may depend on $n$, the only random variable that may appear in its argument is $I_n$; the random variable $M_n$ may not appear. You will need to use the formula in part $(i)$. The conclusion of part $(ii)$ is that the process $I_0, I_1, I_2, \dots$ is a Markov process.

**Solution**

$$
\begin{align}
\text{From part (i), we know:} \quad I_n &= \frac{1}{2} M_n^2 - \frac{n}{2}. \\
\text{For } I_{n+1}, \text{ substitute } n+1 \text{ for } n: \quad
I_{n+1} &= \frac{1}{2} M_{n+1}^2 - \frac{n+1}{2}. \\
\text{Using } M_{n+1} = M_n + X_{n+1}, \text{ expand } M_{n+1}^2: \quad
M_{n+1}^2 &= (M_n + X_{n+1})^2, \\
&= M_n^2 + 2 M_n X_{n+1} + X_{n+1}^2. \\
\text{Substitute into } I_{n+1}: \quad
I_{n+1} &= \frac{1}{2} \left(M_n^2 + 2 M_n X_{n+1} + X_{n+1}^2\right) - \frac{n+1}{2}, \\
&= \frac{1}{2} M_n^2 + M_n X_{n+1} + \frac{1}{2} X_{n+1}^2 - \frac{n+1}{2}. \\
\text{Using } X_{n+1}^2 = 1, \text{ since } X_{n+1} \in \{-1, 1\}: \quad
I_{n+1} &= \frac{1}{2} M_n^2 + M_n X_{n+1} + \frac{1}{2} - \frac{n+1}{2}. \\
\text{Group terms:} \quad
I_{n+1} &= \frac{1}{2} M_n^2 - \frac{n}{2} + M_n X_{n+1}. \\
\text{Substitute } I_n = \frac{1}{2} M_n^2 - \frac{n}{2}: \quad
I_{n+1} &= I_n + M_n X_{n+1}.
\end{align}
$$


$$
\begin{align*}
\text{Define the function } g(I_n) \text{ such that:} \quad
\mathbb{E}_n[f(I_{n+1})] &= g(I_n). \\
\text{Substitute } I_{n+1} = I_n + M_n X_{n+1} \text{ into } f(I_{n+1}): \quad
\mathbb{E}_n[f(I_{n+1})] &= \mathbb{E}_n[f(I_n + M_n X_{n+1})]. \\
\text{Since } X_{n+1} \in \{-1, 1\} \text{ with equal probability:} \quad
\mathbb{E}_n[f(I_{n+1})] &= \frac{1}{2} f(I_n + M_n) + \frac{1}{2} f(I_n - M_n). \\
\text{Using } M_n = \pm \sqrt{2 I_n + n}: \quad
\mathbb{E}_n[f(I_{n+1})] &= \frac{1}{2} f(I_n + \sqrt{2 I_n + n}) + \frac{1}{2} f(I_n - \sqrt{2 I_n + n}). \\
\text{Define:} \quad
g(I_n) &= \frac{1}{2} f(I_n + \sqrt{2 I_n + n}) + \frac{1}{2} f(I_n - \sqrt{2 I_n + n}).
\end{align*}
$$


**Exercise: Discrete-time Stochastic Integral**
Suppose $M_0, M_1, \dots, M_N$ is a martingale, and let $\Delta_0, \Delta_1, \dots, \Delta_{N - 1}$ be an adapted process. Define the discrete-time stochastic integral (sometimes called a martingale transform) $I_0, I_1, \dots, I_N$ by setting $I_0 = 0$ and:

$$
I_n = \sum_{j = 0}^{n - 1} \Delta_j (M_{j + 1} - M_j),\quad n = 1, \dots, N
$$

Show that $I_0, I_1, \dots, I_N$ is a martingale. 

**Solution**
First we assume the following, then the computation is pretty straight forward:

$$
I_0 = 0, \quad I_n = \sum_{j=0}^{n-1} \Delta_j (M_{j+1} - M_j), \quad n = 1, \dots, N
$$

- $I_n$ is adapted to $F_n$, the neutral filtration of $M_n$
- $\mathbb{E}[I_n] < \infty$ for all $n$
- $\mathbb{E}_n [I_{n + 1} | F_n] = I_n$

$$
\begin{align}
I_{n+1} &= \sum_{j=0}^n \Delta_j (M_{j+1} - M_j). \\
I_{n+1} - I_n &= \Delta_n (M_{n+1} - M_n). \\
I_{n+1} &= I_n + \Delta_n (M_{n+1} - M_n). \\
\mathbb{E}[I_{n+1} | \mathcal{F}_n] &= \mathbb{E}[I_n | \mathcal{F}_n] + \mathbb{E}[\Delta_n (M_{n+1} - M_n) | \mathcal{F}_n]. \\
\mathbb{E}[I_n | \mathcal{F}_n] &= I_n. \\
\mathbb{E}[\Delta_n (M_{n+1} - M_n) | \mathcal{F}_n] &= \Delta_n \cdot \mathbb{E}[M_{n+1} - M_n | \mathcal{F}_n]. \\
\mathbb{E}[M_{n+1} - M_n | \mathcal{F}_n] &= 0. \\
\mathbb{E}[\Delta_n (M_{n+1} - M_n) | \mathcal{F}_n] &= 0. \\
\mathbb{E}[I_{n+1} | \mathcal{F}_n] &= I_n.
\end{align}
$$

Thus, we have that $I_0, I_1, \dots, I_n$ is a martingale. 


**Exercise**
In a binomial model:
Give an example of a stochastic process that is a martingale but is not Markov.

**Solution**
Let $S_n$ denote the price of an asset at time $n$, following a binomial model: 
$$ S_{n+1} = \begin{cases} u S_n & \text{with probability } p, \\ d S_n & \text{with probability } 1-p, \end{cases} $$
where $u > 1$ (up factor), $d < 1$ (down factor), and $0 < p < 1$ (probability of an up move).

Define the filtration $\mathcal{F}_n$, representing the information available up to time $n$.
We define the process $Y_n$ as: 
$$ Y_n = S_n + Z_n, $$
With $Z_n$ defined as:

$$ Z_n = \sum_{j=0}^{n-1} S_j, $$
 the cumulative sum of past prices up to time $n-1$. To check if $Y_n$ is a martingale, we compute the conditional expectation $\mathbb{E}[Y_{n+1} | \mathcal{F}_n]$: 
$$ \mathbb{E}[Y_{n+1} | \mathcal{F}_n] = \mathbb{E}[S_{n+1} | \mathcal{F}_n] + \mathbb{E}[Z_{n+1} | \mathcal{F}_n]. $$
 Since $S_n$ is a martingale under the appropriate risk-neutral measure: 
$$ \mathbb{E}[S_{n+1} | \mathcal{F}_n] = S_n. $$
For $Z_{n+1}$, observe that: 
$$ Z_{n+1} = Z_n + S_n \quad \implies \quad \mathbb{E}[Z_{n+1} | \mathcal{F}_n] = Z_n + S_n. $$
Thus, $Y_n$ is a martingale. 
$$ \mathbb{E}[Y_{n+1} | \mathcal{F}_n] = S_n + (Z_n + S_n) = Y_n. $$
The Markov property requires: 
$$ \mathbb{P}(Y_{n+1} | \mathcal{F}_n) = \mathbb{P}(Y_{n+1} | Y_n). $$
However, $Y_n$ depends on the entire history of $S_n$ through 
$$ Z_n = \sum_{j=0}^{n-1} S_j. $$
The future evolution of $Y_n$ is influenced by $Z_n$, which cannot be determined solely from $Y_n$ at time $n$. Thus, $Y_n$ does not satisfy the Markov property.


**Exercise**
Consider an $N$-period binomial model.

**(i)** Let $M_0, M_1, \dots, M_N$ and $M_0', M_1', \dots, M_N'$ be martingales under the risk-neutral measure $\tilde{P}$. Show that if $M_N = M_N'$ (for every possible outcome of the sequence of coin tosses), then, for each $n$ between $0$ and $N$, we have $M_n = M_n'$ (for every possible outcome of the sequence of coin tosses). 

**Solution**
Let $\tilde{\mathbb{P}}$ be the risk-neutral measure under which both $M_n$ and $M_n'$ are martingales. The martingale property means: 
$$ \mathbb{E}_{\tilde{\mathbb{P}}}[M_{n+1} | \mathcal{F}_n] = M_n, \quad \mathbb{E}_{\tilde{\mathbb{P}}}[M_{n+1}' | \mathcal{F}_n] = M_n'. $$
 We are given that: 
$$ M_N = M_N' \quad \text{for all possible outcomes of the sequence of coin tosses}. $$
 We aim to show: 
$$ M_n = M_n' \quad \text{for all } n \text{ (from } 0 \text{ to } N\text{)}. $$
We use backward induction, starting from $n = N$ and moving backward to $n = 0$. **Base Case ($n = N$):** From the problem statement, we know: 
$$ M_N = M_N' \quad \text{for all outcomes}. $$
 **Inductive Hypothesis:** Assume that $M_{k+1} = M_{k+1}'$ for all outcomes for some $k \leq N-1$. We will show that $M_k = M_k'$. **Inductive Step:** Since $M_n$ and $M_n'$ are martingales under $\tilde{\mathbb{P}}$, we have: 
$$ M_k = \mathbb{E}_{\tilde{\mathbb{P}}}[M_{k+1} | \mathcal{F}_k], \quad M_k' = \mathbb{E}_{\tilde{\mathbb{P}}}[M_{k+1}' | \mathcal{F}_k]. $$
 By the inductive hypothesis, $M_{k+1} = M_{k+1}'$ for all outcomes. Therefore: 
$$ \mathbb{E}_{\tilde{\mathbb{P}}}[M_{k+1} | \mathcal{F}_k] = \mathbb{E}_{\tilde{\mathbb{P}}}[M_{k+1}' | \mathcal{F}_k]. $$
 Thus: 
$$ M_k = M_k'. $$


**(ii)** Let $V_N$ be the payoff at time $N$ of some derivative security. This is a random variable that can depend on all $N$ coin tosses. Define recursively $V_{N - 1}, V_{N - 2}, \dots, V_0$ by the algorithm (1.2.16) of Chapter 1. Show that:

$$
V_0, \frac{V_1}{1 + r}, \dots, \frac{V_{N - 1}}{(1 + r)^{N - 1}}, \frac{V_{N}}{(1 + r)^N}
$$

is a martingale under $\tilde{\mathbb{P}}$.

**Solution**
The algorithm defines the value of the derivative security at earlier times as: 
$$ V_n = \frac{1}{1 + r} \tilde{\mathbb{E}}[V_{n+1} | \mathcal{F}_n], $$
 where: 
- $V_n$ is the value of the derivative security at time $n$, 
- $\tilde{\mathbb{E}}$ is the expectation under the risk-neutral measure, 
- $\mathcal{F}_n$ is the filtration (information up to time $n$), 
- $r$ is the risk-free rate.

To show that the given sequence is a martingale under $\tilde{\mathbb{P}}$, we need to verify that: 

$$ 
\mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{V_{n+1}}{(1 + r)^{n+1}} \bigg| \mathcal{F}_n \right] = \frac{V_n}{(1 + r)^n}. 
$$

Start with $V_n$, which is recursively defined as: 

$$ 
V_n = \frac{1}{1 + r} \tilde{\mathbb{E}}[V_{n+1} | \mathcal{F}_n]. 
$$


$$ 
\frac{V_n}{(1 + r)^n} = \frac{1}{(1 + r)^n} \cdot \frac{1}{1 + r} \tilde{\mathbb{E}}[V_{n+1} | \mathcal{F}_n]. 
$$
 Simplify the factor $\frac{1}{(1 + r)^n} \cdot \frac{1}{1 + r}$: 
$$ 
\frac{V_n}{(1 + r)^n} = \frac{1}{(1 + r)^{n+1}} \tilde{\mathbb{E}}[V_{n+1} | \mathcal{F}_n]. 
$$
 Since conditional expectation is linear and $\frac{V_{n+1}}{(1 + r)^{n+1}}$ is $\mathcal{F}_n$-measurable: 

$$ 
\mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{V_{n+1}}{(1 + r)^{n+1}} \bigg| \mathcal{F}_n \right] = \frac{V_n}{(1 + r)^n}. 
$$

This proves that: 
$$ 
V_0, \frac{V_1}{1 + r}, \dots, \frac{V_{N-1}}{(1 + r)^{N-1}}, \frac{V_N}{(1 + r)^N} 
$$
 is a martingale under the risk-neutral measure $\tilde{\mathbb{P}}$, as the conditional expectation at each step satisfies the martingale property: 

$$ 
\mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{V_{n+1}}{(1 + r)^{n+1}} \bigg| \mathcal{F}_n \right] = \frac{V_n}{(1 + r)^n}. 
$$

**(iii)** Using the risk-neutral pricing formula:

$$
\frac{V_n}{(1 + r)^n} = \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^N} \right] \Longleftrightarrow V_n = \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - n}} \right]
$$

we define:

$$
V_n' = \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - n}} \right],\quad n = 0, 1, \dots, N - 1
$$

Show that:

$$
V_0', \frac{V_1'}{1 + r}, \cdots, \frac{V_{N-1}'}{(1 + r)^{N - 1}},\frac{V_N}{(1 + r)^N}
$$

is a martingale. 

**Solution**

$$
\begin{align*}
V_n' &= \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - n}} \right], \quad n = 0, 1, \dots, N-1. \\
\frac{V_n'}{(1 + r)^n} &= \frac{1}{(1 + r)^n} \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - n}} \right], \\
&= \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^N} \right]. \\
\frac{V_{n+1}'}{(1 + r)^{n+1}} &= \frac{1}{(1 + r)^{n+1}} \tilde{\mathbb{E}}_{n+1} \left[\frac{V_N}{(1 + r)^{N - (n+1)}} \right]. \\
\mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{V_{n+1}'}{(1 + r)^{n+1}} \Bigg| \mathcal{F}_n \right] &= \mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{1}{(1 + r)^{n+1}} \tilde{\mathbb{E}}_{n+1} \left[\frac{V_N}{(1 + r)^{N - (n+1)}} \right] \Bigg| \mathcal{F}_n \right]. \\
\mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{V_{n+1}'}{(1 + r)^{n+1}} \Bigg| \mathcal{F}_n \right] &= \frac{1}{(1 + r)^{n+1}} \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - (n+1)}} \right]. \\
\frac{1}{(1 + r)^{n+1}} &= \frac{1}{(1 + r)^n} \cdot \frac{1}{1 + r}. \\
\mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{V_{n+1}'}{(1 + r)^{n+1}} \Bigg| \mathcal{F}_n \right] &= \frac{1}{(1 + r)^n} \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - n}} \right]. \\
\mathbb{E}_{\tilde{\mathbb{P}}} \left[ \frac{V_{n+1}'}{(1 + r)^{n+1}} \Bigg| \mathcal{F}_n \right] &= \frac{V_n'}{(1 + r)^n}.
\end{align*}
$$


**(iv)** Conclude that $V_n = V_n'$ for every $n$ (i.e., the algorithm (1.2.16) of Theorem 1.2.2 of Chapter 1 gives the same derivative security prices as the risk-neutral pricing formula (2.4.11)).
```tikz
\begin{document}

\begin{tikzpicture}

% Tree Nodes
\node (S0) at (0,0) {$S_0$};
\node (S1H) at (2,2.5) {$S_1(H) = uS_0$};
\node (S1T) at (2,-2.5) {$S_1(T) = dS_0$};
\node (S2HH) at (4,4.5) {$S_2(HH) = u^2S_0$};
\node (S2HT) at (4,0) {$S_2(HT) = S_2(TH) = udS_0$};
\node (S2TT) at (4,-4.5) {$S_2(TT) = d^2S_0$};
\node (S3HHH) at (6,5.5) {$S_3(HHH) = u^3S_0$};
\node (S3HHT) at (6,3) {$S_3(HHT) = S_3(HTH) = S_3(THH) = u^2dS_0$};
\node (S3HTT) at (6,-3) {$S_3(HTT) = S_3(THT) = S_3(TTH) = ud^2S_0$};
\node (S3TTT) at (6,-5.5) {$S_3(TTT) = d^3S_0$};

% Connections
\draw[->, thick] (S0) -- (S1H);
\draw[->, thick] (S0) -- (S1T);
\draw[->, thick] (S1H) -- (S2HH);
\draw[->, thick] (S1H) -- (S2HT);
\draw[->, thick] (S1T) -- (S2HT);
\draw[->, thick] (S1T) -- (S2TT);
\draw[->, thick] (S2HH) -- (S3HHH);
\draw[->, thick] (S2HH) -- (S3HHT);
\draw[->, thick] (S2HT) -- (S3HHT);
\draw[->, thick] (S2HT) -- (S3HTT);
\draw[->, thick] (S2TT) -- (S3HTT);
\draw[->, thick] (S2TT) -- (S3TTT);

% Time Labels
\node at (0,-1) {$t = 0$};
\node at (2,-3) {$t = 1$};
\node at (4,-5) {$t = 2$};
\node at (6,-6) {$t = 3$};

\end{tikzpicture}

\end{document}
```
**Solution**
This can be simply proven via induction: Let's start with our definitions,

$$
V_n = \frac{1}{1 + r} \tilde{\mathbb{E}}_n [V_{n + 1} | F_n]\quad V_n' = \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - n}} \right]
$$

**Base Case:** $n = N \implies V_N = V_N'$
**Inductive Step:** We want to show $V_k = V_k'$ for all $k = N - 1, N - 2, \dots, 0$
Assume $V_{k + 1} = V_{k + 1}'$ for $k \le N - 1$

$$
\begin{align*}
V_k &= \frac{1}{1 + r} \tilde{\mathbb{E}}_k [V_{k + 1} | F_k]\\
&= \frac{1}{1 + r} \tilde{\mathbb{E}}_k [V_{k + 1}' | F_k]\\
\\
V_{k + 1}' &= \tilde{\mathbb{E}}_{k + 1} \left[\frac{V_N}{(1 + r)^{N - (k + 1)}} \right]\\
&= \frac{1}{1 + r} \tilde{\mathbb{E}}_k \left[\frac{V_N}{(1 + r)^{N - (k + 1)}} \right]\\
&= \tilde{\mathbb{E}}_k \left[\frac{V_N}{(1 + r)^{N - k}} \right]
\end{align*}
$$

Thus, we have $V_k = V_k'$.
Therefore, we've shown that $V_n = V_n'$ for all $n = 0, 1, \dots, N$. Therefore, 1.2.16 gives the same derivative security prices as the risk-neutral pricing formula. 


**Exercise: Stochastic Volatility, Random Interest Rate**
Consider a two-period stochastic volatility, random interest rate model of the type described in Exercise 1.9, shown in the image. 

The stock prices and interest rates are shown in the following:
```tikz
\begin{document}

\begin{tikzpicture}

% Tree Nodes
\node (S0) at (0,0) {$S_0$};
\node (S1H) at (2,2.5) {$S_1(H) = uS_0$};
\node (S1T) at (2,-2.5) {$S_1(T) = dS_0$};
\node (S2HH) at (4,4.5) {$S_2(HH) = u^2S_0$};
\node (S2HT) at (4,0) {$S_2(HT) = S_2(TH) = udS_0$};
\node (S2TT) at (4,-4.5) {$S_2(TT) = d^2S_0$};
\node (S3HHH) at (6,5.5) {$S_3(HHH) = u^3S_0$};
\node (S3HHT) at (6,3) {$S_3(HHT) = S_3(HTH) = S_3(THH) = u^2dS_0$};
\node (S3HTT) at (6,-3) {$S_3(HTT) = S_3(THT) = S_3(TTH) = ud^2S_0$};
\node (S3TTT) at (6,-5.5) {$S_3(TTT) = d^3S_0$};

% Connections
\draw[->, thick] (S0) -- (S1H);
\draw[->, thick] (S0) -- (S1T);
\draw[->, thick] (S1H) -- (S2HH);
\draw[->, thick] (S1H) -- (S2HT);
\draw[->, thick] (S1T) -- (S2HT);
\draw[->, thick] (S1T) -- (S2TT);
\draw[->, thick] (S2HH) -- (S3HHH);
\draw[->, thick] (S2HH) -- (S3HHT);
\draw[->, thick] (S2HT) -- (S3HHT);
\draw[->, thick] (S2HT) -- (S3HTT);
\draw[->, thick] (S2TT) -- (S3HTT);
\draw[->, thick] (S2TT) -- (S3TTT);

% Time Labels
\node at (0,-1) {$t = 0$};
\node at (2,-3) {$t = 1$};
\node at (4,-5) {$t = 2$};
\node at (6,-6) {$t = 3$};

\end{tikzpicture}

\end{document}
```

**(i)** Determine the risk-neutral probabilities:

$$
\tilde{\mathbb{P}}(HH), \tilde{\mathbb{P}}(HT), \tilde{\mathbb{P}}(TH), \tilde{\mathbb{P}}(TT)
$$

such that the time-zero value of an option that pays off $V_2$ at time two is given by the risk-neutral pricing formula:

$$
V_0 = \tilde{\mathbb{E}} \left[\frac{V_2}{(1 + r_0)(1 + r_2)} \right]
$$

**Solution**
We first want to find the expected value of $S_2$ given the following:

$$
\begin{align*} 
&\tilde{\mathbb{E}}[S_2] = \tilde{\mathbb{P}}(HH)S_2(HH) + \tilde{\mathbb{P}}(HT)S_2(HT) + \tilde{\mathbb{P}}(TH)S_2(TH) + \tilde{\mathbb{P}}(TT)S_2(TT), \\ 
&\tilde{\mathbb{E}}[S_2] = S_0 \left[ p^2 u^2 + 2p(1 - p)ud + (1 - p)^2 d^2 \right]. \end{align*}
$$

Then using the martingale condition and assuming $(1 + r_0)(1 + r_2) = 1$:

$$
\begin{align*}
&S_0 = \frac{\tilde{\mathbb{E}}[S_2]}{(1 + r_0)(1 + r_2)}, \\ 
&S_0 = S_0 \left[ p^2 u^2 + 2p(1 - p)ud + (1 - p)^2 d^2 \right], \\ 
&1 = p^2 u^2 + 2p(1 - p)ud + (1 - p)^2 d^2. 
\end{align*}
$$

Given our parameters:

$$
\begin{align*} &S_0 = 80, \quad u = \frac{80 + 10}{80} = 1.125, \quad d = \frac{80 - 10}{80} = 0.875. \\ &\tilde{\mathbb{E}}[S_2] = S_0 \left[ p^2 (1.125)^2 + 2p(1 - p)(1.125)(0.875) + (1 - p)^2 (0.875)^2 \right], \\ &\tilde{\mathbb{E}}[S_2] = 80 \left[ p^2 (1.265625) + 2p(1 - p)(0.984375) + (1 - p)^2 (0.765625) \right]. \end{align*}
$$

And thus, we can directly compute:

$$
\begin{align*} &1 = p^2 (1.265625) + 2p(1 - p)(0.984375) + (1 - p)^2 (0.765625), \\ &1 = 1.265625p^2 + 1.96875p - 1.96875p^2 + 0.765625 - 1.53125p + 0.765625p^2, \\ &1 = (1.265625 - 1.96875 + 0.765625)p^2 + (1.96875 - 1.53125)p + 0.765625, \\ &1 = 0.0625p^2 + 0.4375p + 0.765625. \end{align*}
$$


$$
\begin{align*} &0.0625p^2 + 0.4375p - 0.234375 = 0, \\ &p^2 + 7p - 3.75 = 0, \\ &p = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}, \quad a = 1, \, b = 7, \, c = -3.75, \\ &p = \frac{-7 \pm \sqrt{7^2 - 4(1)(-3.75)}}{2}, \\ &p = \frac{-7 \pm \sqrt{49 + 15}}{2}, \\ &p = \frac{-7 \pm \sqrt{64}}{2}, \\ &p = \frac{-7 + 8}{2} = \frac{1}{2}, \quad p = \frac{-7 - 8}{2} = -\frac{15}{2} \, (\text{discarded}). \end{align*}
$$

Thus our final probability is the following:

$$
\begin{align*} &p = \frac{1}{2}, \quad \tilde{\mathbb{P}}(HH) = p^2 = \frac{1}{4}, \quad \tilde{\mathbb{P}}(HT) = \tilde{\mathbb{P}}(TH) = p(1 - p) = \frac{1}{4}, \quad \tilde{\mathbb{P}}(TT) = (1 - p)^2 = \frac{1}{4}. \end{align*}
$$


**(ii)** Let $V_2 = (S_2 - 7)^+$. Compute $V_0, V_1(H)$ and $V_(T)$.

