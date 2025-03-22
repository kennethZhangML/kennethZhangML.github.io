---
layout: page
title: Chapter 4 - Stochastic Calculus
description: Notes on Brownian motion and its applications.
parent: course-2
importance: 6
permalink: /notes/course-2/chapter-4-stochastic-calculus/
nav: false
---

**Ito's Integral**
We fix a positive number $T$, and seek to interpret,

$$
\int_0^T \Delta(t) dW(t)
$$

where
- $W(t)$ is the Brownian motion
- $\mathcal{F}(t)$ is the filtration 
- and $\Delta(t)$ is the adapted stochastic process
	- note, this will eventually be the position we take in an asset at time $t$
	- and, depends on the price path of the asset up to time $t$
- $\Delta(t)$ is $\mathcal{F}(t)$ measurable, and thus, is independent of future Brownian increments that drives those prices 

**Constructing the Integral**
Let's start with the Ito integral for simple integrands $\Delta(t)$. We have our $\Pi$, partition, as defined in cases before of $[0, T]$ for $0 = t_0 < t_1 < \dots < t_n = T$. $\Delta(t)$ is constant in $t$ on each subinterval $[t_j, t_{j + 1})$. Thus, we define $\Delta(t)$ as the simple process.

For each $\omega$, assume that each sequence $\omega$ is different, there are different paths of a Brownian motion generated from choosing different $\omega$ sequences. However, since $\Delta(t)$ can only depend on the information available at time $t$, we know that $\Delta(0)$ must be the same for all paths. 

Let's interpret $t_0, t_1, \dots, t_{n - 1}$ as the trading dates in the asset, and think of $\Delta(t_0), \Delta(t_1), \dots, \Delta(t_{n - 1})$ as the position taken in the asset at each trading date held to the next trading date. Thus, the gain from trading at each $t$ is therefore given by,

$$
\begin{align*}
I(t) &= \Delta(t_0)[W(t) - W(t_0)] = \Delta(0)W(t),\quad 0 \le t \le t_1,\\
I(t) &= \Delta(0)W(t_1) + \Delta(t_1)[W(t) - W(t_1)],\quad t_1 \le t \le t_2,\\
I(t) &= \Delta(0)W(t_1) + \Delta(t_1)[W(t_2) - W(t_1)] + \Delta(t_2)[W(t) - W(t_2)],
\end{align*}
$$

Generally, we can write for $t_k \le t \le t_{k + 1}$, as,

$$
I(t) = \sum_{j = 0}^{k - 1} \Delta(t_j) [W(t_{j + 1}) - W(t_j)] + \Delta(t_k)[W(t) - W(t_k)] \implies I(t) = \int_0^t \Delta(u) dW(u)
$$

where $I(t)$ above is the Ito integral of the simple process $\Delta(t)$, which can be written as the integral on the very right hand side of the equation above. This is defined as the integral for not only the upper limit of integration $T$, but also for every upper limit of integration $t$ between $[0, T]$. 

**Properties of the Ito Integral**
Gains from trading in the martingale $W(t)$ have no tendency to rise or fall, and thus $I(t)$ also has no tendency to rise or fall as it is the upper limit of integration of $t$. 

**Theorem**
The Ito integral defined above is a martingale.

**Proof** 
We assume that $s$ and $t$ are in different subintervals of the partition $\Pi$ and assume that $t_l < t_k$ so for $s \in [t_l t_{l + 1})$ and $t \in [t_k, t_{k + 1})$. If $s = t$ then the proof is simplified. Generally, we can re-write,

$$
\begin{align*}
I(t) &= \sum_{.j = 0}^{l - 1} \Delta(t_j) [W(t_{j + 1}) - W(t_j)] + \Delta(t_l)[W(t_{l + 1}) - W(t_l)]\\
&+ \sum_{j = l + 1}^{k - 1}\Delta(t_j)[W(t_{j + 1}) - W(t_j)] + \Delta(t_k)[W(t) - W(t_k)]
\end{align*}
$$

Now, we must show that $\mathbb{E}[I(t) | \mathcal{F}(s)] = I(s)$ and take the conditional expectation of each of the four terms on the RHS. Every random variable in the first sum,

$$
\sum_{j = 0}^{l - 1} \Delta(t_j) [W(t_{j + 1}) - W(t_j)]
$$

which is $\mathcal{F}(s)$ measurable because the latest time appearing in this sum is $t_l$ and $t_l \le s$, thus,

$$
\mathbb{E} \left[\sum_{j = 0}^{l - 1} \Delta(t_j)[W(t_{j + 1}) - W(t_j)] | \mathcal{F}(s) \right] = \sum_{j = 0}^{l - 1} \Delta(t_j) [W(t_{j + 1}) - W(t_j)]
$$

We take out what is known and use the martingale property of $W$ to write,

$$
\begin{align*}
\mathbb{E}[\Delta(t_l) W(t_{l + 1}) - W(t_l) | \mathcal{F}(s)] &= \Delta(t_l) (\mathbb{E}[W(t_{l + 1}) | \mathcal{F}(s)] - W(t_l))\\
&= \Delta(t_l) (W(s) - W(t_l))
\end{align*}
$$

It remains to show that the conditional expectations of the third and fourth terms on the RHS are both zero. Then we have that $\mathbb{E}[I(t) | \mathcal{F}(s)] = I(s)$, since $\Delta(t_j) [W(t_{j + 1}) - W(t_j)]$ where $t_j \ge t_{l + 1} > s$ and use iterated conditioning trick to obtain,

$$
\begin{align}
    \mathbb{E} \left\{ \Delta(t_j) (W(t_{j+1}) - W(t_j)) \mid \mathcal{F}(s) \right\} 
    &= \mathbb{E} \left\{ \mathbb{E} \left[ \Delta(t_j) (W(t_{j+1}) - W(t_j)) \mid \mathcal{F}(t_j) \right] \mid \mathcal{F}(s) \right\} \\
    &= \mathbb{E} \left\{ \Delta(t_j) \left( \mathbb{E} [ W(t_{j+1}) \mid \mathcal{F}(t_j) ] - W(t_j) \right) \mid \mathcal{F}(s) \right\} \\
    &= \mathbb{E} \left\{ \Delta(t_j) (W(t_j) - W(t_j)) \mid \mathcal{F}(s) \right\} = 0.
\end{align}
$$

Thus, we have used the fact that $W$ is a martingale, and because of the conditional expectation of each of the summands in the third term of the RHS, is zero, the conditional expectation of the whole term is therefore zero,

$$
\mathbb{E} \left\{ \sum_{j=\ell+1}^{k-1} \Delta(t_j) \left[ W(t_{j+1}) - W(t_j) \right] \Bigg| \mathcal{F}(s) \right\} = 0.
$$

The fourth term on the RHS is treated like the summands in the third term with the result,

$$
\begin{align}
    \mathbb{E} \left\{ \Delta(t_k)(W(t) - W(t_k)) \mid \mathcal{F}(s) \right\} 
    &= \mathbb{E} \left\{ \mathbb{E} \left[ \Delta(t_k)(W(t) - W(t_k)) \mid \mathcal{F}(t_k) \right] \mid \mathcal{F}(s) \right\} \\
    &= \mathbb{E} \left\{ \Delta(t_k) \left( \mathbb{E} [ W(t) \mid \mathcal{F}(t_k) ] - W(t_k) \right) \mid \mathcal{F}(s) \right\} \\
    &= \mathbb{E} \left\{ \Delta(t_k) (W(t_k) - W(t_k)) \mid \mathcal{F}(s) \right\} = 0.
\end{align}
$$

Thus, this concludes the proof.
Because $I(t)$ is a martingale and $I(0) = 0$ we have $\mathbb{E}I(t) = 0$ for all $t \ge 0$ It follows that $Var I(t) = \mathbb{E} I^2(t)$, a quantity evaluated below.

---

**Theorem**
The Ito integral defined by the above, satisfies,

$$
\mathbb{E} I^2(t) = \mathbb{E} \int_0^t \Delta^2(u) du
$$

**Proof**
Set $D_j = W(t_{j + 1}) - W(t_j)$ for $j = 0, \dots, k - 1$ and $D_k = W(t) - W(t_k)$ so that we can write,

$$
I(t) = \sum_{j = 0}^k \Delta(t_j) D_j \implies I^2(t) = \sum_{j = 0}^{k} \Delta^2(t_j) D_j^2 + 2 \sum_{0 \le i < j \le k} \Delta(t_i) \Delta(t_j) D_i D_j
$$

We can first show that the expected value of each of the cross terms is 0. For $i < j$, the random variable $\Delta(t_i) \Delta(t_j) D_i$ is $\mathcal{F}(t_j)$-measurable, while the Brownian increment $D_j$ is independent of $\mathcal{F}(t_j)$. Moreover, we have $\mathbb{E}D_j = 0$, therefore we can write,

$$
\mathbb{E}[\Delta(t_i) \Delta(t_j) D_i D_j] = \mathbb{E}[\Delta(t_i)\Delta(t_j) D_i] \cdot \mathbb{E}D_j = \mathbb{E}[\Delta(t_i)\Delta(t_j) D_j] \cdot 0 = 0
$$

Consider $\Delta^2(t_j) D_j^2$, the random variable $\Delta^2(t_j)$ is $\mathcal{F}(t_j)$-measurable and the squared Brownian increment $D_j^2$ is independent of $\mathcal{F}(t_j)$. Furthermore, $\mathbb{E}D_j^2 = t_{j + 1} - t_j$ and $\mathbb{E}D_k^2 = t - t_k$. 

$$
\begin{align*}
\mathbb{E}I^2(t) &= \sum_{j = 0}^k \mathbb{E}[\Delta^2(t_j) D_j^2] = \sum_{j = 0}^k \mathbb{E}\Delta^2(t_j) \cdot \mathbb{E}D_j^2 \\
&= \sum_{j = 0}^{k - 1} \mathbb{E} \Delta^2(t_j) (t_{j + 1} - t_j) + \mathbb{E}\Delta^2(t_k)(t - t_k)
\end{align*}
$$

Since $\Delta(t_j)$ is constant on the interval $[t_j, t_{j + 1})$ and hence $\Delta^2(t_j)(t_{j + 1} - t_j) = \int_{t_j}^{t_{j + 1}} \Delta^2(u) du$. 

$$
\begin{align*}
\mathbb{E}I^2(t) &= \sum_{j = 0}^{k - 1} \mathbb{E} \int_{t_j}^{t_{j + 1}} \Delta^2(u) du + \mathbb{E}\int_{t_k}^t \Delta^2(u) du \\
&= \mathbb{E} \left[\sum_{j = 0}^{k - 1} \int_{t_j}^{t_{j+1}} \Delta^2(u) du + \int_{t_k}^{t} \Delta^2(u) du \right] = \mathbb{E}\int_0^t \Delta^2(u) du
\end{align*}
$$


---

**Theorem**
The quadratic variation accumulated up to time $t$ by the Ito integral, 

$$
[I, I](t) = \int_0^t \Delta^2(u) du
$$

The quadratic variation of the Ito integral $I(t)$ thought of as a process in its upper limit of integration $t$. The Brownian motion accumulated quadratic variation at rate one per unit time. However, the Brownian motion is scaled in a time and path-dependent way by the integrand $\Delta(u)$ as it enters the Ito integral $I(t) = \int_0^t \Delta(u) d B(u)$. Because increments are squared in the computation of QV, the QV of BM will be scaled by $\Delta^2(u)$ as it enters the Ito integral.

**Proof**
The quadratic variation accumulated by the Ito integral on $[t_j, t_{j + 1}]$ on which $\Delta(u)$ is constant,

$$
t_j = s_0 < s_1 < \dots < s_m = t_{j + 1}
$$

...


