---
layout: page
title: Chapter 1 - No-Arbitrage Pricing Model
description: Notes on the No-Arbitrage Pricing Model.
parent: course-1
importance: 1
permalink: /notes/course-1/chapter-1-no-arbitrage/
nav: false
tikzjax: true  # Enables TikZJax on this page
---

### 1.1 One-Period Binomial Model 

##### Introduction to One-Period BM Parameters
The general **one-period** model for our binomial pricing model has:
- **Time Zero**: the beginning of the period 
- **Time One**: the end of the period 
```tikz
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
```

At time zero, we have a stock price whose price per share we denote by $S_0$, a positive quantity known at time zero. 

At time one, the price per share of this stock will be either:
1. $S_1(H)$
2. $S_1(T)$

**Note**: Both are positive values where $H$ denotes Heads and $T$ denotes Tails. 

**Assume** that we have a coin (**need not be a fair coin**) that is tossed, and the outcome of the coin toss determines the price at time one (either $S_1(H)$ or $S_1(T)$).

Denote the probability of head's as $p$ and tails $q = 1 - p$ (both positive probabilities). 
**Remark**: As a result of the coin toss, we know the value which the stock price will take at time one at time one, but NOT at time zero (referred to as a random quantity).

##### Up and Down Factors 
Denote the up-factor ($u$) and down-factors ($d$) of our stock prices from $S_0$ to either $S_1(H)$ or $S_2(H)$ as the following, whilst assuming that $d < u$:


$$
u = \frac{S_1(H)}{S_0} \quad\text{and} \quad d = \frac{S_1(T)}{S_0}
$$



Note: If $d > u$, then we can achieve $d < u$ by relabelling the sides of the coin. If $d = u$ then the stock price at time one is not really random and the model is therefore not useful for simulations.

##### Interest Rates
1. For every 1 dollar invested into the money market at time zero, we yield $1 + r$ dollars at time one (via time-value of money) where $r$ is our interest rate. 
2. For every 1 dollar borrowed from the money market at time zero results in a debt of $1 + r$ at time one (interest for borrowing = interest for investing).

Note: Always the case that $r \ge 0$, but mathematically, we only require $r > -1$

##### Arbitrage: Efficient Market 
Arbitrage is a trading strategy that 
- **begins with no money**, 
- **zero probability of losing money**, and 
- **has positive probability of making money**
Models that admit arbitrage $\implies$ should not be used for analysis. 

**No-Arbitrage Condition**:


$$
0 < d < 1 + r < u
$$


- $d > 0$; follows from positivity of the stock prices and is previously assumed 
- $d \ge 1 +r$; Start with 0 wealth, at time zero borrow from MM to buy stock. With the worst case ($S_1(T)$), the stock at time 1 still is worth enough to pay off MM debt and has a positive probability of being worth strictly more since $u > d \ge 1 + r$
- $u \le 1 + r$; Sell a stock short, invest proceeds in MM, with best case $S_1(H)$ still yielding a replacement at time 1 that is $\le$ to the value of the money in MM. 
	- Thus, there is a positive probability that the cost of replacing the stock is strictly less than the value of MM investment. 

**e.g., European Call Option**
Confers the owner the right but NOT the obligation buy one share of the stock at time one for the strike price $K$. Consider when $S_1(T) < K < S_1(H)$.
- If we get a tail on the toss, the option expires 
- If we get a head on the toss, the option can be exercised and yields a profit of $S_1(H) - K$ 
In general, we say that the option at time $1$ is worth $(S_1 - K)^{+}$ where the notation $(\dots)^{+}$ indicates that we take the maximum of the expression in parentheses and zero. 

**Goal of Arbitrage Pricing Theory**: 
Replicate the option (or some other derivative) by trading in the stock and money market.


**e.g., Take $S(0) = 4, u = 2, d=\frac{1}{2}, r=\frac{1}{4}$**
We get that $S_1(H) = 4 \times 2 = 8$ and that we get $S_1(T) = 4 \times \frac{1}{2} = 2$. Suppose that the strike price of the European Call Option is $K = 5$. 

Moreover, let's say we begin with initial wealth $X_0 = 1.2$ and buy $\Delta_0 = \frac{1}{2}$ shares of stock at time $0$. Since $S(0) = 4$, it would cost us:


$$
\Delta_0 \times \frac{1}{2} = 4 \times 0.5 = 2
$$


But, we would need to borrow $2 - 1.2 = 0.8$ from the money market to do this. Thus, this would result in a debt of $X_0 - \Delta_0 S_0 = -0.8$ in the money market. 

At time 1, our cash position would be:


$$
(1 + r)(X_0 - \Delta_0 S_0) = -1

$$


with a debt of $1$ to the money market.

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
Thus, at time 1, we will have stock $S$ valued at:


$$
\frac{1}{2} S_1(H) = 4 \quad\text{or}\quad \frac{1}{2}S_1(T) = 1
$$


Thus, the value of our portfolio for heads or tails would be, respectively:


$$
X_1(H) = \frac{1}{2}S_1(H) + (1 + r)(X_0 - \Delta_0 S_0) = 3
$$



$$
X_(T) = \frac{1}{2}S_1(T) + (1+r)(X_0 - \Delta_0 S_0) = 0
$$


This approach accurately replicates the European Call Option in the stock and money market as it agrees with $(S_1(H) - 5)^{+}$ or $(S_1(T) - 5)^{+} = 0$.

Thus, we have shown that in the market with the stock, the money market, and the option, there is an arbitrage unless the time-zero price of the option is 1.20. 
- Shares of the stock can be subdivided for sale/purchase
- The interest rate for investing is the same as the interest rate for borrowing
- The purchase price of stock is the same as the selling price (zero bid-ask spread)
- At any time, the stock can take only two possible values in the next period 

Note: Sometimes, the bid-ask spread can be ignored because not too much trading is taking place, otherwise, departure of the model from reality becomes a serious issue. 


### Recap:
$S_{n + 1}$ represents the price of the stock at time $n$, which evolves based on the outcomes of the coin tosses, as such:


$$
S_{n + 1}(H) = uS_n, S_{n + 1}(T) = dS_n
$$


where $u > 1$ and $d < 1$ are the up-factor and down-factor respectively. We assume that $S_n$ follows a binomial tree structure with its value at each step depending on the cumulative outcomes of the coin toss. 

$X_n$ represents the value of our portfolio at time $n$ consisting of:
- $\Delta_n$ the number of shares of stock held at time $n$, and 
- The cash position in the money market account


$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - \Delta_n S_n)
$$


where:
- $\Delta_n S_{n + 1}$ is the value of the stock holdings at time $n + 1$, and
- $(1 + r)(X_n - \Delta_n S_n)$ is the value of the money market account after interest accrual 
Essentially, $X_n$ tracks the wealth of the portfolio, dynamically adjusted through hedging in the stock and money market. 

$V_n$ represents the no-arbitrage price of the derivative security at time $n$. Moreover, it is the value to perfectly replicate the derivative's payoff via a self-financing portfolio. 


$$
V_{n + 1} = \frac{1}{1 + r}[\tilde{p} V_{n + 1}(H) + \tilde{q} V_{n + 1}(T)]
$$


where $\tilde{p}, \tilde{q}$ are risk-neutral probabilities. $V_n$ is determined by the replication strategy and represents the fair market value of the derivative, precluding arbitrage. 

$\Delta_n$ (hedging ratio) is the number of shares of stock to hold in a portfolio at time $n$ to replicate the derivative security's payoff:


$$
\Delta_n = \frac{V_{n + 1}(H) - V_{n + 1}(T)}{S_{n+1}(H) - S_{n + 1}(T)}
$$


where:
- $V_{n + 1}(H)$ and $V_{n + 1}(T)$ are the values of the derivative under two possible outcomes of the stock price 
- $S_{n + 1}(H)$ and $V_{n + 1}(T)$ are the stock prices under the two possible outcomes

### Generalizing the One-Period Binomial Model
Define a **derivative security** that pays some amount $V_1(H)$ at time one if the coin toss results in head and pays a possibly different amount $V_1(T)$ if the coin toss is tails. 

To find $V_0$, we replicate the security in the stock and money market, 
- Suppose we begin with wealth $X_0$
- Then, we buy $\Delta_0$ shares of stock at time $0$
- Our cash position is then $X_0 - \Delta_0 S_0$ 
Thus, the value of our portfolio of stock + money market account at time 1 is:


$$
X_1 = \Delta_0 S_1 + (1 + r)(X_0 - \Delta_0 S_0) = (1+r)X_0 + \Delta_0(S_1 - (1 + r)S_0)
$$


We choose $X_0, \Delta_0$ such that:


$$
X_1(H) = V_1(H) \quad\text{and}\quad X_1(T) = V_1(T)
$$


are satisfied. We know $V_1(H), V_1(T)$ at time zero, but do NOT know, of the two possibilities, which will actually be realized. Thus, our replication requires:


$$
\begin{align*}
X_1 &= \Delta_0 S_1 + (1 + r)(X_0 - \Delta_0 S_0)\\
&= \Delta_0 S_1 + (1 + r)X_0 - (1 + r)\Delta_0 S_0\\
&= (1 + r)X_0 + \Delta_0 S_1 - (1 + r)\Delta_0 S_0\\
&= (1 + r)X_0 + \Delta_0(S_1 - (1 + r)S_0)\\
\\
\text{For } X_1(H) &= V_1(H)\\
X_1(H) &= (1 + r)X_0 + \Delta_0 (S_1(H) - (1 + r)S_0)\\
&= X_0 + \Delta_0 \left(\frac{1}{1 + r} S_1(H) - S_0\right)\\
&= \frac{1}{1 + r} V_1(H)\\
\\
\text{The condition} X_1(T) &= V_1(T) \text{ and isolated similarly.}
\end{align*}
$$



$$
\begin{align*}
X_0 + \Delta_0 \left(\frac{1}{1+r} S_1(H) - S_0 \right) &= \frac{1}{1+r} V_1(H)\\
X_0 + \Delta_0 \left(\frac{1}{1+r} S_1(T) - S_0 \right) &= \frac{1}{1+r} V_1(T)\\
\implies X_0 + \Delta_0 \left(\frac{1}{1 + r}[\tilde{p}S_1(H) + \tilde{q}S_1(T)] - S_0 \right) &= \frac{1}{1 + r}[\tilde{p}S_1(H) + \tilde{q}S_1(T)]
\end{align*}
$$


So, we want to choose $\tilde{p}, \tilde{q}$ that correspond the probability of getting heads and tails, respectively, such that they satisfy the stock price at $S_0$:


$$
S_0 = \frac{1}{1 + r} [\tilde{p}S_1(H) + \tilde{q}S_1(T)] \implies X_0 = \frac{1}{1 + r} [\tilde{p}V_1(H) + \tilde{q}V_1(T)]
$$


Solving for $\tilde{p}$ produces the formulas for our risk-neutral probabilities:


$$
\boxed{
\tilde{p} = \frac{1 + r - d}{u - d} \text{ and } \tilde{q} = \frac{u - 1 - r}{u - d}
}
$$


Solving for $\Delta$ by subtracting gives us the **Delta-Hedging Formula**:


$$
\frac{1}{1 + r}V_1(H) - \frac{1}{1 + r} V_1(T) \implies \boxed{
\Delta_0 = \frac{V_1(H) - V_1(T)}{S_1(H) - S_1(T)}
}
$$


Thus, if we:
- Start with wealth $X_0$ given by the risk-neutral probability expression
- Then, at time 0, buy $\Delta_0$ shares of stock
- Then, at time 1:
	- If heads: have portfolio valued at $V_1(H)$
	- If tails: have portfolio valued at $V_1(T)$
We thus have successfully **hedged a short position in the derivative security**. Thus, the derivative security that pays $V_1$ at time 1, should be priced at:


$$
V_0 = \frac{1}{1 + r} [\tilde{p} V_1(H) + \tilde{q} V_1(T)]
$$


Or, we could set up a hedge to protect against loss of that value. The number of shares of the underlying stock held by a long position hedge is the negative of the number determine by the Delta-Hedging Formula. 

Note: $\tilde{p}, \tilde{q}$ are both positive by the no-arbitrage condition, and are NOT the actual probabilities of the heads and tails, hence being called the risk-neutral probabilities. Under actual probabilities, the average rate of growth of the stock is typically strictly greater than the rate of growth of an investment in the money market. 

Thus, $p, q = 1 - p$ should satisfy:


$$
S_0 < \frac{1}{1 + r} [p S_1(H) + qS_(T)]
$$



### 1.2 Multi-Period Binomial Model 
Assume we have a coin (not necessarily fair). Instead of just one coin toss, we toss the coin repeatedly, where, for every heads, the stock price moves up, and for every tail, the stock price moves down for $u$ and $d$ factors, respectively. 
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

\end{tikzpicture}

\end{document}

```
Our initial stock price $S_0$ is always positive in this model.
At time 1, we denote our price by $S_1(H) = u S_0$ for heads, and $S_1(T) = dS_0$ for tails.
At time 2, after two tosses of our coin, we have 8 possible outcomes:


$$
\begin{align*}
S_2(HH) &= uS_1(H) = u^2 S_0, S_2(HT) = dS_1(H) = du S_0\\
S_2(TH) &= uS_1(T) = udS_0, S_2(TT) = dS_1(T) = d^2 S_0
\end{align*}
$$


```tikz
\begin{document}

\begin{tikzpicture}

% Tree Nodes
\node (S0) at (0,0) {$S_0 = 4$};
\node (S1H) at (2,2.5) {$S_1(H) = 8$};
\node (S1T) at (2,-2.5) {$S_1(T) = 2$};
\node (S2HH) at (4,4.5) {$S_2(HH) = 16$};
\node (S2HT) at (4,0) {$S_2(HT) = S_2(TH) = 4$};
\node (S2TT) at (4,-4.5) {$S_2(TT) = 1$};
\node (S3HHH) at (6,5.5) {$S_3(HHH) = 32$};
\node (S3HHT) at (6,3) {$S_3(HHT) = S_3(HTH) = S_3(THH) = 8$};
\node (S3HTT) at (6,-3) {$S_3(HTT) = S_3(THT) = S_3(TTH) = 2$};
\node (S3TTT) at (6,-5.5) {$S_3(TTT) = 0.5$};

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
\node at (2,-3.5) {$t = 1$};
\node at (4,-5.5) {$t = 2$};
\node at (6,-6.5) {$t = 3$};

\end{tikzpicture}

\end{document}
```
Consider a European Call option with strike $K$ at time 2 (i.e., a European DS that expires $N\ge2$). At expiration the payoff of a call option with strike price $K$ and expiration time 2 is:


$$
V_2 = (S_2 - K)^{+}
$$


where $V_2, S_2$ depend on the first and second coin tosses. We want to determine the no-arbitrage price for this option at time zero. 

Suppose we sell the option at time 0 for $V_0$, then buy $\Delta_0$ shares of stock investing $V_0 - \Delta_0 S_0$ into the money market to finance the transaction.


$$
V_0 - \Delta_0 S_0 < 0 \implies \text{borrowing } \Delta_0 S_0 - V_0
$$


Thus, at time 1, the agent has a portfolio (excluding the short in the option) valued at:


$$
\begin{align*}
X_1 &= \Delta_0 S_1 + (1 + r)(V_0 - \Delta_0 S_0)\\
\\
&\text{2 Equations are implicit in $X_1$}\\
X_1(H) &= \Delta_0 S_1(H) + (1 + r)(V_0 - \Delta_0 S_0)\\
X_1(T) &= \Delta_0 S_1(T) + (1 + r)(V_0 - \Delta_0 S_0)
\end{align*}
$$


Thus, after our first coin toss, our portfolio is valued at $X_1$ dollars and we can re-adjust our hedge, if we want to. Suppose we do, and decide to hold $\Delta_1$ shares of stock, where $\Delta_1$ is allowed to depend on the first coin toss (since it has already realized). Then, we invest $X_1 - \Delta_1 S_1$ in the money market. Thus, in period 2, her wealth will be given by:


$$
V_2 = \Delta_1 S_2 + (1 + r)(X_1 - \Delta_1 S_1)
$$


where $S_2, V_2$ depend on the first two coin tosses:


$$
\begin{align*}
V_2(HH) &= \Delta_1(H) S_2(HH) + (1 + r)(X_1(H) - \Delta_1(H)S_1(H))\\
V_2(HT) &= \Delta_1(H) S_2(HT) + (1 + r)(X_1(H) - \Delta_1(H)S_1(H))\\
V_2(TH) &= \Delta_1(T) S_2(TH) + (1 + r)(X_1(T) - \Delta_1(T) S_1(T))\\
V_2(TT) &= \Delta_1(T) S_2(TT) + (1 + r)(X_1(T) - \Delta_1(T) S_1(T))
\end{align*}
$$


Giving 6 unknowns, $V_0, \Delta_1, \Delta_1(H), \Delta_1(T), X_1(H)$ and $X_1(T)$. We determine the no-arbitrage price of $V_0$ at time zero of the option and replicate our portfolio $\Delta_0, \Delta_1(H), \Delta_1(T)$ solving for $\Delta_1(T)$ to get our **Delta Hedging Formula**:


$$
\Delta_1(T) = \frac{V_2(TH) - V_2(TT)}{S_2(TH) - S_2(TT)} \implies X_1(T) = \frac{1}{1 + r}[\tilde{p}V_2(TH) + \tilde{q}V_2(TT)]
$$


given risk-neutral probabilities, $\tilde{p}, \tilde{q}$. Therefore, the price of the option at time one if the first coin toss results in a head or tail, respectively, is $V_1(H)$ and $V_1(T)$:


$$
\begin{align*}
V_1(T) &= \frac{1}{1 + r}[\tilde{p}V_2(TH) + \tilde{q} V_2(TT)]\\
V_1(H) &= \frac{1}{1 + r}[\tilde{p}V_2(HH) + \tilde{Q} V_2(HT)]
\end{align*}
$$


where $(\Delta_0, \Delta_1)$ and $(X_0, X_1, X_2)$ are stochastic processes (sequence of r.v.'s).


### Generalizing No-Arbitrage Portfolio Replication 
If we begin with initial wealth $X_0$ and specify:
- $\Delta_0$: number of shares of a stock to buy 
- $\Delta_1(H)$: number of shares purchased if first coin toss results in heads
- $\Delta_1(T)$: number of shares purchased if first coin toss results in tails 
Then, the value of this portfolio, defined recursively, beginning with $X_0$, has wealth:


$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - \Delta_n S_n)
$$


**Note**: The actual values of these random variables are NOT realized until the outcomes of the coin tossing are revealed, but this time 0 equation permits us to compute what the value of the portfolio will be at every subsequent time under every coin-toss scenario. 

Choose $\Delta_n$ to be number of shares of stock held by the portfolio, and $X_n$ be the corresponding portfolio values, regardless of how $X_0$ and $\Delta_n$ are chosen. 

When we choose $X_0$ and $\Delta_n$ to replicate a security, we use the symbol $V_n$ in place of $X_n$ as the no-arbitrage price of the derivative security at time $n$.

#### Theorem: Replication under Multi-Period Binomial Model
Consider an $N$-period binomial asset-pricing model, with $0 < d < 1 + r < u$ with:


$$
\tilde{p} = \frac{1 + r - d}{u - d} \quad\text{and}\quad \tilde{q} = \frac{u - 1 - r}{u - d}
$$


Let $V_N$ be a random variable depending on the first $N$ coin tosses $\omega_1 \omega_2 \dots \omega_N$. Define a recursively backward in time sequence of random variable $V_{N - 1}, V_{N -  2}, \dots, V_0$ by:


$$
V_n(\omega_1 \omega_2 \dots \omega_n) = \frac{1}{1 + r}[\tilde{p} V_{n + 1}(\omega_1 \omega_2 \dots \omega_n H) + \tilde{q} V_{n + 1}(\omega_1 \omega_2 \dots \omega_n T)]
$$


so that each $V_n$ depends on the first $n$ coin tosses $\omega_1 \omega_2 \dots \omega_n$ where $n$ ranges between $N - 1$ and $0$. Next we define the **General Delta Hedging Equation**:


$$
\Delta_n (\omega_1 \dots \omega_n) = \frac{V_{n + 1}(\omega_1 \dots \omega_n H) - V_{n + 1}(\omega_1 \dots \omega_n T)}{S_{n + 1} (\omega_1 \dots \omega_n H) - S_{n + 1}(\omega_1 \dots \omega_n T)}
$$


where $n$ ranges between $0$ and $N - 1$. Set $X_0 = V_0$ and define a recursively forward in time the portfolio values $X_1, X_2, \dots, X_N$ by:


$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - \Delta_n S_n)
$$


Then, we have that:


$$
X_N(\omega_1 \omega_2 \dots \omega_N) = V_N(\omega_1 \omega_2 \dots \omega_n) \text{ for all } \omega_1 \omega_2 \dots \omega_N
$$


**Definition**: The price of the derivative security at time $n$ if the outcomes of the first $n$ tosses are $\omega_1, \dots, \omega_n$ is the random variable $V_n(\omega_1, \dots, \omega_n)$ for $n = 1, 2, \dots, N$. The price of the derivative security at time zero is defined to be $V_0$. 

#### Proof: Arbitrage Pricing Theorem
We prove by forward induction on $n$ that:


$$
X_n(\omega_1 \omega_2 \dots \omega_n) = V_n(\omega_1 \omega_2 \dots \omega_n), \quad \text{for all } \omega_1 \omega_2 \dots \omega_n,
$$


where $n$ ranges between $0$ and $N$.

**Base Case: $n = 0$:**
The case of $n = 0$ is given by the definition of $X_0$ as $V_0$.

**Inductive Step:**
Assume that $X_n(\omega_1 \omega_2 \dots \omega_n) = V_n(\omega_1 \omega_2 \dots \omega_n)$ holds for some value of $n$ less than $N$. We aim to show that this holds for $n+1$.
Fix $\omega_1 \omega_2 \dots \omega_n$. For the particular coin toss $\omega_{n+1}$, we consider the cases $\omega_{n+1} = H$ and $\omega_{n+1} = T$. Using (1.2.14), we compute:


$$
X_{n+1}(\omega_1 \omega_2 \dots \omega_n H) = \Delta_n S_{n+1}(\omega_1 \dots \omega_n H) + (1+r)(X_n - \Delta_n S_n),
$$


and similarly for $\omega_{n+1} = T$.
Substituting $\Delta_n$ from (1.2.17) into (1.2.20), and using the induction hypothesis $X_n = V_n$, we simplify:


$$
X_{n+1}(H) = (1+r) V_n + \Delta_n S_{n+1}(u - (1+r)),
$$


where:


$$
\Delta_n = \frac{V_{n+1}(H) - V_{n+1}(T)}{S_{n+1}(H) - S_{n+1}(T)}.
$$


Using the definition of $V_n$ in (1.2.16), this reduces to:


$$
X_{n+1}(H) = V_{n+1}(H).
$$


A similar argument applies for $\omega_{n+1} = T$, and we conclude that:


$$
X_{n+1}(\omega_1 \omega_2 \dots \omega_{n+1}) = V_{n+1}(\omega_1 \omega_2 \dots \omega_{n+1}).
$$


Since $\omega_1 \omega_2 \dots \omega_{n+1}$ is arbitrary, the induction step is complete. The multi-period binomial model is said to be **complete** because every derivative security can be replicated by trading in the underlying stock and the money market. In a complete market, every derivative security has a unique price that precludes arbitrage, and this is the price defined in Definition 1.2.3.

The Theorem above applies to **path-dependent** options as well as derivative securities whose payoff depends only on the final stock price. 


**e.g., Suppose $S_0 = 4, u = 2, d = \frac{1}{2}$ with interest $r = \frac{1}{4}$ and $\tilde{p} = \tilde{q} = \frac{1}{2}$.** 
```tikz
\begin{document}

\begin{tikzpicture}

% Tree Nodes
\node (S0) at (0,0) {$S_0 = 4$};
\node (S1H) at (2,2.5) {$S_1(H) = 8$};
\node (S1T) at (2,-2.5) {$S_1(T) = 2$};
\node (S2HH) at (4,4.5) {$S_2(HH) = 16$};
\node (S2HT) at (4,0) {$S_2(HT) = S_2(TH) = 4$};
\node (S2TT) at (4,-4.5) {$S_2(TT) = 1$};
\node (S3HHH) at (6,5.5) {$S_3(HHH) = 32$};
\node (S3HHT) at (6,3) {$S_3(HHT) = S_3(HTH) = S_3(THH) = 8$};
\node (S3HTT) at (6,-3) {$S_3(HTT) = S_3(THT) = S_3(TTH) = 2$};
\node (S3TTT) at (6,-5.5) {$S_3(TTT) = 0.5$};

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
\node at (2,-3.5) {$t = 1$};
\node at (4,-5.5) {$t = 2$};
\node at (6,-6.5) {$t = 3$};

\end{tikzpicture}

\end{document}
```
Consider a look-back option that gives:


$$
V_3 = \max_{0 \le n \le 3} S_n - S_3
$$


at time 3 (the value of the option at time 3).


$$
\begin{align*}
V_3(HHH) &= S_3(HHH) - S_3(HHH) = 32 - 32 = 0, \\
V_3(HHT) &= S_2(HH) - S_3(HHT) = 16 - 8 = 8, \\
V_3(HTH) &= S_1(H) - S_3(HTH) = 8 - 8 = 0, \\
V_3(HTT) &= S_1(H) - S_3(HTT) = 8 - 2 = 6, \\
V_3(THH) &= S_3(THH) - S_3(THH) = 8 - 8 = 0, \\
V_3(THT) &= S_2(TH) - S_3(THT) = 4 - 2 = 2, \\
V_3(TTH) &= S_0 - S_3(TTH) = 4 - 2 = 2, \\
V_3(TTT) &= S_0 - S_3(TTT) = 4 - 0.5 = 3.50, \\
\\
V_2(HH) &= \frac{4}{5} \left[ \frac{1}{2} V_3(HHH) + \frac{1}{2} V_3(HHT) \right] = 3.20, \\
V_2(HT) &= \frac{4}{5} \left[ \frac{1}{2} V_3(HTH) + \frac{1}{2} V_3(HTT) \right] = 2.40, \\
V_2(TH) &= \frac{4}{5} \left[ \frac{1}{2} V_3(THH) + \frac{1}{2} V_3(THT) \right] = 0.80, \\
V_2(TT) &= \frac{4}{5} \left[ \frac{1}{2} V_3(TTH) + \frac{1}{2} V_3(TTT) \right] = 2.20, \\
V_1(H) &= \frac{4}{5} \left[ \frac{1}{2} V_2(HH) + \frac{1}{2} V_2(HT) \right] = 2.24, \\
\\
V_1(T) &= \frac{4}{5} \left[ \frac{1}{2} V_2(TH) + \frac{1}{2} V_2(TT) \right] = 1.20, \\
\\
\implies V_0 &= \frac{4}{5} \left[ \frac{1}{2} V_1(H) + \frac{1}{2} V_1(T) \right] = 1.376, \\
\Delta_0 &= \frac{V_1(H) - V_1(T)}{S_1(H) - S_1(T)} = \frac{2.24 - 1.20}{8 - 2} = 0.1733.
\end{align*}
$$







