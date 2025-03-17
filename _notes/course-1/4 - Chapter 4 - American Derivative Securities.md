---
layout: page
title: Chapter 4 - American Derivative Securities
description: Notes on American derivative securities and their valuation.
parent: course-1
importance: 7
permalink: /notes/course-1/chapter-4-american-derivatives/
nav: false
---


**American vs. European Options**
- European: exercise on expiration date
- American: exercise at any time up to and including expiration date 
**American** is at least as valuable at as **European** option counterpart. Moreover, American and European calls have the same price. 

American options have early exercise premium, premium paid at early exercise and never can be worth less than the payoff $\rightarrow$ intrinsic value.
- Under $\tilde{\mathbb{P}}$, European option discounted price process is martingale 
- Under $\tilde{\mathbb{P}}$, American option discounted price process is a supermartingale 
	- fail to exercise at optimal exercise date, tendency to lose value $\implies$ supermartingale
	- For some initial capital, we sell the option, and use the capital to **hedge a short position in the option**

**Non-Dependent American Derivatives**

**European Algorithm**
Take $N$-period binomial model, with $u$ and $d$ parameters, and interest $r$ satisfying:

$$
0 < d < 1 + r < u
$$

Take derivative security paying $g(S_N)$ at time$N$ for some function $g$. Since the stock price is Markov, $V_n$ of this derivative security at each time $n$ as a function $v_n$ of the stock price at time:

$$
v_n = v_n(S_n),\quad n = 0, 1, \dots, N
$$

for $0 \le n \le N$ the function $v_n$ is defined by the European algorithm:

$$
v_N(s) = \max \{g(s), 0\},\quad v_n(s) = \frac{1}{1 + r} \left[\tilde{p}v_{n + 1}(us)) + \tilde{q} v_{n + 1}(ds) \right], \quad n = N - 1, N - 2, \dots, 0
$$

We replicating portfolio which hedges a short position in the option:

$$
\Delta_n = \frac{v_{n + 1}(uS_n) - v_{n + 1}(dS_n)}{(u - d)S_n},\quad n = 0, 1, \dots, N
$$


**American Algorithm**
A payoff function $g$ with $n \le N$ such that our exercise receives payment $g(S_n)$ at current stock price $S_n$. The portfolio hedges a short position has value $X_n$ satisfying:

$$
X_n \ge g(S_n),\quad n = 0, 1, \dots, N
$$

i.e., $g(S_n)$ is the intrinsic value and the replicating portfolio at that time must be equal to the value of the derivative security. 

$$
v_N(s) = \max\{g(s), 0\},\quad v_n(s) = \max\left\{g(s), \frac{1}{1 + r} \left[\tilde{p}v_{n + 1}(us) + \tilde{q}v_{n + 1}(ds) \right] \right\}
$$

Then $V_n = v_n(S_n)$ is the price of the derivative security at time $n$. 


e.g., Assume $r = \frac{1}{4}$ and $\tilde{p} = \tilde{q} = \frac{1}{2}$. Take an American option with strike $5, so, the owner at time $n$ when exercising the option, receives $5 - S_n$ so $g(s) = 5 - s$, in a 2-period model.

$$
\begin{align*}
v_2(s) &= \max\{5 - s, 0\}\\
v_n(s) &= \max \left\{5 - s, \frac{2}{5}\left[v_{n + 1}(2s) + v_{n + 1}(\frac{s}{2}) \right] \right\}
\end{align*}
$$

for $n = 1, 0$. 

$$
\begin{align*}
S_0 &= 4\\
S_1(H) &= 8, S_1(T) = 2\\
S_2(HH) &= 16, S_2(HT) = S_2(TH) = 4, S_2(TT) = 1
\end{align*}
$$

which gives $v_n(s)$ for each level:

$$
\begin{align}
    v_2(16) &= 0, \\
    v_2(4) &= 1, \\
    v_2(1) &= 4, \\
    v_1(8) &= \max \left\{ (5 - 8), \frac{2}{5} (0 + 1) \right\} = \max \{-3, 0.40\} = 0.40, \\
    v_1(2) &= \max \left\{ (5 - 2), \frac{2}{5} (1 + 4) \right\} = \max \{3, 2\} = 3, \\
    v_0(4) &= \max \left\{ (5 - 4), \frac{2}{5} (0.40 + 3) \right\} = \max \{1, 1.36\} = 1.36.
\end{align}
$$

Now, let's find a replicating portfolio, with initial capital $1.36$ and compute $\Delta_0$ so that the value of the hedging portfolio at time one agrees with the option value. 

$$
\begin{align*}
0.40 &= v_1(S_1(H))\\
&= S_1(H) + (1 + r)(X_0 - \Delta_0 S_0)\\
&= 8 \Delta_0 + \frac{5}{4}(1.36 - 4 \Delta_0)\\
&= 3 \Delta_0 + 1.70 \implies \Delta_0 = -0.43
\end{align*}
$$

Similarly, if we have a tail on the first toss:

$$
\begin{align*}
3 &= v_1(S_1(T))\\
&= S_1(T) \Delta_0 + (1 + r)(X_0 - \Delta_0 S_0)\\
&= 2 \Delta_0 + \frac{5}{4}(1.36 - 4 \Delta_0)\\
&= -3 \Delta_0 +1.70 \implies \Delta_0 = -0.43
\end{align*}
$$

We can find $\Delta_0$:

$$
\Delta_0 = \frac{v_1(8) - v_1(2)}{8 - 2} = \frac{0.40 - 3}{8 - 2} = -0.43
$$

If we begin with initial capital $X_0 = 1.36$ then take position $\Delta_0$ shares of stock at time zero, then at time one we will have $X_1 = V_1 = v_1(S_1)$ regardless of the outcome of the coin toss. 

What if the owner refuses to exercise? Thus, we must continue hedging the option. 
The value in time 2, if the toss is heads, the value of the option is $v_2(4) = 1$ and if tails then the value of the option would be $v_2(1) = 4$. Using the risk-neutral pricing formula, to construct a hedge against these two probabilities, at time 1, we need to have a portfolio value of:

$$
\frac{2}{5} (v_2(4) + v_2(1)) = 2
$$

But our hedging portfolio valued at $v_1(2) = 3$, thus we have to consume $1 to continue hedging with the remaining $2 in our portfolio, i.e., consume $1 and change position to $\Delta_1(T)$ shares,

If heads,

$$
\begin{align*}
1 &= v_2(S_2(TH))\\
&= 4 \Delta_1(T) + \frac{5}{4}(2 - 2 \Delta_1 (T))\\
&= 1.5 \Delta_1(T) + 2.50 \implies \Delta_1(T) = -1
\end{align*}
$$

If tails,

$$
\begin{align*}
4 &= v_2(S_2(TT))\\
&= \Delta_1(T) + \frac{5}{4}(2 - 2\Delta_1(T))\\
&=-1.5 \Delta_1(T) + 2.50
\end{align*}
$$

Thus, 

$$
\Delta_1(T) = \frac{v_2(4) - v_2(1)}{4 - 1} = \frac{1 - 4}{4 - 1} = -1
$$

which we got from the delta-hedging formula, verifying that our calculation when changing our hedging position to $\Delta_1(T)$ shares results in the same number of shares. 

**Theorem: Replicating Path-Independent American Derivatives**
Assume risk-neutral probabilities calculated as defined for the $N$-period binomial model. Let a payoff function $g(s)$ be defined recursively backward in time by a sequence of functions, 

$$
v_N(s), v_{N - 1}(s), v_{N - 2}(s), \dots, v_0(s)
$$

Define,

$$
\Delta_n = \frac{v_{n + 1}(uS_n) - v_{n + 1}(dS_n)}{(u - d)S_n}
$$

and,

$$
C_n = v_n(S_n) - \frac{1}{1 + r}[\tilde{p}v_{n + 1}(uS_n) + \tilde{q}v_{n + 1}(dS_n)]
$$

for $n = 0, \dots, N - 1$. Then $C_n \ge 0$ for all $n$. If we set $X_0 = v_0(S_0)$ then we define recursively forward in time the portfolio values $X_1, \dots, X_N$ by:

$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - C_n - \Delta_n S_n)
$$

where $X_n(\omega_1, \dots, \omega_n) = v_n (S_n (\omega_1, \dots, \omega_n))$ for all $n$ and $\omega_1, \dots, \omega_n$. Moreover, $X_n \ge g(S_n)$ for all $n$

Thus, we have hedged a short position in the American derivative security with intrinsic value $g(S_n)$ at each time $n$. Moreover, we can do so and still consume money at certain times, with the value of our hedging portfolio $X_n$ guaranteed to be at least as great as the intrinsic value of the derivative security, since:

$$
v_n(S_n) \ge g(S_n)
$$

i.e., the non-negativity of $C_n$ guarantees and implies that:

$$
v_n(S_n) \ge \frac{1}{1 + r}[\tilde{p}v_{n + 1}(uS_n) + \tilde{q}v_{n + 1}(dS_n)]
$$


**Stopping Times**
Exercise of an American derivative security is random, dependent on price movements of underlying asset. We describe the exercise rule by a random variable $\tau$. 
- Where $\tau = \infty$ options should be allowed to expire without exercise
- Where $\tau = i \in \mathbb{Z}$ defined on some $\Omega$ and takes values in a set of integers and $\infty$, we can thinking of this as **stopping** the American put hedging problem by exercising the put.

If the owner uses the exercise rule, regardless of the coin tossing, they would exercise the put in the money. The decision of whether or not to exercise can only be made based on previous observations. 

**Definition**: Take an $N$-period binomial model, a stopping time is a random variable $\tau$ that takes values $0, 1, \dots, N$ or $\infty$ and satisfies the condition:

$$
\text{if } \tau(\omega_1\omega_2 \dots \omega_n \omega_{n + 1} \dots \omega_N) = n,\quad\text{then } \tau(\omega_1\omega_2 \dots \omega_n \omega_{n + 1}' \dots \omega_N') = n \text{ for } \omega_{n + 1}' \dots \omega_N'  
$$

The condition in the definition above that if $\tau(\omega_1 \omega_2 \dots \omega_n \omega_{n + 1} \dots \omega_N) = n$ then $\tau(\omega_1 \omega_2 \dots \omega_n \omega_{n + 1}' \dots \omega_N') = n$ for all $\omega_{n + 1}' \dots \omega_N'$ ensures that stopping is based only on available information. The decision of stopping at time $n$ is only based on the first $n$ coin tosses and not on the outcome of any subsequent toss. 
$\implies$ we can call this stochastic process (stopping time) as a stopped process 

$\tau$ is our stopping time, and the stopped process $Y_{n \wedge \tau}$:

$$
Y_{0 \wedge \tau} = Y_0 = 1.36 \leftrightarrow Y_{1 \wedge \tau} = Y_1
$$

because $1 \wedge \tau = 1$ regardless of coin tossing. But $2 \wedge \tau$ depends on the coin tossing, getting $HH$ or $HT$ and $TH$ or $TT$ results in $2 \wedge \tau$ equalling 2 or 1, respectively. i.e., $Y_{n \wedge \tau}$ is a frozen process.

The discounted American put price process $Y_n$ is a supermartingale but not a martingale under the risk-neutral probabilities. However, if this process is stopped at the optimal exercise time, it become a martingale. If the owner of the security permits a time to pass in which the supermartingale inequality is strict, they have failed to exercise optimally. 

**Theorem**: Optional Sampling, A martingale stopped at a stopping time is a martingale. A supermartingale (or submartingale) stopped at a stopping time is a supermartingale (or submartingale, respectively).


e.g., Consider the discounted stock price process: 
$$ M_n = \left(\frac{4}{5}\right)^n S_n $$
 which is assumed to be a martingale under the risk-neutral probability measure $\tilde{\mathbb{P}}$. At every node, the value is the average of the values at the two subsequent nodes. 
The evolution of $M_n$ is shown below: 
- **Initial Value**: $M_0 = 4$ 
- **First Level**: 
	- $M_1(H) = 6.40$ 
	- $M_1(T) = 1.60$ 
- **Second Level**: 
	- $M_2(HH) = 10.24$ 
	- $M_2(HT) = M_2(TH) = 2.56$ 
	- $M_2(TT) = 0.64$ 
This demonstrates the martingale property, where the expectation at each node is the average of the subsequent nodes. We now see the effect of stopping the process at a stopping time $\tau$. 

The stopped process: 
$$ M_{n \wedge \tau} $$
preserves the martingale property, meaning that at each node, the expectation remains unchanged. 
- **Initial Value**: $M_0 \wedge \tau = 4$ 
	- **First Level**: 
		- $M_{1 \wedge \tau}(H) = 6.40$ 
		- $M_{1 \wedge \tau}(T) = 1.60$ 
	- **Second Level**: 
		- $M_{2 \wedge \tau}(HH) = 10.24$ 
		- $M_{2 \wedge \tau}(HT) = M_{2 \wedge \tau}(TH) = 2.56$ 
		- $M_{2 \wedge \tau}(TT) = 1.60$ 

The key result is that stopping at $\tau$ maintains the martingale property. If we stop at a non-stopping time $\rho$, the martingale property is destroyed. In this case, the stopping rule looks ahead and chooses to stop when the stock price is to increase, introducing a downward bias. 

Stopped Process at $\rho$ 
- **Initial Value**: $M_0 \wedge \rho = 4$ 
- **First Level**: - $M_{1 \wedge \rho}(H) = 4$ 
	- $M_{1 \wedge \rho}(T) = 1.60$ 
- **Second Level**: 
	- $M_{2 \wedge \rho}(HH) = 4$ 
	- $M_{2 \wedge \rho}(HT) = 4$ 
	- $M_{2 \wedge \rho}(TH) = 1.60$ 
	- $M_{2 \wedge \rho}(TT) = 0.64$
This biased process demonstrates why stopping at a non-stopping time $\rho$ results in a violation of the martingale property.

**Theorem**: Let $X_n$ for $n = 0, 1, \dots, N$ be a submartingale and let $\tau$ be a stopping time. Then,

$$
\mathbb{E} X_{n \wedge \tau} \le \mathbb{E}X_n
$$

If $X_n$ is a submartingale, then $\mathbb{E} X_{n \wedge \tau} \ge \mathbb{E} X_n$; if $X_n$ is a martingale, then,

$$
\mathbb{E}X_{n \wedge \tau} = \mathbb{E} X_n
$$


**General American Derivatives**
Let's look at path-dependent American derivative securities. Define the price process for such as security and develop its properties, and develop process for hedging a short position in such a derivative security and study the optimal exercise time. 

**Definition**: $G_n$ depends on first $n$ coin tosses, and an American derivative security with intrinsic value process $G_n$ is a contract that can be exercised at any time prior to and including time $N$ and if exercised at $n$, pays off $G_n$. 

Define $V_n$ the price process, by the American risk-neutral pricing formula,

$$
V_n = \max_{\tau \in S_n} \tilde{\mathbb{E}} \left[\mathbb{I}_{\tau \le N} \frac{1}{(1 + r)^{\tau - n}} G_\tau \right],\quad n = 0, 1, \dots, N
$$

Date of exercise can depend on path of the stock price up to the exercise time but not beyond it, i.e., the exercise date will be a stopping time $\tau$ or must be in $S_n$. The owner exercises according to a stopping time $\tau \in S_n$ the value of the derivative to the owner at time $n$ is the risk-neutral discounted expectation of its payoff. 

$n = N$ gives:

$$
V_N = \sup_{\tau \in S_N} \mathbb{I}_{\tau \in N} \frac{1}{(1 + r)^{\tau - N}} G_\tau
$$

To maximize:

$$
\mathbb{I}_{\tau \le N} \frac{1}{(1 + r)^{\tau - N}} G_\tau = \mathbb{I}_{\tau = N} G_N
$$

we choose:

$$
\tau(\omega_1 \dots \omega_n) = N \quad\text{if}\quad G_N(\omega_1 \dots \omega_N) > 0 \quad\text{and}\quad \tau(\omega_1 \dots \omega_N) = \infty \quad\text{if}\quad G_N(\omega_1 \dots \omega_N) \le 0
$$


**Theorem**: The American derivative security price process given by the definition:
1. $V_n \ge \max\{G_n, 0\}$ for all $n$
2. the discounted process $\frac{1}{(1 + r)^n} V_n$ is a supermartingale
3. if $Y_n$ is another process satisfying $Y_n \ge \max\{G_n, 0\}$ for all $n$ and for which we have that $\frac{1}{(1 + r)^n} Y_n$ is a supermartingale, then $Y_n \ge V_n$ for all $n$

Property 2. guarantees that agent with initial capital $V_n$ can construct a hedging portfolio whose value at each time $n$ is $V_n$. Property 1. guarantees that if an agent does this, we have hedged a short position in the derivative security no matter when it was exercised and has sufficient amount of pay off the derivative security. 

**Theorem**: Pricing American Derivative Security Algorithm for path-dependent security 

$$
V_N(\omega_1 \dots \omega_N) = \max \{G_N(\omega_1 \dots \omega_N)\}
$$

where we can recursively compute:

$$
V_n(\omega_1 \dots \omega_n) = \max \{G_n(\omega_1 \dots \omega_n), \frac{1}{1 + r} \tilde{p}V_{n + 1}(\omega_1 \dots \omega_n H) + \tilde{q}V_{n + 1}(\omega_1 \dots \omega_n T) \}
$$

The process $V_n$ given by th definition is the smallest process with these properties and thus the algorithm above must generate the same process as the formula given in our previous definition. 

**Theorem**: Replication of Path-Dependent American Derivatives 
Take $N$-period binomial asset pricing mode with risk-neutral probabilities $p, q$. Let $G_n$ be a random variable depending on the first $n$ coin tosses, with $V_n$ being the value process.

$$
\Delta_n(\omega \dots \omega_n) = \frac{V_{n + 1}(\omega_1 \dots \omega_n H) - V_{n + 1}(\omega_1 \dots \omega_n T)}{S_{n + 1}(\omega_1 \dots \omega_n H) - S_{n + 1}(\omega_1 \dots \omega_n T)}
$$

and we define:

$$
C_n(\omega_1 \dots \omega_1) = V_n(\omega_1 \dots \omega_n) - \frac{1}{1 + r}\left[\tilde{p} V_{n + 1}(\omega_1 \dots \omega_n H) + \tilde{q}V_{n + 1}(\omega_1 \dots \omega_n T) \right]
$$

We have that $C_n \ge 0$ and that if we set $X_0 = V_0$ then we can recursively get the portfolio wealth process as mentioned previously $X_1, X_2, \dots, X_N$ with $X_{n + 1}$ defined by the wealth eq'n
Then we have that $X_n(\omega_1 \dots \omega_n) = V_n(\omega_1 \dots \omega_n)$. 

This is an acceptable sale to the seller because he can construct a hedge for the short position. Also it is also acceptable for the buyer.

If the owner of the derivative security exercises it according to the stopping time $\tau^*$ then the owner will receive cash flows $C_n, C_{n + 1}, \dots, C_{N}$ at times $n, n + 1, \dots, N$ respectively. 


**Theorem**: Optimal exercise
The stopping time 

$$
\tau^* = \min \{n; V_n = G_n\} 
$$

maximizes the right hand side of 

$$
V_n = \max_{\tau \in S_n} \tilde{\mathbb{E}} \left[\mathbb{I}_{\tau \le N} \frac{1}{(1 + r)^{\tau - n}} G_\tau \right],\quad n = 0, 1, \dots, N
$$

when $n = 0$, thus we have that

$$
V_n = \tilde{\mathbb{E}} \left[\mathbb{I}_{\tau \le N} \frac{1}{(1 + r)^{\tau - n}} G_\tau \right],\quad n = 0, 1, \dots, N
$$

The stopping time $\tau^*$ is the first time these two are equal, and may it that they are never equal. 


**American Call Options**
An American call on a non-dividend paying stock there is no advantage to early exercise. This is the consequence of Jensen's inequality for conditional expectations:

Define convex function $g$ for $g(0) = 0$, whenever $s_1 \ge 0, s_2 \ge 0$ and $0 \le \lambda \le 1$ we have:

$$
g(\lambda s_1 + (1 - \lambda) s_2) \le \lambda g(s_1) + (1 - \lambda) g(s_2)
$$


**Theorem**: We consider the $N$-period binomial asset pricing model with the standard conditions and define a convex payoff function $g(s)$ satisfying $g(0) = 0$. 

The value of this derivative security at time zero is then:

$$
V_0^A = \max_{\tau \in S_0} \tilde{\mathbb{E}} \left[\mathbb{I}_{\tau \in N} \frac{1}{(1 + r)^\tau} g(S_\tau) \right]
$$

same as the value of a European derivative security with payoff $g(S_N)$ at expiration $N$

$$
V_0^E = \tilde{\mathbb{E}} \left[\frac{1}{(1 + r)^N} \max \{g(S_N), 0\} \right]
$$

