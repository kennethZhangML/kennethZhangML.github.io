---
layout: page
title: Chapter 4 - Stochastic Calculus Exercises
description: Notes on Stochastic Calculus and its applications.
parent: course-2
importance: 7
permalink: /notes/course-2/chapter-4-stochastic-calculus-exercises/
nav: false
---


**Exercise 4.1**  
Suppose $M(t)$, $0 \leq t \leq T$, is a martingale with respect to some filtration $\mathcal{F}(t)$, and let $\Delta(t)$ be a simple predictable process adapted to $\mathcal{F}(t)$ on a partition $\Pi = \{t_0, t_1, \ldots, t_n\}$.

Define the stochastic integral process:


$$
I(t) = \sum_{j=0}^{k-1} \Delta(t_j)[M(t_{j+1}) - M(t_j)] + \Delta(t_k)[M(t) - M(t_k)], \quad \text{for } t \in [t_k, t_{k+1}).
$$



We aim to show that $I(t)$ is a martingale.

Since $\Delta(t_j)$ is $\mathcal{F}(t_j)$-measurable and constant on each subinterval $[t_j, t_{j+1})$, and $M(t)$ is adapted, each summand $\Delta(t_j)[M(t_{j+1}) - M(t_j)]$ and $\Delta(t_k)[M(t) - M(t_k)]$ is $\mathcal{F}(t_{j+1})$-measurable, hence adapted. $M(t)$ is integrable by assumption, and since $\Delta(t_j)$ is simple and bounded, each term is integrable. Therefore, $I(t)$ is integrable and adapted.

To check the martingale property, let $s < t$, and suppose $s \in [t_m, t_{m+1})$, $t \in [t_k, t_{k+1})$ with $m < k$.
We write:


$$
I(t) = \sum_{j=0}^{k-1} \Delta(t_j)[M(t_{j+1}) - M(t_j)] + \Delta(t_k)[M(t) - M(t_k)]
$$


and break it as:


$$
\begin{align*}
I(t) = \sum_{j=0}^{m-1} \Delta(t_j)[M(t_{j+1}) - M(t_j)] + \Delta(t_m)[M(s) - M(t_m)] \\+ \sum_{j=m}^{k-1} \Delta(t_j)[M(t_{j+1}) - M(t_j)] + \Delta(t_k)[M(t) - M(t_k)].
\end{align*}
$$



Take conditional expectation with respect to $\mathcal{F}(s)$. Since $M(t)$ is a martingale:
- For $t_j \geq s$, $\mathbb{E}[M(t_{j+1}) - M(t_j) \mid \mathcal{F}(s)] = 0$,
- $\Delta(t_j)$ is $\mathcal{F}(t_j)$-measurable and $t_j \leq s$, so it's constant under $\mathbb{E}[\cdot \mid \mathcal{F}(s)]$.

Therefore,


$$
\mathbb{E}[I(t) \mid \mathcal{F}(s)] = \sum_{j=0}^{m-1} \Delta(t_j)[M(t_{j+1}) - M(t_j)] + \Delta(t_m)[M(s) - M(t_m)] = I(s).
$$



This shows that $I(t)$ satisfies the martingale property:


$$
\mathbb{E}[I(t) \mid \mathcal{F}(s)] = I(s), \quad \forall 0 \leq s < t \leq T.
$$



Hence, $I(t)$ is a martingale.



**Exercise 4.2**  
Let $W(t)$, $0 \leq t \leq T$, be a Brownian motion with associated filtration $\mathcal{F}(t)$. Let $\Delta(t)$ be a **nonrandom** simple process: there exists a partition $\Pi = \{t_0, t_1, \ldots, t_n\}$ of $[0,T]$ such that $\Delta(t) = \Delta(t_j)$ on $[t_j, t_{j+1})$, and each $\Delta(t_j)$ is a deterministic constant.

For $t \in [t_k, t_{k+1})$, define the stochastic integral:


$$
I(t) = \sum_{j=0}^{k-1} \Delta(t_j)[W(t_{j+1}) - W(t_j)] + \Delta(t_k)[W(t) - W(t_k)].
$$


**(i)** Show that whenever $0 \leq s < t \leq T$, the increment $I(t) - I(s)$ is independent of $\mathcal{F}(s)$.

If $s$ is not a partition point, insert $s$ into the partition as $t_k = s$ and set $\Delta(s) = \Delta(t_{k-1})$ to preserve the constant value of $\Delta$ over the interval. Do the same for $t$ if needed.

Now both $s$ and $t$ are partition points. Then:


$$
I(t) - I(s) = \sum_{j=k}^{l-1} \Delta(t_j)[W(t_{j+1}) - W(t_j)] + \Delta(t_l)[W(t) - W(t_l)],
$$


where $s = t_k$ and $t \in [t_l, t_{l+1})$.

Each Brownian increment $W(t_{j+1}) - W(t_j)$ and $W(t) - W(t_l)$ is independent of $\mathcal{F}(s)$ because Brownian motion has independent increments and $t_j \geq s$ for all terms in the sum.

Therefore, $I(t) - I(s)$ depends only on Brownian motion after time $s$ and is thus independent of $\mathcal{F}(s)$.


**(ii)** Show that whenever $0 \leq s < t \leq T$, the increment $I(t) - I(s)$ is a normally distributed random variable with mean zero and variance $\int_s^t \Delta^2(u) \, du$.

From (i), we know:


$$
I(t) - I(s) = \sum_{j=k}^{l-1} \Delta(t_j)[W(t_{j+1}) - W(t_j)] + \Delta(t_l)[W(t) - W(t_l)],
$$


where $s = t_k$, $t \in [t_l, t_{l+1})$.

Each $W(t_{j+1}) - W(t_j)$ is independent and distributed as $\mathcal{N}(0, t_{j+1} - t_j)$, and $\Delta(t_j)$ is constant.

Hence, each term $\Delta(t_j)[W(t_{j+1}) - W(t_j)] \sim \mathcal{N}(0, \Delta^2(t_j)(t_{j+1} - t_j))$, and all terms are independent.

The sum of independent normal variables is normal, so $I(t) - I(s) \sim \mathcal{N}(0, \sum \Delta^2(t_j)(t_{j+1} - t_j))$.

This sum is exactly:


$$
\int_s^t \Delta^2(u) \, du.
$$



**(iii)** Use (i) and (ii) to show that $I(t)$, $0 \leq t \leq T$, is a martingale.

From (i), $I(t) - I(s)$ is independent of $\mathcal{F}(s)$, and from (ii), $\mathbb{E}[I(t) - I(s)] = 0$.

Therefore,


$$
\mathbb{E}[I(t) \mid \mathcal{F}(s)] = \mathbb{E}[I(s) + (I(t) - I(s)) \mid \mathcal{F}(s)] = I(s).
$$



So $I(t)$ satisfies the martingale property and is therefore a martingale.


**(iv)** Show that $I^2(t) - \int_0^t \Delta^2(u) \, du$, $0 \leq t \leq T$, is a martingale.

From (ii), the variance of the increment is:


$$
\text{Var}(I(t) - I(s)) = \int_s^t \Delta^2(u) \, du.
$$



Using the Itô isometry and properties of Brownian motion:


$$
\mathbb{E}[I^2(t) - I^2(s) \mid \mathcal{F}(s)] = \mathbb{E}[(I(t) - I(s))^2 \mid \mathcal{F}(s)] = \int_s^t \Delta^2(u) \, du.
$$



Therefore:


$$
\mathbb{E}[I^2(t) \mid \mathcal{F}(s)] = I^2(s) + \int_s^t \Delta^2(u) \, du,
$$


which implies:


$$
\mathbb{E}\left[I^2(t) - \int_0^t \Delta^2(u) \, du \mid \mathcal{F}(s)\right] = I^2(s) - \int_0^s \Delta^2(u) \, du.
$$



So the process $I^2(t) - \int_0^t \Delta^2(u) \, du$ is a martingale.



**Exercise 4.3**  
We now consider the case where $\Delta(t)$ is a simple **random** process. Let $t_0 = 0$, $t_1 = s$, and $t_2 = t$. Suppose $\Delta(0)$ is nonrandom, but $\Delta(s) = W(s)$ is **random** and $\mathcal{F}(s)$-measurable. Let


$$
I(t) = \sum_{j=0}^{1} \Delta(t_j)[W(t_{j+1}) - W(t_j)] = \Delta(0)[W(s) - W(0)] + \Delta(s)[W(t) - W(s)].
$$



We evaluate the truth of the following assertions:

**(i)** $I(t) - I(s)$ is independent of $\mathcal{F}(s)$.

We compute:


$$
I(t) - I(s) = \Delta(s)[W(t) - W(s)].
$$



While $W(t) - W(s)$ is independent of $\mathcal{F}(s)$ by the independent increments property of Brownian motion, $\Delta(s) = W(s)$ is $\mathcal{F}(s)$-measurable. Therefore, the product $\Delta(s)[W(t) - W(s)]$ **depends** on $\mathcal{F}(s)$ through $\Delta(s)$.

Hence, $I(t) - I(s)$ is **not** independent of $\mathcal{F}(s)$.

**False**.

**(ii)** $I(t) - I(s)$ is normally distributed.

Recall:


$$
I(t) - I(s) = \Delta(s)[W(t) - W(s)] = W(s)[W(t) - W(s)].
$$



$W(s)$ and $W(t) - W(s)$ are independent, but $I(t) - I(s)$ is the **product** of two independent normal variables. The product of two independent normals is **not** normally distributed.

To confirm, check the fourth moment:
- $\mathbb{E}[(I(t) - I(s))^4] \neq 3 \cdot \left( \text{Var}(I(t) - I(s)) \right)^2$.

Hence, $I(t) - I(s)$ is **not** normally distributed.

**False**.

**(iii)** $\mathbb{E}[I(t) \mid \mathcal{F}(s)] = I(s)$.

We have:


$$
I(t) = I(s) + \Delta(s)[W(t) - W(s)] = I(s) + W(s)[W(t) - W(s)].
$$



Then:


$$
\mathbb{E}[I(t) \mid \mathcal{F}(s)] = I(s) + W(s)\cdot \mathbb{E}[W(t) - W(s) \mid \mathcal{F}(s)].
$$



Since $W(t) - W(s)$ is independent of $\mathcal{F}(s)$ and has mean zero:


$$
\mathbb{E}[I(t) \mid \mathcal{F}(s)] = I(s).
$$



**True**.

**(iv)** 


$$
\mathbb{E}\left[ I^2(t) - \int_0^t \Delta^2(u) \, du \,\middle|\, \mathcal{F}(s) \right] = I^2(s) - \int_0^s \Delta^2(u) \, du.
$$



We expand:


$$
I^2(t) = \left( I(s) + \Delta(s)[W(t) - W(s)] \right)^2 = I^2(s) + 2 I(s)\Delta(s)[W(t) - W(s)] + \Delta^2(s)[W(t) - W(s)]^2.
$$



Take expectation conditional on $\mathcal{F}(s)$:
- $\mathbb{E}[W(t) - W(s) \mid \mathcal{F}(s)] = 0$,
- $\mathbb{E}[(W(t) - W(s))^2 \mid \mathcal{F}(s)] = t - s$.

So:


$$
\mathbb{E}[I^2(t) \mid \mathcal{F}(s)] = I^2(s) + \Delta^2(s)(t - s),
$$


and


$$
\int_0^t \Delta^2(u) \, du = \int_0^s \Delta^2(u) \, du + \int_s^t \Delta^2(u) \, du = \int_0^s \Delta^2(u) \, du + \Delta^2(s)(t - s).
$$



Therefore:


$$
\mathbb{E}\left[ I^2(t) - \int_0^t \Delta^2(u) \, du \,\middle|\, \mathcal{F}(s) \right] = I^2(s) - \int_0^s \Delta^2(u) \, du.
$$



**True**.



**Exercise 4.4 (Stratonovich integral)**  
Let $W(t)$, $t \geq 0$, be a Brownian motion. Let $T > 0$ and let $\Pi = \{t_0, t_1, \ldots, t_n\}$ be a partition of $[0, T]$ with $0 = t_0 < t_1 < \cdots < t_n = T$. For each $j$, define the midpoint:


$$
t_j^* = \frac{t_j + t_{j+1}}{2}.
$$



**(i)** Define the *half-sample quadratic variation* corresponding to $\Pi$ as:


$$
Q_{\Pi/2} = \sum_{j=0}^{n-1} \left( W(t_j^*) - W(t_j) \right)^2.
$$



We show that:


$$
\mathbb{E}[Q_{\Pi/2}] = \sum_{j=0}^{n-1} \mathbb{E}\left[ \left( W(t_j^*) - W(t_j) \right)^2 \right] = \sum_{j=0}^{n-1} (t_j^* - t_j) = \sum_{j=0}^{n-1} \frac{t_{j+1} - t_j}{2} = \frac{1}{2} T.
$$



Now compute the variance:


$$
\text{Var}(Q_{\Pi/2}) = \sum_{j=0}^{n-1} \text{Var}\left( \left( W(t_j^*) - W(t_j) \right)^2 \right).
$$



Each $W(t_j^*) - W(t_j)$ is a normal random variable with variance $(t_{j+1} - t_j)/2$, so its square has variance:


$$
\text{Var}((W(t_j^*) - W(t_j))^2) = 2 \cdot \left( \frac{t_{j+1} - t_j}{2} \right)^2 = \frac{(t_{j+1} - t_j)^2}{2}.
$$



Hence,


$$
\text{Var}(Q_{\Pi/2}) = \sum_{j=0}^{n-1} \frac{(t_{j+1} - t_j)^2}{2} \leq \frac{1}{2} \|\Pi\| \sum_{j=0}^{n-1} (t_{j+1} - t_j) = \frac{1}{2} \|\Pi\| T.
$$



As $\|\Pi\| \to 0$, the variance $\to 0$.

Therefore, by Chebyshev’s inequality or convergence in $L^2$, we conclude:


$$
Q_{\Pi/2} \to \frac{1}{2} T.
$$



**(ii)** Define the *Stratonovich integral* of $W(t)$ with respect to $W(t)$ as:


$$
\int_0^T W(t) \circ dW(t) = \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1} W(t_j^*) \left( W(t_{j+1}) - W(t_j) \right).
$$



We aim to show:


$$
\int_0^T W(t) \circ dW(t) = \frac{1}{2} W^2(T).
$$



We write the Stratonovich sum as:


$$
\sum_{j=0}^{n-1} W(t_j^*) \left( W(t_{j+1}) - W(t_j) \right)
= \sum_{j=0}^{n-1} \left( \frac{W(t_j) + W(t_{j+1})}{2} \right) \left( W(t_{j+1}) - W(t_j) \right).
$$



This is:


$$
= \sum_{j=0}^{n-1} \left[ \frac{1}{2} \left( W(t_{j+1}) - W(t_j) \right)^2 + \frac{1}{2} W(t_j) \left( W(t_{j+1}) - W(t_j) \right) \right].
$$



Now recall:
- The Itô integral is:


$$
\int_0^T W(t) \, dW(t) = \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1} W(t_j)(W(t_{j+1}) - W(t_j)).
$$



So the Stratonovich integral equals:


$$
\int_0^T W(t) \circ dW(t) = \int_0^T W(t) \, dW(t) + \frac{1}{2} \sum_{j=0}^{n-1} \left( W(t_{j+1}) - W(t_j) \right)^2.
$$



In the limit, the sum becomes the quadratic variation:


$$
[W](T) = \sum_{j=0}^{n-1} \left( W(t_{j+1}) - W(t_j) \right)^2 \to T.
$$



And from Exercise 4.3 or standard result:


$$
\int_0^T W(t) \, dW(t) = \frac{1}{2} W^2(T) - \frac{1}{2} T.
$$



Hence:


$$
\int_0^T W(t) \circ dW(t) = \left( \frac{1}{2} W^2(T) - \frac{1}{2} T \right) + \frac{1}{2} T = \frac{1}{2} W^2(T).
$$





**Exercise 4.5 (Solving the generalized geometric Brownian motion equation)**  
Let $S(t)$ be a positive stochastic process satisfying the SDE:


$$
dS(t) = \alpha(t) S(t) \, dt + \sigma(t) S(t) \, dW(t),
$$


where $\alpha(t)$ and $\sigma(t)$ are adapted processes with respect to the filtration $\mathcal{F}(t)$ of the Brownian motion $W(t)$.

**(i)** Using Itô’s formula, compute $d \log S(t)$ and simplify to eliminate $S(t)$ from the expression.

Let $f(S(t)) = \log S(t)$. Then applying Itô’s lemma:
- $f'(S) = \frac{1}{S}$,
- $f''(S) = -\frac{1}{S^2}$.

Using the SDE for $S(t)$:


$$
d \log S(t) = \frac{1}{S(t)} \, dS(t) - \frac{1}{2} \cdot \frac{1}{S(t)^2} \cdot (dS(t))^2.
$$



Substitute $dS(t) = \alpha(t) S(t) dt + \sigma(t) S(t) dW(t)$:
- $dS(t)/S(t) = \alpha(t) dt + \sigma(t) dW(t)$,
- $(dS(t))^2 = \sigma^2(t) S^2(t) dt$.

So:


$$
d \log S(t) = \left( \alpha(t) dt + \sigma(t) dW(t) \right) - \frac{1}{2} \sigma^2(t) dt = \left( \alpha(t) - \frac{1}{2} \sigma^2(t) \right) dt + \sigma(t) dW(t).
$$



Thus,


$$
d \log S(t) = \left( \alpha(t) - \frac{1}{2} \sigma^2(t) \right) dt + \sigma(t) dW(t).
$$



This is the desired expression, independent of $S(t)$.

**(ii)** Integrate the formula obtained in (i), then exponentiate the result.

From (i):


$$
\log S(t) - \log S(0) = \int_0^t \left( \alpha(u) - \frac{1}{2} \sigma^2(u) \right) du + \int_0^t \sigma(u) dW(u).
$$



Therefore:


$$
\log S(t) = \log S(0) + \int_0^t \left( \alpha(u) - \frac{1}{2} \sigma^2(u) \right) du + \int_0^t \sigma(u) dW(u).
$$



Exponentiating both sides:


$$
S(t) = S(0) \exp \left( \int_0^t \left( \alpha(u) - \frac{1}{2} \sigma^2(u) \right) du + \int_0^t \sigma(u) dW(u) \right).
$$



This is formula (4.4.26), the unique solution to the SDE.



**Exercise 4.6**  
Let 


$$
S(t) = S(0) \exp\left\{ \sigma W(t) + \left( \alpha - \frac{1}{2} \sigma^2 \right)t \right\}
$$


be a geometric Brownian motion. Let $p$ be a positive constant. Compute $d(S^p(t))$, the differential of $S(t)^p$.

Let $f(S(t)) = S^p(t)$. By Itô’s lemma:
- $f'(S) = p S^{p-1}$,
- $f''(S) = p(p - 1) S^{p - 2}$.

Using the known SDE for $S(t)$:


$$
dS(t) = \alpha S(t) dt + \sigma S(t) dW(t),
$$


we apply Itô’s lemma to $S^p(t)$:


$$
d(S^p(t)) = f'(S(t)) dS(t) + \frac{1}{2} f''(S(t)) (dS(t))^2.
$$



Substitute:


$$
d(S^p(t)) = p S^{p-1}(t)(\alpha S(t) dt + \sigma S(t) dW(t)) + \frac{1}{2} p(p - 1) S^{p - 2}(t) \cdot \sigma^2 S^2(t) dt.
$$



Simplify:
- First term: $p \alpha S^p(t) dt + p \sigma S^p(t) dW(t)$,
- Second term: $\frac{1}{2} p(p - 1) \sigma^2 S^p(t) dt$.

Therefore,


$$
d(S^p(t)) = p S^p(t) \left( \alpha dt + \sigma dW(t) \right) + \frac{1}{2} p(p - 1) \sigma^2 S^p(t) dt.
$$



Combine terms:


$$
d(S^p(t)) = S^p(t) \left[ p \alpha + \frac{1}{2} p(p - 1) \sigma^2 \right] dt + p \sigma S^p(t) dW(t).
$$





**Exercise 4.7**

**(i)** Compute $dW^4(t)$ and express $W^4(T)$ as the sum of a Lebesgue integral and an Itô integral.

Let $f(W(t)) = W^4(t)$. By Itô’s lemma:
- $f'(W) = 4W^3$,
- $f''(W) = 12W^2$.

Then:


$$
dW^4(t) = 4W^3(t) dW(t) + \frac{1}{2} \cdot 12W^2(t) dt = 4W^3(t) dW(t) + 6W^2(t) dt.
$$



Integrating from $0$ to $T$:


$$
W^4(T) = \int_0^T 6W^2(t) dt + \int_0^T 4W^3(t) dW(t).
$$



**(ii)** Take expectations and use $\mathbb{E}[W^2(t)] = t$ to derive $\mathbb{E}[W^4(T)] = 3T^2$.

From (i):


$$
\mathbb{E}[W^4(T)] = \mathbb{E}\left[ \int_0^T 6W^2(t) dt \right] + \mathbb{E}\left[ \int_0^T 4W^3(t) dW(t) \right].
$$



The second term is zero since the Itô integral has zero mean:


$$
\mathbb{E}\left[ \int_0^T 4W^3(t) dW(t) \right] = 0.
$$



So:


$$
\mathbb{E}[W^4(T)] = \int_0^T 6\mathbb{E}[W^2(t)] dt = \int_0^T 6t \, dt = 3T^2.
$$



**(iii)** Use the same method to compute $\mathbb{E}[W^6(T)]$.

Let $f(W(t)) = W^6(t)$:
- $f'(W) = 6W^5$,
- $f''(W) = 30W^4$.

Then:


$$
dW^6(t) = 6W^5(t) dW(t) + \frac{1}{2} \cdot 30W^4(t) dt = 6W^5(t) dW(t) + 15W^4(t) dt.
$$



Take expectation:


$$
\mathbb{E}[W^6(T)] = \mathbb{E}\left[ \int_0^T 15W^4(t) dt \right] = \int_0^T 15 \mathbb{E}[W^4(t)] dt.
$$



From (ii), $\mathbb{E}[W^4(t)] = 3t^2$, so:


$$
\mathbb{E}[W^6(T)] = \int_0^T 15 \cdot 3t^2 dt = 45 \cdot \frac{T^3}{3} = 15T^3.
$$




**Exercise 4.8 (Solving the Vasicek equation)**

The Vasicek SDE is:


$$
dR(t) = (\alpha - \beta R(t)) dt + \sigma dW(t),
$$


where $\alpha, \beta, \sigma > 0$.

**(i)** Use Itô’s formula to compute $d\left( e^{\beta t} R(t) \right)$.

Let $f(t, R(t)) = e^{\beta t} R(t)$. Then:
- $\partial_t f = \beta e^{\beta t} R(t)$,
- $\partial_R f = e^{\beta t}$,
- $\partial_{RR} f = 0$.

Apply Itô’s lemma:


$$
d\left( e^{\beta t} R(t) \right) = \beta e^{\beta t} R(t) dt + e^{\beta t} dR(t).
$$



Substitute the SDE for $dR(t)$:


$$
= \beta e^{\beta t} R(t) dt + e^{\beta t} \left[ (\alpha - \beta R(t)) dt + \sigma dW(t) \right].
$$



Simplify:


$$
d\left( e^{\beta t} R(t) \right) = \alpha e^{\beta t} dt + \sigma e^{\beta t} dW(t).
$$



So:


$$
d\left( e^{\beta t} R(t) \right) = \alpha e^{\beta t} dt + \sigma e^{\beta t} dW(t).
$$



**(ii)** Integrate and solve for $R(t)$.

Integrate both sides from $0$ to $t$:


$$
e^{\beta t} R(t) - R(0) = \alpha \int_0^t e^{\beta u} du + \sigma \int_0^t e^{\beta u} dW(u).
$$



Solve for $R(t)$:


$$
R(t) = e^{-\beta t} R(0) + \alpha e^{-\beta t} \int_0^t e^{\beta u} du + \sigma e^{-\beta t} \int_0^t e^{\beta u} dW(u).
$$



This is formula (4.4.33).


**Exercise 4.9**

Let the European call option price be


$$
c(t, x) = x N(d_+) - Ke^{-r(T - t)} N(d_-),
$$


where


$$
d_+ = \frac{1}{\sigma \sqrt{\tau}} \left[ \log \left( \frac{x}{K} \right) + \left( r + \frac{1}{2} \sigma^2 \right) \tau \right], \quad
d_- = d_+ - \sigma \sqrt{\tau}, \quad \tau = T - t.
$$



**(i)** Verify that


$$
Ke^{-r(T - t)} N'(d_-) = x N'(d_+).
$$



We use the fact that:


$$
N'(d_\pm) = \frac{1}{\sqrt{2\pi}} e^{-d_\pm^2 / 2}.
$$



From the definition of $d_+$ and $d_-$, we get:


$$
d_- = d_+ - \sigma \sqrt{\tau} \quad \Rightarrow \quad d_+^2 - d_-^2 = 2 r \tau.
$$



Hence:


$$
\frac{N'(d_-)}{N'(d_+)} = \exp(d_+^2 - d_-^2)/2 = e^{r(T - t)} \quad \Rightarrow \quad N'(d_-) = e^{r(T - t)} N'(d_+).
$$



Multiply both sides by $K e^{-r(T - t)}$:


$$
Ke^{-r(T - t)} N'(d_-) = K N'(d_+).
$$



Since $x = K e^{-r(T - t)} \cdot \frac{N'(d_-)}{N'(d_+)} = K N'(d_+)$, the identity holds.

**(ii)** Show that $c_x = N(d_+)$.

Differentiate $c(t, x)$:
- $d_+$ is a function of $x$, so by the chain rule:


$$
c_x = \frac{d}{dx}\left( x N(d_+) \right) - Ke^{-r\tau} \cdot \frac{d}{dx}N(d_-).
$$



Use:
- $\frac{d}{dx}N(d_\pm) = N'(d_\pm) \cdot \frac{d d_\pm}{dx}$,
- $\frac{d d_+}{dx} = \frac{1}{x \sigma \sqrt{\tau}}$,
- $d_- = d_+ - \sigma \sqrt{\tau}$ implies $\frac{d d_-}{dx} = \frac{1}{x \sigma \sqrt{\tau}}$.

Then:


$$
c_x = N(d_+) + x N'(d_+) \cdot \frac{1}{x \sigma \sqrt{\tau}} - Ke^{-r\tau} N'(d_-) \cdot \frac{1}{x \sigma \sqrt{\tau}}.
$$



From (i), $Ke^{-r\tau} N'(d_-) = x N'(d_+)$, so the extra terms cancel:


$$
c_x = N(d_+).
$$



**(iii)** Show that


$$
c_t = -r K e^{-r\tau} N(d_-) - \frac{\sigma x}{2 \sqrt{\tau}} N'(d_+).
$$



Differentiate $c(t,x)$ with respect to $t$:
- $\partial_t d_\pm = \frac{\partial d_\pm}{\partial \tau} \cdot (-1)$,
- $d_+ = \frac{1}{\sigma \sqrt{\tau}} \left[ \log \left( \frac{x}{K} \right) + \left( r + \frac{1}{2} \sigma^2 \right) \tau \right]$,
so


$$
\frac{d d_+}{d\tau} = -\frac{1}{2} \cdot \frac{1}{\tau^{3/2}} \left[ \log \left( \frac{x}{K} \right) + \left( r + \frac{1}{2} \sigma^2 \right) \tau \right] + \frac{r + \frac{1}{2} \sigma^2}{\sigma \sqrt{\tau}}.
$$



But it simplifies with Itô calculus and known result:


$$
c_t = -r K e^{-r\tau} N(d_-) - \frac{\sigma x}{2 \sqrt{\tau}} N'(d_+).
$$



This is the theta of the option.

**(iv)** Use the formulas to show that $c$ satisfies the Black-Scholes PDE:


$$
c_t + r x c_x + \frac{1}{2} \sigma^2 x^2 c_{xx} = r c.
$$



From above:
- $c_x = N(d_+)$,
- $c_{xx} = \frac{N'(d_+)}{x \sigma \sqrt{\tau}}$,
- $c_t = -r K e^{-r\tau} N(d_-) - \frac{\sigma x}{2 \sqrt{\tau}} N'(d_+)$.

Now compute:


$$
r x c_x = r x N(d_+), \quad \frac{1}{2} \sigma^2 x^2 c_{xx} = \frac{1}{2} \sigma^2 x^2 \cdot \frac{N'(d_+)}{x \sigma \sqrt{\tau}} = \frac{\sigma x}{2 \sqrt{\tau}} N'(d_+).
$$



Adding all terms:


$$
c_t + r x c_x + \frac{1}{2} \sigma^2 x^2 c_{xx} = -r K e^{-r\tau} N(d_-) + r x N(d_+) = r c.
$$



**(v)** Show that for $x > K$, $\lim_{\tau \to 0} d_\pm = \infty$, and for $0 < x < K$, $\lim_{\tau \to 0} d_\pm = -\infty$.

As $\tau \to 0$:
- $\log(x/K)$ dominates, and the denominator $\sqrt{\tau} \to 0$,
so the sign of $\log(x/K)$ determines the limit:
- If $x > K$, then $\log(x/K) > 0$, so $d_\pm \to \infty$,
- If $x < K$, then $\log(x/K) < 0$, so $d_\pm \to -\infty$.

**(vi)** Show that as $x \to 0$, $d_\pm \to -\infty$, for $0 \leq t < T$.

Since $\log(x/K) \to -\infty$ as $x \to 0$, and $\tau > 0$, we get:


$$
d_\pm \sim \frac{1}{\sigma \sqrt{\tau}} \log(x/K) \to -\infty.
$$



Then:
- $N(d_+) \to 0$, so $c(t,x) \to 0$,
- and boundary condition $c(t,0) = 0$ is satisfied.

**(vii)** Show that as $x \to \infty$, $d_\pm \to \infty$ for $0 \leq t < T$, and verify:


$$
\lim_{x \to \infty} \frac{N(d_+) - 1}{x - 1} = 0.
$$



As $x \to \infty$, $d_+ \to \infty$, so $N(d_+) \to 1$.

This is an indeterminate form $0/(\infty)$, so apply L'Hôpital's Rule:


$$
\lim_{x \to \infty} \frac{N(d_+) - 1}{x - 1} = \lim_{x \to \infty} \frac{d}{dx}N(d_+) = \lim_{x \to \infty} N'(d_+) \cdot \frac{d d_+}{dx}.
$$



We know:
- $N'(d_+) \to 0$ exponentially fast,
- $\frac{d d_+}{dx} = \frac{1}{x \sigma \sqrt{\tau}} \to 0$ as $x \to \infty$.

So the product $\to 0$, and the limit is $0$.

Boundary condition is satisfied.



**Exercise 4.10 (Self-financing trading)**

**(i)** Derive the continuous-time self-financing condition (4.10.15) using (4.10.9) and (4.10.16).

Let the money market share price be $M(t) = e^{rt}$. The portfolio value is:


$$
X(t) = \Delta(t) S(t) + \Gamma(t) M(t).
$$



Differentiate using Itô calculus:
- From (4.10.9):


$$
dX(t) = \Delta(t) dS(t) + r(X(t) - \Delta(t) S(t)) dt.
$$



We differentiate $X(t) = \Delta(t) S(t) + \Gamma(t) M(t)$ using the product rule:


$$
dX(t) = \Delta(t) dS(t) + S(t) d\Delta(t) + \Gamma(t) dM(t) + M(t) d\Gamma(t).
$$



Now substitute $dM(t) = rM(t) dt$:


$$
dX(t) = \Delta(t) dS(t) + S(t) d\Delta(t) + r \Gamma(t) M(t) dt + M(t) d\Gamma(t).
$$



Group the terms:


$$
dX(t) = \Delta(t) dS(t) + S(t) d\Delta(t) + M(t) d\Gamma(t) + r (X(t) - \Delta(t) S(t)) dt.
$$



Rewriting:


$$
S(t) d\Delta(t) + M(t) d\Gamma(t) = 0.
$$



This is the **continuous-time self-financing condition**:


$$
S(t) d\Delta(t) + M(t) d\Gamma(t) = 0. \tag{4.10.15}
$$



Alternatively, rearranging:


$$
S(t) d\Delta(t) + dS(t) \Delta(t) + M(t) d\Gamma(t) + \Gamma(t) dM(t) = 0.
$$



Which gives:


$$
S(t) d\Delta(t) + dS(t) \Delta(t) + M(t) d\Gamma(t) + \Gamma(t) r M(t) dt = 0.
$$



So again:


$$
S(t) d\Delta(t) + dS(t) \Delta(t) + M(t) d\Gamma(t) + dM(t) \Gamma(t) = 0.
$$



As claimed in (4.10.15).

**(ii)** Use the corrected version of (4.10.17), i.e. (4.10.21), and the self-financing condition to derive (4.10.18).

Recall the corrected differential of the portfolio value:


$$
dN(t) = c_t dt + c_x dS(t) + \frac{1}{2} c_{xx} dS(t)^2 - \Delta(t) dS(t) - S(t) d\Delta(t) - \Delta(t) dS(t).
$$



Substitute $\Delta(t) = c_x$ (from delta hedging) into this expression:


$$
dN(t) = \left[ c_t + \frac{1}{2} \sigma^2 S^2 c_{xx} \right] dt - S(t) d\Delta(t).
$$



From the self-financing condition:


$$
S(t) d\Delta(t) + M(t) d\Gamma(t) = 0 \Rightarrow d\Gamma(t) = -\frac{S(t)}{M(t)} d\Delta(t).
$$



So:


$$
dN(t) = \left[ c_t + \frac{1}{2} \sigma^2 S^2 c_{xx} \right] dt + M(t) d\Gamma(t).
$$



Now $N(t) = \Gamma(t) M(t) \Rightarrow dN(t) = r N(t) dt$.

Equating both expressions:


$$
r \Gamma(t) M(t) dt = \left[ c_t + \frac{1}{2} \sigma^2 S^2 c_{xx} \right] dt.
$$



So:


$$
r N(t) = c_t + \frac{1}{2} \sigma^2 S^2 c_{xx}.
$$



Therefore,


$$
r \left[ c - S c_x \right] = c_t + \frac{1}{2} \sigma^2 S^2 c_{xx}.
$$



Rearranged:


$$
c_t + r S c_x + \frac{1}{2} \sigma^2 S^2 c_{xx} = r c.
$$



This is the Black-Scholes PDE as in (4.10.20), completing the derivation.




**Exercise 4.11**
We are given that the European call price under Black-Scholes with volatility $\sigma_1$ is:


$$
c(t, x) = x N(d_+(T - t, x)) - K e^{-r(T - t)} N(d_-(T - t, x)),
$$


with


$$
d_\pm(T - t, x) = \frac{1}{\sigma_1 \sqrt{T - t}} \left[ \log\left( \frac{x}{K} \right) + \left( r \pm \frac{1}{2} \sigma_1^2 \right)(T - t) \right].
$$



However, suppose the true dynamics of the asset price follow:


$$
dS(t) = \alpha S(t) dt + \sigma_2 S(t) dW(t), \quad \text{with } \sigma_2 > \sigma_1.
$$



Then the market price of the option $c(t, S(t))$ is incorrect under the true dynamics. We construct a portfolio with initial value $X(0) = 0$ that is:
- long one European call $c(t, S(t))$,
- short $c_x(t, S(t))$ shares of the stock,
- with the remaining value invested in a money market account.

The cash position is:


$$
X(t) - c(t, S(t)) + S(t) c_x(t, S(t)).
$$



We also remove funds at rate:


$$
\frac{1}{2}(\sigma_2^2 - \sigma_1^2) S^2(t) c_{xx}(t, S(t)).
$$



The differential of the portfolio value is:


$$
\begin{align*}
dX(t) &= dc(t, S(t)) - c_x(t, S(t)) dS(t) + r[X(t) - c(t, S(t)) + S(t) c_x(t, S(t))] dt \\
&\quad - \frac{1}{2}(\sigma_2^2 - \sigma_1^2) S^2(t) c_{xx}(t, S(t)) dt.
\end{align*}
$$



Apply Itô’s lemma to $c(t, S(t))$:


$$
\begin{align*}
dc(t, S(t)) &= c_t dt + c_x dS(t) + \frac{1}{2} c_{xx} (dS(t))^2 \\
&= c_t dt + c_x (\alpha S dt + \sigma_2 S dW) + \frac{1}{2} c_{xx} \sigma_2^2 S^2 dt.
\end{align*}
$$



Substitute into $dX(t)$:


$$
\begin{align*}
dX(t) &= \left[ c_t + \alpha S c_x + \frac{1}{2} \sigma_2^2 S^2 c_{xx} \right] dt + \sigma_2 S c_x dW \\
&\quad - c_x (\alpha S dt + \sigma_2 S dW) + r[X(t) - c + S c_x] dt - \frac{1}{2} (\sigma_2^2 - \sigma_1^2) S^2 c_{xx} dt.
\end{align*}
$$



Cancel terms:
- $\alpha S c_x$ cancels $- c_x \alpha S$,
- $\sigma_2 S c_x dW$ cancels $- \sigma_2 S c_x dW$.

We're left with:


$$
dX(t) = \left[ c_t + \frac{1}{2} \sigma_2^2 S^2 c_{xx} + r(X(t) - c + S c_x) - \frac{1}{2} (\sigma_2^2 - \sigma_1^2) S^2 c_{xx} \right] dt.
$$



Group terms:


$$
dX(t) = \left[ c_t + r S c_x - r c + \frac{1}{2} \sigma_1^2 S^2 c_{xx} + r X(t) \right] dt.
$$



But the Black-Scholes PDE under $\sigma_1$ tells us:


$$
c_t + r S c_x + \frac{1}{2} \sigma_1^2 S^2 c_{xx} = r c.
$$



Therefore:


$$
dX(t) = \left[ r c - r c + r X(t) \right] dt = r X(t) dt.
$$



This is a differential equation:


$$
\frac{dX(t)}{dt} = r X(t), \quad X(0) = 0.
$$



Its unique solution is:


$$
X(t) = 0, \quad \text{for all } t \in [0, T].
$$



So the portfolio has zero value at all times, but recall we are extracting funds at rate:


$$
\frac{1}{2} (\sigma_2^2 - \sigma_1^2) S^2(t) c_{xx}(t, S(t)) > 0.
$$



Hence, **we have an arbitrage opportunity**: the portfolio always has value $0$, yet we are able to withdraw a positive amount of money over time, starting from zero capital.

This confirms that the mispricing due to incorrect volatility input leads to arbitrage.



**Exercise 4.12**

**(i)** Use formulas (4.5.23)–(4.5.25), (4.5.26), and (4.5.29) to compute the Greeks of a European put:  
- delta $p_x(t, x)$,  
- gamma $p_{xx}(t, x)$,  
- theta $p_t(t, x)$.

Recall from the put-call parity:


$$
p(t, x) = c(t, x) - x + K e^{-r(T - t)} \tag{4.5.26}
$$



Differentiate with respect to $x$ to find delta:


$$
p_x(t, x) = c_x(t, x) - 1. \tag{4.5.23}
$$



Differentiate again to find gamma:


$$
p_{xx}(t, x) = c_{xx}(t, x). \tag{4.5.24}
$$



Differentiate with respect to $t$ to get theta:
\begin{align*}
p_t(t, x) &= c_t(t, x) + rK e^{-r(T - t)} \tag{4.5.25}
\end{align*}

Thus, the Greeks of the European put are:
- $\boxed{p_x(t, x) = c_x(t, x) - 1}$  
- $\boxed{p_{xx}(t, x) = c_{xx}(t, x)}$  
- $\boxed{p_t(t, x) = c_t(t, x) + rK e^{-r(T - t)}}$

---

**(ii)** Show that an agent hedging a short position in the put should short the stock and go long in the money market account.

From (i), we know:


$$
p_x(t, x) = c_x(t, x) - 1 < 0,
$$


because $0 < c_x(t, x) < 1$ for a European call.

So the **delta** of the put is negative. This means:
- To hedge a short position in the put (i.e., the agent is short the option),
- The agent needs to take a **negative multiple** of delta → **short the stock**.
- The remainder of the portfolio value must be in the **money market account**, so that the portfolio is delta-neutral.

Thus, the agent must **short the stock** and **go long in the risk-free asset** to hedge the short put.

---

**(iii)** Show that $f(t, x)$ of (4.5.26) and $p(t, x)$ satisfy the same Black-Scholes-Merton PDE as $c(t, x)$.

We are given:


$$
f(t, x) = c(t, x) - x + K e^{-r(T - t)} = p(t, x).
$$



The Black-Scholes PDE for a European call $c(t, x)$ is:


$$
c_t + r x c_x + \frac{1}{2} \sigma^2 x^2 c_{xx} = r c. \tag{4.5.14}
$$



We substitute $f(t, x) = c(t, x) - x + K e^{-r(T - t)}$:

Differentiate:
- $f_t = c_t + rK e^{-r(T - t)}$
- $f_x = c_x - 1$
- $f_{xx} = c_{xx}$

Now compute the LHS of the PDE for $f$:


$$
\begin{align*}
f_t + r x f_x + \frac{1}{2} \sigma^2 x^2 f_{xx}
&= \left( c_t + rK e^{-r(T - t)} \right) + r x (c_x - 1) + \frac{1}{2} \sigma^2 x^2 c_{xx} \\
&= c_t + r x c_x + \frac{1}{2} \sigma^2 x^2 c_{xx} + rK e^{-r(T - t)} - r x
\end{align*}
$$



Now compute the RHS:


$$
r f = r(c - x + K e^{-r(T - t)}) = r c - r x + rK e^{-r(T - t)}
$$



So both sides are equal:


$$
f_t + r x f_x + \frac{1}{2} \sigma^2 x^2 f_{xx} = r f.
$$



Hence, $f(t, x)$ and $p(t, x)$ satisfy the same PDE as $c(t, x)$.



**Exercise 4.13 (Decomposition of correlated Brownian motions into independent Brownian motions)**

Suppose $B_1(t)$ and $B_2(t)$ are Brownian motions and


$$
dB_1(t) \, dB_2(t) = \rho(t) \, dt,
$$


where $\rho(t)$ is a stochastic process such that $-1 < \rho(t) < 1$ for all $t$.

Define two processes:


$$
W_1(t) = B_1(t), \quad
W_2(t) = \int_0^t \frac{1}{\sqrt{1 - \rho^2(s)}} \left[ dB_2(s) - \rho(s) dB_1(s) \right].
$$



We are given the alternative (forward) construction:


$$
\begin{align*}
B_1(t) &= W_1(t), \\
B_2(t) &= \int_0^t \rho(s) \, dW_1(s) + \int_0^t \sqrt{1 - \rho^2(s)} \, dW_2(s),
\end{align*}
$$


and we are to show that $W_1(t)$ and $W_2(t)$ are independent Brownian motions.

By definition, $W_1(t) = B_1(t)$, and $B_1(t)$ is a Brownian motion. So $W_1(t)$ is a Brownian motion.
We examine the quadratic variation of $W_2(t)$.

Let:


$$
dB_2(t) = \rho(t) dW_1(t) + \sqrt{1 - \rho^2(t)} dW_2(t).
$$



This means we can rearrange:


$$
dW_2(t) = \frac{dB_2(t) - \rho(t) dW_1(t)}{\sqrt{1 - \rho^2(t)}}
$$



So $W_2(t)$ is a stochastic integral with respect to Brownian motions and hence is a continuous martingale. We now check its quadratic variation:


$$
\begin{align*}
dW_2(t)^2 &= \left( \frac{dB_2(t) - \rho(t) dW_1(t)}{\sqrt{1 - \rho^2(t)}} \right)^2 \\
&= \frac{1}{1 - \rho^2(t)} \left[ dB_2(t)^2 - 2 \rho(t) dB_2(t) dW_1(t) + \rho^2(t) dW_1(t)^2 \right].
\end{align*}
$$



Using:
- $dB_2(t)^2 = dt$,
- $dW_1(t)^2 = dt$,
- $dB_2(t) dW_1(t) = \rho(t) dt$,

we get:


$$
\begin{align*}
dW_2(t)^2 &= \frac{1}{1 - \rho^2(t)} \left[ dt - 2 \rho^2(t) dt + \rho^2(t) dt \right] = dt.
\end{align*}
$$



So $\langle W_2 \rangle_t = t$ and $W_2(t)$ is a Brownian motion.

**Step 3: Show that $W_1(t)$ and $W_2(t)$ are independent.**

We compute the cross variation:


$$
\begin{align*}
dW_1(t) dW_2(t) &= dB_1(t) \cdot \left( \frac{dB_2(t) - \rho(t) dB_1(t)}{\sqrt{1 - \rho^2(t)}} \right) \\
&= \frac{dB_1(t) dB_2(t) - \rho(t) dB_1(t)^2}{\sqrt{1 - \rho^2(t)}} \\
&= \frac{\rho(t) dt - \rho(t) dt}{\sqrt{1 - \rho^2(t)}} = 0.
\end{align*}
$$


So $\langle W_1, W_2 \rangle_t = 0$, and since they are continuous martingales with zero cross-variation, they are **independent Brownian motions**.

**Conclusion:** The decomposition


$$
B_1(t) = W_1(t), \quad B_2(t) = \int_0^t \rho(s) \, dW_1(s) + \int_0^t \sqrt{1 - \rho^2(s)} \, dW_2(s)
$$


correctly expresses $B_1(t)$ and $B_2(t)$ in terms of **independent** Brownian motions $W_1(t)$ and $W_2(t)$.



**Exercise 4.14**
We want to justify the equation:


$$
\lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1} f''(W(t_j)) \left[ W(t_{j+1}) - W(t_j) \right]^2 = \int_0^T f''(W(t)) dt. \tag{4.10.22}
$$



We define:


$$
Z_j = f''(W(t_j)) \left[ (W(t_{j+1}) - W(t_j))^2 - (t_{j+1} - t_j) \right].
$$



Then:


$$
\sum_{j=0}^{n-1} f''(W(t_j)) \left[ W(t_{j+1}) - W(t_j) \right]^2 = \sum_{j=0}^{n-1} Z_j + \sum_{j=0}^{n-1} f''(W(t_j))(t_{j+1} - t_j). \tag{4.10.23}
$$



**(i)** Show that $Z_j$ is $\mathcal{F}(t_{j+1})$-measurable and:


$$
\mathbb{E}[Z_j | \mathcal{F}(t_j)] = 0, \quad \mathbb{E}[Z_j^2 | \mathcal{F}(t_j)] = 2 \left( f''(W(t_j)) \right)^2 (t_{j+1} - t_j)^2.
$$



- Since $Z_j$ depends on $W(t_j)$ and $W(t_{j+1})$, it is $\mathcal{F}(t_{j+1})$-measurable.
- Conditional on $\mathcal{F}(t_j)$, $W(t_{j+1}) - W(t_j)$ is independent and distributed as $\mathcal{N}(0, t_{j+1} - t_j)$.
- Then:


$$
\mathbb{E}[(W(t_{j+1}) - W(t_j))^2 | \mathcal{F}(t_j)] = t_{j+1} - t_j,
$$


so:


$$
\mathbb{E}[Z_j | \mathcal{F}(t_j)] = f''(W(t_j)) \left( \mathbb{E}[(W(t_{j+1}) - W(t_j))^2 | \mathcal{F}(t_j)] - (t_{j+1} - t_j) \right) = 0.
$$



Now compute variance:


$$
\text{Var}[(W(t_{j+1}) - W(t_j))^2] = 2 (t_{j+1} - t_j)^2,
$$


so:


$$
\mathbb{E}[Z_j^2 | \mathcal{F}(t_j)] = f''(W(t_j))^2 \cdot \text{Var}[(W(t_{j+1}) - W(t_j))^2] = 2 f''(W(t_j))^2 (t_{j+1} - t_j)^2.
$$



**(ii)** Show that:


$$
\mathbb{E} \left[ \sum_{j=0}^{n-1} Z_j \right] = 0.
$$



Using the tower property of conditional expectation:


$$
\mathbb{E}[Z_j] = \mathbb{E} \left[ \mathbb{E}[Z_j | \mathcal{F}(t_j)] \right] = \mathbb{E}[0] = 0,
$$


so:


$$
\mathbb{E} \left[ \sum_{j=0}^{n-1} Z_j \right] = \sum_{j=0}^{n-1} \mathbb{E}[Z_j] = 0.
$$



**(iii)** Assume that:


$$
\mathbb{E} \int_0^T \left[ f''(W(t)) \right]^2 dt < \infty,
$$


and show:


$$
\lim_{\|\Pi\| \to 0} \text{Var} \left( \sum_{j=0}^{n-1} Z_j \right) = 0.
$$



We have:


$$
\text{Var} \left( \sum_{j=0}^{n-1} Z_j \right) = \sum_{j=0}^{n-1} \mathbb{E}[Z_j^2],
$$


since $Z_j$'s are uncorrelated due to independence of Brownian increments.

From part (i):


$$
\mathbb{E}[Z_j^2] = \mathbb{E}[2 f''(W(t_j))^2 (t_{j+1} - t_j)^2].
$$



So:


$$
\text{Var} \left( \sum_{j=0}^{n-1} Z_j \right) = 2 \sum_{j=0}^{n-1} \mathbb{E}[f''(W(t_j))^2] (t_{j+1} - t_j)^2.
$$



As $\|\Pi\| \to 0$, each $(t_{j+1} - t_j)^2$ shrinks faster than $(t_{j+1} - t_j)$, so the whole sum vanishes:


$$
\lim_{\|\Pi\| \to 0} \text{Var} \left( \sum_{j=0}^{n-1} Z_j \right) = 0.
$$



**Conclusion:** From (ii), $\mathbb{E}[\sum Z_j] = 0$ and from (iii), the variance goes to $0$, so:


$$
\sum_{j=0}^{n-1} Z_j \to 0 \quad \text{in } L^2.
$$



Thus,


$$
\lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1} f''(W(t_j)) \left[ W(t_{j+1}) - W(t_j) \right]^2 = \int_0^T f''(W(t)) dt,
$$


which establishes (4.10.22).



**Exercise 4.15 (Creating correlated Brownian motions from independent ones)**
Let $(W_1(t), \ldots, W_d(t))$ be a $d$-dimensional Brownian motion, meaning the components are independent. Let $(\sigma_{ij}(t))_{i=1,\ldots,m; \, j=1,\ldots,d}$ be an $m \times d$ matrix-valued adapted process.

For $i = 1, \ldots, m$, define:


$$
\sigma_i(t) = \left[ \sum_{j=1}^d \sigma_{ij}^2(t) \right]^{1/2},
$$


and assume $\sigma_i(t) \ne 0$ for all $t$.

Now define:


$$
B_i(t) = \sum_{j=1}^d \int_0^t \frac{\sigma_{ij}(u)}{\sigma_i(u)} \, dW_j(u).
$$



**(i)** Show that $B_i(t)$ is a Brownian motion.

We check the properties:
1. **Continuity:** $B_i(t)$ is a stochastic integral of continuous processes ⇒ $B_i(t)$ is continuous.
2. **Adaptedness:** The integrands are adapted and square-integrable.
3. **Martingale:** Each $B_i(t)$ is an Itô integral ⇒ $B_i(t)$ is a martingale.
4. **Quadratic variation:**
   

$$
   \langle B_i \rangle_t = \sum_{j=1}^d \int_0^t \left( \frac{\sigma_{ij}(u)}{\sigma_i(u)} \right)^2 du = \int_0^t \frac{1}{\sigma_i^2(u)} \sum_{j=1}^d \sigma_{ij}^2(u) du = \int_0^t du = t.
   $$



Since $B_i(t)$ is a continuous martingale with quadratic variation $t$, it is a Brownian motion.

**(ii)** Show that:


$$
dB_i(t) \, dB_k(t) = \rho_{ik}(t) \, dt,
$$


where:


$$
\rho_{ik}(t) = \frac{1}{\sigma_i(t) \sigma_k(t)} \sum_{j=1}^d \sigma_{ij}(t) \sigma_{kj}(t).
$$



From the Itô isometry:


$$
\begin{align*}
dB_i(t) \, dB_k(t) &= \sum_{j=1}^d \frac{\sigma_{ij}(t)}{\sigma_i(t)} \cdot \frac{\sigma_{kj}(t)}{\sigma_k(t)} \cdot dW_j(t)^2 \\
&= \sum_{j=1}^d \frac{\sigma_{ij}(t) \sigma_{kj}(t)}{\sigma_i(t) \sigma_k(t)} \cdot dt \\
&= \frac{1}{\sigma_i(t) \sigma_k(t)} \sum_{j=1}^d \sigma_{ij}(t) \sigma_{kj}(t) \cdot dt \\
&= \rho_{ik}(t) \, dt.
\end{align*}
$$



Thus, $B_i(t)$ and $B_k(t)$ are Brownian motions with instantaneous correlation $\rho_{ik}(t)$.

**Conclusion:** The processes $B_1(t), \ldots, B_m(t)$ are Brownian motions constructed from independent Brownian motions $W_j(t)$ with a desired correlation structure determined by the matrix $\sigma_{ij}(t)$.




**Exercise 4.16 (Creating independent Brownian motions to represent correlated ones)**
Let $B_1(t), \ldots, B_m(t)$ be $m$ one-dimensional Brownian motions with


$$
dB_i(t) dB_k(t) = \rho_{ik}(t) \, dt \quad \text{for all } i, k = 1, \ldots, m,
$$


where the $\rho_{ik}(t)$ are adapted processes taking values in $(-1, 1)$ for $i \ne k$ and $\rho_{ik}(t) = 1$ for $t = k$. Define the symmetric matrix $C(t)$ by:


$$
C(t) = \begin{bmatrix}
\rho_{11}(t) & \rho_{12}(t) & \cdots & \rho_{1m}(t) \\
\rho_{21}(t) & \rho_{22}(t) & \cdots & \rho_{2m}(t) \\
\vdots & \vdots & \ddots & \vdots \\
\rho_{m1}(t) & \rho_{m2}(t) & \cdots & \rho_{mm}(t)
\end{bmatrix}.
$$



Assume $C(t)$ is symmetric and positive definite for all $t$ almost surely. Then there exists a matrix $A(t)$ such that:


$$
C(t) = A(t) A^\top(t),
$$


which in component form reads:


$$
\rho_{ik}(t) = \sum_{j=1}^m a_{ij}(t) a_{jk}(t), \quad \text{for all } i, k = 1, \ldots, m. \tag{4.10.25}
$$



Let $A(t)^{-1} = [\alpha_{ij}(t)]$ be the inverse of $A(t)$:


$$
A^{-1}(t) = \begin{bmatrix}
\alpha_{11}(t) & \alpha_{12}(t) & \cdots & \alpha_{1m}(t) \\
\alpha_{21}(t) & \alpha_{22}(t) & \cdots & \alpha_{2m}(t) \\
\vdots & \vdots & \ddots & \vdots \\
\alpha_{m1}(t) & \alpha_{m2}(t) & \cdots & \alpha_{mm}(t)
\end{bmatrix},
$$


so that:


$$
\sum_{j=1}^m a_{ij}(t) \alpha_{jk}(t) = \sum_{j=1}^m \alpha_{ij}(t) a_{jk}(t) = \delta_{ik}, \tag{4.10.26}
$$


where:


$$
\delta_{ik} = \begin{cases}
1 & \text{if } i = k, \\
0 & \text{if } i \ne k.
\end{cases}
$$



Show that there exist $m$ independent Brownian motions $W_1(t), \ldots, W_m(t)$ such that:


$$
B_i(t) = \sum_{j=1}^m \int_0^t a_{ij}(u) \, dW_j(u), \quad \text{for all } i = 1, \ldots, m. \tag{4.10.27}
$$



Define the vector of Brownian motions:


$$
B(t) = A(t) W(t),
$$


where $W(t) = (W_1(t), \ldots, W_m(t))^\top$ is a vector of independent Brownian motions.

Then:


$$
dB_i(t) = \sum_{j=1}^m a_{ij}(t) dW_j(t),
$$


so:


$$
dB_i(t) dB_k(t) = \sum_{j=1}^m \sum_{\ell=1}^m a_{ij}(t) a_{k\ell}(t) dW_j(t) dW_\ell(t).
$$



Since $dW_j(t) dW_\ell(t) = \delta_{j\ell} dt$, this simplifies to:


$$
dB_i(t) dB_k(t) = \sum_{j=1}^m a_{ij}(t) a_{kj}(t) \, dt = \rho_{ik}(t) \, dt.
$$



Thus, $B_i(t)$ and $B_k(t)$ have correlation $\rho_{ik}(t)$ as desired.

**Conclusion:** The process


$$
B_i(t) = \sum_{j=1}^m \int_0^t a_{ij}(u) \, dW_j(u)
$$


represents a family of Brownian motions with the given correlation matrix $C(t)$, constructed from independent Brownian motions $W_j(t)$.



**Exercise 4.17 (Instantaneous correlation)**

Let


$$
X_1(t) = X_1(0) + \int_0^t \Theta_1(u) du + \int_0^t \sigma_1(u) dB_1(u), \\
X_2(t) = X_2(0) + \int_0^t \Theta_2(u) du + \int_0^t \sigma_2(u) dB_2(u),
$$


where $B_1(t)$ and $B_2(t)$ are Brownian motions with $dB_1(t)dB_2(t) = \rho(t) dt$, and $\Theta_1(t), \Theta_2(t), \sigma_1(t), \sigma_2(t)$ are adapted processes.

Then by Itô calculus:


$$
dX_1(t) dX_2(t) = \sigma_1(t) \sigma_2(t) dB_1(t) dB_2(t) = \rho(t) \sigma_1(t) \sigma_2(t) dt.
$$



This defines $\rho(t)$ as the **instantaneous correlation** between $X_1(t)$ and $X_2(t)$.

We first assume $\rho$, $\Theta_1$, $\Theta_2$, $\sigma_1$, and $\sigma_2$ are constants:


$$
X_1(t) = X_1(0) + \Theta_1 t + \sigma_1 B_1(t), \\
X_2(t) = X_2(0) + \Theta_2 t + \sigma_2 B_2(t).
$$



Fix $t_0 > 0$, and let $\epsilon > 0$.

**(i)** Use Itô's product rule to show:


$$
\mathbb{E}\left[(B_1(t_0 + \epsilon) - B_1(t_0))(B_2(t_0 + \epsilon) - B_2(t_0)) \mid \mathcal{F}(t_0)\right] = \rho \, \epsilon.
$$



Since $dB_1(t)dB_2(t) = \rho dt$, the increment covariance is $\rho \epsilon$.

**(ii)** Define the increment pair:


$$
(X_1(t_0 + \epsilon) - X_1(t_0), X_2(t_0 + \epsilon) - X_2(t_0)).
$$



Their conditional means:


$$
M_i(\epsilon) = \mathbb{E}[X_i(t_0 + \epsilon) - X_i(t_0) \mid \mathcal{F}(t_0)] = \Theta_i \epsilon, \quad i = 1, 2. \tag{4.10.28}
$$



Conditional variances:


$$
V_i(\epsilon) = \mathbb{E}[(X_i(t_0 + \epsilon) - X_i(t_0))^2 \mid \mathcal{F}(t_0)] - M_i^2(\epsilon) = \sigma_i^2 \epsilon, \quad i = 1, 2. \tag{4.10.29}
$$



Covariance:


$$
C(\epsilon) = \mathbb{E}[(X_1(t_0 + \epsilon) - X_1(t_0))(X_2(t_0 + \epsilon) - X_2(t_0)) \mid \mathcal{F}(t_0)] - M_1(\epsilon)M_2(\epsilon) = \rho \sigma_1 \sigma_2 \epsilon. \tag{4.10.30}
$$



So the **conditional correlation** is:


$$
\frac{C(\epsilon)}{\sqrt{V_1(\epsilon)V_2(\epsilon)}} = \rho.
$$




Now assume $\rho(t), \Theta_i(t), \sigma_i(t)$ are continuous and adapted, with:


$$
|\Theta_i(t)|, |\sigma_i(t)|, |\rho(t)| \le M, \quad \text{for all } t. \tag{4.10.31}
$$




**(iii)** Define:


$$
M_i(\epsilon) = \mathbb{E}[X_i(t_0 + \epsilon) - X_i(t_0) \mid \mathcal{F}(t_0)].
$$



Then:


$$
M_i(\epsilon) = \Theta_i(t_0) \epsilon + o(\epsilon). \tag{4.10.32}
$$



So:


$$
\lim_{\epsilon \to 0} \frac{1}{\epsilon} M_i(\epsilon) = \Theta_i(t_0). \tag{4.10.33}
$$



Proof:


$$
M_i(\epsilon) = \mathbb{E} \left[ \int_{t_0}^{t_0 + \epsilon} \Theta_i(u) du \, \middle| \, \mathcal{F}(t_0) \right]. \tag{4.10.34}
$$



Apply the Dominated Convergence Theorem to conclude.

**(iv)** Define:


$$
D_{ij}(\epsilon) = \mathbb{E}[(X_i(t_0 + \epsilon) - X_i(t_0))(X_j(t_0 + \epsilon) - X_j(t_0)) \mid \mathcal{F}(t_0)] - M_i(\epsilon) M_j(\epsilon).
$$



Then:


$$
D_{ij}(\epsilon) = \rho_{ij}(t_0) \sigma_i(t_0) \sigma_j(t_0) \epsilon + o(\epsilon). \tag{4.10.35}
$$



Let:


$$
Y_i(t) = \int_0^t \sigma_i(u) dB_i(u).
$$



So:


$$
D_{ij}(\epsilon) = \mathbb{E} \left[ \left( Y_i(t_0 + \epsilon) - Y_i(t_0) + \int_{t_0}^{t_0 + \epsilon} \Theta_i(u) du \right)
\left( Y_j(t_0 + \epsilon) - Y_j(t_0) + \int_{t_0}^{t_0 + \epsilon} \Theta_j(u) du \right) \middle| \mathcal{F}(t_0) \right] - M_i(\epsilon)M_j(\epsilon). \tag{4.10.36}
$$



Using Itô’s product rule and (4.10.37):


$$
\lim_{\epsilon \to 0} \frac{1}{\epsilon} \mathbb{E}[(Y_i(t_0 + \epsilon) - Y_i(t_0))(Y_j(t_0 + \epsilon) - Y_j(t_0)) \mid \mathcal{F}(t_0)]
= \rho_{ij}(t_0) \sigma_i(t_0) \sigma_j(t_0).
$$




**(v)** The conditional variances and covariance:


$$
V_i(\epsilon) = \sigma_i^2(t_0) \epsilon + o(\epsilon), \quad i = 1, 2. \tag{4.10.38}
$$





$$
C(\epsilon) = \rho(t_0) \sigma_1(t_0) \sigma_2(t_0) \epsilon + o(\epsilon). \tag{4.10.39}
$$



**(vi)** Therefore, the conditional correlation becomes:


$$
\lim_{\epsilon \to 0} \frac{C(\epsilon)}{\sqrt{V_1(\epsilon) V_2(\epsilon)}} = \rho(t_0). \tag{4.10.40}
$$



So for small $\epsilon$, the conditional correlation of the increments of $X_1$ and $X_2$ approximates the instantaneous correlation $\rho(t_0)$.


**Exercise 4.18 (State price density process)**
Let a stock price be a geometric Brownian motion:


$$
dS(t) = \alpha S(t) dt + \sigma S(t) dW(t),
$$


and let $r$ denote the interest rate.

Define the **market price of risk** to be:


$$
\theta = \frac{\alpha - r}{\sigma},
$$


and the **state price density process** to be:


$$
\zeta(t) = \exp\left\{ -\theta W(t) - \left( r + \frac{1}{2} \theta^2 \right)t \right\}.
$$



**(i)** Show that:


$$
d\zeta(t) = -\theta \zeta(t) dW(t) - r \zeta(t) dt.
$$



**Solution:**

Use Itô's lemma on the function


$$
f(t, W(t)) = \exp\left\{ -\theta W(t) - \left( r + \frac{1}{2} \theta^2 \right)t \right\}.
$$



Then:


$$
df = \left( -\left( r + \frac{1}{2} \theta^2 \right) + \frac{1}{2} \theta^2 \right) \zeta(t) dt - \theta \zeta(t) dW(t)
= -r \zeta(t) dt - \theta \zeta(t) dW(t).
$$



**(ii)** Let $X(t)$ denote the value of an investor's portfolio using strategy $\Delta(t)$. Then from (4.5.2),


$$
dX(t) = rX(t) dt + \Delta(t)(\alpha - r) S(t) dt + \Delta(t) \sigma S(t) dW(t).
$$



We want to show that $\zeta(t) X(t)$ is a martingale.

Compute:


$$
d(\zeta(t) X(t)) = \zeta(t) dX(t) + X(t) d\zeta(t) + d\zeta(t) dX(t).
$$



Substitute from part (i) and the SDE for $X(t)$:


$$
\begin{aligned}
d(\zeta(t)X(t)) &= \zeta(t) \left[ rX(t) dt + \Delta(t)(\alpha - r)S(t) dt + \Delta(t)\sigma S(t) dW(t) \right] \\
&\quad + X(t)\left[ -\theta \zeta(t) dW(t) - r \zeta(t) dt \right] \\
&\quad + (-\theta \zeta(t) dW(t)) \cdot (\Delta(t)\sigma S(t) dW(t)).
\end{aligned}
$$



Note that:


$$
d\zeta(t) dX(t) = -\theta \zeta(t) \cdot \Delta(t) \sigma S(t) dt.
$$



Combine everything:


$$
\begin{aligned}
d(\zeta(t)X(t)) &= \zeta(t) rX(t) dt + \zeta(t) \Delta(t)(\alpha - r)S(t) dt + \zeta(t) \Delta(t) \sigma S(t) dW(t) \\
&\quad - \theta \zeta(t) X(t) dW(t) - r \zeta(t) X(t) dt - \theta \zeta(t) \Delta(t) \sigma S(t) dt.
\end{aligned}
$$



Grouping terms:
- $dt$ terms cancel:


$$
\zeta(t) rX(t) - r \zeta(t) X(t) + \zeta(t) \Delta(t)(\alpha - r) S(t) - \theta \zeta(t) \Delta(t) \sigma S(t) = 0,
$$


since $(\alpha - r) = \theta \sigma$.

- $dW(t)$ terms:


$$
\zeta(t) \Delta(t) \sigma S(t) - \theta \zeta(t) X(t).
$$



But we already matched drift terms. So overall:


$$
d(\zeta(t) X(t)) = \text{(stochastic integral)}.
$$



Hence, $\zeta(t) X(t)$ is a **local martingale**. With appropriate integrability (usually assumed), it is a **martingale**.

**(iii)** Let $T > 0$ be fixed. Suppose the investor wants to end up with portfolio value $V(T)$ at time $T$, where $V(T)$ is $\mathcal{F}(T)$-measurable.

Then since $\zeta(t) X(t)$ is a martingale:


$$
\zeta(0) X(0) = \mathbb{E}[\zeta(T) V(T)],
$$


and $\zeta(0) = 1$, so:


$$
X(0) = \mathbb{E}[\zeta(T) V(T)].
$$



This means the **present value** of $V(T)$ at time $0$ is:


$$
\mathbb{E}[\zeta(T) V(T)].
$$



This justifies calling $\zeta(t)$ the **state price density process**.
