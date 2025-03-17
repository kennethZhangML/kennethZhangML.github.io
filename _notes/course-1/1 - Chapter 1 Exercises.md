---
layout: page
title: Chapter 1 Exercises
description: Exercises for Chapter 1 - No-Arbitrage Pricing Model.
parent: course-1
importance: 2
permalink: /notes/course-1/chapter-1-exercises/
nav: false
---


**Exercise 1.1**
Assume in the one-period binomial market of Section 1.1 that both $H$ and $T$ have positive probability of occurring. Show that condition 1.1.2 precludes arbitrage. In other words, show that if $X_0 = 0$ and:


$$
X_1 = \Delta_0 S_1 + (1 + r)(X_0 - \Delta_0 S_0)
$$


then we cannot have $X_1$ strictly positive with positive probability unless $X_1$ is strictly negative with positive probability as well, and this is the case regardless of the choice of the number $\Delta_0$

**Solution**:
If we set $X_0 = 0$:


$$
\begin{align*}
X_1 &= \Delta_0 S_1 + (1 + r)(X_0 - \Delta_0 S_0)\\
&= \Delta_0 S_1 - (1 + r)\Delta_0 S_0\\
&= \Delta_0 (S_1 - (1 + r)S_0)
\end{align*}
$$


Meaning that :
For $S_1(H)$, we have:


$$
X_1(H) = \Delta_0 (uS_0 - (1 + r) S_0) = \Delta_0 S_0(u - (1 + r))
$$


For $S_1(T)$ we have:


$$
X_1(T) = \Delta_0 (dS_0 - (1 + r)S_0) = \Delta_0 S_0 (d - (1 + r))
$$


Thus, for no arbitrage, we require $X_1$ to not be strictly positive with a zero probability of being strictly negative. Thus, we evaluate the following cases:
1. If $\Delta_0 > 0$ this implies that $X_1(H) > 0$ which in turn tells us that $u > (1 + r)$. Equivalently, we can say that $X_1(T) < 0$ and that this also requires $d < (1 + r)$.
2. If $\Delta_0 < 0$ this implies that $X_1(H) < 0$ which in turn tells us that $u < (1 + r)$. Equivalently, we can say that $X_1(T) > 0$ and that this also requires $d > (1 + r)$. 

Both the positive and negative outcomes occur as long as $0 < d < 1 + r < u$ ensuring that we have no arbitrage. Therefore, $X_1$ cannot be strictly positive or negative with positive probability in both cases, unless there is no arbitrage. 



**Exercise 1.2**
Suppose in the situation of example 1.1.1 that the option sells for 1.20 at time zero. Consider an agent who begins with wealth $X_0 = 0$ and at time zero buys $\Delta_0$ shares of stock and $\Gamma_0$ options. The numbers $\Delta_0$ and $\Gamma_0$ can be either positive or negative or zero. This leaves the agent with a cash position of $-4 \Delta_0 - 1.20 \Gamma_0$. If this is positive, it is invested in the money market. If it is negative, it represents money borrowed from the money market. At time one, the value of the agent's portfolio of stock, option, and money market assets is:

$$
X_1 = \Delta_0 S_0 + \Gamma(S_1 - 5)^{+} - \frac{5}{4}(4 \Delta_0 + 1.20 \Gamma_0)
$$

Assume that both $H$ and $T$ have positive probability of occurring. Show that if there is a positive probability that $X_1$ is positive, then there is a positive probability that $X_1$ is negative. In other words, one cannot find an arbitrage when the time-zero price of the options is 1.20.

**Solution**:
We start with $X_0 = 0$ at time $0$ and we purchase $\Delta_0$ shares of stock and $\Gamma_0$ options. Thus, we can equate our cash position as:

$$
-4 \Delta_0 - 1.20 \Gamma_0
$$

At $t = 1$ then we have:

$$
X_1 = \Delta_0 S_0 + \Gamma(S_1 - 5)^{+} - \frac{5}{4}(4 \Delta_0 + 1.20 \Gamma_0)
$$

- $\Delta_0 S_1$ takes $S_1(H) = uS_0$ and,
- $S_1(T) = dS_0$ 
for $u > 1 + r > d > 0$. Thus, we have our option value at:

$$
\Gamma_0(S_1 - 5)^{+}
$$

with strike price $K = 5$. 
- If $S_1 \ge 5$ then we have payoff $S_1 - 5$
- If $S_1 < 5$ then we have payoff is $0$
The money market debt is:

$$
-\frac{5}{4}(4 \Delta_0 + 1.20 \Gamma_0)
$$

with interest rate $r = \frac{1}{4}$. Thus we have cases:

If $S_1 = uS_0$ then:

$$
X_1(H) = \Delta_0 u S_0 + \Gamma_0 (uS_0 - 5) + -\frac{5}{4}(4 \Delta_0 + 1.20 \Gamma_0)
$$

If $S_1 = dS_0$ then:

$$
X_1(T) = \Delta_0 dS_0 + \Gamma_0(0) - \frac{5}{4}(4 \Delta_0 + 1.20 \Gamma_0)
$$

Thus, if $X_1(H) > 0$
- $\Delta_0 uS_0$ grows with $u > 1 + r$ and,
- $\Gamma_0 (uS_0 - 5)$ grows if $uS_0 > 5$ 
This means that $-\frac{5}{4} (4 \Delta_0 + 1.20 \Gamma_0)$ reduces portfolio value depending on the size of $\Delta_0$ and $\Gamma_0$. Moreover, we have the case where if $X_1(T) < 0$:
- $\Delta_0 dS_0$ shrinks with $d < 1 + r$ and,
- $\Gamma_0$ is not affected because the option is worthless if $dS_0 < 5$
This means that $-\frac{5}{4} (4 \Delta_0 + 1.20 \Gamma_0)$ reduces portfolio value as well.

Now, we combine our cases:
If $\Delta_0 > 0$ and $\Gamma_0 > 0$:
- $X_1(H) > 0$ has positive contributions from stock and option growth.
- $X_1(T) < 0$ since the stock falls, the option is worthless, and the debt reduces wealth 
If $\Delta_0 < 0$ and $\Gamma_0 < 0$:
- $X_1(H) < 0$ has negative stock and option contributions 
- $X_1(T) > 0$ since the short positions gain as the stock falls 
We see that the dynamics of the portfolio under $H$ and $T$ make it that any choice of $\Delta_0$ and $\Gamma_0$ that makes $X_1 > 0$ with positive probability will also make $X_1 < 0$ with positive probability. This confirms the absence of arbitrage when the option's price at $t = 0$ is 1.20. 


**Exercise 1.3**
In the one-period binomial model of section 1.1, suppose we want to determine the price at time zero of the derivative security $V_1 = S_1$ (i.e., the derivative security pays off the stock price.) (This can be regarded as a European call with strike price $K = 0$). What is the time-zero price $V_0$ given by the risk-neutral pricing formula?

**Solution**:
The solution is quite algebraic and straight forward

$$
\begin{align*}
V_1(H) = uS_0\\
V_1(T) = dS_0
\end{align*}
$$

Using the risk-neutral pricing definition of $V_0$:

$$
\begin{align*}
V_0 &= \frac{1}{1 + r}(\tilde{p}(uS_0) + \tilde{q}(dS_0))\\
&= \frac{1}{1 + r} S_0 (\tilde{p}u + \tilde{q}d)\\
\\
\implies \tilde{p}u + \tilde{q}d &= \frac{1 + r - d}{u - d}u + \frac{u - 1 - r}{u - d}d\\
&= \frac{u(1 + r - d) + d(u - 1 - r)}{u - d}\\
\\
\implies u(1 + r - d) + d(u - 1 - r) &= u + ur - ud + du - d - dr\\
&= u + du + ud - d + r(u - d)\\
\\
u + du - ud - d + r(u - d) &= (u + d - d) + r(u - d)\\
&= (1 + r)(u - d)\\
\\
\implies \tilde{p}u + \tilde{q}d &= \frac{(1 + r)(u - d)}{u - d} = 1 + r\\
\\
\implies V_0 &= \frac{1}{1 + r} S_0 (1 + r) = S_0 \implies V_0 = S_0
\end{align*}
$$

Thus, the time zero price $V_0$ of the derivative security $V_1 = S_1$ is:

$$
V_0 = S_0
$$

This is intuitive as the derivative security replicates the stock itself so its time-zero price must be equal the current stock price. 


**Exercise 1.4**
In the proof of Theorem $1.2.2$ show under the induction hypothesis that:

$$
X_{n + 1}(\omega_1 \omega_2 \dots \omega_n T) = V_{n + 1}(\omega_1 \omega_2 \dots \omega_n T)
$$


**Solution**:
Start by using the recursive definition of $X_{n + 1}$:

$$
X_{n+1}(\omega_1 \omega_2 \dots \omega_n T) = \Delta_n S_{n+1}(\omega_1 \omega_2 \dots \omega_n T) + (1 + r) \big(X_n - \Delta_n S_n\big)
$$

Then, by the induction hypothesis:

$$
X_n(\omega_1 \omega_2 \dots \omega_n) = V_n(\omega_1 \omega_2 \dots \omega_n)
$$


$$
\begin{align*}
X_{n+1}(\omega_1 \omega_2 \dots \omega_n T) &= \Delta_n S_{n+1}(\omega_1 \omega_2 \dots \omega_n T) + (1 + r) \big(V_n - \Delta_n S_n\big), \\
\Delta_n &= \frac{V_{n+1}(\omega_1 \omega_2 \dots \omega_n H) - V_{n+1}(\omega_1 \omega_2 \dots \omega_n T)}{S_{n+1}(\omega_1 \omega_2 \dots \omega_n H) - S_{n+1}(\omega_1 \omega_2 \dots \omega_n T)}, \\
V_n &= \frac{1}{1 + r} \big[ \tilde{p} V_{n+1}(\omega_1 \omega_2 \dots \omega_n H) + \tilde{q} V_{n+1}(\omega_1 \omega_2 \dots \omega_n T) \big], \\
X_{n+1}(\omega_1 \omega_2 \dots \omega_n T) &= \frac{V_{n+1}(\omega_1 \omega_2 \dots \omega_n H) - V_{n+1}(\omega_1 \omega_2 \dots \omega_n T)}{S_{n+1}(\omega_1 \omega_2 \dots \omega_n H) - S_{n+1}(\omega_1 \omega_2 \dots \omega_n T)} S_{n+1}(\omega_1 \omega_2 \dots \omega_n T) \\
&\quad + (1 + r) \Bigg[\frac{\tilde{p} V_{n+1}(\omega_1 \omega_2 \dots \omega_n H) + \tilde{q} V_{n+1}(\omega_1 \omega_2 \dots \omega_n T)}{1 + r} \Bigg], \\
X_{n+1}(\omega_1 \omega_2 \dots \omega_n T) &= V_{n+1}(\omega_1 \omega_2 \dots \omega_n T).
\end{align*}
$$



**Exercise 1.5**
In example 1.2.4, we considered an agent who sold the look-back options for $V_0 = 1.376$ and bought $\Delta_0 = 1.733$ shares of stock at time zero. At time one, if the stock goes up, she has a portfolio valued at $V_1(H) = 2.24$. Assume that she now takes a position of:

$$
\Delta_1 (H) = \frac{V_2(HH) - V_2(HT)}{S_2(HH) - S_2(HT)}
$$

in the stock. Show that, at time two, if the stock goes up again, she will have a portfolio valued at $V_2(HH) = 3.20$, whereas if the stock goes down, her portfolio will be worth $V_2(HT) = 2.40$. Finally, under the assumption that the stock goes up in the first period and down in the second period, assume the agent takes a position of:

$$
\Delta_2(HT) = \frac{V_3(HTH) - V_3(HTT)}{S_3(HTH) - S_3(HTT)}
$$

in the stock. Show that, at time three, if the stock goes up in the third period, she will have a portfolio valued at $V_3(HTH) = 0$, whereas if the stock goes down, her portfolio will be worth $V_3(HTT) = 6$. In other words, she has hedged her short position in the option. 

**Solution**
The portfolio value at time $2$ is:

$$
X_2 = \Delta_1(H) S_2 + (1+r)(V_1(H) - \Delta_1(H) S_1(H))
$$

Thus we substitute the values:

$$
S_1(HH) = 16, S_2(HT) = 4, S_1(H) = 8, 1 + r = \frac{5}{4}
$$

For the $HH$ case:

$$
\begin{align*}
\Delta_1(H) &= \frac{V_2(HH) - V_2(HT)}{S_2(HH) - S_2(HT)} = \frac{3.20 - 2.40}{16 - 4} = \frac{0.80}{12} = 0.0667, \\
X_2(HH) &= \Delta_1(H) S_2(HH) + (1 + r)(V_1(H) - \Delta_1(H) S_1(H)), \\
X_2(HH) &= (0.0667)(16) + \frac{5}{4} \left( 2.24 - (0.0667)(8) \right), \\
X_2(HH) &= 1.0672 + \frac{5}{4}(2.24 - 0.5336), \\
X_2(HH) &= 1.0672 + \frac{5}{4}(1.7064), \\
X_2(HH) &= 1.0672 + 2.1328 = 3.20.
\end{align*}
$$

For the $HT$ case:

$$
\begin{align*}
X_2(HT) &= \Delta_1(H) S_2(HT) + (1 + r)(V_1(H) - \Delta_1(H) S_1(H)), \\
X_2(HT) &= (0.0667)(4) + \frac{5}{4} \left( 2.24 - (0.0667)(8) \right), \\
X_2(HT) &= 0.2668 + \frac{5}{4}(1.7064), \\
X_2(HT) &= 0.2668 + 2.1328 = 2.40.
\end{align*}
$$


Similarly, at time $3$, the portfolio value is:

$$
X_3 = \Delta_2 S_3 + (1 + r)(V_2 - \Delta_2 S_2)
$$

Then, again, we can substitute the values:

$$
S_3(HTH) = 8, S_3(HTT) = 2, S_2(HT) = 4, 1 + r = \frac{5}{4}
$$

For the $HTH$ case:

$$
\begin{align*}
\Delta_2(HT) &= \frac{V_3(HTH) - V_3(HTT)}{S_3(HTH) - S_3(HTT)} = \frac{0 - 6}{8 - 2} = \frac{-6}{6} = -1, \\
X_3(HTH) &= \Delta_2(HT) S_3(HTH) + (1 + r)(V_2(HT) - \Delta_2(HT) S_2(HT)), \\
X_3(HTH) &= (-1)(8) + \frac{5}{4} \left( 2.40 - (-1)(4) \right), \\
X_3(HTH) &= -8 + \frac{5}{4}(2.40 + 4), \\
X_3(HTH) &= -8 + \frac{5}{4}(6.40), \\
X_3(HTH) &= -8 + 8 = 0.
\end{align*}
$$

For the $HTT$ case:

$$
\begin{align*}
X_3(HTT) &= \Delta_2(HT) S_3(HTT) + (1 + r)(V_2(HT) - \Delta_2(HT) S_2(HT)), \\
X_3(HTT) &= (-1)(2) + \frac{5}{4} \left( 2.40 - (-1)(4) \right), \\
X_3(HTT) &= -2 + \frac{5}{4}(2.40 + 4), \\
X_3(HTT) &= -2 + \frac{5}{4}(6.40), \\
X_3(HTT) &= -2 + 8 = 6.
\end{align*}
$$



**Exercise 1.6**
Consider a bank that has a long position in the European call written on the stock price in Figure 1.1.2. The call expires at time one and has strike price $K = 5$. In Section 1.1, we determined the time-zero price of this call to be $V_0 = 1.20$. At time zero, the bank owns this option, which ties up capital $V_0 = 1.20$. The bank wants to earn the interest rate 25% on this capital until time one (i.e., without investing any more money, and regardless of how the coin tossing turns out, the bank wants to have:

$$
\frac{5}{4} \cdot 1.20 = 1.50
$$

at time 1, after collecting the payoff from the option (if any) at time one). Specify how the bank's trader should invest the stock and money markets to accomplish this. 

```tikz
\begin{document} 
\begin{tikzpicture} 
% Tree Nodes 
\node (S0) at (0,0) {$S_0$};
% Root node 
\node (S1H) at (2,1.5) {$S_1(H) = uS_0$}; 
% Upward move 
\node (S1T) at (2,-1.5) {$S_1(T) = dS_0$}; 
% Downward move % Connections 
\draw[thick] (S0) -- (S1H); \draw[thick] (S0) -- (S1T); 
% Time Labels 
\node at (0,-0.8) {$t = 0$}; 
\node at (2,-0.8) {$t = 1$}; 
\node at (2, 0.8) {$t = 1$};
\end{tikzpicture} 
\end{document}
```

**Solution**
We can use the formulas for the risk-neutral probabilities and $S_0$ to induce backward induction to solve for $V_0$ from $V_2$ and $V_1$, then use the Delta-Hedging formula to solve for the amount of shares needed to be purchased for every case $H$ or $T$ in order for the bank to achieve a long-position-one period via hedging. 

First, given the following, we can solve for $\tilde{p}$ and $\tilde{q}$:

$$
S_0 = 4, u = 2, d = \frac{1}{4}, K = 5
$$

Thus, we have the formulas for the risk-neutral probabilities. 

$$
\begin{align*}
\tilde{p} &= \frac{1 + r - d}{u - d} = \frac{\frac{5}{4} - \frac{1}{2}}{2 - \frac{1}{2}} = \frac{\frac{3}{4}}{\frac{3}{2}} = \frac{1}{2}, \\
\tilde{q} &= \frac{1}{2}.
\end{align*}
$$

Thus, from Figure 1.1.2, we get the stock price tree:

$$
\begin{align*}
S_1(H) &= 8, \\
S_1(T) &= 2, \\
S_2(HH) &= 16, \\
S_2(HT) &= 4, \\
S_2(TT) &= 1.
\end{align*}
$$

Using the definition of $V_N$ we can conduct backward induction for $t = N$:

$$
\begin{align*}
V_N &= (S_N - K)^+.
\end{align*}
$$

at any $t$:

$$
\begin{align*}
V_n &= \frac{1}{1 + r} \left[ \tilde{p} V_{n+1}(H) + \tilde{q} V_{n+1}(T) \right].
\end{align*}
$$

We have the following option payoffs at $t = 2$:

$$
\begin{align*}
V_2(HH) &= (16 - 5)^+ = 11, \\
V_2(HT) &= (4 - 5)^+ = 0, \\
V_2(TT) &= (1 - 5)^+ = 0.
\end{align*}
$$

At $t = 1$:

$$
\begin{align*}
V_1(H) &= \frac{1}{1 + r} \left[ \tilde{p} V_2(HH) + \tilde{q} V_2(HT) \right], \\
&= \frac{4}{5} \left[ \frac{1}{2} \cdot 11 + \frac{1}{2} \cdot 0 \right], \\
&= \frac{4}{5} \cdot 5.5, \\
&= 4.4.
\end{align*}
$$


$$
\begin{align*}
V_1(T) &= \frac{1}{1 + r} \left[ \tilde{p} V_2(HT) + \tilde{q} V_2(TT) \right], \\
&= \frac{4}{5} \left[ \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot 0 \right], \\
&= 0.
\end{align*}
$$

At $t = 0$:

$$
\begin{align*}
V_0 &= \frac{1}{1 + r} \left[ \tilde{p} V_1(H) + \tilde{q} V_1(T) \right], \\
&= \frac{4}{5} \left[ \frac{1}{2} \cdot 4.4 + \frac{1}{2} \cdot 0 \right], \\
&= \frac{4}{5} \cdot 2.2, \\
&= 1.76.
\end{align*}
$$

Finally, we solve using the hedging ratios at $t = 0$:

$$
\begin{align*}
\Delta_0 &= \frac{V_1(H) - V_1(T)}{S_1(H) - S_1(T)}, \\
&= \frac{4.4 - 0}{8 - 2}, \\
&= 0.733.
\end{align*}
$$

and at $t = 1$:

$$
\begin{align*}
\Delta_1(H) &= \frac{V_2(HH) - V_2(HT)}{S_2(HH) - S_2(HT)}, \\
&= \frac{11 - 0}{16 - 4}, \\
&= \frac{11}{12}.
\end{align*}
$$



**Exercise 1.7**
Consider a bank that has a long position in the look-back option. The bank intends to hold this option until expiration and receive the payoff $V_3$. At time zero, the bank has capital $V_0 = 1.376$ tied up in the option and wants to earn the interest rate of 25% on this capital until time three (i.e., without investing any more money, and regardless of how the coin tossing turns out, the bank wants to have

$$
\left(\frac{5}{4} \right)^3 \cdot 1.376 = 2.6875
$$

at time three, after collecting the payoff from the look-back option at time three). Specify how the bank's trader should invest the stock and the money market account to accomplish this. 

**Solution**
Again, quite algebraic and still quite intuitive via backward induction on $V_3, V_2, V_1$, then using the Delta-Hedging strategy to get the number of shares.

$$
\begin{align*}
\tilde{p} = \frac{5/4 - 1/2}{2 - 1/2} = \frac{1}{2}, \quad \tilde{q} = \frac{1}{2}
\end{align*}
$$


$$
\begin{align*}
V_3(HHH) = 0, V_3(HTH) = 0, V_3(THH) = 0\\
V_3(HHT) = 8, V_3(HTT) = 6, V_3(THT) = 2\\
V_3(TTH) = 2, V_3(TTT) = 3.5
\end{align*}
$$

We now perform backward induction:

$$
\begin{align*}
V_3(HHH) &= S_3(HHH) - S_3(HHH) = 32 - 32 = 0, \\
V_3(HHT) &= S_2(HH) - S_3(HHT) = 16 - 8 = 8, \\
V_3(HTH) &= S_1(H) - S_3(HTH) = 8 - 8 = 0, \\
V_3(HTT) &= S_1(H) - S_3(HTT) = 8 - 2 = 6, \\
V_3(THH) &= S_3(THH) - S_3(THH) = 8 - 8 = 0, \\
V_3(THT) &= S_2(TH) - S_3(THT) = 4 - 2 = 2, \\
V_3(TTH) &= S_0 - S_3(TTH) = 4 - 2 = 2, \\
V_3(TTT) &= S_0 - S_3(TTT) = 4 - 0.5 = 3.5.
\end{align*}
$$


$$
\begin{align*}
V_2(HH) &= \frac{1}{1 + r} \left[ \tilde{p} V_3(HHH) + \tilde{q} V_3(HHT) \right] \\
        &= \frac{4}{5} \left[ \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot 8 \right] = 3.20, \\
V_2(HT) &= \frac{1}{1 + r} \left[ \tilde{p} V_3(HTH) + \tilde{q} V_3(HTT) \right] \\
        &= \frac{4}{5} \left[ \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot 6 \right] = 2.40, \\
V_2(TH) &= \frac{1}{1 + r} \left[ \tilde{p} V_3(THH) + \tilde{q} V_3(THT) \right] \\
        &= \frac{4}{5} \left[ \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot 2 \right] = 0.80, \\
V_2(TT) &= \frac{1}{1 + r} \left[ \tilde{p} V_3(TTH) + \tilde{q} V_3(TTT) \right] \\
        &= \frac{4}{5} \left[ \frac{1}{2} \cdot 2 + \frac{1}{2} \cdot 3.5 \right] = 2.20.
\end{align*}
$$


$$
\begin{align*}
V_1(H) &= \frac{1}{1 + r} \left[ \tilde{p} V_2(HH) + \tilde{q} V_2(HT) \right] \\
       &= \frac{4}{5} \left[ \frac{1}{2} \cdot 3.20 + \frac{1}{2} \cdot 2.40 \right] = 2.24, \\
V_1(T) &= \frac{1}{1 + r} \left[ \tilde{p} V_2(TH) + \tilde{q} V_2(TT) \right] \\
       &= \frac{4}{5} \left[ \frac{1}{2} \cdot 0.80 + \frac{1}{2} \cdot 2.20 \right] = 1.20.
\end{align*}
$$


$$
\begin{align*}
V_0 &= \frac{1}{1 + r} \left[ \tilde{p} V_1(H) + \tilde{q} V_1(T) \right] \\
    &= \frac{4}{5} \left[ \frac{1}{2} \cdot 2.24 + \frac{1}{2} \cdot 1.20 \right] = 1.376.
\end{align*}
$$

Then, we get the following result from the Delta-Hedging Strategy:

$$
\begin{align*}
\Delta_0 &= \frac{V_1(H) - V_1(T)}{S_1(H) - S_1(T)} \\
         &= \frac{2.24 - 1.20}{8 - 2} = 0.1733.
\end{align*}
$$



**Exercise 1.8**
Consider the three-period model of Example 1.2.1 with $S_0 = 4, u = 2, d = \frac{1}{2}$ and take the interest rate $r = \frac{1}{4}$ so that $\tilde{p} = \tilde{q} = \frac{1}{2}$. For $n = 0, 1, 2, 3$ define:

$$
Y_n = \sum_{k = 0}^n S_k
$$

to be the sum of the stock prices between times zero and $n$. Consider an Asian call option that expires at time three and has strike $K = 4$ (i.e., whose payoff at time three is:

$$
\left(\frac{1}{4} Y_3 - 4\right)^{+}
$$

). This is like a European call, except the payoff of the option is based on the average stock price rather than the final stock price. Let $v_n(s, y)$ denote the price of this option at time $n$ if $S_n = s$ and $Y_n = y$. In particular, $v_3(s, y) = \left(\frac{1}{4}y - 4 \right)^{+}$:
1. Develop and algorithm for computing $v_n$ recursively. In particular, write a formula for $v_n$ in terms of $v_{n + 1}$
2. Apply the algorithm developed in 1. to compute $v_0(4, 4)$, the price of the asian option at time zero. 
3. Provide a formula for $\delta_n (s, y)$, the number of shares of stock that should be held by the replicating portfolio at time $n$ if $S_n = s$ and $Y_n = y$.


**Solution**:
At time $n$, the price of the Asian option is given by:

$$
\begin{align*} 
v_n(s, y) = \frac{1}{1 + r} \left[ \tilde{p} v_{n+1}(us, y + us) + \tilde{q} v_{n+1}(ds, y + ds) \right]. 
\end{align*}
$$

At time $n = 3$ the payoff of the Asian option is:

$$
\begin{align*} 
v_3(s, y) = \left( \frac{1}{4} y - 4 \right)^+
\end{align*}
$$

with Parameters:

$$
\begin{align*}
S_0 = 4, \, u = 2, \, d = \frac{1}{2}, \, r = \frac{1}{4}, \, \tilde{p} = \tilde{q} = \frac{1}{2}. 
\end{align*}
$$

We compute $v_n(s, y)$ recursively: 

$$
\begin{align*} 
v_3(32, 60) &= \left( \frac{1}{4} \cdot 60 - 4 \right)^+ = 11, \\ 
v_3(8, 36) &= \left( \frac{1}{4} \cdot 36 - 4 \right)^+ = 5, \\ 
v_3(2, 18) &= \left( \frac{1}{4} \cdot 18 - 4 \right)^+ = 0, \\ 
v_3(0.5, 7.5) &= \left( \frac{1}{4} \cdot 7.5 - 4 \right)^+ = 0. 
\end{align*}
$$

Now, we can compute $v_2(s, y)$:

$$
\begin{align*} 
v_2(s, y) = \frac{1}{1 + r} \left[ \tilde{p} v_3(us, y + us) + \tilde{q} v_3(ds, y + ds) \right]. 
\end{align*}
$$


$$
\begin{align*} 
v_2(16, 28) &= \frac{4}{5} \left[ \frac{1}{2} \cdot 11 + \frac{1}{2} \cdot 5 \right] = \frac{4}{5} \cdot 8 = 6.4, \\ 
v_2(4, 10) &= \frac{4}{5} \left[ \frac{1}{2} \cdot 5 + \frac{1}{2} \cdot 0 \right] = \frac{4}{5} \cdot 2.5 = 2.0, \\ 
v_2(1, 5) &= \frac{4}{5} \left[ \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot 0 \right] = 0. 
\end{align*}
$$

And now we can compute $v_1(s, y)$:

$$
\begin{align*} 
v_1(s, y) = \frac{1}{1 + r} \left[ \tilde{p} v_2(us, y + us) + \tilde{q} v_2(ds, y + ds) \right]. 
\end{align*}
$$


$$
\begin{align*} 
v_1(8, 12) &= \frac{4}{5} \left[ \frac{1}{2} \cdot 6.4 + \frac{1}{2} \cdot 2.0 \right] = \frac{4}{5} \cdot 4.2 = 3.36, \\ 
v_1(2, 6) &= \frac{4}{5} \left[ \frac{1}{2} \cdot 2.0 + \frac{1}{2} \cdot 0 \right] = \frac{4}{5} \cdot 1.0 = 0.8. 
\end{align*}
$$

and get $v_0(4, 4)$:

$$
\begin{align*} 
v_0(4, 4) = \frac{1}{1 + r} \left[ \tilde{p} v_1(8, 12) + \tilde{q} v_1(2, 6) \right]. 
\end{align*}
$$


$$
\begin{align*} 
v_0(4, 4) &= \frac{4}{5} \left[ \frac{1}{2} \cdot 3.36 + \frac{1}{2} \cdot 0.8 \right] \\ 
&= \frac{4}{5} \cdot 2.08 = 1.664. 
\end{align*}
$$

The hedging ratio $\delta_n (s, y)$ is given by: 

$$
\begin{align*} 
\delta_n(s, y) = \frac{v_{n+1}(us, y + us) - v_{n+1}(ds, y + ds)}{us - ds}. \end{align*}
$$
