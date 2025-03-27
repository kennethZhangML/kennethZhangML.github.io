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

where the above are the partition points we choose and consider the sum,

$$
\sum_{i = 0}^{m - 1}[I(s_{i + 1} - I(s_i))]^2 = \sum_{i = 0}^{m - 1} [\Delta(t_j)(W(s_{i + 1}) - W(s_i))]^2 = \Delta^2(t_j) \sum_{i = 0}^{m - 1} (W(s_{i + 1}) - W(s_i))^2
$$

The term $\sum_{i = 0}^{m - 1} (W(s_{i + 1}) - W(s_i))^2$ converges to the QV accumulated by the Brownian motion between $t_j$ and $t_{j + 1}$ which is simply $t_{j + 1} - t_j$. Thus, the limit of the QV accumulated by the integral between $t_j$ and $t_{j + 1}$ is given by,

$$
\Delta^(t_j) (t_{j + 1} - t_j) = \int_{t_j}^{t_{j + 1}} \Delta^2(u) du
$$

The QV accumulated by the Ito integral between $t_k$ and $t$ is,

$$
\int^t_{t_k} \Delta^2(u) du
$$

which is computed path-by-path and the result depends on the path. If we choose large positions $\Delta(u)$ the Ito integral will have a large QV. Otherwise, along a different path with smaller positions, then the Ito integral would have small QV. 

---

Recall, $dW(t) dW(t) = dt$ which can be interpreted as the BM accumulates QV at rate one per unit time. Another way of writing this is $[W, W](t) = t, \ge 0$. Given this, we can write the Ito integral in differential form,

$$
dI(t) = \Delta(t) dW(t) \implies dI(t) dI(t) = \Delta^2 (t) dW(t) dW(t) = \Delta^2(t) dt
$$

where, the notations below are equivalent,

$$
I(t) = \int_0^t \Delta(u) dW(u) \implies dI(t) = \Delta(t) dW(t)
$$

Integrating both sides, we must also add a constant of integration $I(0)$,

$$
I(t) = I(0) + \int_0^t \Delta(u) dW(u)
$$

---

**Ito's Integral for General Integrands**
Now, we allow the Ito integral $\int_0^T \Delta(t) dW(t)$ for integrands $\Delta(t)$ to vary continuously with time and also jump, thus not being a simple process anymore. Moreover, we assume the square-integrability condition, given by,

$$
\mathbb{E} \int_0^T \Delta^(t) dt < \infty
$$

Thus, we hold the simple process constant over the subinterval $[t_j, t_{j + 1})$, so as the max step size of the partition approaches zero, the approximating integral will become a better and better approximation of the continuously varying one, 

More generally, we choose a sequence $\Delta_n(t)$ of simple processes, that is as $n \rightarrow \infty$, these processes converge to the continuously varying $\Delta(t)$ meaning that,

$$
\lim_{n \rightarrow \infty} \mathbb{E} \int_0^T |\Delta_n(t) - \Delta(t)|^2 dt = 0
$$

So, for each $\Delta_n(t)$ the Ito integral $\int_0^t \Delta_n(u) dW(u)$ has already been defined for $0 \le t \le T$ and we define the Ito integral for the continuously varying integrand $\Delta(t)$ by the formula,

$$
\int_0^t \Delta(u)dW(u) = \lim_{n \rightarrow \infty} \int_0^t \Delta_n(u) dW(u),\quad 0 \le t \le T
$$

**Properties of the Ito Integral**
1. Continuity, as a function of the upper limit of integration $t$, the paths of $I(t)$ are continuous
2. Adaptivity, for each $t$, $I(t)$ is $\mathcal{F}(t)$-measurable
3. Linearity, If $I(t) = \int_0^t \Delta(u) dW(u)$ and $J(t) = \int_0^t \Gamma(u) dW(u)$ then,
	- $I(t) \pm J(t) = \int_0^t (\Delta(u) \pm \Gamma(u)) dW(u)$ 
	- $cI(t) = \int_0^t c \Delta(u) dW(u)$
4. Martingale, $I(t)$ is a martingale 
5. Ito Isometry, $\mathbb{E}I^2(t) = \mathbb{E} \int_0^t \Delta^2(u) du$ 
6. Quadratic Variation, $[I, I](t) = \int_0^t \Delta^2(u) du$

---

e.g., Let's take $\int_0^T W(t) dW(t)$, so we choose large integer $n$ approximating the integrand,

$$
\Delta(t) = W(t)
$$

by simple processes,

$$
\Delta_n(t) = \begin{cases}
W(0) = 0\quad &\text{if } 0 \le t < \frac{T}{n},\\
W\left(\frac{T}{n}\right)\quad &\text{if } \frac{T}{n} \le t < \frac{2T}{n}\\
\vdots\\
W \left(\frac{(n - 1)T}{n} \right)\quad &\text{if } \frac{(n - 1)T}{n} \le t < T
\end{cases}
$$

Thus, when $\lim_{n \rightarrow \infty} \mathbb{E} \int_0^T |\Delta_n(t) - \Delta(t)|^2 dt = 0$, by definition we have,

$$
\begin{align*}
\int_0^T W(t) \, dW(t) &= \lim_{n \rightarrow \infty} \int_0^T \Delta_n(t) \, dW(t) \\
&= \lim_{n \rightarrow \infty} \sum_{j = 0}^{n - 1} W \left( \frac{jT}{n} \right) \left[ W \left( \frac{(j + 1)T}{n} \right) - W \left( \frac{jT}{n} \right) \right]
\end{align*}
$$

Denote $W_j = W \left(\frac{jT}{n} \right)$,

$$
\begin{align*}
\frac{1}{2} \sum_{j=0}^{n-1} (W_{j+1} - W_j)^2 
&= \frac{1}{2} \sum_{j=0}^{n-1} W_{j+1}^2 - \sum_{j=0}^{n-1} W_j W_{j+1} + \frac{1}{2} \sum_{j=0}^{n-1} W_j^2 \\
&= \frac{1}{2} \sum_{k=1}^{n} W_k^2 - \sum_{j=0}^{n-1} W_j W_{j+1} + \frac{1}{2} \sum_{j=0}^{n-1} W_j^2 \\
&= \frac{1}{2} W_n^2 + \frac{1}{2} \sum_{k=0}^{n-1} W_k^2 - \sum_{j=0}^{n-1} W_j W_{j+1} + \frac{1}{2} \sum_{j=0}^{n-1} W_j^2 \\
&= \frac{1}{2} W_n^2 + \sum_{j=0}^{n-1} W_j^2 - \sum_{j=0}^{n-1} W_j W_{j+1} \\
&= \frac{1}{2} W_n^2 + \sum_{j=0}^{n-1} W_j (W_j - W_{j+1}).
\end{align*}
$$

which gives us,

$$
\sum_{j = 0}^{n - 1} W_j (W_{j + 1} - W_j) = \frac{1}{2} W_n^2 - \frac{1}{2} \sum_{j = 0}^{n - 1} (W_{j + 1} - W_j)^2
$$

given in the original notation as the following,

$$
\sum_{j = 0}^{n - 1} W \left(\frac{jT}{n} \right) \left[W \left(\frac{(j + 1)T}{n} - W \left( \frac{jT}{n}\right) \right) \right] = \frac{1}{2} W^2(T) - \frac{1}{2} \sum_{j = 0}^{n - 1} \left[W \left(\frac{(j + 1)T}{n} \right) - W \left(\frac{jT}{n} \right)  \right]^2
$$

Letting $n \rightarrow \infty$ and using this equation will give us,

$$
\int_0^T W(t) dW(t) = \frac{1}{2} W^2(T) - \frac{1}{2} [W, W](T) = \frac{1}{2}W^2(T) - \frac{1}{2}T
$$

---

**Ito-Doeblin Formula**
Because $W$ has non-zero quadratic variation, the correct formula has an extra term named,

$$
df(W(t)) = f'(W(t))dW(t) + \frac{1}{2} f''(W(t)) dt
$$

We call this the Ito-Doeblin formula in differential form, which, after integrating, gives us the Ito-Doeblin formula in integral form,

$$
f(W(t)) - f(W(0)) = \int_0^t f'(W(u))dW(u) + \frac{1}{2} \int_0^t f''(W(u)) du
$$

$df(W(t))$ essentially means the change in $f(W(t))$ when $t$ changes a little bit $dt$ and $dW(t)$ is the change in the Brownian motion when $t$ changes a little bit $dt$ and the whole formula is exact only when the little bit is infinitesimally small. 

**Theorem**
Let $f(t, x)$ be a function for which the partial derivative $f_t(t, x)$, $f_x(t, x)$ and $f_{xx}(t, x)$ are defined and continuous and let $W(t)$ be the Brownian motion, then for every $T \ge 0$, we get,

$$
\begin{align*}
f(T, W(T)) &= f(0, W(0)) + \int_0^T f_t(t, W(t))dt\\
&+ \int_0^T f_x(t, W(t))dW(t) + \frac{1}{2}\int_0^T f_{xx}(t, W(t)) dt
\end{align*}
$$

**Proof**
We show that for $x_{j + 1}$ and $x_j$ the Taylor's formula implies that,

$$
f(x_{j + 1}) - f(x_j) = f'(x_j)(x_{j + 1} - x_j) + \frac{1}{2}f''(x_j)(x_{j + 1} - x_{j})^2
$$

The Taylor's formula to second order is exact, because $f'''$ and all higher derivatives of $f$ are zero. Thus, now we fix $T > 0$ and have $\Pi$ be a partition of $[0, T]$ and are interested in the difference given by $f(W(0))$ and $f(W(T))$. This change in $f(W(t))$ between $t = 0$ and $t = T$ can be written as the sum of the changes in $f(W(t))$ over each of the sub-intervals $[t_j, t_{j + 1}]$. We do this and then use Taylor's formula with $x_j = W(t_j)$ and $x_{j + 1} = W(t_{j + 1})$ to obtain,

$$
\begin{align*}
f(W(T)) - f(W(0)) &= \sum_{j = 0}^{n - 1} [f(W(t_{j + 1})) - f(W(t_j))] \\
&= \sum_{j = 0}^{n - 1} f'(W(t_j))[W(t_{j + 1}) - W(t_j)] \\
&+ \sum_{j = 0}^{n - 1} f''(W(t_j)) [W(t_{j + 1}) - W(t_j)]^2
\end{align*}
$$

For the function $f(x) = \frac{1}{2} x^2$ the RHS of the above gives,

$$
\sum_{j = 0}^{n - 1} W(t_j) [W(t_{j + 1}) - W(t_j)] + \frac{1}{2} \sum_{j =0}^{n - 1} [W(t_{j + 1}) - W(t_j)]^2
$$

If we let $||\Pi|| \rightarrow 0$, the LHS is unaffected and the terms on the RHS converge to an Ito integral and one half of the QV of the Brownian motion, respectively,

$$
\begin{align*}
f(W(T)) - f(W(0))&\\
&= \lim_{||\Pi|| \rightarrow 0}\sum_{j = 0}^{n - 1} W(t_j)[W(t_{j + 1}) - W(t_j)] + \lim_{||\Pi|| \rightarrow 0} \frac{1}{2} \sum_{j = 0}^{n - 1} [W(t_{j + 1}) - W(t_j)]^2 \\
&= \int_0^T W(t) dW(t) + \frac{1}{2} T\\
&= \int_0^T f'(W(t)) dW(t) + \frac{1}{2} \int_0^T f''(W(t)) dt
\end{align*}
$$

which is the Ito-Doeblin formula in integral form for the function $f(x) = \frac{1}{2}x^2$.  The term $\sum_{j = 0}^{n - 1} |W(t_{j + 1}) - W(t_j)|^2$ contributes nothing to the final answer as it has limit 0 and $||\Pi || \rightarrow 0$. 

Similarly, if we have the following Taylor expansion,

$$
\begin{align*}
f(t_{j+1}, x_{j+1}) - f(t_j, x_j)
&= f_t(t_j, x_j)(t_{j+1} - t_j) + f_x(t_j, x_j)(x_{j+1} - x_j) \\
&= \frac{1}{2} f_{xx}(t_j, x_j)(x_{j+1} - x_j)^2 + f_x(t_j, x_j)(t_{j+1} - t_j)(x_{j+1} - x_j) \\
&\quad + \frac{1}{2} f_{tt}(t_j, x_j)(t_{j+1} - t_j)^2 + \text{higher-order terms.}
\end{align*}
$$

we can replace $x_j$ by $W(t_j)$ and replace $x_{j + 1}$ by $W(t_{j + 1})$,

$$
\begin{align*}
f(T, W(T)) - f(0, W(0)) 
&= \sum_{j=0}^{n-1} \left[ f(t_{j+1}, W(t_{j+1})) - f(t_j, W(t_j)) \right] \\
&= \sum_{j=0}^{n-1} f_t(t_j, W(t_j))(t_{j+1} - t_j) + \sum_{j=0}^{n-1} f_x(t_j, W(t_j))(W(t_{j+1}) - W(t_j)) \\
&\quad + \frac{1}{2} \sum_{j=0}^{n-1} f_{xx}(t_j, W(t_j))(W(t_{j+1}) - W(t_j))^2 \\
&\quad + \sum_{j=0}^{n-1} f_{tx}(t_j, W(t_j))(t_{j+1} - t_j)(W(t_{j+1}) - W(t_j)) \\
&\quad + \frac{1}{2} \sum_{j=0}^{n-1} f_{tt}(t_j, W(t_j))(t_{j+1} - t_j)^2 + \text{higher-order terms.}
\end{align*}
$$

When we take the limit as $||\Pi||\rightarrow 0$ the LHS is unaffected. Thus, the first term on the RHS contributes the ordinary Lebesgue integral,

$$
\lim_{||\Pi|| \rightarrow 0} \sum_{j = 0}^{n - 1} f_t(t_j, W(t_j)) (t_{j + 1} - t_j) = \int_0^T f_t(t, W(t)) dt
$$

The limits of the first three terms appear on the RHS, however the fourth and fifth terms contribute 0, as we can see below,

$$
\begin{align*}
\lim_{\|\Pi\| \to 0} &\left| \sum_{j=0}^{n-1} f_{tx}(t_j, W(t_j))(t_{j+1} - t_j)(W(t_{j+1}) - W(t_j)) \right| \\
&\leq \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1} |f_{tx}(t_j, W(t_j))| \cdot (t_{j+1} - t_j) \cdot |W(t_{j+1}) - W(t_j)| \\
&\leq \lim_{\|\Pi\| \to 0} \max_{0 \leq k \leq n-1} |W(t_{k+1}) - W(t_k)| \cdot \sum_{j=0}^{n-1} |f_{tx}(t_j, W(t_j))| (t_{j+1} - t_j) \\
&= 0 \cdot \int_0^T |f_{tx}(t, W(t))| dt = 0.
\end{align*}
$$

as well as,

$$
\begin{align*}
\lim_{\|\Pi\| \to 0} \left| \frac{1}{2} \sum_{j=0}^{n-1} f_{tt}(t_j, W(t_j))(t_{j+1} - t_j)^2 \right|
&\leq \frac{1}{2} \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1} |f_{tt}(t_j, W(t_j))| (t_{j+1} - t_j)^2 \\
&\leq \frac{1}{2} \cdot \lim_{\|\Pi\| \to 0} \max_{0 \leq k \leq n-1} (t_{k+1} - t_k) \cdot \sum_{j=0}^{n-1} |f_{tt}(t_j, W(t_j))| (t_{j+1} - t_j) \\
&= \frac{1}{2} \cdot 0 \cdot \int_0^T |f_{tt}(t, W(t))| dt = 0.
\end{align*}
$$

**Remark**
The sum of the terms above containing the product $(t_{j + 1} - t_j)(W(t_{j + 1}) - W(t_j))$ has limit 0 can be informally recorded by the formula $dt dW(t) = 0$. Similarly, the sum of terms containing $(t_{j + 1} - t_j)^2$ also has limit 0, and can be recorded by the formula $dt dt = 0$, thus, we can write the terms in Ito-Doeblin formula so that in differential form we get,

$$
\begin{align*}
df(t, W(t)) &= f_t(t, W(t))\, dt + f_x(t, W(t))\, dW(t) + \frac{1}{2} f_{xx}(t, W(t))\, dW(t)\, dW(t) \\
&= f_{tx}(t, W(t))\, dt\, dW(t) + \frac{1}{2} f_{tt}(t, W(t))\, dt\, dt,
\end{align*}
$$

which in the Ito-Doeblin formula in differential form simplifies to,

$$
\begin{align*}
df(t, W(t)) = f_t(t, W(t))\, dt + f_x(t, W(t))\, dW(t) + \frac{1}{2} f_{xx}(t, W(t))\, dt
\end{align*}
$$

given,

$$
\begin{align*}
dW(t)\, dW(t) = dt, \quad dt\, dW(t) = dW(t)\, dt = 0, \quad dt\, dt = 0
\end{align*}
$$

---

**Formula for Ito Processes**
Processes for which we develop stochastic calculus are the Ito processes defined below. Almost all stochastic processes except those with jumps are called Ito processes.

**Definition**
For $W(t)$ for $t \ge 0$, a Brownian motion, and $\mathcal{F}(t)$ be the filtration for which it is associated with, an Ito process is a stochastic process of the form,

$$
X(t) = X(0) + \int_0^t \Delta(u) dW(u) + \int_0^t \Theta (u) du
$$

where $X(0)$ is non-random and $\Delta(u)$ and $\Theta(u)$ are adapted stochastic processes. We understand the volatility associated with Ito processes by determining the rate at which they accumulate quadratic variation. Think of an Ito process has having a deterministic constant term, plus two adapted terms that are stochastic processes. 

**Lemma**
The quadratic variation of the Ito process is given by,

$$
[X, X](t) = \int_0^t \Delta^2(u) du
$$

**Proof**
We denote the following,

$$
I(t) = \int_0^t \Delta(u) dW(u),\quad R(t) = \int_0^t \Theta(u) du
$$

Both are continuous processes in their upper limit of integration $t$, so we determine the quadratic variation of $X$ on $[0, t]$ by choosing $\Pi$ of $[0, t]$, and write the sampled QV as,

$$
\begin{align*}
\sum_{j=0}^{n-1} \left[ X(t_{j+1}) - X(t_j) \right]^2 
&= \sum_{j=0}^{n-1} \left[ I(t_{j+1}) - I(t_j) \right]^2 + \sum_{j=0}^{n-1} \left[ R(t_{j+1}) - R(t_j) \right]^2 \\
&\quad + 2 \sum_{j=0}^{n-1} \left[ I(t_{j+1}) - I(t_j) \right] \left[ R(t_{j+1}) - R(t_j) \right].
\end{align*}
$$

As the partition approaches 0, the first term on the RHS converges to the QV of $I$ on $[0, t]$ which is $[I, I](t) = \int_0^t \Delta^2(u) du$ so, the absolute value of the 2nd term is bounded above by,

$$
\begin{align*}
\max_{0 \leq k \leq n-1} |R(t_{k+1}) - R(t_k)| \cdot \sum_{j=0}^{n-1} |R(t_{j+1}) - R(t_j)| 
&= \max_{0 \leq k \leq n-1} |R(t_{k+1}) - R(t_k)| \cdot \sum_{j=0}^{n-1} \left| \int_{t_j}^{t_{j+1}} \Theta(u) du \right| \\
&\leq \max_{0 \leq k \leq n-1} |R(t_{k+1}) - R(t_k)| \cdot \sum_{j=0}^{n-1} \int_{t_j}^{t_{j+1}} |\Theta(u)| du \\
&= \max_{0 \leq k \leq n-1} |R(t_{k+1}) - R(t_k)| \cdot \int_{0}^{t} |\Theta(u)| du.
\end{align*}
$$

which, as the partition approaches 0, this limit has limit 0 since $R(t)$ is continuous. Thus the absolute value of the third term is bounded above by,

$$
\begin{align*}
2 \max_{0 \leq k \leq n-1} |I(t_{k+1}) - I(t_k)| &\cdot \sum_{j=0}^{n-1} |R(t_{j+1}) - R(t_j)| \\
&\leq \max_{0 \leq k \leq n-1} |R(t_{k+1}) - R(t_k)| \cdot \sum_{j=0}^{n-1} |R(t_{j+1}) - R(t_j)| \cdot \int_{0}^{t} |\Theta(u)| du.
\end{align*}
$$

The highlight of this lemma is noted by first writing the differential notation,

$$
\begin{align*}
dX(t) &= \Delta(t) dW(t) + \Theta(t) dt \tag{4.4.18} \\
dX(t) dX(t) &= \Delta^2(t) dW(t) dW(t) + 2 \Delta(t) \Theta(t) dW(t) dt + \Theta^2(t) dt dt \\
&= \Delta^2(t) dt. \tag{4.4.19}
\end{align*}
$$

which tells us that at each time $t$, the process $X$ is accumulating quadratic variation at rate $\Delta^2(t)$ per unit time and thus the total QV accumulated on $[0, t]$ is,

$$
[X, X](t) = \int_0^t \Delta^2(u) du
$$

---

**Definition**
$X(t)$ is a Ito process and $\Gamma(t)$ for $t \ge 0$ is an adapted process. We define the integral with respect to an Ito process as the following,

$$
\int_0^t \Gamma(u) dX(u) = \int_0^t \Gamma(u) \Delta(u) dW(u) + \int_0^t \Gamma(u) \Theta(u) du
$$

**Proof**
The proof of this follows by replacing $X(t)$ with the Brownian motion $W(t)$ making it more interpretable. Here, we have the following sum with higher order terms,

$$
\begin{align*}
f(T, X(T)) - f(0, X(0)) 
&= \sum_{j=0}^{n-1} f_t(t_j, X(t_j))(t_{j+1} - t_j) + \sum_{j=0}^{n-1} f_x(t_j, X(t_j))\left( X(t_{j+1}) - X(t_j) \right) \\
&\quad + \frac{1}{2} \sum_{j=0}^{n-1} f_{xx}(t_j, X(t_j)) \left( X(t_{j+1}) - X(t_j) \right)^2 \\
&\quad + \sum_{j=0}^{n-1} f_{tx}(t_j, X(t_j)) (t_{j+1} - t_j) \left( X(t_{j+1}) - X(t_j) \right) \\
&\quad + \frac{1}{2} \sum_{j=0}^{n-1} f_{tt}(t_j, X(t_j))(t_{j+1} - t_j)^2 + \text{higher-order terms.}
\end{align*}
$$

where, notice that the last two sums have zero limits as our partition approaches zero for the same reasons analogous with the proof of the previous theorem. We can see that the limit of the second term can decompose $dX(t)$ into its adapted $\Delta(t)$ and $\Theta(t)$ terms to get,

$$
\int_0^T f_x(t, X(t)) dX(t) = \int_0^T f_x(t, X(t)) \Delta(t) dW(t) + \int_0^T f_x(t, X(t)) \Theta(t) dt
$$

and the limit of the third term using the fact that $X(t)$ accumulates QV at rate $\Delta^2(t)$ we get,

$$
\frac{1}{2} \int_0^T f_{xx}(t, X(t)) d[X, X](t) = \frac{1}{2}\int_0^T f_{xx}(t, X(t)) \Delta^2(t) dt
$$

---

**Theorem**
For $X(t)$, an Ito process, and $f(t, x)$ be a function for which the partial derivatives $f_t(t, x), f_x(t, x)$ and $f_{xx}(t, x)$ are defined and continuous. Then, for every $T \ge 0$, we get that,

$$
\begin{align*}
f(T, X(T)) &= f(0, X(0)) + \int_0^T f_t(t, X(t))\, dt + \int_0^T f_x(t, X(t))\, dX(t) \\
&\quad + \frac{1}{2} \int_0^T f_{xx}(t, X(t))\, d[X, X](t) \\
&= f(0, X(0)) + \int_0^T f_t(t, X(t))\, dt + \int_0^T f_x(t, X(t))\, \Delta(t)\, dW(t) \\
&\quad + \int_0^T f_x(t, X(t))\, \Theta(t)\, dt + \frac{1}{2} \int_0^T f_{xx}(t, X(t))\, \Delta^2(t)\, dt.
\end{align*}
$$

notice that $f(T, X(T))$ contains a deterministic component still $f(0, X(0))$ and it's 4th term uses the fact that the Ito integral accumulates QV at rate $\Delta^2(t)$. Which might be re-written as,

$$
df(t, X(t)) = f_t(t, X(t))dt + f_x(t, X(t))dX(t) + \frac{1}{2}f_{xx}(t, X(t))dX(t)dX(t)
$$

The guiding principle here is that we write out the Taylor series expansion of $f(t, X(t))$ with respect to all its arguments which are in this case $t$ and $X(t)$. Thus, we take this Taylor series expansion out to the first order for every argument that has zero QV which is in this case $t$ and take the expansion out to second order for every argument that has non-zero QV which is $X(t)$.

Alternatively, we can make explicit definitions and substitutions for,

$$
dX(t) = \Delta(t)dW(t) + \Theta(t)dt \quad\text{and}\quad dX(t) dX(t) = \Delta^2(t) dt
$$

giving us the differential equation as such,

$$
df(t, X(t)) = f_t(t, X(t))dt + f_x(t, X(t))\Delta(t) dW(t) + f_x(t, X(t))\Theta(t) dt + \frac{1}{2}f_{xx}(t, X(t)) \Delta^2(t) dt
$$

---

e.g., Generalized Geometric Brownian Motion
$W(t)$ for $t \ge 0$ is a Brownian motion, and let $\mathcal{F}(t)$ for $t \ge 0$ be an associated filtration, and let $\alpha(t), \sigma(t)$ be adapted stochastic processes, then we define the Ito process,

$$
X(t) = \int_0^t \sigma(s) dW(s) + \int_0^t \left(\alpha(s) - \frac{1}{2} \sigma^2(s) \right) ds
$$

Or, in differential form, we can write this process as,

$$
dX(t) = \sigma(t) dW(t) + \left(\alpha(t) - \frac{1}{2} \sigma^2(t) \right) dt
$$

which also gives,

$$
dX(t) dX(t) = \sigma^2(t) dW(t) dW(t) = \sigma^2(t) dt
$$

Consider the asset price process given by,

$$
S(t) = S(0)e^{X(t)} = S(0) \exp \left\{\int_0^t \sigma(s) dW(s) + \int_0^t \left(\alpha(s) - \frac{1}{2}\sigma^2(s)ds \right) \right\}
$$

where $S(0)$ is non-random and positive, and we may write that $S(t) = f(X(t))$ where all the derivatives are equal to $S(0)e^x$, so by the Ito-Doeblin formula, we have,

$$
\begin{align*}
dS(t) &= df\left( X(t) \right) \\
&= f'\left( X(t) \right) dX(t) + \frac{1}{2} f''\left( X(t) \right) dX(t) dX(t) \\
&= S(0) e^{X(t)} dX(t) + \frac{1}{2} S(0) e^{X(t)} dX(t) dX(t) \\
&= S(t) dX(t) + \frac{1}{2} S(t) dX(t) dX(t) \\
&= \alpha(t) S(t) dt + \sigma(t) S(t) dW(t).
\end{align*}
$$

Thus, $S(t)$ has instantaneous mean rate of return $\alpha(t)$ and volatility $\sigma(t)$. Both the instantaneous mean rate of return and the volatility are allowed to be time-varying and random.
However, $S(t)$ need not be distributed log-normal because $\sigma(t), \alpha(t)$ are allowed to be time-varying and random. Constant $\alpha, \sigma$ yield,

$$
S(t) = S(0) \exp \left\{\sigma W(t) + \left(\alpha - \frac{1}{2}\sigma^2 \right) t \right\}
$$

$S(t)$ after adding $\alpha t$ to the exponential and subtract $\frac{1}{2} \sigma^2 t$ in the exponential the process $S(t)$ is now a martingale with a mean rate of return $\alpha$. 

If $\alpha = 0$, we get $dS(t) = \sigma(t) S(t) dW(t)$ and integration of both sides gives,

$$
S(t) = S(0) + \int_0^t \sigma(s) S(s) dW(s) \implies S(t) = S(0) \exp \left\{ \int_0^t \sigma(s) dW(s) - \frac{1}{2} \sigma^2(s) ds \right\}
$$

where the RHS is the non-random constant $S(0)$ plus an Ito integral which is a martingale and thus in the case of $\alpha = 0$, gives the result above. Therefore, the $\sigma(t) S(t) dW(t)$ on the RHS of the application of the Ito-Doeblin formula for $dS(t)$ contributes no drift and just pure volatility to the asset price. So, we conclude that: 
1. When $\alpha(t)$ is a non-zero random process, it plays the role of the mean rate of return. 
2. In the case of the time-varying and random $\alpha(t)$, we call this the instantaneous mean rate of return since it depends on the time and the sample path where it's evaluated. 

---

**Theorem**
$W(s)$ for $s \ge 0$ is a Brownian motion and $\Delta(s)$ is a non-random function of time. We define,

$$
I(t) = \int_0^t \Delta(s) dW(s)
$$

For each $t \ge 0$ the random variable $I(t)$ is normally distributed with expected value zero and variance given by the following:

$$
\int_0^t \Delta^2(s) ds
$$

**Proof**
The mean and variance of $I(t)$ are easy to determine. $I(t)$ is a martingale and $I(0) = 0$ so we must have that $\mathbb{E} I(t) = I(0) = 0$. By Ito isometry, we are given,

$$
Var I(t) = \mathbb{E} I^2(t) = \int_0^t \Delta^2(s) ds
$$

We need not take the expected value of $\int_0^t \Delta^2(s) ds$ on the RHS because $\Delta(s)$ is not random. So the challenge is to show that $I(t)$ is normally distributed, which can be done by showing that $I(t)$ has a moment-generating function of a normal random variable with mean zero and variance $\int_0^t \Delta^2(s) ds$, thus we can write,

$$
\mathbb{E} e^{uI(t)} = \exp \left\{\frac{1}{2} u^2 \int_0^t \Delta^2(s) ds \right\}\quad \text{for all }u \in \mathbb{R}
$$

Because $\Delta(s)$ is non-random, we can write the above as,

$$
\begin{align*}
\mathbb{E} e^{u I(t)} = \exp\left\{ \frac{1}{2} u^2 \int_0^t \Delta^2(s) ds \right\} \quad \text{for all } u \in \mathbb{R} \tag{4.4.30} \\
\implies \mathbb{E} \exp\left\{ u I(t) - \frac{1}{2} u^2 \int_0^t \Delta^2(s) ds \right\} &= 1 \\
\implies \mathbb{E} \exp\left\{ \int_0^t u \Delta(s) dW(s) - \frac{1}{2} \int_0^t \left( u \Delta(s) \right)^2 ds \right\} &= 1 \tag{4.4.31} \\
\implies \exp\left\{ \int_0^t u \Delta(s) dW(s) - \frac{1}{2} \int_0^t \left( u \Delta(s) \right)^2 ds \right\} &\text{ is a martingale.}
\end{align*}
$$

Thus, this is the generalized geometric Brownian motion with mean rate of return $\alpha = 0$ with $\sigma = u\Delta(s)$, and takes value $1$ at time $0$ with expectation always $1$. 

---

e.g., The Vasicek model for the interest rate process $R(t)$ is

$$
\begin{align}
dR(t) = (\alpha - \beta R(t)) dt + \sigma dW(t), \tag{4.4.32}
\end{align}
$$

where $\alpha$, $\beta$, and $\sigma$ are positive constants. Equation (4.4.32) is an example of a stochastic differential equation. It defines a random process, $R(t)$ in this case, by giving a formula for its differential, and the formula involves the random process itself and the differential of a Brownian motion. The solution to the stochastic differential equation (4.4.32) can be determined in closed form and is given by the following,

$$
\begin{align}
R(t) = e^{-\beta t} R(0) + \frac{\alpha}{\beta} (1 - e^{-\beta t}) + \sigma e^{-\beta t} \int_0^t e^{\beta s} dW(s), \tag{4.4.33}
\end{align}
$$

a claim that we now verify. In particular, we compute the differential of the right-hand side of (4.4.33). To do this, we use the Ito-Doeblin formula with

$$
\begin{align}
f(t, x) = e^{-\beta t} R(0) + \frac{\alpha}{\beta} (1 - e^{-\beta t}) + \sigma e^{-\beta t} x
\end{align}
$$



$$
\begin{align}
X(t) = \int_0^t e^{\beta s} dW(s).
\end{align}
$$

Then the right-hand side of (4.4.33) is $f(t, X(t))$. The technique we are using is to separate the right-hand side into two parts: an ordinary function of two variables $t$ and $x$, which has no randomness in it, and an Ito process $X(t)$, which contains all the randomness. For the Ito-Doeblin formula, we shall need the following partial derivatives of $f(t, x)$:

$$
\begin{align}
f_t(t, x) &= -\beta e^{-\beta t} R(0) + \alpha e^{-\beta t} - \sigma \beta e^{-\beta t} x = \alpha - \beta f(t, x) \\
f_x(t, x) &= \sigma e^{-\beta t} \\
f_{xx}(t, x) &= 0.
\end{align}
$$

We shall also need the differential of $X(t)$, which is

$$
\begin{align}
dX(t) = e^{\beta t} dW(t).
\end{align}
$$

We shall not need $dX(t) dX(t)$ because $f_{xx}(t, x) = 0$. The Itô-Doeblin formula states that

$$
\begin{align}
df(t, X(t)) &= f_t(t, X(t)) dt + f_x(t, X(t)) dX(t) + \frac{1}{2} f_{xx}(t, X(t)) dX(t) dX(t) \\
&= (\alpha - \beta f(t, X(t))) dt + \sigma dW(t).
\end{align}
$$

This shows that $f(t, X(t))$ satisfies the stochastic differential equation (4.4.32) that defines $R(t)$. Moreover, $f(0, X(0)) = R(0)$. Because $f(t, X(t))$ satisfies the equation defining $R(t)$ and has the same initial condition as $R(t)$, it must be the case that $f(t, X(t)) = R(t)$ for all $t \geq 0$.

Theorem 4.4.9 implies that the random variable $\int_0^t e^{\beta s} dW(s)$ appearing on the right-hand side of (4.4.33) is normally distributed with mean zero and variance

$$
\begin{align}
\int_0^t e^{2\beta s} ds = \frac{1}{2\beta} (e^{2\beta t} - 1).
\end{align}
$$

Therefore, $R(t)$ is normally distributed with mean $e^{-\beta t} R(0) + \frac{\alpha}{\beta} (1 - e^{-\beta t})$ and variance $\frac{\sigma^2}{2\beta} (1 - e^{-2\beta t})$. In particular, no matter how the parameters $\alpha > 0$, $\beta > 0$, and $\sigma > 0$ are chosen, there is positive probability that $R(t)$ is negative, an undesirable property for an interest rate model.

The Vasicek model has the desirable property that the interest rate is mean-reverting. When $R(t) = \frac{\alpha}{\beta}$, the drift term (the $dt$ term) in (4.4.32) is zero. When $R(t) > \frac{\alpha}{\beta}$, this term is negative, which pushes $R(t)$ back toward $\frac{\alpha}{\beta}$. When $R(t) < \frac{\alpha}{\beta}$, this term is positive, which again pushes $R(t)$ back toward $\frac{\alpha}{\beta}$. If $R(0) = \frac{\alpha}{\beta}$, then $\mathbb{E}[R(t)] = \frac{\alpha}{\beta}$ for all $t \geq 0$. If $R(0) \neq \frac{\alpha}{\beta}$, then $\lim_{t \to \infty} R(t) = \frac{\alpha}{\beta}$.

**Comments**
- This example introduces the **Vasicek model**, a classic mean-reverting model for interest rates.
- The SDE $dR(t) = (\alpha - \beta R(t)) dt + \sigma dW(t)$ has a **drift** driving $R(t)$ toward the long-term mean $\frac{\alpha}{\beta}$ and a **diffusion** term adding randomness.
- The closed-form solution for $R(t)$ decomposes into deterministic and stochastic parts via the integrating factor method.
- The Itô-Doeblin formula is used to rigorously verify the closed-form solution.
- **Mean-reversion:** If $R(t) > \frac{\alpha}{\beta}$, $R(t)$ is pushed down; if $R(t) < \frac{\alpha}{\beta}$, it's pushed up.
- However, $R(t)$ can be **negative**, which is unrealistic for modeling interest rates in some contexts.
- The variance decreases exponentially over time as $t \to \infty$, meaning $R(t)$ stabilizes around $\frac{\alpha}{\beta}$.

---

e.g., Let $W(t), t \geq 0$, be a Brownian motion. The Cox-Ingersoll-Ross model for the interest rate process $R(t)$ is

$$
\begin{align}
dR(t) = (\alpha - \beta R(t)) dt + \sigma \sqrt{R(t)} dW(t)
\end{align}
$$

where $\alpha$, $\beta$, and $\sigma$ are positive constants. Unlike the Vasicek equation (4.4.32), the CIR equation (4.4.34) does not have a closed-form solution.
The advantage of (4.4.34) over the Vasicek model is that the interest rate in the CIR model does not become negative. If $R(t)$ reaches zero, the term multiplying $dW(t)$ vanishes and the positive drift term $\alpha dt$ in equation (4.4.34) drives the interest rate back into positive territory. Like the Vasicek model, the CIR model is mean-reverting.

Although one cannot derive a closed-form solution for (4.4.34), the distribution of $R(t)$ for each positive $t$ can be determined. That computation would take us too far afield. We instead content ourselves with the derivation of the expected value and variance of $R(t)$. To do this, we use the function $f(t, x) = e^{\beta t} x$ and the Itô-Doeblin formula to compute

$$
\begin{align}
d(e^{\beta t} R(t)) = df(t, R(t)) 
&= f_t(t, R(t)) dt + f_x(t, R(t)) dR(t) + \frac{1}{2} f_{xx}(t, R(t)) dR(t) dR(t) \notag \\
&= \beta e^{\beta t} R(t) dt + e^{\beta t} (\alpha - \beta R(t)) dt + e^{\beta t} \sigma \sqrt{R(t)} dW(t) \notag \\
&= \alpha e^{\beta t} dt + \sigma e^{\beta t} \sqrt{R(t)} dW(t). \tag{4.4.35}
\end{align}
$$

Integration of both sides of (4.4.35) yields

$$
\begin{align}
e^{\beta t} R(t) &= R(0) + \alpha \int_0^t e^{\beta u} du + \sigma \int_0^t e^{\beta u} \sqrt{R(u)} dW(u) \notag \\
&= R(0) + \frac{\alpha}{\beta} (e^{\beta t} - 1) + \sigma \int_0^t e^{\beta u} \sqrt{R(u)} dW(u).
\end{align}
$$

Recalling that the expectation of an Itô integral is zero, we obtain

$$
\begin{align}
e^{\beta t} \mathbb{E}[R(t)] = R(0) + \frac{\alpha}{\beta} (e^{\beta t} - 1)
\end{align}
$$

or equivalently,

$$
\begin{align}
\mathbb{E}[R(t)] = e^{-\beta t} R(0) + \frac{\alpha}{\beta} (1 - e^{-\beta t}). \tag{4.4.36}
\end{align}
$$

**This is the same expectation as in the Vasicek model.**

To compute the variance of $R(t)$, we set $X(t) = e^{\beta t} R(t)$, for which we have already computed

$$
\begin{align}
dX(t) = \alpha e^{\beta t} dt + \sigma e^{\beta t} \sqrt{R(t)} dW(t) = \alpha e^{\beta t} dt + \sigma e^{\frac{\beta t}{2}} \sqrt{X(t)} dW(t).
\end{align}
$$

According to the Itô-Doeblin formula (with $f(x) = x^2$, $f'(x) = 2x$, and $f''(x) = 2$),

$$
\begin{align}
d(X^2(t)) &= 2X(t) dX(t) + dX(t) dX(t) \notag \\
&= 2\alpha e^{\beta t} X(t) dt + 2\sigma e^{\frac{\beta t}{2}} X^{\frac{3}{2}}(t) dW(t) + \sigma^2 e^{\beta t} X(t) dt. \tag{4.4.37}
\end{align}
$$

Integration of (4.4.37) yields

$$
\begin{align}
X^2(t) = X^2(0) + (2\alpha + \sigma^2) \int_0^t e^{\beta u} X(u) du + 2\sigma \int_0^t e^{\frac{\beta u}{2}} X^{\frac{3}{2}}(u) dW(u).
\end{align}
$$

Taking expectations, using the fact that the expectation of an Itô integral is zero and the formula already derived for $\mathbb{E}[X(t)]$, we obtain

$$
\begin{align}
\mathbb{E}[X^2(t)] &= X^2(0) + (2\alpha + \sigma^2) \int_0^t e^{\beta u} \mathbb{E}[X(u)] du \notag \\
&= R^2(0) + (2\alpha + \sigma^2) \int_0^t e^{\beta u} \left( R(0) + \frac{\alpha}{\beta} (e^{\beta u} - 1) \right) du \notag \\
&= R^2(0) + \frac{2\alpha + \sigma^2}{\beta} \left( R(0) - \frac{\alpha}{\beta} \right) (e^{\beta t} - 1) + \frac{2\alpha + \sigma^2}{2\beta^2} \frac{\alpha}{\beta} (e^{2\beta t} - 1).
\end{align}
$$

Therefore,

$$
\begin{align}
\mathbb{E}[R^2(t)] = e^{-2\beta t} \mathbb{E}[X^2(t)] = e^{-2\beta t} R^2(0) + \frac{2\alpha + \sigma^2}{\beta} \left( R(0) - \frac{\alpha}{\beta} \right) (e^{-\beta t} - e^{-2\beta t}) + \frac{\alpha(2\alpha + \sigma^2)}{2\beta^2} (1 - e^{-2\beta t}).
\end{align}
$$

Finally,

$$
\begin{align}
\text{Var}(R(t)) = \mathbb{E}[R^2(t)] - (\mathbb{E}[R(t)])^2.
\end{align}
$$

This simplifies to

$$
\begin{align}
\text{Var}(R(t)) &= e^{-2\beta t} R^2(0) + \frac{2\alpha + \sigma^2}{\beta} \left( R(0) - \frac{\alpha}{\beta} \right) (e^{-\beta t} - e^{-2\beta t}) + \frac{\alpha(2\alpha + \sigma^2)}{2\beta^2} (1 - e^{-2\beta t}) \notag \\
&\quad - \left[ e^{-\beta t} R(0) + \frac{\alpha}{\beta} (1 - e^{-\beta t}) \right]^2.
\end{align}
$$

Simplifying further gives (as shown in the text)

$$
\begin{align}
\text{Var}(R(t)) &= \frac{\sigma^2}{\beta} R(0) \left( e^{-\beta t} - e^{-2\beta t} \right) + \frac{\alpha \sigma^2}{2\beta^2} \left(1 - 2e^{-\beta t} + e^{-2\beta t} \right). \tag{4.4.38}
\end{align}
$$

In particular,

$$
\begin{align}
\lim_{t \to \infty} \text{Var}(R(t)) = \frac{\alpha \sigma^2}{2 \beta^2}.
\end{align}
$$

---

**Black-Scholes Merton Equation**
We aim to derive the Black-Scholes-Merton PDE for the price of an option on an asset modeled as a Geometric Brownian Motion. 

**Idea**: Determine the initial capital required to perfectly hedge a short position in the option.

**Evolution of Portfolio Value**
Let $X(t)$ be the portfolio value at time $t$ and take constant rate of interest in a stock modeled by a GBM defined in the DE below,

$$
dS(t) = \alpha S(t) dt + \sigma S(t) dW(t)
$$

The investor holds $\Delta(t)$ shares of stock at time $t$ so that at time $t$ the remainder of the portfolio value $X(t) - \Delta(t) S(t)$ is invested in the money market. We establish a capital gain $\Delta(t) dS(t)$ on the stock position and the interest earnings $r(X(t) - \Delta(t) S(t)) dt$ on the cash position.

$$
\begin{align*}
dX(t) &= \Delta(t)dS(t) + r(X(t) - \Delta(t) S(t))dt\\
&= \Delta(t)(\alpha S(t) dt + \sigma S(t) dW(t)) + r(X(t) - \Delta(t) S(t))dt\\
&= rX(t) dt + \Delta(t) (\alpha - r) S(t)dt + \Delta(t) \sigma S(t) dW(t)
\end{align*}
$$

where the terms,
- $rX(t)dt$ is the **average underlying rate of return $r$** on the portfolio 
- $\Delta(t) (\alpha - r) S(t) dt$ is the **risk premium** $\alpha - r$ for investing in the stock 
- $\Delta(t) \sigma S(t) dW(t)$ is the **volatility term proportional to the size of the stock investment** 

We consider the **discounted stock price** and **portfolio value** of our agent,

$$
e^{-rt}S(t) \quad\text{and}\quad e^{-rt}X(t)
$$

Applying the Ito-Doeblin formula for $f(t, x) = e^{-rt} x$ where $x$ and either be $S(t)$ and $X(t)$,

$$
\begin{align}
d(e^{-rt} S(t)) &= df(t, S(t)) \notag \\
&= f_t(t, S(t)) dt + f_x(t, S(t)) dS(t) + \frac{1}{2} f_{xx}(t, S(t)) dS(t) dS(t) \notag \\
&= -r e^{-rt} S(t) dt + e^{-rt} dS(t) \notag \\
&= (\alpha - r) e^{-rt} S(t) dt + \sigma e^{-rt} S(t) dW(t),
\end{align}
$$



$$
\begin{align}
d(e^{-rt} X(t)) &= df(t, X(t)) \notag \\
&= f_t(t, X(t)) dt + f_x(t, X(t)) dX(t) + \frac{1}{2} f_{xx}(t, X(t)) dX(t) dX(t) \notag \\
&= -r e^{-rt} X(t) dt + e^{-rt} dX(t) \notag \\
&= \Delta(t)(\alpha - r) e^{-rt} S(t) dt + \Delta(t) \sigma e^{-rt} S(t) dW(t) \notag \\
&= \Delta(t) d(e^{-rt} S(t)).
\end{align}
$$

for the **discounted stock price** and **discounted portfolio value**, respectively derived above. 

---

**Evolution of Option Value**
BS-Merton assumed that the value of a European call paying $(S(T) - K)^+$ at time $T$, should depend on the time to expiration, value of the stock price at that time, of which, only time and the stock price are variable. 

Let $c(t, x)$ denote the value of the call at time $t$ if the stock price at that time is $S(t) = x$, i.e., nothing is random about the function $c(t, x)$ but the value of the option is random i.e., $c(t, S(t))$ by replacing the dummy variable $x$ by $S(t)$ in this function.

At initial time, we do not know the future stock prices $S(t)$ and do not know the future option values $c(t, S(t))$. We wish to determine the function $c(t, x)$ so we have a formula for the future option values in terms of the future stock price. We compute the DE of $c(t, S(t))$,

$$
\begin{align}
dc(t, S(t)) &= c_t(t, S(t)) dt + c_x(t, S(t)) dS(t) + \frac{1}{2} c_{xx}(t, S(t)) dS(t) dS(t) \notag \\
&= c_t(t, S(t)) dt + c_x(t, S(t)) \left( \alpha S(t) dt + \sigma S(t) dW(t) \right) + \frac{1}{2} c_{xx}(t, S(t)) \sigma^2 S^2(t) dt \notag \\
&= \Bigg[ c_t(t, S(t)) + \alpha S(t) c_x(t, S(t)) + \frac{1}{2} \sigma^2 S^2(t) c_{xx}(t, S(t)) \Bigg] dt \notag \\
&\quad + \sigma S(t) c_x(t, S(t)) dW(t).
\end{align}
$$

then, compute the DE of the discounted option price $e^{-rt}c(t, S(t))$, for $f(t, x) = e^{-rt} x$,

$$
\begin{align}
d\left( e^{-rt} c(t, S(t)) \right) &= df\left( t, c(t, S(t)) \right) \notag \\
&= f_t\left( t, c(t, S(t)) \right) dt + f_x\left( t, c(t, S(t)) \right) dc(t, S(t)) \notag \\
&\quad + \frac{1}{2} f_{xx}\left( t, c(t, S(t)) \right) dc(t, S(t)) dc(t, S(t)) \notag \\
&= -r e^{-rt} c(t, S(t)) dt + e^{-rt} dc(t, S(t)) \notag \\
&= e^{-rt} \Bigg[ -r c(t, S(t)) + c_t(t, S(t)) + \alpha S(t) c_x(t, S(t)) \notag \\
&\quad + \frac{1}{2} \sigma^2 S^2(t) c_{xx}(t, S(t)) \Bigg] dt + e^{-rt} \sigma S(t) c_x(t, S(t)) dW(t).
\end{align}
$$

---

**Equating the Evolutions**

**Delta Hedging Rule**
A short option hedging portfolio starts with $X(0)$ and invests in the stock and money market account so that the portfolio value $X(t)$ at each $t \in [0, T]$ agrees with $c(t, S(t))$.

This happens if and only if $e^{-rt}X(t) = e^{-rt} c(t, S(t))$ for all $t$, which is ensured by,

$$
d(e^{-rt}X(t)) = d(e^{-rt}c(t, S(t))),\quad\text{for all } t \in [0, T]
$$

and $X(0) = c(0, S(0))$, which, after integration, becomes,

$$
e^{-rt}X(t) - X(0) = e^{-rt}c(t, S(t)) - c(0, S(0)),\quad\text{for all }t \in [0, T)
$$

Thus, the above hold if and only if,

$$
\begin{align*}
\Delta(t)(\alpha - r)S(t)dt + \Delta(t)\sigma S(t)dW(t) 
&= \Bigg[ -r c(t, S(t)) + c_t(t, S(t)) + \alpha S(t) c_x(t, S(t)) \\
&\quad + \frac{1}{2} \sigma^2 S^2(t) c_{xx}(t, S(t)) \Bigg] dt \\
&\quad + \sigma S(t) c_x(t, S(t)) dW(t) \tag{4.5.10}
\end{align*}
$$

which hold for $\Delta(t) = c_x(t, S(t))$ for all $t \in [0, T)$ which implies that the number of shares held by the hedge of the short option position is the partial derivative w.r.t. the stock price of the option value at that time, $c_x(t, S(t))$ also called the **delta** of the option.

$$
\begin{align*}
(\alpha - r) S(t) c_x(t, S(t)) &= - r c(t, S(t)) \\
&+ c_t(t, S(t)) + \alpha S(t) c_x(t, S(t)) + \frac{1}{2} \sigma^2 S^2(t) c_{xx}(t, S(t)) \tag{4.5.12} \\[1em]
r c(t, S(t)) &= c_t(t, S(t)) + r S(t) c_x(t, S(t)) + \frac{1}{2} \sigma^2 S^2(t) c_{xx}(t, S(t)) \tag{4.5.13} \\[1em]
c_t(t, x) &+ r x c_x(t, x) + \frac{1}{2} \sigma^2 x^2 c_{xx}(t, x) = r c(t, x) \tag{4.5.14}
\end{align*}
$$

Thus, we seek a continuous solution to the BS-Merton PDE given by,

$$
c_t(t, x) + rxc_x(t, x) + \frac{1}{2}\sigma^2 x^2 c_{xx}(t, x) = rc(t, x)\quad\text{for all } t \in [0, T),\quad x\ge 0
$$

satisfying the terminal condition $c(T, x) = (x - K)^+$.

**Steps to Hedging**
1.  Start with initial capital $X(0) = c(0, S(0))$
	1. use hedge $\Delta(t) = c_x(t, S(t))$
	2. 4.5.10 above holds
2. $dW(t)$ terms on RHS and LHS of 4.5.10 agree since $\Delta(t) = c_x(t, S(t))$
3. $dt$ terms agree since 4.5.14 guarantees 4.5.13
4. Cancelling $X(0) = c(0, S(0))$ and $e^{-rt}$ in the equation 
5. Thus, $X(t) = c(t, S(t))$ for $t \in [0, T)$. 
6. Taking the $\lim_{t \rightarrow T}$ and given $X(T)$ and $c(t, S(t))$ are continuous tells us that

$$
X(T) = c(T, S(T)) = (S(T) - K)^+
$$

Therefore, the short position has been successfully hedged. 
**Note**: No matter which of its possible paths the stock price follows, when the option expires, the agent hedging the shot position has a portfolio whose value agrees with the option payoff.

---

**Solution to the Black Scholes Merton Equation**
For 4.5.14, we impose boundary conditions at $x = 0$ and $x = \infty$ to determine the solution. By substituting $x = 0$ into 4.5.14, we get $c_t(t, 0) = rc(t, 0)$ which is an ODE for the function $c(t, 0)$ of $t$ which has solution $c(t, 0) = e^{rt}c(0, 0)$. Substituting $t = T$ into the equation gives us that $c(0, 0) = 0$which gives $c(t, 0) = 0$ for all $t \in [0, T]$; i.e., the boundary condition at $x = 0$.

As $x \rightarrow \infty$, $c(t, x)$ grows without bound which gives the boundary condition at $x = \infty$ by specifying the rate of growth which can be defined as,

$$
\lim_{x \rightarrow \infty} [c(t, x) - (x - e^{-r(T - t)} K)] = 0
$$

for all $t \in [0, T]$, which grows at the same rate as $x$ as $x \rightarrow \infty$, where $c(t, x)$is the value at time $t$ of a call on a stock whose price at time $t$ is $x$. For large $x$ this call is **deep ITM** and is very likely to end ITM. Thus, we define the solution to the BS-Merton equation with terminal condition,

$$
c(t, x) = xN(d_+ (T - t, x)) - Ke^{-r(T - t)} N(d_- (T - t, x)),\quad 0 \le t < T,\quad x > 0
$$

where $d_\pm (\tau, x)$ is defined as:

$$
d_\pm(\tau, x) = \frac{1}{\sigma \sqrt{\tau}} \left[\log \frac{x}{K} + \left(r \pm \frac{\sigma^2}{2} \right) \tau \right]
$$

and, where $N$ is the cum. standard normal distribution given by,

$$
N(y) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^y e^{-\frac{z^2}{2}} dz = \frac{1}{\sqrt{2\pi}} \int_{-y}^\infty e^{-\frac{z^2}{2}} dz
$$

where,
- $BSM(\tau, x; K, r, \sigma)$ is the BS-Merton function with $\tau, x$ denoting time to expiration and current stock price, respectively, and $K, r, \sigma$ denoting the strike, interest rate, and stock's volatility, respectively
- note the above does not define $c(t, x)$ for when $t = T$ because $\tau = T - t = 0$ and appears in the denominator, nor for when $x = 0$ because $\log 0$ is not a real number 
---

**The Greeks**
Recall this formula (we will use this for reference for the greeks)

$$
c(t, x) = xN(d_+ (T - t, x)) - Ke^{-r(T - t)} N(d_- (T - t, x)),\quad 0 \le t < T,\quad x > 0
$$

The derivatives of $c(t, x)$ with respect to various variables are called the Greeks.

**Delta**: We define the delta as,

$$
\boxed{
c_x(t, x) = N(d_+ (T - t, x))
}
$$

- Measures the sensitivity of the option price to changes in the underlying asset price $x$.  
- Delta is the amount by which the option price is expected to change for a small change in $x$.  
- For call options, delta ranges between 0 and 1; for put options, delta ranges between -1 and 0.

**Theta**: We define the theta as,

$$
\boxed{
c_t(t, x) = -rKe^{-r(T - t)}N(d_-(T - t, x)) - \frac{\sigma x}{2 \sqrt{T - t}} N'(d_+(T - t, x))
}
$$

- Measures the sensitivity of the option price to the passage of time, also called time decay.  
- Represents how much the option's value decreases as time to expiration decreases (all else being equal).  
- Typically, theta is negative for long call and put options since options lose value as they approach expiry.

**Gamma**: We define the gamma as,

$$
\boxed{
c_{xx}(t, x) = \frac{N'(d_+(T - t, x))}{x\sigma\sqrt{T - t}}
}
$$

- Measures the sensitivity of delta to changes in the underlying asset price $x$ (i.e., the second derivative of $c$ with respect to $x$).  
- Gamma shows how "curved" the option price is with respect to the underlying price; it is highest when the option is near the money.  
- A high gamma indicates that delta will change rapidly as $x$ changes, increasing the risk of holding a delta-hedged position.

**Vega**: We define the vega as,

$$
\boxed{
c_\sigma(t, x) = x \sqrt{T - t} N'(d_+ (T - t, x))
}
$$

- Measures the sensitivity of the option price to changes in the volatility $\sigma$ of the underlying asset.  
- Vega indicates how much the option price will change when implied volatility changes by 1 percentage point.  
- Options near the money and with more time to expiration tend to have higher vega.

**Rho**: We define the rho as,

$$
\boxed{c_r(t, x) = K(T - t)e^{-r(T - t)} N(d_-(T - t, x))}
$$

- Measures the sensitivity of the option price to changes in the risk-free interest rate $r$.  
- Rho shows how much the option price will change with a 1 percentage point change in interest rates.  
- For call options, rho is typically positive; for put options, it is typically negative.

**Notes:**
1. $N, N'$ are both always positive, thus Delta is always positive and Theta is always negative
2. Gamma is always positive 

---

Assuming that at time $t$ the stock price is $x$ giving us the short hedge of 4.5.11 as seen previously calling for $c_x(t, x)$ of stock where our position is $xc_x = xN(d_+)$. Thus our hedging portfolio is valued at:

$$
c = xN(d_+) - Ke^{-r(T - t)}N(d_-) \implies c(t, x) - xc_x(t, x) = -Ke^{-r(T - t)}N(d_-)
$$

is the amount invested in the money market. 

To hedge a short position in a call option, we must borrow money and for a long position in a call, we must hold $-c_x$ shares of stock (short position in stock) and invest $Ke^{-r(T - t)}N(d_-)$ in the money market account. 

Delta and Gamma are positive for fixed $t$ meaning that our function $c(t, x)$ is a convex increasing function in the variable $x$. Thus, taking a long position in the option and hedging it requires us to purchase the option for $c(t, x_1)$ and shorting $c_x(t, x_1)$ shares of stock generating $x_1 x_c(t, x_1)$ and investing the remaining difference int he money market:

$$
M = x_1 c_x (t, x_1) - c(t, x_1)
$$

The sensitivity of our portfolio to stock price changes can be measured by:
1. Long option Short stock
2. Long money market account 
With initial portfolio value defined as,

$$
c(t, x_1) - x_1 c_x(t, x_1) + M
$$

where it is $0$ at the moment $t$ when we set up these positions. 

Say $x$ were to fall to $x_0$. If we were not to change our positions in the stock or money market account, then the value of the option would fall to $c(t, x_0)$ and our liability in the short position of the stock would fall to $x_0 c_x(t, x_1)$ making our portfolio value,

$$
c(t, x_0) - x_0 c_x(t, x_1) + M = c(t, x_0) - c_x(t, x_1)(x_0 - x_1) - c(t, x_1)
$$

which is the difference between the curve and the straight line. Since this difference is positive, our portfolio benefits from an instantaneous drop in the stock price. If the stock were to instantaneously rise, on the contrary, and we do not change our positions in the stock or money market account, the value of the option would rise to $c(t, x_2)$ and the liability due to our short position in stock would increase to $x_2 c_x(t, x_1)$ and our total portfolio value including $M$ in the money market account would be given as,

$$
c(t, x_2) - x_2 c_x(t, x_1) + M = c(t, x_2) - c_x(t, x_1)(x_2 - x_1) - c(t, x_1)
$$

again, being the difference at $x_2$ between the curve and the straight line. 
We call this portfolio to be **delta-neutral** and **long gamma** since it benefits from the convexity of $c(t, x)$. If there is an instantaneous rise or an instantaneous fall in the stock price the value of the portfolio increases. A long gamma portfolio is profitable in times of high stock volatility. 

---

**Put-Call Parity**
A forward contract obliges it's holder to buy one share of stock at expiration time $T$ in exchange for payment $K$. At expiration, the value of the forward contract is $S(T) - K$. Define $f(t, x)$ as the value of the forward contract at earlier times $t \in [0, T]$ if $S(t) = x$ is the stock price at time $t$.

**Value of Forward Contract** at time $t$ for stock price $x$ is given by,

$$
f(t, x) = x - e^{-r(T - t)} K
$$

We set up a static hedge when the agent sells the FC for $f(0, S(0)) = S(0) - e^{-rT} K$, which is where the hedge does not trade except at the initial time in order to protect themself.
- Agent should buy one share of stock
- From initial capital $S(0) - e^{-rT} K$ from sale of FC, agent borrows $e^{-rT} K$ from MM acc't
- So, the agent's portfolio value is $S(T) - K$, exactly the FC value 
- Agent is able to replicate the payoff of the FC with a portfolio whose value at each time $t$ is given by $S(t) - e^{-r(T - T)}K$, this must be the value at each time of the FC 
- This is $f(t, S(t))$.

**Forward Price** is the value $K$ that causes the FC at time $t$ to have value $0$, and is the value of $K$ that satisfies the equation at time $t$ to have $S(t) - e^{r(T - t)} K = 0$. In a model with constant interest rate, we can see that the FP at time $t$ is,

$$
ForwardPrice(t) = e^{r(T - t)} S(t)
$$

The forward price at time $t$ is the price one can lock in at time $t$ for the purchase of one share of stock at time $T$, settling for the price at time $T$. No money changes hands at the time that the price is locked in. 

Let's assume, that at time $t = 0$, we lock in a price $ForwardPrice(0) = e^{rT} S(0)$ for purchase of the stock at time $T$. We set $K = e^{rT}S(0)$. The value of this FC is $0$ at time $t = 0$ but as we move forward in time, the value of the forward contract at $t$ is,

$$
f(t, S(t)) = S(t) - e^{rT} S(0)
$$

Take a European put option, which pays off $(K - S(T))^+$ at $T$, so that for any number $x$,

$$
x - K = (x - K)^+ - (K - x)+
$$

is true. We see for $x \ge K$ that $(x - K)^+ = x - K$ and that $(K - x)^+ = 0$. Otherwise, for $x \le K$ we see that $(x - K)^+ = 0$ and that $-(K - x)^+ = -(K - x) = x - K$ so that either case results in the LHS equalling the RHS. We denote the value of the European put at $t$ as $p(t, x)$ where $S(t) = x$. Moreover, we denote $c(t, x)$ as the value of the European call expiring at time $T$ with strike $K$. Thus, we can see that the equation above implies that,

$$
f(T, S(T)) = c(T, S(T)) - p(T, S(T))
$$

which is the payoff of the FC that agrees with the payoff of a portfolio with one long call and one short put. Since the value at time $T$ of the FC agrees with the value of the portfolio above, then these values must agree at all previous times:

$$
f(t, x) = c(t, x) - p(t, x)
$$

Otherwise, we could at some time $t$ either sell or buy the portfolio that is long forward, short call, and long put for a realized instantaneous profit. The equation above establishes the **put-call parity** formula and making the additional assumption for constant volatility with a GBM for $\sigma > 0$ we have the BS-Merton call formula, the solve to get the put formula,

$$
\begin{align*}
p(t, x) &= x(N(d_+ (T - t, x)) - 1) - Ke^{-r(T - t)}(N(d_- (T - t, x)) - 1)\\
&= Ke^{-r(T - t)} N(-d_- (T - t, x)) -xN(-d_+(T - t, x))
\end{align*}
$$

where we defined $d_\pm$ as the following,

$$
d_\pm(\tau, x) = \frac{1}{\sigma \sqrt{\tau}} \left[\log \frac{x}{K} + \left(r \pm \frac{\sigma^2}{2} \right) \tau \right]
$$

---

**Multivariable Stochastic Calculus**

**Multiple Brownian Motions ($d$-Dimensional)**
A $d$-dimensional Brownian motion is a process given by:

$$
W(t) = (W_1(t),\dots, W_d(t))
$$

1. Each $W_i(t)$ is a 1-dimensional Brownian motion
2. For $i \neq j$, processes $W_i(t)$ and $W_j(t)$ are independent.
We saw that the quadratic variation formula $[W_i, W_i](t) = t$ can be informally written as

$$
dW_i(t) dW_i(t) = dt
$$

But for $i \neq j$ we can see that the independence between the two corresponding Brownian motions implies that $[W_i, W_j](0) = 0$ which can be written informally as,

$$
dW_i (t) dW_j (t) = 0,\quad i \neq j
$$

This can be justified by taking the partition and defining the sampled cross-variation,

$$
C_\Pi = \sum_{k = 0}^{n - 1} [W_i(t_{k + 1}) - W_i(t_k)][W_j(t_{k + 1}) - W_j(t_k)]
$$

After some algebra and cancellation, we see that the sum of the cross-terms are independent of one another and all have mean zero. Thus, we see now that,

$$
Var(C_\Pi) = \sum_{k = 0}^{n - 1}(t_{k + 1} - t_k)^2 \le ||\Pi|| \cdot \sum_{k = 0}^{n - 1} (t_{k + 1} - t_k) = ||\Pi|| \cdot T
$$

So, as $||\Pi|| \rightarrow 0$, we can see that $Var(C_\Pi) \rightarrow 0$, and $C_\Pi$ converges to the constant $\mathbb{E}C_\Pi = 0$.

---

**Ito-Doeblin Formula for Multiple Processes**
We can write the Ito-Doeblin formula for two processes driven by two-dimensional BMs. Let $X(t), Y(t)$ be two Ito processes, meaning they can be written as,

$$
\begin{align*}
X(t) &= X(0) + \int_0^t \Theta_1(u) \, du + \int_0^t \sigma_{11}(u) \, dW_1(u) + \int_0^t \sigma_{12}(u) \, dW_2(u), \\
Y(t) &= Y(0) + \int_0^t \Theta_2(u) \, du + \int_0^t \sigma_{21}(u) \, dW_1(u) + \int_0^t \sigma_{22}(u) \, dW_2(u).
\end{align*}
$$

where $\Theta_i, \sigma_{ij}$ are adapted stochastic processes. Equivalently, we can write the above in differential form, which directly gives us,

$$
\begin{align*}
dX(t) &= \Theta_1(t) \, dt + \sigma_{11}(t) \, dW_1(t) + \sigma_{12}(t) \, dW_2(t), \\
dY(t) &= \Theta_2(t) \, dt + \sigma_{21}(t) \, dW_1(t) + \sigma_{22}(t) \, dW_2(t).
\end{align*}
$$

- $\int_0^t \sigma_{11}(u) dW_1(u)$ accumulates QV at rate $\sigma_{11}^2(t)$ per unit time
- $\int_0^t \sigma_{12}(u) dW_2(u)$ accumulates QV at rate $\sigma_{12}^2(t)$ per unit time
- Both of these integrals appear in $X(t)$ thus the process $X(t)$ accumulates QV at rate

$$
\sigma_{11}^2(t) + \sigma_{12}^2(t)
$$

per unit time. Thus, we can write this as,

$$
[X, X](t) = \int_0^t (\sigma_{11}^2(t) + \sigma_{12}^2(t))du \implies dX(t) dX(t) = (\sigma_{11}^2(t) + \sigma_{12}^2(t))dt
$$

which gives the informal derivations of,

$$
dt\, dt = 0, \quad dt\, dW_i(t) = 0, \quad dW_i(t)\, dW_i(t) = dt, \quad dW_i(t)\, dW_j(t) = 0 \text{ for } i \neq j
$$

We can also derive the differential formulas,

$$
\begin{align}
dY(t)\, dY(t) &= \left( \sigma_{21}^2(t) + \sigma_{22}^2(t) \right) dt\\
dX(t)\, dY(t) &= \left( \sigma_{11}(t)\sigma_{21}(t) + \sigma_{12}(t)\sigma_{22}(t) \right) dt
\end{align}
$$

Thus, giving us that,

$$
[X, Y](T) = \int_0^T \left( \sigma_{11}(t)\sigma_{21}(t) + \sigma_{12}(t)\sigma_{22}(t) \right) dt. \tag{4.6.6}
$$

**Theorem**
Let $f(t, x, y)$ be a function whose partials are $f_t, f_x, f_y, f_{xx}, f_{xy}, f_{yx}, f_{yy}$ are defined and continuous. $X(t), Y(t)$ are Ito processes, so the two-dimensional Ito-Doeblin formula,

$$
\begin{align*}
df(t, X(t), Y(t)) 
&= f_t(t, X(t), Y(t)) \, dt + f_x(t, X(t), Y(t)) \, dX(t) + f_y(t, X(t), Y(t)) \, dY(t) \\
&\quad + \frac{1}{2} f_{xx}(t, X(t), Y(t)) \, dX(t) dX(t) + f_{xy}(t, X(t), Y(t)) \, dX(t) dY(t) \\
&\quad + \frac{1}{2} f_{yy}(t, X(t), Y(t)) \, dY(t) dY(t).
\end{align*}
$$

Leaving out instances of $t$ gives us a more compact definition of the two-dim ID formula,

$$
\begin{align*}
df(t, X, Y) = f_t \, dt + f_x \, dX + f_y \, dY + \frac{1}{2} f_{xx} \, dX \, dX + f_{xy} \, dX \, dY + \frac{1}{2} f_{yy} \, dY \, dY.
\end{align*}
$$

Note, for functions whose second-order partials exist and are continuous, we can write that $f_{xy} = f_{yx}$ so that we combined these terms into the term $f_{xy} dX dY$ giving the integral form,

$$
\begin{align*}
f&(t, X(t), Y(t)) - f(0, X(0), Y(0))\\
&= \int_0^t \left[ \sigma_{11}(u) f_x(u, X(u), Y(u)) + \sigma_{21}(u) f_y(u, X(u), Y(u)) \right] dW_1(u) \\
&\quad + \int_0^t \left[ \sigma_{12}(u) f_x(u, X(u), Y(u)) + \sigma_{22}(u) f_y(u, X(u), Y(u)) \right] dW_2(u) \\
&\quad + \int_0^t \Bigg[ f_t(u, X(u), Y(u)) + \Theta_1(u) f_x(u, X(u), Y(u)) + \Theta_2(u) f_y(u, X(u), Y(u)) \\
&\qquad + \frac{1}{2} \left( \sigma_{11}^2(u) + \sigma_{12}^2(u) \right) f_{xx}(u, X(u), Y(u)) \\
&\qquad + \left( \sigma_{11}(u)\sigma_{21}(u) + \sigma_{12}(u)\sigma_{22}(u) \right) f_{xy}(u, X(u), Y(u)) \\
&\qquad + \frac{1}{2} \left( \sigma_{21}^2(u) + \sigma_{22}^2(u) \right) f_{yy}(u, X(u), Y(u)) \Bigg] du.
\end{align*}
$$

Notice the RHS is an Ordinary Lebesgue integral wrt $du$ and two Ito integrals wrt $dW_1(u)$ and $dW_2(u)$. Thus we can also define a product rule, similar to ordinary calculus.

**Corollary (Ito Product Rule)**
$X(t)$ and $Y(t)$ are Ito processes, then we can write the product of the two as,

$$
\begin{align*}
d(X(t) Y(t)) = X(t) \, dY(t) + Y(t) \, dX(t) + dX(t) \, dY(t).
\end{align*}
$$

Taking $f(t, x, y) = xy$ so that $f_t = 0, f_x = y, f_y = x, f_{xx} = 0, f_{xy} = 1$ and $f_{yy} = 0$. 

---

**Theorem - Levy One-Dimension**
$M(t)$ is a martingale relative to $\mathcal{F}(t)$ for $t \ge 0$. Assume $M(0) = 0$, and $M(t)$ has continuous paths, and $[M, M](t) = t$ for all $t \ge 0$. Then, $M(t)$ is a Brownian motion!

**Theorem - Levy Two-Dimension**
$M_1(t)$ and $M_2(t)$, for all $t \ge 0$ be martingales relative to a filtration $\mathcal{F}(t)$ for $t \ge 0$. Assume that for $i = 1, 2$ we have that $M_i(0) = 0$ and $M_i(t)$ has continuous paths, and $[M_i, M_i](t) = t$ for all $t \ge 0$. In addition, $[M_1, M_2](t) = 0$ for all $t \ge 0$, then $M_1(t)$ and $M_2(t)$ are independent Brownian motions.

**e.g., Correlated Stock Prices** 
Suppose,

$$
\begin{align*}
\frac{dS_1(t)}{S_1(t)} &= \alpha_1 dt + \sigma_1 dW_1(t)\\
\frac{dS_2(t)}{S_2(t)} &= \alpha_2 dt + \sigma_2 \left[\rho dW_1(t) + \sqrt{1 - p^2} dW_2(t) \right]
\end{align*}
$$

where $W_1(t), W_2(t)$ are independent Brownian motions and $\sigma_1 > 0, \sigma_2 > 0$ and $-1 \le \rho \le 1$ are constants. The second stock price process, after defining,

$$
W_3(t) = \rho W_1(t) + \sqrt{1 - p^2} W_2(t)
$$

Then, $W_3(t)$ is a continuous martingale with $W_3(0) = 0$ and that we have,

$$
\begin{align*}
dW_3(t) dW_3(t) &= \rho^2 dW_1(t) dW_1(t) + 2\rho \sqrt{1 - \rho^2} \, dW_1(t) dW_2(t) + (1 - \rho^2) dW_2(t) dW_2(t) \\
&= \rho^2 dt + (1 - \rho^2) dt = dt.
\end{align*}
$$

and that $[W_3, W_3](t)$. According to the 1-dim Levy theorem, $W_3(t)$ is a Brownian motion, thus, we can wrote the differential of $S_2(t)$ as,

$$
\begin{align*}
\frac{dS_2(t)}{S_2(t)} = \alpha_2 dt + \sigma_2 dW_3(t),
\end{align*}
$$

$S_2(t)$ is a GBM with mean rate of return $\alpha_2$ and volatility $\sigma_2$. The Brownian motions $W_1(t)$ and $W_3(t)$ are correlated, so given Ito's product, we can write,

$$
\begin{align*}
d(W_1(t) W_3(t)) &= W_1(t) \, dW_3(t) + W_3(t) \, dW_1(t) + dW_1(t) \, dW_3(t) \\
&= W_1(t) \, dW_3(t) + W_3(t) \, dW_1(t) + \rho \, dt.
\end{align*}
$$

Integrating gives Ito integrals on the RHS with expectation zero, so the covariance of $W_1(t)$ and $W_3(t)$ is $\mathbb{E}[W_1(t)W_3(t)] = \rho t$.

$$
\begin{align*}
W_1(t) W_3(t) = \int_0^t W_1(s) \, dW_3(s) + \int_0^t W_3(s) \, dW_1(s) + \rho t.
\end{align*}
$$

Since both Brownian motions have standard deviation $\sqrt{t}$ the number $\rho$ is the correlation between the two Brownian motions.

---



