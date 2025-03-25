---
layout: page
title: Chapter 3 - Brownian Motion
description: Notes on Brownian motion and its applications.
parent: course-2
importance: 5
permalink: /notes/course-2/chapter-3-brownian-motion/
nav: false
---

------------------------------------------------------------------------
### Scaled Random Walks 

#### Symmetric Random Walk 
Construct a symmetric random walk by repeatedly tossing a fair coin, (i.e., $p$ is probability of heads, and $q = 1 - p$ is probability of tails). Successive outcomes of the tosses,

$$
\omega = \omega_1 \omega_2 \omega_3 \dots 
$$

$\omega$ is the infinite sequence of coin tosses and $\omega_n$ is outcome of $n$-th toss,

$$
X_j = \begin{cases}
1 & \text{if }\omega_j = H,\\
-1 & \text{if }\omega_j = T
\end{cases}
$$

By default, $M_0 = 0$, thus, we define,

$$
M_k = \sum_{j = 1}^k X_j,\quad k = 1, 2, \dots
$$

$M_k$ is the process that is what we call a **symmetric random walk**. Each toss makes it steps up one unit or down one unit and each of these two possibilities is equally likely. 

```tikz
\begin{document}
\begin{tikzpicture}[scale=2.5]
    \draw[->] (-0.5,0) -- (5.5,0) node[right] {};
    \draw[->] (0,-2.5) -- (0,1.5) node[above] {};
    \draw[very thin,gray!50] (-0.5,-2.5) grid (5.5,1.5);
    \coordinate (M0) at (0,0);
    \coordinate (M1) at (1,1);
    \coordinate (M2) at (2,0);
    \coordinate (M3) at (3,-1);
    \coordinate (M4) at (4,-2);
    \coordinate (M5) at (5,-1);
    \draw[thick] (M0) -- (M1) -- (M2) -- (M3) -- (M4) -- (M5);
    \foreach \i in {0,1,2,3,4,5} {
        \fill (M\i) circle (2pt);
    }
    \node[above left] at (M0) {$M_0$};
    \node[above] at (M1) {$M_1$};
    \node[above] at (M2) {$M_2$};
    \node[below] at (M3) {$M_3$};
    \node[below] at (M4) {$M_4$};
    \node[above] at (M5) {$M_5$};
    \foreach \x in {1,2,3,4,5} {
        \draw (\x,-0.1) -- (\x,0.1);
        \node[below] at (\x,0) {\x};
    }
    \foreach \y in {-2,-1,1} {
        \draw (-0.1,\y) -- (0.1,\y);
        \node[left] at (0,\y) {\y};
    }
\end{tikzpicture}
\end{document}
```

------------------------------------------------------------------------

**Properties of Random Walks**
1. Independent increments, for $0 = k_0 < k_1 < \dots < k_m$,

$$
M_1 = (M_{k_1} - M_{k_0}), (M_{k_2} - M_{k_1}), \dots, (M_{k_m} - M_{k_{m - 1}})
$$

2. Each of the random increments is a random variable that is,

$$
M_{k_{i + 1}} - M_{k_i} = \sum_{j = k_i + 1}^{k_{i + 1}}X_j
$$

which is an increment of the random walk, and is the change in position of the random walk between times $k_i$ and $k_{i + 1}$.
3. Non-overlapping time intervals are independent because they depend on different coin tosses 
4. Each increment $M_{k_{i + 1}} - M_{k _i}$ has expected value 0 and variance $k_{i + 1} - k_i

$$$
Var(X_j) = \mathbb{E}X_j^2 = 1 \implies Var(M_{k_{i + 1}} - M_{k_i}) = \sum_{j = k_{i} + 1}^{k_{i + 1}} Var(X_j) = \sum_{j = k_i + 1}^{k_{i + 1}} 1 = k_{i + 1} - k_i
$$

5. Variance of a symmetric random walk accumulates are rate one per unit time so that variance of the increment over any time interval $k$ to $l$ for non-negative integers $k < l$ is $l - k$
6. A symmetric random walk is a martingale,

$$
\begin{align*}
\mathbb{E}[M_k | \mathcal{F}_k] &= \mathbb{E}[(M_l - M_k) + M_k | \mathcal{F}_k]\\
&= \mathbb{E}[M_l - M_k | \mathcal{F}_k] + \mathbb{E}[M_k | \mathcal{F}_k]\\
&= \mathbb{E}[M_l - M_k | \mathcal{F}_k] + M_k\\
&= \mathbb{E}[M_l - M_k] + M_k = M_k
\end{align*}
$$

Line one results from separating, line 2 results from linearity of conditional expectations, line 3 is because $M_k$ only depends on $\mathcal{F}_k$ i.e., the first $k$ coin tosses by information and conditioning, and line 4 results from independence.

------------------------------------------------------------------------

**Quadratic Variation of Symmetric Random Walks**
Quadratic variation up to time $k$ is defined as,

$$
[M, M]_k = \sum_{j = 1}^k (M_j - M_{j - 1})^2 = k
$$

and is computed path-by-path, by taking the sum of all the squares of all the one-step increments $M_j - M_{j - 1}$, which are either $1$ or $-1$, thus making $\sum_{j = 1}^k 1 = k$. 

**Note:**
- $Var(M_k)$ is computed by taking the average over all paths, considering probabilities 
- $[M, M]_k$ is computed along a single path, so up, down probabilities do not enter the computation
- i.e., $Var(M_k)$ is only computed theoretically whereas $[M, M]_k$ does not depend on the particular path chosen so can be computed along realized path explicitly

------------------------------------------------------------------------

**Scaled Symmetric Random Walk**
Approximate Brownian motion by speeding up time and scaling down step size of a symmetric random walk, by fixing $n \in \mathbb{Z}^+$, defining the scaled symmetric random walk as,

$$
W^{(n)}(t) = \frac{1}{\sqrt{n}} M_{nt}
$$

when $nt$ is an integer, otherwise, the above would be a linear interpolation between the values of the nearest two points (one to the left, one to the right). 
Like a random walk, a scaled random walk has independent increments for $0 = t_0 < t_1 < \dots < t_m$ and $nt_j$ is an integer, we can say that:

$$
(W^{(n)}(t_1) - W^{(n)}(t_0)), (W^{(n)}(t_2) - W^{(n)}(t_1)), \dots, (W^{(n)}(t_m) - W^{(n)}(t_{m - 1}))
$$

are independent increments. 
For $0 \le s \le t$, for $ns, nt$ are integers, we can say that:

$$
\mathbb{E}(W^{(n)}(t) - W^{(n)}(s)) = 0, \quad Var(W^{(n)}(t) - W^{(n)}(s)) = t - s
$$

since the increment is the sum of $n(t - s)$ independent random variables each with expected value 0 and variance $\frac{1}{n}$. 

------------------------------------------------------------------------
e.g., We have the following increment,

$$
W^{(100)}(0.70) - W^{(100)}(0.20)
$$

i.e., $n = 100$ and $(0.70 - 0.20) \times 100 = 50$ so we have 50 independent random variables each that takes value of $\pm \frac{1}{\sqrt{100}} = \pm \frac{1}{10}$ each of which has expected value 0 and variance $\frac{1}{100}$ so variance of the increment written above is,

$$
50 \cdot \frac{1}{100} = 0.50 \implies \text{equals } 0.70 - 0.20
$$

------------------------------------------------------------------------
**Note:** If $s, t$ are chosen so that $ns, nt$ are integers, then the first term on the RHS is independent of $\mathcal{F}(s)$ and $W^{(n)}(s)$ is $\mathcal{F}(s)$-measurable, depending only on the first $ns$ coin tosses, it proves,

$$
\mathbb{E}[W^{(n)}(t) | \mathcal{F}(s)] = W^{(n)}(s)
$$

for $0 \le s \le t$ such that $ns$ and $nt$ are integers. 

------------------------------------------------------------------------
**Quadratic Variation of Scaled Random Walk**
For time $t \ge 0$, such that $nt$ is an integer, we can consider the **quadratic variation of the scaled random walk,** along the path, we evaluate the increment over each time step and square these increments before summing to get the **length of the time interval** over which we are doing the computation,

$$
\begin{align*}
[W^{(n)}, W^{(n)}](t) &= \sum_{j = 1}^{nt} \left[W^{(n)}\left(\frac{j}{n}\right)
 - W^{(n)}\left(\frac{j - 1}{n} \right) \right]^2\\
&= \sum_{j = 1}^nt \left[\frac{1}{\sqrt{n}} X_j \right]^2 = \sum_{j = 1}^{nt} \frac{1}{n} = t
\end{align*}
$$

NOT an average over all possible paths, but obtains the same answer $t$ along all paths. 

**Limiting Distribution of Scaled Random Walk**
Fix time $t$, consider set of all possible paths at the time $t$ for a scaled random walk, and think about the scaled random walk corresponding to different values of $\omega$, sequence of tosses.

e.g., $t = 0.25$ and consider set of all possible values of $W^{(100)}(0.25) = \frac{1}{10} M_{25}$.
Thus, $n = 100$ and we have $100 \times 0.25 = 25$ coin tosses, because $M_{25}$ can take any value of odd integer between $-25$ and $25$. So $W^{(100)}(0.25)$ can take any value:

$$
-2.5, -2.3, -2.1, \dots, -0.1, 0.1, \dots, 2.1, 2.3, 2.5
$$

For $W^{(100)}(0.25) = 0.1$ that is to equal 0.1, we must get 13 heads and 12 tails in 25 tosses,

$$
\mathbb{P}\{W^{(100)} (0.25) = 0.1\} = \frac{25!}{13!12!} \left(\frac{1}{2}\right)^{25} = 0.1555
$$

From a plot, we can see that this information nearly is normal, with expected value zero and variance 0.25. Thus, we can get a good approximation for the function $g(x)$ that is continuous and models this distribution by multiplying $g(x)$ by the normal density and integrating,

$$
\mathbb{E}g(W^{(100)}(0.25)) \approx = \frac{2}{2 \pi} \int_{-\infty}^\infty g(x) e^{-2x^2}dx
$$

------------------------------------------------------------------------

**Theorem**: Central Limit
$t \ge 0$, and as $n \rightarrow \infty$, the distribution of the scaled random walk $W^{(n)}(t)$ evaluated at $t$ converges to the normal distribution with mean zero and variance $t$.

**Proof:**

$$
\begin{align}
    f(x) &= \frac{1}{\sqrt{2\pi t}} e^{-\frac{x^2}{2t}} \\
    \varphi(u) &= \int_{-\infty}^{\infty} e^{ux} f(x) dx \\
    &= \frac{1}{\sqrt{2\pi t}} \int_{-\infty}^{\infty} \exp \left\{ ux - \frac{x^2}{2t} \right\} dx \\
    &= e^{\frac{1}{2} u^2 t} \cdot \frac{1}{\sqrt{2\pi t}} \int_{-\infty}^{\infty} \exp \left\{ - \frac{(x - ut)^2}{2t} \right\} dx \\
    &= e^{\frac{1}{2} u^2 t} \\
    \varphi_n(u) &= \mathbb{E} e^{u W^{(n)}(t)} = \mathbb{E} \exp \left\{ \frac{u}{\sqrt{n}} M_{nt} \right\} \\
    &= \mathbb{E} \exp \left\{ \frac{u}{\sqrt{n}} \sum_{j=1}^{nt} X_j \right\} = \mathbb{E} \prod_{j=1}^{nt} \exp \left\{ \frac{u}{\sqrt{n}} X_j \right\} \\
    &= \prod_{j=1}^{nt} \mathbb{E} \exp \left\{ \frac{u}{\sqrt{n}} X_j \right\} \\
    &= \prod_{j=1}^{nt} \left( \frac{1}{2} e^{\frac{u}{\sqrt{n}}} + \frac{1}{2} e^{-\frac{u}{\sqrt{n}}} \right) \\
    &= \left( \frac{1}{2} e^{\frac{u}{\sqrt{n}}} + \frac{1}{2} e^{-\frac{u}{\sqrt{n}}} \right)^{nt} \\
    \log \varphi_n(u) &= nt \log \left( \frac{1}{2} e^{\frac{u}{\sqrt{n}}} + \frac{1}{2} e^{-\frac{u}{\sqrt{n}}} \right) \\
    \lim_{n \to \infty} \log \varphi_n(u) &= t \lim_{x \to 0} \frac{\log \left( \frac{1}{2} e^{ux} + \frac{1}{2} e^{-ux} \right)}{x^2} \\
    \frac{\partial}{\partial x} \log \left( \frac{1}{2} e^{ux} + \frac{1}{2} e^{-ux} \right) 
    &= \frac{\frac{u}{2} e^{ux} - \frac{u}{2} e^{-ux}}{\frac{1}{2} e^{ux} + \frac{1}{2} e^{-ux}} \\
    \frac{\partial}{\partial x} x^2 &= 2x \\
    \lim_{n \to \infty} \log \varphi_n(u) &= t \lim_{x \to 0} \frac{\frac{u}{2} e^{ux} - \frac{u}{2} e^{-ux}}{2x \left( \frac{1}{2} e^{ux} + \frac{1}{2} e^{-ux} \right)} \\
    \lim_{x \to 0} \left( \frac{1}{2} e^{ux} + \frac{1}{2} e^{-ux} \right) &= 1 \\
    \frac{\partial}{\partial x} \left( \frac{u}{2} e^{ux} - \frac{u}{2} e^{-ux} \right) 
    &= \frac{u^2}{2} e^{ux} + \frac{u^2}{2} e^{-ux} \\
    \frac{\partial}{\partial x} x &= 1 \\
    \lim_{n \to \infty} \log \varphi_n(u) &= \frac{t}{2} \lim_{x \to 0} \left( \frac{\frac{u^2}{2} e^{ux} + \frac{u^2}{2} e^{-ux}}{1} \right) \\
    &= \frac{1}{2} u^2 t 
\end{align}
$$

------------------------------------------------------------------------

**Log-Normal Distribution as Limit of Binomial Model**
Build a model for a stock price on the time interval $[0, t]$, by choosing $n \in \mathbb{Z}$ and creating a binomial for stock price that takes $n$ steps per unit time.

$$
u_n = 1 + \frac{\sigma}{\sqrt{n}},\quad, d_n = 1 - \frac{\sigma}{\sqrt{n}}
$$

where $u_n$ and $d_n$ are the up and down factor, respectively. $\sigma$ is a positive constant, which is also the volatility of the limiting stock price process.

$$
\tilde{p} = \frac{1 + r - d_n}{u_n - d_n} = \frac{\sigma / \sqrt{n}}{2 \sigma / \sqrt{n}} = \frac{1}{2},\quad \tilde{q} = \frac{u_n - 1 - r}{u_n - d_n} = \frac{\sigma / \sqrt{n}}{2 \sigma / \sqrt{n}} = \frac{1}{2}
$$

$nt$ is the sum of $H_{nt}$ and $T_{nt}$ the number of heads and tails in the first $nt$ coin tosses, respectively. We can write the following, given random walk $M_{nt}$,

$$
nt = H_{nt} + T_{nt} \implies M_{nt} = H_{nt} - T_{nt} \implies H_{nt} = \frac{1}{2}(nt + M_{nt})
$$

the same can be done with the opposite sign for $T_{nt}$. 
For the model with $u_n$ and $d_n$ the stock price at $t$ is,

$$
S_n(t) = S(0) u_n^{H_{nt}} d_n^{T_{nt}} = S(0) \left(1 + \frac{\sigma}{\sqrt{n}} \right)^{\frac{1}{2} (nt + M_{nt})} \cdot \left(1 - \frac{\sigma}{\sqrt{n}} \right)^{\frac{1}{2} (nt - M_{nt})}
$$

**Theorem**: $n \rightarrow \infty$ the distribution of $S_n(t)$,

$$
S_n(t) = S(0) u_n^{H_{nt}} d_n^{T_{nt}} = S(0) \left(1 + \frac{\sigma}{\sqrt{n}} \right)^{\frac{1}{2} (nt + M_{nt})} \cdot \left(1 - \frac{\sigma}{\sqrt{n}} \right)^{\frac{1}{2} (nt - M_{nt})}
$$

converges to the distribution of,

$$
S(t) = S(0) \exp \left\{\sigma W(t) - \frac{1}{2} \sigma^2 t \right\}
$$

where $W(t)$ is a normal random variable with mean 0 and variance $t$, $S(t)$ is log-normal. Generally, $ce^X$ for any random variable $X$ is normally distributed. For the above,  $X = \sigma W(t) - \frac{1}{2} \sigma^2 t$ with mean $-\frac{1}{2} \sigma^2 t$ and variance $\sigma^2 t$. 

The proof follows by using the Taylor expansion of $f(x) = \log (1 + x)$.

$$
\begin{align*}
\log S_n(t) &= \log S(0) + \frac{1}{2} (nt + M_{nt}) \log \left(1 + \frac{\sigma}{\sqrt{n}} \right) + \frac{1}{2}(nt - M_{nt}) \log \left(1 - \frac{\sigma}{\sqrt{n}} \right)\\
&= \log S(0) + \frac{1}{2} (nt + M_{nt}) \left(\frac{\sigma}{\sqrt{n}} - \frac{\sigma^2}{2n} + O\left(n^{-\frac{3}{2}}\right) \right) \\ 
&+ \frac{1}{2} (nt - M_{nt}) \left(-\frac{\sigma}{\sqrt{n}} - \frac{\sigma^2}{2n} + O\left(n^{-\frac{3}{2}} \right) \right)\\
&= \log S(0) + nt \left(- \frac{\sigma^2}{2n} + O \left(n^{-\frac{3}{2}} \right) \right) + M_{nt} \left(\frac{\sigma}{\sqrt{n}} + O \left(n^{-\frac{3}{2}} \right) \right)\\
&= \log S(0) - \frac{1}{2} \sigma^2 t + O\left(n^{-\frac{1}{2}} \right) + \sigma W^{(n)}(t) + O(n^{-1}) W^{(n)}(t)
\end{align*}
$$

The distribution of $W^{(n)}(t) = \frac{1}{\sqrt{n}} M_{nt}$ converges to the distribution of a normal random variable with mean zero and variance $t$ a random variable we call $W(t)$. $W^{(n)}(t)$ is multiplied by a term that has $n$ in the denominator and this will have limit zero. 

------------------------------------------------------------------------
**Brownian Motion**
Take the limit of scaled random walks $W^{(n)}(t)$ as $n \rightarrow \infty$. From this we can get the Brownian motion which inherits properties from the scaled random walk,

**Definition: Brownian Motion**
For a probability space, for each $\omega \in \Omega$, suppose there is a continuous function $W(t)$ of $t \ge 0$ that satisfies $W(0) = 0$ and depends on $\omega$. Then $W(t)$ for $t \ge 0$ is a Brownian motion if for all $0 = t_0 < t_1 < \dots < t_m$ the increments,

$$
W(t_1) = W(t_1) - W(t_0), W(t_2) - W(t_1), \dots, W(t_m) - W(t_{m - 1})
$$

are independent and each of these increments is normally distributed and has expected value 0 and variance $t_{i + 1} - t_i$. 
- Brownian motion, unlike a scaled random walk, has no linear pieces 
- Also, BMs are exactly normal for each $t$ as a consequence of the Central Limit theorem.
- Increments $W(t) - W(s)$ is normally distributed for all $0 \le s < t$. 

**Intuition**
1. A random experiment is performed and the outcome is the path of the BM, so $W(t)$ is the value of the path at time $t$ and this value depends on which path resulted from the random experiment
2. $\omega$ is akin to the outcome of a sequence of coin tosses although now the coin is being toss "infinitely fast"; once the coin tosses are performed and the result $\omega$ is being obtained, then the path of the BM can be drawn. If tossed again, a different $\omega$ is obtained and a different path will be drawn 
For $\mathcal{F}$ is the $\sigma$-algebra of subsets of $\Omega$ whose probabilities are defined, $\mathbb{P}$ is the probability measure for which distributional statements are made about the Brownian Motion.

------------------------------------------------------------------------

e.g., let $\{\omega: 0 \le W^{(100)} (0.25) \le 0.2\}$ be the set we are working in,
Define $M_{25} = 10 W^{(100)} (0.25)$ must fall between 0 and 2 after 25 tosses. because

$$
0 \times 0 \le M_{25} \le 10 \times 0.2 \implies 0 \le 10 W^{(100)}(0.25) \le 2
$$

Since $M_{25}$ can only be an odd number, it falls between 0 and 2, it can only be equal to 1,

$$
W^{(100)}(0.25) = 0.1 
$$

Thus, we must get 13 heads and 12 tails in the first 25 tosses. Thus, we can describe the probability of this set as the following,

$$
\mathbb{P}\{0 \le W(0.25) \le 0.2\} = \frac{2}{\sqrt{2 \pi}} \int_0^{0.2} e^{-2x^2}dx
$$

------------------------------------------------------------------------
**Distribution of Brownian Motion**
As we said before, the increments of a Brownian motions are independent and normally distributed. Thus, the Brownian motion at specific time-steps are jointly normally distributed. 

Since each $W(t_i)$ has mean 0, then the covariance for $0 \le s < t$, $W(s), W(t)$ is,

$$
\begin{align*}
\mathbb{E}[W(s)W(t)] &= \mathbb{E}[W(s)(W(t) - W(s)) + W^2(s)]\\
&= \mathbb{E}[W(s)] \cdot \mathbb{E}[W(t) - W(s)] + \mathbb{E}[W^2(s)]\\
&= 0 + Var[W(s)] = s,
\end{align*}
$$

We define the **$m$-dimensional covariance matrix** for the brownian motion,

$$
\begin{bmatrix}
    \mathbb{E} \left[ W^2(t_1) \right] & \mathbb{E} \left[ W(t_1) W(t_2) \right] & \cdots & \mathbb{E} \left[ W(t_1) W(t_m) \right] \\
    \mathbb{E} \left[ W(t_2) W(t_1) \right] & \mathbb{E} \left[ W^2(t_2) \right] & \cdots & \mathbb{E} \left[ W(t_2) W(t_m) \right] \\
    \vdots & \vdots & \ddots & \vdots \\
    \mathbb{E} \left[ W(t_m) W(t_1) \right] & \mathbb{E} \left[ W(t_m) W(t_2) \right] & \cdots & \mathbb{E} \left[ W^2(t_m) \right]
\end{bmatrix}
=
\begin{bmatrix}
    t_1 & t_1 & \cdots & t_1 \\
    t_1 & t_2 & \cdots & t_2 \\
    \vdots & \vdots & \ddots & \vdots \\
    t_1 & t_2 & \cdots & t_m
\end{bmatrix}
$$

To get a moment-generating function for a zero-mean normal random variable with variance $t$ and the independence of the increments as specified previously,

$$
\begin{align}
    u_3 W(t_3) + u_2 W(t_2) + u_1 W(t_1) 
    &= u_3 (W(t_3) - W(t_2)) + (u_2 + u_3)(W(t_2) - W(t_1)) \notag \\
    &\quad + (u_1 + u_2 + u_3)W(t_1)
    \sum_{j=1}^{m} u_j W(t_j) \\
    &= u_m (W(t_m) - W(t_{m-1})) + (u_{m-1} + u_m)(W(t_{m-1}) - W(t_{m-2})) \notag \\
    &\quad + \dots + (u_1 + \dots + u_m) W(t_1)
    \varphi(u_1, \dots, u_m) \\
    &= \mathbb{E} \exp \left\{ u_m W(t_m) + u_{m-1} W(t_{m-1}) + \dots + u_1 W(t_1) \right\} \\
    &= \exp \Bigg\{ \frac{1}{2} (u_1 + \dots + u_m)^2 t_1 
    + \frac{1}{2} (u_2 + \dots + u_m)^2 (t_2 - t_1) \notag \\
    &\quad + \dots + \frac{1}{2} (u_{m-1} + u_m)^2 (t_{m-1} - t_{m-2}) 
    + \frac{1}{2} u_m^2 (t_m - t_{m-1}) \Bigg\}
\end{align}
$$

Thus, the moment-generating function for a Brownian motion (i.e., the $m$-dimensional random vector $(W(t_1), W(t_2), \dots, W(t_m))$ is given by,

$$
\phi(x) = \exp \Bigg\{ \frac{1}{2} (u_1 + \dots + u_m)^2 t_1 
    + \frac{1}{2} (u_2 + \dots + u_m)^2 (t_2 - t_1) + \dots + \frac{1}{2} (u_{m-1} + u_m)^2 (t_{m-1} - t_{m-2}) 
    + \frac{1}{2} u_m^2 (t_m - t_{m-1}) \Bigg\}
$$

The distribution of the brownian increments can be specified by the specifying the joint-density or the joint-moment-generating function of the random variables $W(t_1), W(t_2), \dots, W(t_n)$.

**Theorem**: Characterizations of Brownian Motions 
We have a continuous function $W(t)$ for $W(0) = 0$, that depends on $\omega$, thus the following three properties are considered equivalent,
1. For all $0 = t_0 < t_1 < \dots < t_m$, the increments,

$$
W(t_1) = W(t_1) - W(t_0), W(t_2) - W(t_1), \dots, W(t_m) - W(t_{m - 1})
$$

are independent and each is normally distributed with mean $0$ and variance $t_i - t_{i + 1}$
2. For all $0 = t_0 < t_1 < \dots < t_m$ the random variables $W(t_1), W(t_2), \dots, W(t_m)$ are jointly normally distributed with means equal to 0 and covariance matrix given previously
3. For all "", the random variables "", have jointly moment-generating function,

$$
\phi(x) = \exp \Bigg\{ \frac{1}{2} (u_1 + \dots + u_m)^2 t_1 
    + \frac{1}{2} (u_2 + \dots + u_m)^2 (t_2 - t_1) + \dots + \frac{1}{2} (u_{m-1} + u_m)^2 (t_{m-1} - t_{m-2}) 
    + \frac{1}{2} u_m^2 (t_m - t_{m-1}) \Bigg\}
$$

------------------------------------------------------------------------

**Filtration for Brownian Motion**
For a filtration $\mathcal{F}(t)$ for the Brownian Motion is a collection of $\sigma$-algebras $\mathcal{F}(t)$ satisfying,
1. Every set in $\mathcal{F}(s)$ is also in $\mathcal{F}(t)$ for $s < t$, thus there is at least as much information available at time later time $\mathcal{F}(t)$ as there is at the earlier time $\mathcal{F}(s)$.
2. Information available at time $t$ is sufficient to evaluate the Brownian motion at that time; for each $t \ge 0$, the BM $W(t)$ is $\mathcal{F}(t)$-measurable
3. The increment $W(u) - W(t)$ is independent of $\mathcal{F}(t)$, any increment of the BM after $t$ is independent of the information available at time $t$
$\Delta(t)$ is a stochastic process, and is adapted to $\mathcal{F}(t)$ if for each $t \ge 0$ the r.v. $\Delta(t)$ is $\mathcal{F}(t)$-measurable. 

**Two Possibilities of $\mathcal{F}(t)$ for BM**
4. contains only info obtained by observing BM up to $t$
5. contains info obtained by observing BM and one or more other processes 

**Martingale Property for Brownian Motion**
Brownian motion is a martingale.

**Proof:** For $0 \le s < t$ then we have the following,

$$
\begin{align*}
 \mathbb{E}[W(t) | \mathcal{F}(s)] &= \mathbb{E}[W(t) - W(s) + W(s) | \mathcal{F}(s)]\\
 &= \mathbb{E}[W(t) - W(s) | \mathcal{F}(s)] + \mathbb{E}[W(s) | \mathcal{F}(s)]\\
 &= \mathbb{E}[W(t) - W(s) ] + W(s)\\
 &= W(s)
\end{align*}
$$

------------------------------------------------------------------------

**Quadratic Variation**

We showed that the quadratic variation of a scaled random walk $W^{(n)}(t)$ up to time $T$ is $T$. For a BM, there is no natural step size, so if we are given $T > 0$ then we could choose a step size $\frac{T}{n}$ for some large $n$, and compute the quadratic variation up to time $T$ with this step size.

$$
\sum_{j = 0}^{n - 1} \left[W \left(\frac{(j + 1)T}{n} \right) - W\left(\frac{jT}{n} \right) \right]^2
$$

We want to evaluate this quantity but for small step sizes, so we take the limit of the above from $n \rightarrow \infty$. Thus, we also get $T$ as the quadratic variation. Paths of BM are unusual in that their quadratic variation is not zero making stochastic calculus different from ordinary. 

------------------------------------------------------------------------

**First Order Variation**
**Goal**: Compute amount of up and down oscillation undergone by $f(t)$ between $[0, T]$, with down moves adding and up moves subtracting (counterintuitive, but this will be useful in the future).

For $f$,

$$
\begin{align*}
FV_T(f) &= [f(t_1) - f(0)] - [f(t_2) - f(t_1)] + [f(T) - f(t_2)]\\
&= \int_0^{t_1} f'(t) dt + \int_{t_1}^{t_2} (-f'(t))dt + \int_{t_2}^T f'(t) dt\\
&= \int_0^T |f'(t)| dt
\end{align*}
$$

where the middle term $-[f(t_2) - f(t_1)] = f(t_1) - f(t_2)$ guarantees that the magnitude of the down move of the function $f(t)$ between $t_1, t_2$ is added to rather than subtracted from total.

Take partition $\Pi = \{t_0, t_1, \dots t_n\}$ of $[0, T]$ which is a set of times, not necessarily equally spaces:

$$
0 = t_0 < t_1 < \dots < t_n = T
$$

with max step size of the partition denoted:

$$
||\Pi|| = \max_{j = 0, \dots, n - 1}(t_{j + 1} - t_j)
$$

Thus, first order variation, we take the limit as the number of $n$ partition points goes to infinity, and the longest subinterval $t_{j + 1} - t_j$ goes to zero.

$$
FV_T(f) = \lim_{||\Pi|| \rightarrow 0} \sum_{j = 1}^{n - 1} | f(t_{j + 1}) - f(t_j)|
$$

Using MVT, we can show,

$$
\frac{f(t_{j + 1})-f(t_j)}{t_{j + 1}-t_j} = f'(t_j^*)
$$

on interval $[t_j, t_{j + 1}]$ there is such a point $t_j^*$. Thus, somewhere between these two points, the tangent line is parallel to the chord. Thus, we can get:

$$
f(t_{j + 1}) - f(t_j) = f'(t_j^*)(t_{j + 1} - t_j) \implies \sum_{j = 1}^{n - 1} | f'(t_j^*)| (t_{j + 1} - t_j)
$$

which is the Riemann sum for the integral of $|f'(t)|$, thus we get

$$
FV_T(f) = \lim_{||\Pi|| \rightarrow 0}\sum_{j = 1}^{n - 1} |f'(t_j^*)|(t_{j + 1} - t_j) = \int_0^T |f'(t)|dt
$$

------------------------------------------------------------------------

**Definition: Quadratic Variation**
The quadratic variation of $f$ up to time $T$ is given by,

$$
[f, f](T) = \lim_{||\Pi|| \rightarrow 0} \sum_{j = 0}^{n - 1} [f(t_{j + 1} - f(t_j))]^2
$$

where $\Pi$ and the partitions are defined like before.

Suppose $f$ has a continuous derivative, then

$$
\sum_{j = 0}^{n - 1} [f(t_{j + 1}) - f(t_j)]^2 = \sum_{j = 0}^{n - 1} |f'(t_j^*)|^2 (t_{j + 1} - t_j)^2 \le ||\Pi| \cdot \sum_{j = 0}^{n - 1} |f'(t_j^*)|^2 (t_{j + 1} - t_j)
$$



$$
\begin{align}
    [f,f](T) &= \lim_{\|\Pi\| \to 0} \left[ \|\Pi\| \cdot \sum_{j=0}^{n-1} |f'(t_j^*)|^2 (t_{j+1} - t_j) \right] \\
    &= \lim_{\|\Pi\| \to 0} \|\Pi\| \cdot \lim_{\|\Pi\| \to 0} \sum_{j=0}^{n-1} |f'(t_j^*)|^2 (t_{j+1} - t_j) \\
    &= \lim_{\|\Pi\| \to 0} \int_0^T |f'(t)|^2 dt = 0.
\end{align}
$$

- The quadratic variation measures the accumulation of squared increments over finer and finer partitions of an interval
- If $f$ is continuously differentiable then its quadratic variation disappears, meaning it does not exhibit erratic or jumpy behaviour 
- Thus, as we can see from the derivation above, the quadratic variation for a continuous-derivative function, is **zero**.
- Thus, we never consider quadratic variation in ordinary calculus; 
- paths of brownian motion can not be differentiated with respect to the time variable

------------------------------------------------------------------------

**Theorem:** $W$ is a Brownian Motion, then $[W, W](T) = T$ for all $T \ge 0$ almost surely. 

**Proof:**
For sampled quadratic variation corresponding to this partition, we have,

$$
Q_{\Pi} = \sum_{j = 0}^{n - 1} (W(t_{j + 1}) - W(t_j))^2
$$

We show that this is a random variable and converges to $T$ as $\left\lVert \Pi\right\rVert \rightarrow 0$. Moreover, it has expected value $T$ and variance that converges to 0. Hence, it converges to expected value $T$ regardless of the path along which we are doing the computation. 

------------------------------------------------------------------------

The sampled quadratic variation is the sum of independent random variables, therefore its mean and variance are the sums of the means and variances of these random variables.

$$
\mathbb{E} \left[(W(t_{j + 1}) - W(t_j))^2 \right] = Var\left[W(t_{j + 1}) - W(t_j) \right] = t_{j + 1} - t_j
$$

Which gives us the implication that,

$$
\mathbb{E} Q_{\Pi} = \sum_{j = 0}^{n - 1} \mathbb{E}\left[(W(t_{j + 1}) - W(t_j))^2 \right] = \sum_{j = 0}^{n - 1} (t_{j + 1} - t_j) = T
$$

Moreover,

$$
\begin{align}
\text{Var} \left[ (W(t_{j+1}) - W(t_j))^2 \right] 
&= \mathbb{E} \left[ \left( (W(t_{j+1}) - W(t_j))^2 - (t_{j+1} - t_j) \right)^2 \right] \\
&= \mathbb{E} \left[ (W(t_{j+1}) - W(t_j))^4 \right] - 2 (t_{j+1} - t_j) \mathbb{E} \left[ (W(t_{j+1}) - W(t_j))^2 \right] \\&+ (t_{j+1} - t_j)^2.
\end{align}
$$



$$
\begin{align}
\mathbb{E} \left[ (W(t_{j+1}) - W(t_j))^4 \right] 
&= 3 (t_{j+1} - t_j)^2.
\end{align}
$$



$$
\begin{align}
\text{Var} \left[ (W(t_{j+1}) - W(t_j))^2 \right] 
&= 3 (t_{j+1} - t_j)^2 - 2 (t_{j+1} - t_j)^2 + (t_{j+1} - t_j)^2 \\
&= 2 (t_{j+1} - t_j)^2.
\end{align}
$$



$$
\begin{align}
\text{Var}(Q_{\Pi}) &= \sum_{j=0}^{n-1} \text{Var} \left[ (W(t_{j+1}) - W(t_j))^2 \right] \\
&= \sum_{j=0}^{n-1} 2 (t_{j+1} - t_j)^2 \\
&\leq \sum_{j=0}^{n-1} 2 \| \Pi \| (t_{j+1} - t_j) \\
&= 2 \| \Pi \| T.
\end{align}
$$



$$
\begin{align}
\lim_{\|\Pi\| \to 0} \text{Var}(Q_{\Pi}) &= 0, \quad \text{and we conclude that} \quad \lim_{\|\Pi\| \to 0} Q_{\Pi} = \mathbb{E} Q_{\Pi} = T.
\end{align}
$$

Above, we saw that $\mathbb{E}[(W(t_{j + 1}) - W(t_j))^2] = t_{j + 1} - t_j$ and $Var[(W(t_{j + 1}) - W(t_j))^2] = 2(t_{j + 1} - t_j)^2$ so when $t_{j + 1} - t_j$ is small, the square of it is very small. Therefore, we can write,

$$
(W(t_{j + 1}) - W(t_j))^2 \approx t_{j + 1} - t_j
$$

Probabilistically, given the approximate equality above, we can write,

$$
\frac{(W(t_{j + 1}) - W(t_j))^2}{t_{j + 1} - t_j} \approx 1
$$

but is not in fact near one, no matter how small $t_{j + 1} - t_j$ is, so it is the square of the standard normal random variable given by,

$$
Y_{j + 1} = \frac{W(t_{j + 1}) - W(t_j)}{\sqrt{t_{j + 1} - t_j}}
$$

and its distribution is the same no matter how small we make $t_{j + 1} - t_j$. If we choose large $n$ and $t_j = \frac{jT}{n}$ then for $t_{j + 1} - t_j = \frac{T}{n}$ for all $j$, and

$$
(W(t_{j + 1}) - W(t_j))^2 = T \cdot \frac{Y_{j + 1}^2}{n}
$$

Since $Y_1, Y_2, \dots, Y_n$ are iid, then by SLLN, we can see that,

$$
\sum_{j = 0}^{n - 1} \frac{Y_{j + 1}^2}{n} \rightarrow \mathbb{E}Y_{j + 1}^2 \text{ as } n \rightarrow \infty
$$

thus, we can say that,

$$
\sum_{j = 0}^{n - 1}(W(t_{j + 1}) - W(t_j))^2 \rightarrow T
$$

Thus we can write that,

$$
dW(t)dW(t) = dt
$$

meaning that on an interval $[0, T]$ the BM accumulates $T$ units of quadratic variation. Additionally, let's take $0 < T_1 < T_2$, then on an interval $[T_1, T_2]$ the sum of the squared increments of BM for each of the subintervals in the partition gives:

$$
[W, W](T_2) - [W, W](T_1) = T_2 - T_1
$$

Thus, the BM accumulates $T_2 - T_1$ units of QV over the interval $[T_1, T_2]$, and more generally, we can say that BM accumulates quadratic variation at rate one per unit time.

------------------------------------------------------------------------

**Cross Variation**
We can compute the cross variation of $W(t)$ with $t$ and the QV of $t$ with itself,

$$
\lim_{||\Pi|| \rightarrow 0} \sum_{j = 0}^{n - 1} (W(t_{j + 1}) - W(t_j))^2 = T \implies \lim_{||\Pi|| \rightarrow 0} \sum_{j= 0 }^{n - 1} (W(t_{j + 1}) - W(t_j))(t_{j + 1} - t_j) = 0 
$$



$$
\implies \lim_{||\Pi|| \rightarrow 0} \sum_{j = 0}^{n - 1}(t_{j + 1} - t_j)^2 = 0
$$

In the first line, we can see that the limit is 0 because,

$$
\begin{align}
\left| (W(t_{j+1}) - W(t_j))(t_{j+1} - t_j) \right| 
&\leq \max_{0 \leq k \leq n-1} |W(t_{k+1}) - W(t_k)| (t_{j+1} - t_j), \\ 
\left| \sum_{j=0}^{n-1} (W(t_{j+1}) - W(t_j))(t_{j+1} - t_j) \right| 
&\leq \max_{0 \leq k \leq n-1} |W(t_{k+1}) - W(t_k)| \cdot T.
\end{align}
$$



$$
\begin{align}
\sum_{j=0}^{n-1} (t_{j+1} - t_j)^2 
&\leq \max_{0 \leq k \leq n-1} (t_{k+1} - t_k) \cdot \sum_{j=0}^{n-1} (t_{j+1} - t_j) \\ 
&= \|\Pi\| \cdot T.
\end{align}
$$

Thus, we can capture the essence of this by writing,

$$
\begin{align}
dW(t) dt &= 0, \quad dtdt = 0. \quad \quad (3.4.14)
\end{align}
$$

------------------------------------------------------------------------

**Volatility of Geometric Brownian Motion**
For constants $\alpha, \sigma > 0$, we can define the Geometric Brownian Motion,

$$
S(t) = S(0) \exp \left\{\sigma W(t) + \left(\alpha - \frac{1}{2}\sigma^2 \right) \right\}
$$

i.e., the asset-price model used in the Black-Scholes-Merton option-pricing formula. We show how to use the quadratic variation of BM to identify the volatility $\sigma$ from a path of this process.

Using $0 \le T_1 < T_2$ and defined $T_1 = t_0 < t_2 < \dots < t_m = T_2$ and observe the **log returns**,

$$
\log \frac{S(t_{j + 1})}{S(t_j)} = \sigma (W(t_{j + 1}) - W(t_j)) + \left(\alpha - \frac{1}{2}\sigma^2 \right)(t_{j + 1} - t_j)
$$

over each subinterval $[t_j, t_{j + 1}]$. The **sum of squares** of the **log returns** is also called the **realized volatility** and is given by,

$$
\begin{align}
\sum_{j=0}^{m-1} \left( \log \frac{S(t_{j+1})}{S(t_j)} \right)^2 
&= \sigma^2 \sum_{j=0}^{m-1} \left( W(t_{j+1}) - W(t_j) \right)^2 
+ \left( \alpha - \frac{1}{2} \sigma^2 \right) \sum_{j=0}^{m-1} (t_{j+1} - t_j)^2 \\
&\quad + 2\sigma \left( \alpha - \frac{1}{2} \sigma^2 \right) \sum_{j=0}^{m-1} (W(t_{j+1}) - W(t_j))(t_{j+1} - t_j).
\end{align}
$$

1. Term 1: is approximately equal to its limit which is $\sigma^2$ times the amount of QV accumulated by Brownian Motion on the interval $[T_1, T_2]$ which is $T_2 - T_1$.
2. Term 2: is the $\left(\alpha - \frac{1}{2}\sigma^2\right)^2$ times the QV of $t$ which is 0
3. Term 3: is $2 \sigma \left(\alpha - \frac{1}{2}\sigma^2 \right)$ times the cross variation of $W(t)$ and $t$ which is zero

When the maximum step size is small, then the RHS of the above is approx. equal to $\sigma^2(T_2 - T_1)$.

$$
\frac{1}{T_2 - T_1} \sum_{j = 0}^{m - 1}\left(\log \frac{S(t_{j + 1})}{S(t_j)} \right)^2 \approx \sigma^2
$$

If $S(t)$ is a GBM with constant volatility $\sigma$ then $\sigma$ is identified from price observations by computing the LHS of the above and taking the root. 

------------------------------------------------------------------------

**Markov Property**
Let $W(t)$ be a Brownian motion and let $\mathcal{F}(t)$ be a filtration for the Brownian motion, then $W(t)$ is a Markov process. 

**Proof**
$0 \le s \le t$ and let $f$ be a Borel-measurable function, then we define another Borel-measurable function $g$ such that,

$$
\mathbb{E}[f(W(t)) | \mathcal{F}(s)] = \mathbb{E}[f((W(t) - W(s))) + W(s) | \mathcal{F}(s)] \mathbb{E}[f(W(t)) | \mathcal{F}(s)] = g(W(s)) 
$$

where $W(t) - W(s)$ is independent of $\mathcal{F}(s)$ and the random variable $W(s)$ is $\mathcal{F}(s)$-measurable. Thus we compute the expectation on the RHS by replacing $W(s)$ with $x$ and hold it constant and take the unconditional expectation of the remaining random variable.

$$
g(x) = \mathbb{E}f(W(t) - W(s) + x) 
$$

$W(t) - W(s)$ is normally distributed with mean 0 and variance $t - s$ meaning we can write,

$$
g(x) = \frac{1}{\sqrt{2\pi (t-s)}} \int_{-\infty}^\infty f(w + x) e^{- \frac{w^2}{2(t-s)}}dw
$$

Thus, we can now take $g(x)$ and replace $x$ with r.v. $W(s)$, let $\tau = t - s$ and $y = w + x$,

$$
g(x) = \frac{1}{\sqrt{2 \pi \tau}} \int_{-\infty}^{\infty} f(y) e^{-\frac{(y - x)^2}{2\tau}} dy
$$

Thus, we define the **transition density for Brownian Motion** $p(\tau, x, y)$ to be,

$$
p(\tau, x, y) = \frac{1}{\sqrt{2 \pi \tau}} \exp\left\{-\frac{(y-x)^2}{2\tau} \right\}
$$

so we can decompose and re-arrange this into,

$$
g(x) = \int_{-\infty}^{\infty} f(y) p(\tau, x, y) dy \implies \mathbb{E}[f(W(t)) | \mathcal{F}(s)] = \int_{-\infty}^{\infty} f(y) p (\tau, W(s), y) dy
$$

- Conditioned on the information in $\mathcal{F}(s)$, the conditional density of $W(t)$ is $p(\tau, W(s), y)$
- aka, the density in variable $y$
- Density is normal with mean $W(s)$ and variance $\tau = t - s$. 
- Information from $\mathcal{F}(s)$ is the only info relevant to value of $W(s)$
- $W(s)$ is relevant is essence of the Markov property 

------------------------------------------------------------------------

**Theorem: Exponential Martingale**
Exponential martingale corresponding to $\sigma$, is given by

$$
Z(t) = \exp \left\{\sigma W(t) - \frac{1}{2} \sigma^2 t \right\}
$$

where $W(t)$ is a BM with filtration $\mathcal{F}(t)$, the process $Z(t)$ is a martingale.

**Proof**
Let $0 \le s \le t$, thus we have that,

$$
\begin{align*}
\mathbb{E}[Z(t) | \mathcal{F}(s)] &= \mathbb{E} \left[\exp \left\{\sigma W(t) - \frac{1}{2}\sigma^2 t \right\} | \mathcal{F}(s) \right]\\
&= \mathbb{E} \left[\exp \{\sigma (W(t) - W(s))\} \cdot \exp \left\{\sigma W(s) - \frac{1}{2} \sigma^2 t \right\} | \mathcal{F}(s) \right]\\
&= \exp \left\{\sigma W(s) - \frac{1}{2 \sigma^2 t} \right\} \cdot \mathbb{E}[\exp \{\sigma (W(t) - W(s))\} | \mathcal{F}(s)]\\
&= \exp \left\{\sigma W(s) - \frac{1}{2}\sigma^2 s \right\} = Z(s)
\end{align*}
$$

Given by the fact that we can take out what is known and independence to write the last line.

**First Passage Time**
Define the first passage time to level $m$ as,

$$
\tau_m = \min \{t \ge 0; W(t) = m\}
$$

which is the first time the BM $W$ reaches the level $m$. If the BM never reaches level $m$, then we set $\tau_m = \infty$. A martingale stopped at a stopping time is still a martingale and thus must have constant expectation.

$$
1 = Z(0) = \mathbb{E}Z(t \wedge \tau_m) = \mathbb{E} \left[\exp \left\{\sigma W(t \wedge \tau_m) - \frac{1}{2}\sigma^2 (t \wedge \tau_m) \right\} \right]
$$

where $t \wedge \tau_m$ represents the minimum of $t$ and $\tau_m$. Thus, we assume that $\sigma > 0$ and $m > 0$, the BM is always at or below the level $m$ for $\tau \le \tau_m$ so $0 \le \exp \{\sigma W(t \wedge \tau_m\} \le e^{\sigma m}$. The extensive proof of the following theorem is redacted. 

**Theorem**
The first passage time of a BM to level $m$ is finite almost surely, and the LaPlace transform of its distribution is given by the following,

$$
\mathbb{E} e^{-\alpha \tau_m} = e^{- |m| \sqrt{2 \alpha}} \quad \text{for all } \alpha >0
$$

------------------------------------------------------------------------

**Reflection Principle**
Fix positive level $m$ and positive time $t$, and want to count the BM paths that reach $m$ at or before $t$. There are two such paths,
1. reach level $m$ prior to $t$ but at time $t$ are at some level $w$ below $m$ 
2. exceed level $m$ at time $t$
Other cases include ones that are exactly at level $m$ but is unlikely in the case of the Brownian motion and thus has probability 0. 

We construct a reflect by switching the up and down moves of the Brownian motion from time $\tau_m$ onwards. The probability that a Brownian Motion ends at exactly $w$ or at exactly $2m - w$ is zero. Consider the paths that reach level $m$ prior to $t$ and are at or below level $w$ at time $t$. This leads to the key reflection equality given by,

$$
\mathbb{P}\{\tau_m \le t, W(t) \le m\} = \mathbb{P}\{W(t) \ge 2m - w\},\quad w \le m, m > 0
$$

**Theorem: Random Variable $\tau_m$**
The random variable $\tau_m$ has cumulative distribution function given by,

$$
\mathbb{P}\{\tau_m \le t\} = \frac{2}{\sqrt{2 \pi}} \int_{\frac{|m|}{\sqrt{t}}}^\infty e^{-\frac{y^2}{2}} dy,\quad t \ge 0
$$

and density given by,

$$
f_{\tau_m}(t) = \frac{d}{dt} \mathbb{P}\{\tau_m \le t\} = \frac{|m|}{t \sqrt{2 \pi t}} e^{-\frac{m^2}{2t}}, \quad t \ge 0
$$

**Maximum Date of Brownian Motion**
The maximum to date for BM to be:

$$
M(t) = \max_{0 \le s \le t} W(s)
$$

which is used in pricing barrier options. For the value of $t$ the random variable $M(t)$ is indicated. For positive $m$ we have that $M(t) \ge m$ if and only if $\tau_m \le t$.

$$
\mathbb{P}\{M(t) \ge m, W(t) \le w\} = \mathbb{P}\{W(t) \ge 2m - w\},\quad w \le m, m > 0
$$

which can be written as the joint distribution of $W(t)$ and $M(t)$. 

**Theorem** For $t > 0$ the joint density of $(M(t), W(t))$ is given by the following,

$$
f_{M(t), W(t)} (m ,w) = \frac{2(2m - w)}{t \sqrt{2 \pi t}} \exp \left\{-\frac{(2m - w)^2}{2t} \right\},\quad w \le m, m > 0
$$

