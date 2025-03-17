---
layout: page
title: Chapter 2 - Probability Theory on Coin Toss Space
description: Notes on probability theory applied to coin toss spaces.
parent: course-1
importance: 3
permalink: /notes/course-1/chapter-2-probability/
nav: false
---


### Finite Probability Spaces
A finite probability space is a mathematical model for situations where a random experiment has a finite number of possible outcomes. For instance, in the binomial model discussed earlier, a coin was tossed a finite number of times.

**Definition**: A finite probability space consists of two components: a sample space $\Omega$ and a probability measure $\mathbb{P}$. These are defined as follows:
- **Sample Space**: $\Omega$ is a non-empty finite set representing all possible outcomes of the experiment.
- **Probability Measure**: $\mathbb{P}$ is a function that assigns a value in $[0, 1]$ to each element $\omega \in \Omega$ such that:

$$
  \sum_{\omega \in \Omega} \mathbb{P}(\omega) = 1
$$


An **event** is any subset of $\Omega$. The probability of an event $A \subseteq \Omega$ is defined as:

$$
\mathbb{P}(A) = \sum_{\omega \in A} \mathbb{P}(\omega)
$$

This setup models the behavior of random experiments. Specifically:
- $\mathbb{P}(\omega)$ is the probability of the outcome $\omega$.
- $\mathbb{P}(A)$ is the probability that the outcome falls within the subset $A$.

If $\mathbb{P}(A) = 0$, the outcome is certain not to be in $A$. Conversely, if $\mathbb{P}(A) = 1$, the outcome is certain to be in $A$. Since every outcome must belong to $\Omega$, we have:

$$
\mathbb{P}(\Omega) = 1
$$


Even outcomes with zero probability can be included in $\Omega$, as they represent events that are theoretically possible but practically impossible.

**Key Property:** If $A$ and $B$ are disjoint subsets of $\Omega$, the probability of their union is given by:

$$
\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)
$$

**Definition**: Let $(\Omega, \mathbb{P})$ be a finite probability space. A random variable is a real-valued function defined on $\Omega$. (We sometimes also permit a random variable to take the values $+\infty$ and $-\infty$). 

In the example of modelling stock prices in the binomial tree, we have written the arguments of $S_0, S_1, S_2$ and $S_3$ as $\omega_1 \omega_2 \omega_3$ even through some of these random variables do not depend on all the coin tosses. In particular, $S_0$ is actually not random because it takes the value $4$, regardless of how the coin tosses turn out; such a random variable is sometimes called a degenerate random variable. We write the argument of a random variable as $\omega$ even when $\omega = \omega_1 \omega_2 \omega_3$. We shall use these two notations interchangeably. It is even more common to write random variables without any arguments. 

The distribution of a random variable is a specification of the probabilities that the random variable takes various values. A random variable is not a distribution, and a distribution is not a random variable. 

e.g., Toss a coin three times, so the set of possible outcomes is:

$$
\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}
$$

Define the random variables:

$$
X = \text{Total number of heads},\quad Y = \text{Total number of tails}
$$


$$
\begin{align*}
X(HHH) = 3,\\
X(HHT) = X(HTH) = X(THH) = 2,\\
X(HTT) = X(THT) = X(TTH) = 1,\\
X(TTT) = 0\\
\\
Y(TTT) = 2,\\
Y(TTH) = Y(THT) = Y(HTT) = 2,\\
Y(THH) = Y(HTH) = Y(HHT) = 1,\\
Y(HHH) = 0
\end{align*}
$$

Let's define a probability measure on $\Omega$:

$$
\begin{align*}
\widetilde{\mathbb{P}}(\omega \in \Omega; X(\omega) = 0) &= \widetilde{\mathbb{P}}(\{TTT\}) = \frac{1}{8}, \\
\widetilde{\mathbb{P}}(\omega \in \Omega; X(\omega) = 1) &= \widetilde{\mathbb{P}}(\{HTT, THT, TTH\}) = \frac{3}{8}, \\
\widetilde{\mathbb{P}}(\omega \in \Omega; X(\omega) = 2) &= \widetilde{\mathbb{P}}(\{HHT, HTH, THH\}) = \frac{3}{8}, \\
\widetilde{\mathbb{P}}(\omega \in \Omega; X(\omega) = 3) &= \widetilde{\mathbb{P}}(\{HHH\}) = \frac{1}{8}.
\end{align*}
$$

Or shorten the notation to $\tilde{\mathbb{P}}(X = j)$ which refers to the probability of a subset of $\Omega$, the set of elements $\omega$ for which $X(\omega) = j$. Under $\mathbb{P}$ the probability that $X$ takes values $0, 1, 2, 3$ are:

$$
\begin{align*}
\widetilde{\mathbb{P}}(X = 0) &= \frac{1}{8}, & \widetilde{\mathbb{P}}(X = 1) &= \frac{3}{8}, \\
\widetilde{\mathbb{P}}(X = 2) &= \frac{3}{8}, & \widetilde{\mathbb{P}}(X = 3) &= \frac{1}{8}.
\end{align*}
$$

where $X$ counts the number of heads in a given 3-toss sequence. We could also list the table of probabilities where $Y$ counts the number of tails:

$$
\begin{align*}
\widetilde{\mathbb{P}}(Y = 0) &= \frac{1}{8}, & \widetilde{\mathbb{P}}(Y = 1) &= \frac{3}{8}, \\
\widetilde{\mathbb{P}}(Y = 2) &= \frac{3}{8}, & \widetilde{\mathbb{P}}(Y = 3) &= \frac{1}{8}.
\end{align*}
$$

where $Y$ is the random variable that models the number of tails for a 3-toss sequence of coin tosses $\omega_1 \omega_2 \omega_3$.

**Definition**: Let $X$ be a random variable defined on a finite probability space $(\Omega, \mathbb{P})$. The expectation (or expected value) of $X$ is defined to be:

$$
\mathbb{E}X = \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\omega)
$$

When we compute the expectation using the risk-neutral probability measure $\tilde{\mathbb{P}}$, we use the notation:

$$
\tilde{\mathbb{E}}X = \sum_{\omega \in \Omega} X(\omega) \tilde{\mathbb{P}}(\omega)
$$

The variance of $X$ is:

$$
\text{Var}(X) = \mathbb{E} \left[(X - \mathbb{E}X^2)\right]
$$

Clearly, expectation is linear, since if $X$ and $Y$ are random variables and $c_1$ and $c_2$ are constants, we have that:

$$
\mathbb{E}(c_1 X + c_2 Y) = c_1 \mathbb{E} X + c_2 \mathbb{E} Y
$$

In particular, we have that $l(x) = ax + b$ is a linear function of a dummy variable $x$ ($a$ and $b$ are constants), then $\mathbb{E} [l(X)] = l(\mathbb{E} X)$. When dealing with convex functions, we have the following inequality. 

**Theorem: Jensen's Inequality**
Let $X$ be a random variable on a finite probability space, and let $\phi(x)$ be a convex function of a dummy variable $x$, then:

$$
\mathbb{E} [\phi(X)] \ge \phi(\mathbb{E} X)
$$

**Proof**: We first argue that a convex function is the maximum of all linear functions that lie below it, i.e., for every $x \in \mathbb{R}$:

$$
\phi(x) = \max{\{l(x): l \text{ is linear and } l(y) \le \phi(y) \text{ for all } y \in \mathbb{R} \} }
$$

Since we only consider linear functions that lie below $\phi$, it is clear that:

$$
\phi(x) \ge \max{\{l(x); l \text{ is linear and } l(y) \le \phi(y) \text{ for all } y \in \mathbb{R} \} }
$$

On the other hand, let $x$ be an arbitrary point in $\mathbb{R}$. Because $\phi$ is convex, there is always a linear function $l$ that lies below $\phi$ and for which $\phi(x) = l(x)$ for this particular $x$. We call this a support line of $\phi$ at $x$:
Therefore, we have that:

$$
\phi(x) \le \max{\{l(x); l \text{ is linear and } l(y) \le \phi(y) \text{ for all } y \in \mathbb{R} \} }
$$

which gives us:

$$
\mathbb{E}[\phi(X)] \ge \mathbb{E}[l(X)] = l(\mathbb{E}X) \implies \mathbb{E}[\phi(X)] \ge \phi(\mathbb{E} X)
$$

One consequence of Jensen's inequality is that:

$$
\mathbb{E}[X^2] \ge (\mathbb{E}X)^2
$$


### Conditional Expectations 
We chose risk-neutral probabilities $\tilde{p}, \tilde{q}$ for our binomial model:

$$
\tilde{p} = \frac{1 + r - d}{u - d},\quad \tilde{q} = \frac{u - 1 - r}{u - d}
$$

We use can use these to check that:

$$
\frac{\tilde{p}u + \tilde{q}d}{1 + r} = 1
$$

Thus, for every time $n$ and sequence $\omega_1 \dots \omega_n$ of coin tosses:

$$
S_n(\omega_1 \dots \omega_n) = \frac{1}{1 + r} \left[\tilde{p}S_{n + 1}(\omega_1 \dots \omega_n H) + \tilde{q} S_{n + 1}(\omega_1 \dots \omega_n T) \right]
$$

Thus, we say that the stock price at time $n$ is the discounted weighted average of the two possible stock prices at time $n + 1$ where $\tilde{p}, \tilde{q}$ are the weights used in averaging. Moreover, we simplify:

$$
\begin{align*}
\tilde{\mathbb{E}}[S_{n + 1}] (\omega_1 \dots \omega_n) &= \tilde{p} S_{n + 1} (\omega_1 \dots \omega_n H) + \tilde{q} S_{n + 1} (\omega_1 \dots \omega_n T)\\
\implies S_n &= \frac{1}{1 + r} \tilde{\mathbb{E}}[S_{n + 1}]
\end{align*}
$$

where $\tilde{\mathbb{E}}_n [S_{n + 1}]$ is the conditional expectation of $S_{n + 1}$ based on the information at time $n$, where the conditional expectation can be regarded as an approximation of the value of $S_{n + 1}$ given the first $n$ coin tosses.

**Definition**: Let $n$ satisfy $1 \le n \le N$ and let $\omega_1 \dots \omega_n$ be given and for the moment, fixed. There are $2^{N - n}$ possible continuations of $\omega_{n + 1} \dots \omega_N$ of the sequence fixed $\omega_1 \dots \omega_n$. Let $\# H(\omega_{n + 1} \dots \omega_N)$ be the number of heads in $\omega_{n + 1} \dots \omega_N$ and $\# T(\omega_{n + 1} \dots \omega_N)$ be the number of tails in $\omega_{n + 1} \dots \omega_N$. Now, we define:

$$
\tilde{\mathbb{E}}[X] (\omega_1 \dots \omega_n) = \sum_{\omega_{n + 1} \dots \omega_N} \tilde{p}^{\# H(\omega_{n + 1} \dots \omega_N)}\tilde{q}^{\# T(\omega_{n + 1} \dots \omega_N)} X(\omega_1 \dots \omega_n \omega_{n + 1} \dots \omega_N)
$$

where $\tilde{\mathbb{E}}_n [X]$ is the conditional expectation of $X$ based on information at time $n$. 

**Definition**: The two extreme cases of conditioning are $\tilde{\mathbb{E}}_0 [X]$, the conditional expectation of $X$ based on no information, which we define by:

$$
\tilde{\mathbb{E}}_0 [X] = \tilde{\mathbb{E}} X
$$

and $\tilde{\mathbb{E}}_N [X]$, the conditional expectation of $X$ based on knowledge of all $N$ coin tosses which we define by:

$$
\tilde{\mathbb{E}}_N [X] = X
$$


**Theorem: Fundamental Properties of Conditional Expectations**
Let $N$ be a positive integers and $X, Y$ be random variables depending on the first $N$ coin tosses. Let $0 \le n \le N$ be given. The following properties hold:

$$
\begin{align*}
(i) & \quad \textit{Linearity of conditional expectations.} \text{ For all constants } c_1 \text{ and } c_2, \text{ we have:} \\
    & \mathbb{E}_n[c_1X + c_2Y] = c_1\mathbb{E}_n[X] + c_2\mathbb{E}_n[Y]. \\[1em]
(ii) & \quad \textit{Taking out what is known.} \text{ If } X \text{ actually depends only on the first } n \text{ coin tosses, then:} \\
    & \mathbb{E}_n[XY] = X \cdot \mathbb{E}_n[Y]. \\[1em]
(iii) & \quad \textit{Iterated conditioning.} \text{ If } 0 \leq n \leq m \leq N, \text{ then:} \\
    & \mathbb{E}_n\big[\mathbb{E}_m[X]\big] = \mathbb{E}_n[X]. \\
    & \text{In particular, } \mathbb{E}\big[\mathbb{E}_m[X]\big] = \mathbb{E}[X]. \\[1em]
(iv) & \quad \textit{Independence.} \text{ If } X \text{ depends only on tosses } n+1 \text{ through } N, \text{ then:} \\
    & \mathbb{E}_n[X] = \mathbb{E}[X]. \\[1em]
(v) & \quad \textit{Conditional Jensen's Inequality}. \text{If } \phi(x) \text{ is a convex function of the dummy } \\
&\text{variable } x, \text{ then:}\\
&\mathbb{E}_n [\phi(X)] \ge \phi(\mathbb{E}_n [X])

\end{align*}
$$


e.g., Using $p = \frac{2}{3}, q = \frac{1}{3}$, we can express the Linearity of Conditional Expectations 

$$
\begin{align*}
\mathbb{E}_1[S_2](H) &= \frac{2}{3} \cdot S_2(HH) + \frac{1}{3} \cdot S_2(HT) \\
                     &= \frac{2}{3} \cdot 16 + \frac{1}{3} \cdot 4 \\
                     &= 12. \\[1em]
\mathbb{E}_1[S_3](H) &= \frac{4}{9} \cdot S_3(HHH) + \frac{2}{9} \cdot S_3(HHT) + \frac{2}{9} \cdot S_3(HTH) + \frac{1}{9} \cdot S_3(HTT) \\
                     &= \frac{4}{9} \cdot 32 + \frac{2}{9} \cdot 8 + \frac{2}{9} \cdot 8 + \frac{1}{9} \cdot 2 \\
                     &= 18. \\[1em]
\mathbb{E}_1[S_2 + S_3](H) &= \frac{4}{9}(S_2(HH) + S_3(HHH)) + \frac{2}{9}(S_2(HT) + S_3(HHT)) \\
                     &\quad + \frac{2}{9}(S_2(HT) + S_3(HTH)) + \frac{1}{9}(S_2(HT) + S_3(HTT)) \\
                     &= \frac{4}{9}(16 + 32) + \frac{2}{9}(16 + 8) + \frac{2}{9}(4 + 8) + \frac{1}{9}(4 + 2) \\
                     &= 30.
\end{align*}
$$


$$
\text{And consequently, } \mathbb{E}_1[S_2](H) + \mathbb{E}_1[S_3](H) = 12 + 18 = 30. \\[1em]
$$

Similarly, we can show that:

$$
\mathbb{E}[S_2 + S_3](H) = \frac{4}{9}(16 + 32) + \frac{2}{9} (16 + 8) + \frac{2}{9}(4 + 8) + \frac{1}{9}(4 + 2) = 30
$$


$$
\tilde{\mathbb{E_1}}[S_2 + S_3](T) = 7.50 = \mathbb{E}_1 [S_2](T) + \mathbb{E}_1 [S_3](T) \implies \mathbb{E}[S_2 + S_3] = \mathbb{E}_1 [S_2] + \mathbb{E}_1[S_3]
$$


e.g., Iterated Conditioning. We first estimate $S_3$ based on the information at time 2:

$$
\begin{align*}
    \mathbb{E}_2[S_3](HH) &= \frac{2}{3} \cdot 32 + \frac{1}{3} \cdot 8 = 24, \\
    \mathbb{E}_2[S_3](HT) &= \frac{2}{3} \cdot 8 + \frac{1}{3} \cdot 2 = 6, \\
    \mathbb{E}_2[S_3](TH) &= \frac{2}{3} \cdot 8 + \frac{1}{3} \cdot 2 = 6, \\
    \mathbb{E}_2[S_3](TT) &= \frac{2}{3} \cdot 2 + \frac{1}{3} \cdot \frac{1}{2} = 1.50.
\end{align*}
$$

And now we can estimate, based on the information at time 1:

$$
\begin{align*}
    \mathbb{E}_1\big[\mathbb{E}_2[S_3]\big](H) 
    &= \frac{2}{3} \cdot \mathbb{E}_2[S_3](HH) + \frac{1}{3} \cdot \mathbb{E}_2[S_3](HT) \\
    &= \frac{2}{3} \cdot 24 + \frac{1}{3} \cdot 6 = 18, \\
    \mathbb{E}_1\big[\mathbb{E}_2[S_3]\big](T) 
    &= \frac{2}{3} \cdot \mathbb{E}_2[S_3](TH) + \frac{1}{3} \cdot \mathbb{E}_2[S_3](TT) \\
    &= \frac{2}{3} \cdot 6 + \frac{1}{3} \cdot 1.50 = 4.50.
\end{align*}
$$

The estimate of the estimate is an average of averages, and it is not surprising that we can get the same result by a more comprehensive averaging. This more comprehensive averaging occurs when we estimate $S_3$ directly based on the information at time 1:

$$
\begin{align*}
    \mathbb{E}_1[S_3](H) 
    &= \frac{4}{9} \cdot 32 + \frac{2}{9} \cdot 8 + \frac{2}{9} \cdot 8 + \frac{1}{9} \cdot 2 = 18, \\
    \mathbb{E}_1[S_3](T) 
    &= \frac{4}{9} \cdot 8 + \frac{2}{9} \cdot 2 + \frac{2}{9} \cdot 2 + \frac{1}{9} \cdot \frac{1}{2} = 4.50.
\end{align*}
$$


e.g., Independence. The quotient $\frac{S_2}{S_1}$ takes either the value 2 or $\frac{1}{2}$ depending on whether the second coin toss results in head or tails, respectively. In particular, $\frac{S_2}{S_1}$ does not depend on the first coin toss. We complete:

$$
\begin{align*}
    \mathbb{E}_1\left[\frac{S_2}{S_1}\right](H) 
    &= \frac{2}{3} \cdot \frac{S_2(HH)}{S_1(H)} + \frac{1}{3} \cdot \frac{S_2(HT)}{S_1(H)} \\
    &= \frac{2}{3} \cdot 2 + \frac{1}{3} \cdot \frac{1}{2} = \frac{3}{2}, \\
    \mathbb{E}_1\left[\frac{S_2}{S_1}\right](T) 
    &= \frac{2}{3} \cdot \frac{S_2(TH)}{S_1(T)} + \frac{1}{3} \cdot \frac{S_2(TT)}{S_1(T)} \\
    &= \frac{2}{3} \cdot 2 + \frac{1}{3} \cdot \frac{1}{2} = \frac{3}{2}.
\end{align*}
$$


### Martingales

$$
\frac{S_n}{(1 + r)^n} = \tilde{\mathbb{E}}_n \left[\frac{S_{n + 1}}{(1 + r)^{n + 1}} \right]
$$

expresses the fact that under the risk-neutral measure, for a stock that pays no dividend, the best estimate based on the information at time $n$ of the value of the discounted stock price at time $n + 1$ is the discounted stock price at time $n$. The risk-neutral probabilities are chosen to enforce this. Moreover, processes that satisfy this condition are called martingales. 

**Definition: Martingale**
Consider a binomial asset pricing model. Let $M_0, M_1, \dots, M_N$ be a sequence of random variables, with each $M_n$ depending only on the first $n$ coin tosses ($M_0$ is constant). We call this stochastic process *adapted*:

$$
\begin{align*}
(i)\quad &\text{ If } M_n = \mathbb{E}_n [M_{n + 1}] \quad n = 0, 1, \dots, N - 1\\
&\text{We say this process is a martingale.}\\ 
(ii)\quad &\text{ If } M_n \le \mathbb{E}_n [M_{n + 1}] \quad n = 0, 1, \dots, N - 1\\
&\text{We say the process is a submartingale.}\\
&\text{(even thought it may have a tendency to increase)}\\
(iii)\quad &\text{ If } M_n \ge \mathbb{E}_n [M_{n + 1}] \quad n = 0, 1, \dots, N - 1\\
&\text{We say the process is a supermartingale.}\\
&\text{Even though it may have a tendency to decrease.}
\end{align*}
$$


$$
\begin{align*}
M_{n + 1} &= \mathbb{E}_{n + 1}[M_{n + 2}] \quad \text{One-step ahead}\\
\implies \mathbb{E}_n [M_{n + 1}] &= \mathbb{E}_n [\mathbb{E}_{n + 1} [M_{n + 2}]] = \mathbb{E}_n[M_{n + 2}] \quad \text{Two-Step Ahead}\\
\implies M_n &= \mathbb{E}_n[M_{n + 2}]\\
\implies M_n &= \mathbb{E} [M_m] \quad 0 \le n \le m \le N
\end{align*}
$$

**Theorem:** Expectation of a martingale is constant over time. i.e., If $M_0, M_1, \dots, M_N$ is a martingale, then we have that:

$$
M_0 = \mathbb{E}M_n \quad n = 0, 1, \dots, N
$$

Indeed, taking expectations of both side gives that:

$$
\mathbb{E}M_0 = \mathbb{E}M_1 = \mathbb{E}M_2 = \cdots = \mathbb{E}M_{n - 1} = \mathbb{E} M_N
$$


**Theorem** Consider the general binomial model with $0 < d < 1 + r < u$. Let the risk-neutral probabilities be given by:

$$
\tilde{p} = \frac{1 + r - d}{u - d},\quad \tilde{q} = \frac{u - 1 - r}{u - d}
$$

Then, under the risk-neutral measure, the discounted stock price is a martingale, i.e., the following equation:

$$
\frac{S_n}{(1 + r)^n} = \tilde{\mathbb{E}}_n \left[\frac{S_{n + 1}}{(1 + r)^{n + 1}} \right]
$$

holds at every time $n$ and for every sequence of coin tosses. 

**Proof:**

$$
\begin{align*}
\widetilde{\mathbb{E}}_n &\left[ \frac{S_{n+1}}{(1 + r)^{n+1}} \right](\omega_1 \ldots \omega_n) \\
&= \frac{1}{(1 + r)^n} \cdot \frac{1}{1 + r} \left[ 
    \widetilde{p} S_{n+1}(\omega_1 \ldots \omega_n H) + 
    \widetilde{q} S_{n+1}(\omega_1 \ldots \omega_n T) 
\right] \\
&= \frac{1}{(1 + r)^n} \cdot \frac{1}{1 + r} \left[ 
    \widetilde{p} u S_n(\omega_1 \ldots \omega_n) + 
    \widetilde{q} d S_n(\omega_1 \ldots \omega_n) 
\right] \\
&= \frac{S_n(\omega_1 \ldots \omega_n)}{(1 + r)^n} \cdot 
    \frac{\widetilde{p} u + \widetilde{q} d}{1 + r} \\
&= \frac{S_n(\omega_1 \ldots \omega_n)}{(1 + r)^n}.
\end{align*}
$$


$$
\begin{align*}
\widetilde{\mathbb{E}}_n \left[ \frac{S_{n+1}}{(1 + r)^{n+1}} \right] 
&= \widetilde{\mathbb{E}}_n \left[ \frac{S_n}{(1 + r)^{n+1}} \cdot \frac{S_{n+1}}{S_n} \right] \\
&= \frac{S_n}{(1 + r)^n} \widetilde{\mathbb{E}}_n \left[ \frac{1}{1 + r} \cdot \frac{S_{n+1}}{S_n} \right] 
\quad \text{(Taking out what is known)} \\
&= \frac{S_n}{(1 + r)^n} \cdot \frac{1}{1 + r} \widetilde{\mathbb{E}}_n \left[ \frac{S_{n+1}}{S_n} \right] 
\quad \text{(Independence)} \\
&= \frac{S_n}{(1 + r)^n} \cdot \frac{\widetilde{p} u + \widetilde{q} d}{1 + r} \\
&= \frac{S_n}{(1 + r)^n}.
\end{align*}
$$


**Key Concept**: When an investor who, at each time $n$, takes a position of $\Delta_n$ shares of stock and holds this position until $n + 1$, when he takes a new position of $\Delta_{n + 1}$ shares, the portfolio variable $\Delta_n$ may depend on the first $n$ coin tosses and $\Delta_{n + 1}$ may depend on the first $n + 1$ coin tosses. In other words:

$$
\Delta_0, \Delta_1, \dots, \Delta_{N - 1}
$$

is an *adapted* process in the sense that, for each $\Delta_n$ for $n = 0, 1, \dots, N - 1$, depends only on the first $n$ coin tosses. Moreover, if the investor begins with initial wealth $X_0$ and $X_n$, which denotes their wealth at each time $n$, then the evolution of his wealth is governed by the wealth equation:

$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - \Delta_n S_n) \quad n = 0, 1, \dots, N - 1
$$

Note: Each $X_n$ depends only on the first $n$ coin tosses.

**Theorem**: Consider the binomial model with $N$ periods. Let $\Delta_0, \Delta_1, \dots, \Delta_{N - 1}$ be an adapted portfolio process, let $X_0$ be a real number (constant), and let the wealth process $X_1, \dots, X_N$ be generated recursively by:

$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - \Delta_n S_n)\quad n = 0, 1, \dots, N - 1
$$

Then, the **discounted wealth process**:

$$
\frac{X_n}{(1 + r)^n}\quad n = 0, 1, \dots, N
$$

is a martingale under the risk-neutral measure, i.e., 

$$
\frac{X_n}{(1 + r)^n} = \tilde{\mathbb{E}}_n \left[\frac{X_{n + 1}}{(1 + r)^{n + 1}} \right],\quad n = 0, 1, \dots, N - 1
$$

**Proof**:

$$
\begin{align*}
    \widetilde{\mathbb{E}}_n \left[\frac{X_{n+1}}{(1 + r)^{n+1}} \right] 
    &= \widetilde{\mathbb{E}}_n \left[\frac{\Delta_n S_{n+1}}{(1 + r)^{n+1}} + \frac{X_n - \Delta_n S_n}{(1 + r)^n} \right] \\
    &\text{(Linearity)} \\
    &= \widetilde{\mathbb{E}}_n \left[\frac{\Delta_n S_{n+1}}{(1 + r)^{n+1}} \right] + \widetilde{\mathbb{E}}_n \left[\frac{X_n - \Delta_n S_n}{(1 + r)^n} \right]  \\
    &\text{(Taking out what is known)} \\
    &= \Delta_n \widetilde{\mathbb{E}}_n \left[\frac{S_{n+1}}{(1 + r)^{n+1}} \right] + \frac{X_n - \Delta_n S_n}{(1 + r)^n} \quad \\
    &\text{(Theorem 2.4.4)}\\
    &= \Delta_n \frac{S_n}{(1 + r)^n} + \frac{X_n - \Delta_n S_n}{(1 + r)^n} \\
    &= \frac{X_n}{(1 + r)^n}.
\end{align*}
$$

**Corollary**: Under the conditions of the theorem above:

$$
\tilde{\mathbb{E}} \frac{X_n}{(1 + r)^n}\quad n = 0, 1, \dots, N
$$

The expected value of a martingale cannot change with time and so must always be equal to the time-zero value of the martingale. Applying this to our $\tilde{\mathbb{P}}$-martingale $\frac{X_n}{(1 + r)^n}$ for $n = 0, 1, \dots, N$, we can get the equation above. 

Another consequence of the Theorem above is another version of the risk-neutral pricing formula. Define $V_N$ to be a random variable that represents the value of a derivative security paying off at time $N$ depending on the first $N$ coin tosses. We know that there is initial wealth $X_0$ and a replicating portfolio process $\Delta_0, \dots, \Delta_{N - 1}$ that generates a wealth process $X_1, \dots, X_N$ satisfying $X_n = V_N$, no matter how the coin tossing turns out. Because $\frac{X_n}{(1 + r)^n}$ for $n = 0, 1, \dots, N$ is a martingale, the multi-step ahead property shown previously implies:

$$
\frac{X_n}{(1 + r)^n} = \mathbb{E}_n \left[\frac{X_N}{(1 + r)^N} \right] = \mathbb{E}_n \left[\frac{V_N}{(1 + r)^N} \right]
$$

However, we may have derivative securities, such as bonds, that do NOT pay off on a single date, rather, make series of payments. For such a security, we have the following pricing and hedging formulas:

**Theorem:** Consider an $N$-period binomial asset pricing-model with $0 < d < 1 + r < u$ and with risk-neutral probability measure $\tilde{\mathbb{P}}$. Let $C_0, C_1, \dots, C_N$ be a sequence of random variables such that each $C_n$ depends only on $\omega_n, \dots, \omega_n$. The price at time $n$ of the derivative security that makes payments $C_n, \dots, C_N$ at time $n, \dots, N$, respectively, is:

$$
V_n = \tilde{\mathbb{E}}_n \left[\sum_{k = n}^N \frac{C_k}{(1 + r)^{k - n}} \right],\quad n = 0, 1, \dots, N
$$

The price process:

$$
C_n(\omega_1 \dots \omega_n) = V_n(\omega_1 \dots \omega_n) - \frac{1}{1 + r}[\tilde{p} V_{n + 1}(\omega_1 \dots \omega_n H) + \tilde{q}V_{n + 1}(\omega_1 \dots \omega_n T)]
$$

We define the Delta-Hedging Formula as:

$$
\Delta_n(\omega_1 \dots \omega_n) = \frac{V_{n + 1}(\omega_1 \dots \omega_n H) - V_{n + 1}(\omega_1 \dots \omega_n T)}{S_{n + 1}(\omega_1 \dots \omega_n H) - S_{n + 1}(\omega_1 \dots \omega_n T)}
$$

where $n$ ranges between $0$ and $N - 1$. If we set $X_0 = V_0$ and define recursively forward in time the portfolio values $X_1, X_2, \dots X_N$ by:

$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - C_n - \Delta_n S_n)
$$

then we have:

$$
X_n(\omega_1 \dots \omega_n) = V_n(\omega_1 \dots \omega_n)
$$

for all $n$ and all $\omega_1, \dots, \omega_n$.

We call $V_n$ the Net Present Value at time $n$ of the sequence of payments $C_n, \dots, C_N$. It's just the **sum of the value $\tilde{\mathbb{E}}_n \left[ \frac{C_k}{(1 + r)^{k - n}} \right]$** of each of the payments $C_k$ to be made at times $k = n, k = n + 1, \dots, k = N$. Note, that the payment at time $n$ is included. This payment $C_n$, depends on only the first $n$ tosses and so can be taken outside the conditional expectation $\tilde{\mathbb{E}}_n$ such that:

$$
V_n = C_n + \tilde{\mathbb{E}}_n \left[\sum_{k = n + 1}^N \frac{C_k}{(1 + r)^{k - n}} \right],\quad n = 0, 1, \dots, N - 1
$$

In the case that $n = N$, we have that:

$$
V_N = C_N
$$

An agent short cash flows $C_0, \dots, C_n$ hedges the payments by investing in a stock and a money market account. At each time $n$, before making the payment $C_n$, the portfolio value is $X_n$. After the payment, the agent takes a stock position $\Delta_n$ according to the Delta Hedging formula, ensuring the portfolio evolves to $X_{n+1}$ before $C_{n+1}$. Starting with $X_0 = V_0$, this strategy ensures $X_N = V_N = C_N$ at the final time $N$, allowing the agent to make the last payment $C_N$ and reduce the portfolio to zero, achieving a perfect hedge.

**Proof**:
We can proceed by induction on $n$ and show that the by the hypothesis $X_n (\omega_1 \dots \omega_n) = V_n (\omega_1 \dots \omega_n)$ for some $n = 0, 1, \dots, N - 1$ and all $\omega_1 \dots \omega_n$. 

$$
\begin{align*}
X_{n + 1} (\omega_1 \dots \omega_n H) &= V_{n + 1}(\omega_1 \dots \omega_n H)\\
X_{n + 1} (\omega_1 \dots \omega_n T) &= V_{n + 1}(\omega_1 \dots \omega_n T)
\end{align*}
$$

Via iterated conditioning, we have that:

$$
\begin{align*}
V_n &= C_n + \tilde{\mathbb{E}}_n \left[ \frac{1}{1 + r} \tilde{\mathbb{E}}_{n+1} \left[ \sum_{k=n+1}^N \frac{C_k}{(1 + r)^{k - (n+1)}} \right] \right] \\
&= C_n + \tilde{\mathbb{E}}_n \left[ \frac{1}{1 + r} V_{n+1} \right],
\end{align*}
$$


$$
\begin{align*}
V_n(\omega_1 \dots \omega_n) - C_n(\omega_1 \dots \omega_n) 
&= \frac{1}{1 + r} \left[ \tilde{p} V_{n+1}(\omega_1 \dots \omega_n H) + \tilde{q} V_{n+1}(\omega_1 \dots \omega_n T) \right].
\end{align*}
$$


$$
\begin{align*}
V_n - C_n &= \frac{1}{1 + r} \left[ \tilde{p} V_{n+1}(H) + \tilde{q} V_{n+1}(T) \right].
\end{align*}
$$


$$
\begin{align*}
X_{n+1}(H) &= \Delta_n S_{n+1}(H) + (1 + r)(X_n - C_n - \Delta_n S_n) \\
&= \frac{V_{n+1}(H) - V_{n+1}(T)}{S_{n+1}(H) - S_{n+1}(T)} \left( S_{n+1}(H) - (1 + r) S_n \right) \\
&\quad + (1 + r)(V_n - C_n),\\
&= \frac{V_{n+1}(H) - V_{n+1}(T)}{(u - d) S_n} (u S_n - (1 + r) S_n) \\ &\quad + \tilde{p} V_{n+1}(H) + \tilde{q} V_{n+1}(T),\\
&= (V_{n+1}(H) - V_{n+1}(T)) \frac{u - 1 - r}{u - d} + \tilde{p} V_{n+1}(H) + \tilde{q} V_{n+1}(T),\\
&= (V_{n+1}(H) - V_{n+1}(T)) \tilde{q} + \tilde{p} V_{n+1}(H) + \tilde{q} V_{n+1}(T),\\
&= \tilde{p} V_{n+1}(H) + \tilde{q} V_{n+1}(T) = V_{n+1}(H).
\end{align*}
$$



### Markov Processes 

**Definition**
Consider the binomial asset pricing model. Let $X_0, X_1, \dots, X_N$ be an adapted process. If, for every $n$ between $0$ and $N - 1$ and for every function $f(x)$ there is another function $g(x)$ (depending on $n$ and $f$) each that:

$$
\mathbb{E}_n [f(X_{n + 1})] = g(X_n)
$$

we say that $X_0, X_1, \dots, X_N$ is a Markov process. In other words, the information about the coin tosses one needs in order to evaluate $\mathbb{E}_n [f(X_{n + 1})]$ is summarized by $X_n$. Thus, the expected value of some function of the next state $f(X_{n + 1})$ can be entirely determined by applying a function $g$ to the current state $X_n$. Thus to predict $X_{n + 1}$ you only need to know $X_n$. 

**e.g., Stock Price**
The stock price at time $n + 1$ is given in terms of the stock price at time $n$ by:

$$
S_{n+1}(\omega_1 \dots \omega_n \omega_{n+1}) = 
\begin{cases} 
u S_n(\omega_1 \dots \omega_n), & \text{if } \omega_{n+1} = H, \\
d S_n(\omega_1 \dots \omega_n), & \text{if } \omega_{n+1} = T.
\end{cases}
$$

The conditional expectation is:

$$
\mathbb{E}_n [f(S_{n + 1})] (\omega_1 \dots \omega_n) = pf(uS_n (\omega_1 \dots \omega_n)) + qf(dS_n (\omega_1 \dots \omega_n)),
$$

which depends only on $\omega_1 \dots \omega_n$ via $S_n (\omega_1 \dots \omega_n)$. Therefore:

$$
\mathbb{E}_n [f(S_{n + 1})] = g(S_n),
$$

where $g(x) = pf(ux) + qf(dx)$. This shows that the stock price process is Markov under both the risk-neutral and actual probability measures. To price a derivative security with payoff $V_N = v_N(S_N)$, the risk-neutral pricing formula is used:

$$
V_n = \frac{1}{1 + r} \tilde{\mathbb{E}}_n [V_{n + 1}],\quad n = 0, 1, \dots, N - 1.
$$

but $V_N = v_N(S_N)$ and the stock price process is Markov:

$$
\begin{align*}
V_{N - 1} &= \frac{1}{1 + r} \tilde{\mathbb{E}}_{N - 1}[v_N (S_N)] = v_{N - 1} (S_{N - 1})\\
V_{N - 2} &= \frac{1}{1 + r} \tilde{\mathbb{E}}_{N - 2}[v_{N - 1} (S_{N - 1})] = v_{N - 2} (S_{N - 2})
\end{align*}
$$

for some function $v_{N - 2}$. Generally, $V_n = v_n(S_n)$ for some function $v_n$. 

The martingale property is the special case of:

$$
\mathbb{E}_n[f(X_{n + 1})] = g(X_n)
$$

Moreover, we require that for every $f$ there is a corresponding $g$ such that the expectation above holds. The Markov property requires only that:

$$
\mathbb{E}_n [M_{n + 1}] = g(M_n)
$$

for some function $g$ and does not require that the function $g$ be given by $g(x) = x$.
Thus, NOT every Markov process is a martingale. 

$$
v_n(s) = \frac{1}{1 + r}[\tilde{p} v_{n + 1}(us) + \tilde{q}v_{n + 1}(ds)]
$$


**Lemma: (Independence)**
In the $N$-period binomial asset pricing model, let $n$ be an integer between 0 and $N$. Suppose the random variables $X^1, \dots, X^K$ depend only on coin tosses 1 through $n$ and the random variables $Y^1, \dots, Y^L$ depend only on coin tosses $n + 1$ through $N$. Let $f(x^1, \dots, x^K, y^1, \dots, y^L)$ be a function of dummy variables $x^1, \dots, x^K$ and $y^1, \dots, y^L$ and define:

$$
g(x^1, \dots, x^K) = \mathbb{E}f(x^1, \dots, x^K, Y^1, \dots, Y^L)
$$

Assume that $K = L = 1$ then $g(x) = \mathbb{E} f(x, Y)$.
Then, 

$$
\mathbb{E}_n [f(X^1, \dots, X^K, Y^1, \dots, Y^L)] = g(X^1, \dots, X^K)
$$

and $\mathbb{E}_n [f(X, Y)] = g(X)$.
We hold $f$ constant by replacing it with random variable $X$ by an arbitrary fixed dummy variable $x$ and compute the conditional expectation of $f(x, Y)$. 


e.g., Consider the maximum-to-date process $M_n = \max{S_k}_{0 \le k \le n}$ with $p = \frac{2}{3}, q = \frac{1}{3}$.
```tikz
\begin{document}

\begin{tikzpicture}

% Tree Nodes
\node (M0) at (0,0) {$M_0 = 4$};
\node (M1H) at (2,2.5) {$M_1(H) = 8$};
\node (M1T) at (2,-2.5) {$M_1(T) = 4$};
\node (M2HH) at (4,4.5) {$M_2(HH) = 16$};
\node (M2HT) at (4,0) {$M_2(HT) = 8$};
\node (M2TH) at (4,-1) {$M_2(TH) = 4$};
\node (M2TT) at (4,-4.5) {$M_2(TT) = 4$};
\node (M3HHH) at (6,5.5) {$M_3(HHH) = 32$};
\node (M3HHT) at (6,3) {$M_3(HHT) = 16$};
\node (M3HTH) at (6,1) {$M_3(HTH) = 8$};
\node (M3HTT) at (6,-1) {$M_3(HTT) = 8$};
\node (M3THH) at (6,-3) {$M_3(THH) = 8$};
\node (M3THT) at (6,-4.5) {$M_3(THT) = 4$};
\node (M3TTT) at (6,-6.5) {$M_3(TTT) = 4$};

% Connections
\draw[->, thick] (M0) -- (M1H);
\draw[->, thick] (M0) -- (M1T);
\draw[->, thick] (M1H) -- (M2HH);
\draw[->, thick] (M1H) -- (M2HT);
\draw[->, thick] (M1T) -- (M2TH);
\draw[->, thick] (M1T) -- (M2TT);
\draw[->, thick] (M2HH) -- (M3HHH);
\draw[->, thick] (M2HH) -- (M3HHT);
\draw[->, thick] (M2HT) -- (M3HTH);
\draw[->, thick] (M2HT) -- (M3HTT);
\draw[->, thick] (M2TH) -- (M3THH);
\draw[->, thick] (M2TH) -- (M3THT);
\draw[->, thick] (M2TT) -- (M3TTT);

% Time Labels
\node at (0,-1) {$t = 0$};
\node at (2,-3.5) {$t = 1$};
\node at (4,-5.5) {$t = 2$};
\node at (6,-7.5) {$t = 3$};

\end{tikzpicture}

\end{document}
```
Clearly, we have that:

$$
\begin{align*}
    \mathbb{E}_2[M_3](TH) &= \frac{2}{3}M_3(THH) + \frac{1}{3}M_3(THT) = \frac{16}{3} + \frac{4}{3} = 6\frac{2}{3}, \\
    \mathbb{E}_2[M_3](TT) &= \frac{2}{3}M_3(TTH) + \frac{1}{3}M_3(TTT) = \frac{8}{3} + \frac{4}{3} = 4.
\end{align*}
$$

Since $M_2(TH) = M_2(TT) = 4$ there cannot be a function $g$ such that we have that:

$$
\mathbb{E}_3 [M_3] (TH) = g(M_2(TH))\quad\text{and}\quad \mathbb{E}_3 [M_3](TT) = g(M_2(TT))
$$

The maximum-to-date process is not Markov because recording only that the value of the maximum-to-date at time two is 4, without recording the value of the stock price at time two, neglects information relevant to the evolution of the maximum-to-date process after time two. 

**Recovering a Markov property:** We add one or more state variables, recovering the Markov property, having determined a way to describe the state of the market in terms of these variables. 

**Definition**: Consider the binomial asset pricing model. Let $\{(X^1_n, \dots, X_n^K);\quad n = 0, 1, \dots, N\}$ be a $K$-dimensional adapted process, i.e., $K$ one-dimensional adapted processes. If, for every $n$ between $0$ and $N - 1$, and for every function $f(x^1, \dots, x^K)$ there is another function $g(x^1, \dots, x^K)$ (depending on $n$ and $f$) such that:

$$
\mathbb{E}_n [f(X^1_{n + 1}, \dots, X^K_{n + 1})] = g(X^1_n, \dots, X^K_n)
$$

we say that $\{(X^1_n, \dots, X_n^K);\quad n = 0, 1, \dots, N\}$ is a $K$-dimensional Markov process.

**Remark**: 
If $X_0, X_1, \dots, X_N$ is a Markov process and $n \le N - 2$, then the one-step ahead Markov property implies that for every function $h$, there is a function $f$ such that:

$$
\mathbb{E}_{n + 1}[h(X_{n + 2})] = f(X_{n + 1})
$$

Then we can take conditional expectations on both sides based on the information at time $n$, and using iterated conditioning, we get:

$$
\begin{align*}
\mathbb{E}_n [h(X_{n + 2})] &= \mathbb{E}_n \left[\mathbb{E}_{n + 1}[h(X_{n + 2})] \right] = \mathbb{E}_n [f(X_{n + 1})]\\
\mathbb{E}_n [h(X_{n + 2})] &= g(X_n)\\
\mathbb{E}_n [h(X_m)] &= g(X_n)\quad \text{for } 0 \le n \le m \le N
\end{align*}
$$

For our binomial pricing model suppose we have a Markov process $X_0, X_1, \dots, X_N$ under the risk-neutral probability measure $\tilde{\mathbb{P}}$ and we have a derivative security whose payoff $V_N$ at time $N$ is a function $v_N$ of $X_N$ i.e., $V_N = v_N(X_N)$. The difference between $V_N$ and $v_N$ is that the argument of the former sequence of coin tosses, whereas the argument of the latter is a real number. 

In place of $x$ we substitute the random variable $X_N$ to get:

$$
V_N(\omega_1 \dots \omega_N) = v_N(X_N(\omega_1 \dots \omega_N)) \text{ for al } \omega_1 \dots \omega_N
$$

Getting the risk-neutral pricing formula says that the price of this derivative security at earlier times $n$ is:

$$
\begin{align*}
V_n(\omega_1 \dots \omega_n) &= \tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^N - n} \right] (\omega_1 \dots \omega_n) \quad \text{for all } \omega_1 \dots \omega_n\\
\tilde{\mathbb{E}}_n \left[\frac{V_N}{(1 + r)^{N - n}} \right] &(\omega_1 \dots \omega_n) \\
&= v_n (X_n(\omega_1 \dots \omega_n)) \quad \text{ for all } \omega_1 \dots \omega_n
\end{align*}
$$

Thus we get that the price of the derivative security at time $n$ is a function of $X_n$:

$$
V_n = v_n(X_n)
$$

An $N$-period binomial model with derivative security whose payoff at time $N$ is a function $v_N(S_N, M_N)$ of the stock price and the maximum stock price. 

Take $V_N = (M_N - K)^{+}$. The stock price does not appear in $V_N$ we need to execute the pricing algorithm below because the maximum-to-date process is NOT Markov by itself. Thus, for any $n$ between $0$ and $N$, there is a non-random function $v_n(s, m)$ such that the price of the option at time $n$ is:

$$
V_n = v_n(S_n, M_n) = \tilde{\mathbb{E}}_n \left[\frac{v_N(S_N, M_N)}{(1 + r)^{N - n}} \right] \Longleftrightarrow V_n = \frac{1}{1 + r} \tilde{\mathbb{E}}_n [V_{n + 1}]
$$


$$
\begin{align*}
V_n &= \frac{1}{1 + r} \tilde{\mathbb{E}}_n [V_{n + 1}]\\
&= \frac{1}{1 + r} \tilde{\mathbb{E}}_n [v_{n + 1}(S_{n + 1}, M_{n + 1})]\\
&= \frac{1}{1 + r} \tilde{\mathbb{E}}_n \left[v_{n + 1} \left(S_n \cdot \frac{S_{n + 1}}{S_n}, M_n \vee \left(S_n \cdot \frac{S_{n + 1}}{S_n} \right) \right) \right]\\
\\
v_n(s, m) &= \frac{1}{1 + r} \tilde{\mathbb{E}}_n \left[v_{n + 1} \left(s \cdot \frac{S_{n + 1}}{S_n}, m \vee \left(s \cdot \frac{S_{n + 1}}{S_n} \right) \right) \right]\\
&= \frac{1}{1 + r} [\tilde{p} v_{n + 1} (us, m \vee (us)) + \tilde{q} v_{n + 1} (ds, m \vee (ds))]\\
&= \frac{1}{1 + r} [\tilde{p} v_{n + 1} (us, m \vee (us)) + \tilde{q} v_{n + 1}(ds, m)]
\end{align*}
$$


**Theorem**
Let $X_0, X_1, \dots, X_N$ be a Markov process under the risk-neutral probability measure $\tilde{\mathbb{P}}$ in the binomial model. Let $V_N(x)$ be a function of the dummy variable $x$ and consider a derivative security whose payoff at time $N$ is $v_N(X_N)$. Then for each $n$ between $0$ and $N$, the price $V_n$ of this derivative security is some function $v_n$ of $X_n$,

$$
V_n = v_n(X_n),\quad n = 0, 1, \dots, N
$$

There is a recursive algorithm for computing $v_n$ whose exact formula depends on the underlying Markov process $X_0, X_1, \dots, X_N$. Analogous results hold if the underlying Markov process is multi-dimensional.

### Summary of Key Results, Theorems, and Algorithms

#### Finite Probability Spaces
1. **Definition**: A finite probability space consists of:
   - **Sample Space** ($\Omega$): A finite set of outcomes.
   - **Probability Measure** ($\mathbb{P}$): Assigns probabilities to outcomes such that $\sum_{\omega \in \Omega} \mathbb{P}(\omega) = 1$.
2. **Probability of an Event**:
   
$$
   \mathbb{P}(A) = \sum_{\omega \in A} \mathbb{P}(\omega)
   $$

3. **Key Property**: For disjoint subsets $A, B \subseteq \Omega$:
   
$$
   \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)
   $$

4. **Expectation of a Random Variable**:
   
$$
   \mathbb{E}[X] = \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\omega)
   $$

5. **Variance**:
   
$$
   \text{Var}(X) = \mathbb{E}\left[(X - \mathbb{E}[X])^2\right]
   $$

6. **Jensen's Inequality**:
   For a convex function $\phi$ and random variable $X$:
   
$$
   \mathbb{E}[\phi(X)] \geq \phi(\mathbb{E}[X])
   $$


#### Conditional Expectations
1. **Conditional Expectation**:
$$
   \tilde{\mathbb{E}}_n[X] = \sum_{\omega_{n+1} \dots \omega_N} \tilde{p}^{\# H}\tilde{q}^{\# T} X(\omega_1 \dots \omega_N)
   $$

2. **Key Properties**:
   - **Linearity**: $\mathbb{E}_n[c_1X + c_2Y] = c_1\mathbb{E}_n[X] + c_2\mathbb{E}_n[Y]$
   - **Taking Out What is Known**: If $X$ depends only on the first $n$ coin tosses, $\mathbb{E}_n[XY] = X \cdot \mathbb{E}_n[Y]$.
   - **Iterated Conditioning**: $\mathbb{E}_n[\mathbb{E}_m[X]] = \mathbb{E}_n[X]$ for $n \leq m$.
   - **Independence**: If $X$ depends on tosses $n+1$ to $N$, $\mathbb{E}_n[X] = \mathbb{E}[X]$.
3. **Risk-Neutral Stock Pricing**:
$$
   S_n = \frac{1}{1 + r} \tilde{\mathbb{E}}_n[S_{n+1}]
   $$

#### Martingales
1. **Definition**:
   A process $M_n$ is a martingale if:
$$
   M_n = \mathbb{E}_n[M_{n+1}]
   $$

2. **Properties**:
   - Expectation of a martingale is constant over time: $\mathbb{E}[M_n] = M_0$.
   - Risk-neutral discounted stock price is a martingale:
$$
     \frac{S_n}{(1 + r)^n} = \tilde{\mathbb{E}}_n\left[\frac{S_{n+1}}{(1 + r)^{n+1}}\right]
     $$

3. **Wealth Process**:
$$
   X_{n+1} = \Delta_n S_{n+1} + (1 + r)(X_n - \Delta_n S_n)
   $$
The discounted wealth process is also a martingale.

4. **Risk-Neutral Pricing**:
$$
   V_n = \tilde{\mathbb{E}}_n\left[\frac{V_N}{(1 + r)^{N-n}}\right]
   $$

#### Markov Processes
1. **Definition**:
   A process $X_n$ is Markov if:
$$
   \mathbb{E}_n[f(X_{n+1})] = g(X_n)
   $$

2. **Stock Price**:
   The stock price process is Markov:
$$
   S_{n+1} =
   \begin{cases} 
   uS_n, & \text{if } \omega_{n+1} = H, \\
   dS_n, & \text{if } \omega_{n+1} = T.
   \end{cases}
   $$

3. **Pricing with Markov Processes**:
$$
   V_n = v_n(S_n)
   $$
where $v_n$ satisfies the recursive relation:
$$
   v_n(s) = \frac{1}{1 + r}[\tilde{p} v_{n+1}(us) + \tilde{q} v_{n+1}(ds)]
   $$

