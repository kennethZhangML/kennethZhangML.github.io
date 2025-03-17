---
layout: page
title: Chapter 3 - Brownian Motion Exercises
description: Exercises for Chapter 3 - Brownian Motion.
parent: course-2
importance: 6
permalink: /notes/course-2/chapter-3-brownian-motion-exercises/
nav: false
---


**Exercise 3.1**
By Definition 3.3.3(iii), the increment property of Brownian motion states that:

$$
W(u) - W(t) \text{ is independent of } \mathcal{F}(t), \quad \forall 0 \leq t < u.
$$

This means that the future increments of the Brownian motion (beyond time $t$) do not depend on the past, captured by $\mathcal{F}(t)$.
We rewrite the increment $W(u_2) - W(u_1)$ as:

$$
W(u_2) - W(u_1) = \big( W(u_2) - W(t) \big) - \big( W(u_1) - W(t) \big).
$$

From Definition 3.3.3(iii), both $W(u_2) - W(t)$ and $W(u_1) - W(t)$ are independent of $\mathcal{F}(t)$.
By Definition 3.3.3(i), Brownian motion has independent increments, meaning:

$$
(W(u_2) - W(u_1)) \text{ is independent of } (W(u_1) - W(t)).
$$

Since $W(u_1) - W(t)$ is independent of $\mathcal{F}(t)$, and the increment $W(u_2) - W(u_1)$ is independent of $W(u_1) - W(t)$, it follows that:

$$
W(u_2) - W(u_1) \text{ is independent of } \mathcal{F}(t).
$$

By leveraging the independent increments property of Brownian motion and the fact that any increment $W(u) - W(t)$ is independent of $\mathcal{F}(t)$ for $t < u$, we have shown that the increment $W(u_2) - W(u_1)$ is also independent of $\mathcal{F}(t)$ for $t < u_1 < u_2$.


**Exercise 3.2**
To show that $W^2(t) - t$ is a martingale, we must verify that for all $s \leq t$,

$$
\mathbb{E}[W^2(t) - t \mid \mathcal{F}(s)] = W^2(s) - s.
$$

Using the given hint, we expand $W^2(t)$ as:

$$
W^2(t) = (W(t) - W(s))^2 + 2W(t)W(s) - W^2(s).
$$

Taking expectation conditioned on $\mathcal{F}(s)$:

$$
\mathbb{E}[W^2(t) \mid \mathcal{F}(s)] = \mathbb{E}[(W(t) - W(s))^2 \mid \mathcal{F}(s)] + 2W(s) \mathbb{E}[W(t) \mid \mathcal{F}(s)] - W^2(s).
$$

Since $W(t) - W(s) \sim \mathcal{N}(0, t - s)$ and is independent of $\mathcal{F}(s)$, we have:

$$
\mathbb{E}[W(t) - W(s) \mid \mathcal{F}(s)] = 0, \quad \mathbb{E}[(W(t) - W(s))^2 \mid \mathcal{F}(s)] = t - s.
$$

Substituting these,

$$
\mathbb{E}[W^2(t) \mid \mathcal{F}(s)] = (t - s) + 2W(s) \cdot 0 + W^2(s) = W^2(s) + (t - s).
$$


$$
\mathbb{E}[W^2(t) - t \mid \mathcal{F}(s)] = W^2(s) + (t - s) - t = W^2(s) - s.
$$

Since this satisfies the martingale property, we conclude that $W^2(t) - t$ is a martingale.


**Exercise 3.3**

$$\kappa = \frac{\mathbb{E}[(X - \mu)^4]}{\left( \mathbb{E}[(X - \mu)^2] \right)^2}.$$

For a normal random variable, we will verify that $\kappa = 3$. Let $X$ be a normal random variable with mean $\mu$ and variance $\sigma^2$. That is, $X - \mu$ has mean zero and variance $\sigma^2$. The moment-generating function of $X - \mu$ is given by

$$\varphi(u) = \mathbb{E}[e^{u(X - \mu)}] = e^{\frac{1}{2} u^2 \sigma^2}.$$

Differentiating this function with respect to $u$, we obtain

$$\varphi'(u) = \mathbb{E}[(X - \mu)e^{u(X - \mu)}] = \sigma^2 u e^{\frac{1}{2} u^2 \sigma^2}.$$

In particular, $\varphi'(0) = \mathbb{E}[X - \mu] = 0$. Differentiating again, we get

$$\varphi''(u) = \mathbb{E}[(X - \mu)^2 e^{u(X - \mu)}] = (\sigma^2 + \sigma^4 u^2)e^{\frac{1}{2} u^2 \sigma^2}.$$

Evaluating at $u=0$, we find $\varphi''(0) = \mathbb{E}[(X - \mu)^2] = \sigma^2$. Differentiating two more times, we obtain the fourth moment

$$\mathbb{E}[(X - \mu)^4] = 3\sigma^4.$$

Thus, the kurtosis is

$$\kappa = \frac{3\sigma^4}{\sigma^4} = 3.$$

This confirms that the normal distribution has a kurtosis of 3.


**Exercise 3.4**
The theorem states that for a Brownian motion $W(t)$ and a partition $\Pi$ of the interval $[0,T]$, as the number of partition points $n$ increases and the length of the longest subinterval approaches zero, the sample quadratic variation satisfies

$$
\sum_{j=0}^{n-1} (W(t_{j+1}) - W(t_j))^2 \to T
$$

for almost every path of the Brownian motion.
We are also given the multiplication rules:

$$
dW(t) dW(t) = dt, \quad dW(t) dt = 0, \quad dt dt = 0.
$$

(i) We need to show that the sample first variation,

$$
\sum_{j=0}^{n-1} |W(t_{j+1}) - W(t_j)|
$$


approaches $\infty$ for almost every path of $W(t)$. 
Using the hint,

$$
\sum_{j=0}^{n-1} (W(t_{j+1}) - W(t_j))^2 \leq \max_{0 \leq k \leq n-1} |W(t_{k+1}) - W(t_k)| \cdot \sum_{j=0}^{n-1} |W(t_{j+1}) - W(t_j)|.
$$

Since the left-hand side converges to $T$, while the maximum increment $\max_{0 \leq k \leq n-1} |W(t_{k+1}) - W(t_k)|$ does not tend to zero, it follows that the first variation sum must diverge to infinity.

(ii) We now show that the sample cubic variation,

$$
\sum_{j=0}^{n-1} |W(t_{j+1}) - W(t_j)|^3
$$

approaches zero for almost every path of $W(t)$. 
Since we know that the quadratic variation sum converges to a finite value,

$$
\sum_{j=0}^{n-1} (W(t_{j+1}) - W(t_j))^2 \approx T,
$$

we can use Hölder’s inequality to show that the cubic variation is small. Specifically,

$$
\sum_{j=0}^{n-1} |W(t_{j+1}) - W(t_j)|^3 \leq \max_{0 \leq k \leq n-1} |W(t_{k+1}) - W(t_k)| \cdot \sum_{j=0}^{n-1} (W(t_{j+1}) - W(t_j))^2.
$$

Since the quadratic variation remains finite and the maximum increment $\max_{0 \leq k \leq n-1} |W(t_{k+1}) - W(t_k)|$ shrinks to zero as $n \to \infty$, it follows that the cubic variation sum also converges to zero.


**Exercise 3.5**
The Black-Scholes-Merton formula derives the price of a European call option under the risk-neutral measure. The stock price follows a geometric Brownian motion:

$$ 
S(t) = S(0) e^{(r - \frac{1}{2} \sigma^2)t + \sigma W(t)}.
$$

Under the risk-neutral measure, the expectation of the discounted payoff is given by

$$ 
\mathbb{E} \left[ e^{-rT} (S(T) - K)^+ \right].
$$

Using the risk-neutral measure, the stock price at maturity follows

$$ 
S(T) = S(0) e^{(r - \frac{1}{2} \sigma^2)T + \sigma W(T)}.
$$

Taking the logarithm, we get

$$ 
\log \frac{S(T)}{K} = \log \frac{S(0)}{K} + (r - \frac{1}{2} \sigma^2)T + \sigma W(T).
$$

Define,

$$ 
d_{\pm}(T, S(0)) = \frac{1}{\sigma \sqrt{T}} \left[ \log \frac{S(0)}{K} + \left( r \pm \frac{\sigma^2}{2} \right)T \right].
$$

Since $W(T) \sim \mathcal{N}(0,T)$, the probability that $S(T) \geq K$ follows from the cumulative standard normal distribution:

$$ 
N(y) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{y} e^{-\frac{1}{2}z^2} dz.
$$

Thus, computing the expectation,

$$ 
\mathbb{E} \left[ e^{-rT} (S(T) - K)^+ \right] = S(0) N(d_+(T, S(0))) - K e^{-rT} N(d_-(T, S(0))).
$$

This completes the derivation of the Black-Scholes-Merton pricing formula.


**Exercise 3.6**
(i) Consider the Brownian motion with drift $\mu$ given by

$$
X(\mu) = \mu t + W(t).
$$

To show that $X$ has the Markov property, we consider a Borel-measurable function $f(y)$ and define

$$
g(x) = \frac{1}{\sqrt{2\pi (t-s)}} \int_{-\infty}^{\infty} f(y) \exp \left( -\frac{(y - x - \mu (t-s))^2}{2(t-s)} \right) dy.
$$

We compute the conditional expectation given $\mathcal{F}(s)$:

$$
\mathbb{E}[ f(X(t)) | \mathcal{F}(s)].
$$

Since the transition density for a Brownian motion with drift $\mu$ is

$$
p(\tau, x, y) = \frac{1}{\sqrt{2\pi\tau}} \exp \left( -\frac{(y - x - \mu\tau)^2}{2\tau} \right),
$$

we obtain

$$
\mathbb{E}[ f(X(t)) | \mathcal{F}(s)] = g(X(s)),
$$

which confirms that $X$ satisfies the Markov property.

(ii) Consider the geometric Brownian motion defined by

$$
S(t) = S(0)e^{\sigma W(t) + \nu t}.
$$

We set $\tau = t - s$ and consider the transition density

$$
p(\tau, x, y) = \frac{1}{\sigma y \sqrt{2\pi \tau}} \exp \left( -\frac{(\log \frac{y}{x} - \nu\tau)^2}{2\sigma^2 \tau} \right).
$$

For a Borel-measurable function $f(y)$, define

$$
g(x) = \int_0^{\infty} h(y) p(\tau, x, y) dy.
$$

Computing the conditional expectation,

$$
\mathbb{E}[ f(S(t)) | \mathcal{F}(s)] = g(S(s)).
$$

Thus, $S$ satisfies the Markov property with transition density $p(\tau, x, y)$.


**Exercise 3.7**
(i) Define the process

$$
Z(t) = \exp \left\{ \sigma X(t) - \left( \sigma \mu + \frac{1}{2} \sigma^2 \right) t \right\}.
$$

Applying Itô's lemma to $Z(t)$, we compute:

$$
dZ(t) = Z(t) \left\{ \sigma dX(t) + \frac{1}{2} \sigma^2 dt - \left( \sigma \mu + \frac{1}{2} \sigma^2 \right) dt \right\}.
$$

Since $X(t) = \mu t + W(t)$, we have $dX(t) = \mu dt + dW(t)$, so that

$$
dZ(t) = Z(t) \left\{ \sigma (\mu dt + dW(t)) + \frac{1}{2} \sigma^2 dt - \left( \sigma \mu + \frac{1}{2} \sigma^2 \right) dt \right\}.
$$

Simplifying,

$$
dZ(t) = Z(t) \sigma dW(t),
$$

which is a local martingale with zero drift, implying $Z(t)$ is a martingale.

(ii) Since $Z(t)$ is a martingale,

$$
\mathbb{E} \left[ Z(t \wedge \tau_m) \right] = Z(0) = 1.
$$

Rewriting in terms of $Z(t)$,

$$
\mathbb{E} \left[ \exp \left\{ \sigma X(t \wedge \tau_m) - \left( \sigma \mu + \frac{1}{2} \sigma^2 \right) (t \wedge \tau_m) \right\} \right] = 1.
$$


(iii) Suppose $\mu \geq 0$. Setting $t = \tau_m$ in (ii) and conditioning on $\tau_m < \infty$,

$$
\mathbb{E} \left[ \exp \left\{ \sigma m - \left( \sigma \mu + \frac{1}{2} \sigma^2 \right) \tau_m \right\} \mathbf{1}_{\{\tau_m < \infty\}} \right] = 1.
$$

Taking expectations, we obtain

$$
\mathbb{P} (\tau_m < \infty) = 1.
$$

Using this result, we find the Laplace transform:

$$
\mathbb{E} e^{-\alpha \tau_m} = e^{\mu m - m\sqrt{2\alpha + \mu^2}}, \quad \alpha > 0.
$$


(iv) If $\mu > 0$, differentiating the formula for $\mathbb{E} e^{-\alpha \tau_m}$ with respect to $\alpha$ at $\alpha = 0$ gives

$$
\mathbb{E} \tau_m = \frac{m}{\mu}.
$$


(v) If $\mu < 0$ and $\sigma > -2\mu$, using the same argument as in (iii),

$$
\mathbb{E} \left[ \exp \left\{ \sigma m - \left( \sigma \mu + \frac{1}{2} \sigma^2 \right) \tau_m \right\} \mathbf{1}_{\{\tau_m < \infty\}} \right] = 1.
$$

Solving for $\mathbb{P} (\tau_m < \infty)$, we get

$$
\mathbb{P} (\tau_m < \infty) = e^{-2x|\mu|} < 1.
$$

Finally, the Laplace transform is given by

$$
\mathbb{E} e^{-\alpha \tau_m} = e^{\mu m - m\sqrt{2\alpha + \mu^2}}, \quad \alpha > 0.
$$



**Exercise 3.8**
(i) The moment-generating function of $\frac{1}{\sqrt{n}} M_{nt,n}$ is given by

$$
\varphi_n(u) = \left[ e^{\frac{u}{\sqrt{n}}} \left( \frac{\frac{r}{n} + 1 - e^{-\sigma/\sqrt{n}}}{e^{\sigma/\sqrt{n}} - e^{-\sigma/\sqrt{n}}} \right) - e^{-\frac{u}{\sqrt{n}}} \left( \frac{e^{\sigma/\sqrt{n}} - \frac{r}{n} - 1}{e^{\sigma/\sqrt{n}} - e^{-\sigma/\sqrt{n}}} \right) \right]^{nt}.
$$


(ii) We compute the limit

$$
\lim_{n \to \infty} \varphi_n(u) = \lim_{x \downarrow 0} \varphi_{\frac{1}{x^2}}(u),
$$

where we made the substitution $x = \frac{1}{\sqrt{n}}$. Taking the logarithm, we write

$$
\log \varphi_{\frac{1}{x^2}}(u) = \frac{t}{x^2} \log \left[ \frac{(r x^2 + 1) \sinh ux + \sinh (\sigma - u)x}{\sinh \sigma x} \right].
$$

Using the definitions $\sinh z = \frac{e^z - e^{-z}}{2}$ and $\cosh z = \frac{e^z + e^{-z}}{2}$, along with the identity

$$
\sinh(A - B) = \sinh A \cosh B - \cosh A \sinh B,
$$

we rewrite the equation as

$$
\log \varphi_{\frac{1}{x^2}}(u) = \frac{t}{x^2} \log \left[ \cosh ux + \frac{(r x^2 + 1 - \cosh \sigma x) \sinh ux}{\sinh \sigma x} \right].
$$


(iii) Using the Taylor series expansions

$$
\cosh z = 1 + \frac{1}{2} z^2 + O(z^4), \quad \sinh z = z + O(z^3),
$$

we show that

$$
\frac{\cosh ux + \frac{(r x^2 + 1 - \cosh \sigma x) \sinh ux}{\sinh \sigma x}}{\sinh \sigma x} = 1 + \frac{1}{2} u^2 x^2 + \frac{r u x^2}{\sigma} - \frac{1}{2} u x^2 \sigma + O(x^4).
$$

Since $\log(1 + x) = x + O(x^2)$, we obtain

$$
\lim_{x \downarrow 0} \log \varphi_{\frac{1}{x^2}}(u) = t \left( \frac{1}{2} u^2 + \frac{r u}{\sigma} - \frac{1}{2} u \sigma \right).
$$


(iv) The limiting distribution of $\frac{\sigma}{\sqrt{n}} M_{nt,n}$ is normal with mean $(r - \frac{1}{2} \sigma^2)t$ and variance $\sigma^2 t$.


**Exercise 3.9**
Let $m > 0$ be given, and define

$$
f(t,m) = \frac{m}{t\sqrt{2\pi t}} \exp \left\{ -\frac{m^2}{2t} \right\}.
$$

According to (3.7.3) in Theorem 3.7.1, $f(t,m)$ is the density of the first passage time $\tau_m = \min\{t \geq 0; W(t) = m\}$, where $W$ is a Brownian motion without drift. Define the Laplace transform of the density as

$$
g(\alpha, m) = \int_{0}^{\infty} e^{-\alpha t} f(t,m) dt, \quad \alpha > 0.
$$

This problem verifies that

$$
g(\alpha, m) = e^{-m\sqrt{2\alpha}},
$$

which is the formula derived in Theorem 3.6.2.

(i) For $k \geq 1$, define

$$
a_k(m) = \frac{1}{\sqrt{2\pi}} \int_{0}^{\infty} t^{-k/2} \exp \left\{ -\alpha t - \frac{m^2}{2t} \right\} dt.
$$

Thus, we show that

$$
g_m(\alpha, m) = a_3(m) - m^2 a_5(m),
$$


$$
g_{mm}(\alpha, m) = -3 m a_5(m) + m^3 a_7(m).
$$


(ii) Using integration by parts, show that

$$
a_5(m) = -\frac{2\alpha}{3} a_3(m) + \frac{m^2}{3} a_7(m).
$$


(iii) Use (i) and (ii) to show that $g$ satisfies the second-order ordinary differential equation

$$
g_{mm}(\alpha, m) = 2\alpha g(\alpha, m).
$$


(iv) The general solution to a second-order ODE of the form

$$
a y''(m) + b y'(m) + c y(m) = 0
$$


$$
y(m) = A_1 e^{\lambda_1 m} + A_2 e^{\lambda_2 m},
$$

where $\lambda_1$ and $\lambda_2$ are roots of the characteristic equation

$$
a\lambda^2 + b\lambda + c = 0.
$$

Here, assuming distinct roots, solve the equation in (iii) when $\alpha > 0$, obtaining two undetermined parameters $A_1$ and $A_2$.

(v) Derive the bound

$$
g(\alpha, m) \leq \frac{m}{\sqrt{2\pi}} \int_{0}^{m} \sqrt{\frac{m}{t}} t^{-3/2} \exp \left\{ -\frac{m^2}{2t} \right\} dt + \frac{1}{\sqrt{2\pi}m} \int_{m}^{\infty} e^{-\alpha t} dt.
$$

Using this, show that for any $\alpha > 0$,

$$
\lim_{m \to \infty} g(\alpha, m) = 0.
$$

This determines one of the parameters in the general solution in (iii).

(vi) Using the change of variables $s = t/m^2$ and then $y = 1/\sqrt{s}$, show that

$$
\lim_{m \to 0} g(\alpha, m) = 1.
$$

This determines the second parameter in the general solution of (iii).