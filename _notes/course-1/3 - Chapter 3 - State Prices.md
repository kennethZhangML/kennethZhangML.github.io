---
layout: page
title: Chapter 3 - State Prices
description: Notes on State Prices in financial models.
parent: course-1
importance: 5
permalink: /notes/course-1/chapter-3-state-prices/
nav: false
---


Two Probability Measures covered so far:
1. **Actual Probability Measure**: found by empirical estimation
2. **Risk Neutral Probability**: discounted prices of assets are martingales
Disagree on correct positive probabilities, agree on which paths are possible.

**Radon Nikodym Derivative**
Consider $\Omega$ in which we have $\mathbb{P}$ and $\tilde{\mathbb{P}}$. Let's assume that the two measures both given positive probability to every element of $\Omega$ forming the quotient:

$$
Z(\omega) = \frac{\tilde{\mathbb{P}}(\omega)}{\mathbb{P}(\omega)}
$$

$Z$ is a random variable since it depends on the outcome $\omega$ of a random experiment.

**Properties**:
1. $\mathbb{P}(Z > 0) = 1$
2. $\mathbb{E}Z = 1$
3. For any random variable $Y$ we have $\tilde{\mathbb{E}}Y = \mathbb{E}[ZY]$ 

Proofs left as exercise, pretty easy proofs that follow from assumption of $\tilde{\mathbb{P}}(\omega) > 0$ for $\Omega$. 

e.g., Consider the probability space:

$$
\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}
$$

We take $p = \frac{2}{3}$ and $q = \frac{1}{3}$ then the actual probability measures are:

$$
\begin{align}
\mathbb{P}(HHH) &= \left(\frac{2}{3}\right)^3 = \frac{8}{27}, \\
\mathbb{P}(HHT) &= \left(\frac{2}{3}\right)^2 \times \left(\frac{1}{3}\right) = \frac{4}{27}, \\
\mathbb{P}(HTH) &= \left(\frac{2}{3}\right) \times \left(\frac{1}{3}\right) \times \left(\frac{2}{3}\right) = \frac{4}{27}, \\
\mathbb{P}(HTT) &= \left(\frac{2}{3}\right) \times \left(\frac{1}{3}\right)^2 = \frac{2}{27}, \\
\mathbb{P}(THH) &= \left(\frac{1}{3}\right) \times \left(\frac{2}{3}\right)^2 = \frac{4}{27}, \\
\mathbb{P}(THT) &= \left(\frac{1}{3}\right) \times \left(\frac{2}{3}\right) \times \left(\frac{1}{3}\right) = \frac{2}{27}, \\
\mathbb{P}(TTH) &= \left(\frac{1}{3}\right)^2 \times \left(\frac{2}{3}\right) = \frac{2}{27}, \\
\mathbb{P}(TTT) &= \left(\frac{1}{3}\right)^3 = \frac{1}{27}.
\end{align}
$$

Then, the risk-neutral probabilities are computed as:

$$
\begin{align}
\tilde{\mathbb{P}}(HHH) &= \tilde{\mathbb{P}}(HHT) = \tilde{\mathbb{P}}(HTH) = \tilde{\mathbb{P}}(HTT) \\
&= \tilde{\mathbb{P}}(THH) = \tilde{\mathbb{P}}(THT) = \tilde{\mathbb{P}}(TTH) = \tilde{\mathbb{P}}(TTT) = \frac{1}{8}.
\end{align}
$$

Using the Radon-Nikodym derivative, we have:

$$
\begin{align}
Z(HHH) &= \frac{\mathbb{P}(HHH)}{\tilde{\mathbb{P}}(HHH)} = \frac{8/27}{1/8} = \frac{64}{27}, \\
Z(HHT) &= \frac{\mathbb{P}(HHT)}{\tilde{\mathbb{P}}(HHT)} = \frac{4/27}{1/8} = \frac{32}{27}, \\
Z(HTH) &= \frac{\mathbb{P}(HTH)}{\tilde{\mathbb{P}}(HTH)} = \frac{4/27}{1/8} = \frac{32}{27}, \\
Z(HTT) &= \frac{\mathbb{P}(HTT)}{\tilde{\mathbb{P}}(HTT)} = \frac{2/27}{1/8} = \frac{16}{27}, \\
Z(THH) &= \frac{\mathbb{P}(THH)}{\tilde{\mathbb{P}}(THH)} = \frac{4/27}{1/8} = \frac{32}{27}, \\
Z(THT) &= \frac{\mathbb{P}(THT)}{\tilde{\mathbb{P}}(THT)} = \frac{2/27}{1/8} = \frac{16}{27}, \\
Z(TTH) &= \frac{\mathbb{P}(TTH)}{\tilde{\mathbb{P}}(TTH)} = \frac{2/27}{1/8} = \frac{16}{27}, \\
Z(TTT) &= \frac{\mathbb{P}(TTT)}{\tilde{\mathbb{P}}(TTT)} = \frac{1/27}{1/8} = \frac{8}{27}.
\end{align}
$$

Given $V_3$'s we can take the expected value of the discounted prices at time $3$ to get $0$:

$$
V_0 = \tilde{\mathbb{E}} \frac{V_3}{(1 + r)^3} = 1.376
$$


**Definition**
In the $N$-period binomial model with actual probability measure $\mathbb{P}$ and risk-neutral probability measure $\tilde{\mathbb{P}}$, let $Z$ denote the **Radon-Nikodým derivative** of $\tilde{\mathbb{P}}$ with respect to $\mathbb{P}$; 

$$ Z(\omega_1 \dots \omega_N) = \frac{\tilde{\mathbb{P}}(\omega_1 \dots \omega_N)}{\mathbb{P}(\omega_1 \dots \omega_N)} = \left( \frac{\tilde{p}}{p} \right)^{\#H(\omega_1 \dots \omega_N)} \left( \frac{\tilde{q}}{q} \right)^{\#T(\omega_1 \dots \omega_N)}, $$

where $\#H(\omega_1 \dots \omega_N)$ denotes the number of heads appearing in the sequence $\omega_1 \dots \omega_N$ and $\#T(\omega_1 \dots \omega_N)$ denotes the number of tails appearing in this sequence. The **state price density random variable** is given by: 
$$ \zeta(\omega) = \frac{Z(\omega)}{(1 + r)^N}, $$
and $\zeta(\omega) \mathbb{P}(\omega)$ is called the **state price corresponding to** $\omega$. Let $\bar{\omega} = \bar{\omega}_1 \dots \bar{\omega}_N$ be a particular coin toss sequence in the $N$-period model, and consider a **derivative security** that pays off 1 if $\bar{\omega}$ occurs and otherwise pays off 0; i.e.,

$$ 
V_N(\omega) = \begin{cases} 1, & \text{if } \omega = \bar{\omega}, \\ 0, & \text{otherwise}. \end{cases} 
$$

According to the **risk-neutral pricing formula**, value of this derivative security at time zero is:

$$ \mathbb{E}^{\tilde{\mathbb{P}}} \left[ \frac{V_N}{(1 + r)^N} \right] = \frac{\tilde{\mathbb{P}}(\bar{\omega})}{(1 + r)^N} = \frac{Z(\bar{\omega}) \mathbb{P}(\bar{\omega})}{(1 + r)^N} = \zeta(\bar{\omega}) \mathbb{P}(\bar{\omega}). $$

We see that the **state price** $\zeta(\bar{\omega}) \mathbb{P}(\bar{\omega})$ tells the price at time zero of a contract that pays 1 at time $N$ **if and only if** $\bar{\omega}$ occurs. This price should include a **risk-adjusted discounting factor**.


**Theorem**: $Z$ is an r.v. (Radon Nikodym Derivative), in an N-period binomial model, 

$$
Z_n = \mathbb{E}_n Z,\quad n = 0, 1, \dots, N
$$

$Z_n$ for $n = 0, 1, \dots, N$ is a martingale under actual probability measure $\mathbb{P}$.

$$
\mathbb{E}_n [Z_{n + 1}] = \mathbb{E}_n [\mathbb{E}_{n + 1}[Z]] = \mathbb{E}_n [Z] = Z_n
$$


e.g., $n = 0, 1, 2, 3$ define $Z_n = \mathbb{E}_n [Z]$, specifically:

$$
Z_3(\omega_1 \omega_2 \omega_3) = Z(\omega_1 \omega_2 \omega_3)\quad \text{for all } \omega_1 \omega_2 \omega_3
$$


$$
\begin{align}
    Z_2(HH) &= \frac{2}{3} Z_3(HHH) + \frac{1}{3} Z_3(HHT) = \frac{9}{16}, \\
    Z_2(HT) &= \frac{2}{3} Z_3(HTH) + \frac{1}{3} Z_2(HTT) = \frac{9}{8}, \\
    Z_2(TH) &= \frac{2}{3} Z_3(THH) + \frac{1}{3} Z_2(THT) = \frac{9}{8}, \\
    Z_2(TT) &= \frac{2}{3} Z_2(TTH) + \frac{1}{3} Z_2^2(TTT) = \frac{9}{4}.
\end{align}
$$

$Z_1 = \mathbb{E}_1 [Z]$ but we compute it using the martingale $Z_1 = \mathbb{E}[Z_2]$, giving:

$$
\begin{align}
    Z_1(H) &= \frac{2}{3} Z_2(HH) + \frac{1}{3} Z_2(HT) = \frac{3}{4}, \\
    Z_1(T) &= \frac{2}{3} Z_1(TH) + \frac{1}{3} Z_1(TT) = \frac{3}{2}.
\end{align}
$$

Then we further "discount" by martingales to achieve the following:

$$
\begin{align}
    Z_0 &= \frac{2}{3} Z_1(H) + \frac{1}{3} Z_1(T) = 1.
\end{align}
$$


**Definition**: The **Radon Nikodym** derivative process is given by:

$$
Z_n = \mathbb{E}_n [Z],\quad n = 0, 1, \dots, N
$$

Specifically, $Z_N = Z$ and $Z_0 = 1$.

**Lemma**: Assume conditions for the derivative process above, let $Y$ be an r.v. depending only on the first $n$ coin tosses:

$$
\tilde{\mathbb{E}}Y = \mathbb{E}[Z_n Y]
$$

Use theorem to prove, and definition $Z_n$ to define:

$$
\tilde{\mathbb{E}}Y = \mathbb{E}[ZY] = \mathbb{E}[\mathbb{E}_n [ZY]] = \mathbb{E}[Y \mathbb{E}_n [Z]] = \mathbb{E}[Y Z_n]
$$

$Y$ takes value 1 if and only if the first $n$ coin tosses result in the particular sequence $\overline{\omega_1}, \dots, \overline{\omega_n}$ we have fixed in advance. The coin tosses $\omega_{n + 1}, \dots, \omega_N$ are irrelevant. For each $n$, $Z_n(\omega_1, \dots, \omega_n$) is the ratio of the risk-neutral probability and the actual probability of obtaining the sequence of coin tosses $\omega_1, \dots, \omega_n$. Lemma, asserts that, if $Y$ depends only on the first $n$ coin tosses, then we do not need to consider the coin tosses after time $n$. 

**Note**: Might use $Z_n$ as a surrogate for the Radon Nikodym derivative $Z$ in the formula:

$$
\tilde{\mathbb{E}}Y = \mathbb{E}[ZY]
$$


**Lemma**: Assume conditions of our definition, and $Y$ is a random variable depending only on the first $m$ coin tosses:

$$
\tilde{\mathbb{E}}_n [Y] = \frac{1}{Z_n} \mathbb{E}_n [Z_m Y]
$$

**Theorem**: Price of Derivative Security at $n$ by Radon-Nikodym Process
Consider an $N$-period binomial model with $0 < d < 1 + r < u$. Assume that the actual probability for head, $p$, and the actual probability for tail, $q$, are positive. The risk-neutral probabilities for head and tail are given, as usual, by: 

$$ 
\tilde{p} = \frac{1 + r - d}{u - d}, \quad \tilde{q} = \frac{u - 1 - r}{u - d}, 
$$

and these are also both positive. Let $\mathbb{P}$ and $\tilde{\mathbb{P}}$ denote the corresponding actual and risk-neutral probability measures, respectively. Let $Z$ be the **Radon-Nikodým derivative** of $\tilde{\mathbb{P}}$ with respect to $\mathbb{P}$, and let $Z_n$, for $n = 0, 1, \dots, N$, be the **Radon-Nikodým derivative process**. Consider a **derivative security** whose payoff $V_N$ may depend on all $N$ coin tosses. For $n = 0, 1, \dots, N$, the price at time $n$ of this derivative security is: 

$$ 
V_n = \mathbb{E}^{\tilde{\mathbb{P}}}_n \left[ \frac{V_N}{(1 + r)^{N - n}} \right] = \frac{(1 + r)^n}{Z_n} \mathbb{E}_n \left[ \frac{Z_N V_N}{(1 + r)^N} \right] = \frac{1}{\zeta_n} \mathbb{E}_n [\zeta_N V_N]
$$

where the **state price density process** $\zeta_n$ is defined by: 

$$ 
\zeta_n = \frac{Z_n}{(1 + r)^n}, \quad n = 0, 1, \dots, N. 
$$

**Problem**: Optimal Investment: Given $X_0$, find an adapted portfolio process $\Delta_0, \Delta_1, \dots, \Delta_{N - 1}$ that maximizes:

$$
\mathbb{E}U(X_N)
$$

subject to the wealth equation:

$$
X_{n + 1} = \Delta_n S_{n + 1} + (1 + r)(X_n - \Delta_n S_n),\quad n = 0, 1, \dots, N - 1
$$

Risk averse agents use utility functions $U$ to capture trade-off between actual risk and actual return. It does not make sense to do this under a risk-neutral measure because under the risk-neutral measure, both the stock and money-market account have the same rate of return. 


e.g., Consider a two-period model with $S_0 = 4$ and $u = 2, d = \frac{1}{2}$ and assume that $r = \frac{1}{4}$

$$
\begin{align*}
    X_1(H) &= S_1(H) \Delta_0 + \text{cash balance growth} \\
           &= 8\Delta_0 + \left(4 - 4\Delta_0\right) \left(1 + \frac{1}{4}\right) \\
           &= 8\Delta_0 + \frac{5}{4} (4 - 4\Delta_0) \\
           &= 3\Delta_0 + 5. \\
    X_1(T) &= S_1(T) \Delta_0 + \text{cash balance growth} \\
           &= 2\Delta_0 + \left(4 - 4\Delta_0\right) \left(1 + \frac{1}{4}\right) \\
           &= 2\Delta_0 + \frac{5}{4} (4 - 4\Delta_0) \\
           &= -3\Delta_0 + 5. \\
\end{align*}
$$


$$
\begin{align*}
    X_2(HH) &= 16\Delta_1(H) + \frac{5}{4} (X_1(H) - 8\Delta_1(H)) \\
            &= 6\Delta_1(H) + \frac{15}{4} \Delta_0 + \frac{25}{4}, \\
    X_2(HT) &= 4\Delta_1(H) + \frac{5}{4} (X_1(H) - 8\Delta_1(H)) \\
            &= -6\Delta_1(H) + \frac{15}{4} \Delta_0 + \frac{25}{4}, \\
    X_2(TH) &= 4\Delta_1(T) + \frac{5}{4} (X_1(T) - 2\Delta_1(T)) \\
            &= \frac{3}{2} \Delta_1(T) - \frac{15}{4} \Delta_0 + \frac{25}{4}, \\
    X_2(TT) &= \Delta_1(T) + \frac{5}{4} (X_1(T) - 2\Delta_1(T)) \\
            &= -\frac{3}{2} \Delta_1(T) - \frac{15}{4} \Delta_0 + \frac{25}{4}. \\
    \mathbb{E} \ln X_2 &= \frac{4}{9} \ln X_2(HH) + \frac{2}{9} \ln X_2(HT) \\
    &+ \frac{2}{9} \ln X_2(TH) + \frac{1}{9} \ln X_2(TT).
\end{align*}
$$

Where we are aiming to maximize $\mathbb{E} \ln X_2$.

$$
\begin{align*}
    \frac{\partial}{\partial \Delta_0} \mathbb{E} \ln X_2 &= 0 \Rightarrow 
    \frac{4}{X_2(HH)} + \frac{2}{X_2(HT)} - \frac{2}{X_2(TH)} - \frac{1}{X_2(TT)} = 0, \\
    \frac{\partial}{\partial \Delta_1(H)} \mathbb{E} \ln X_2 &= 0 \Rightarrow 
    \frac{2}{X_2(HH)} = \frac{1}{X_2(HT)}, \\
    \frac{\partial}{\partial \Delta_1(T)} \mathbb{E} \ln X_2 &= 0 \Rightarrow 
    \frac{2}{X_2(TH)} = \frac{1}{X_2(TT)}. \\
\end{align*}
$$

This gives us three linear equations with 4 unknowns, where we can get:

$$
\begin{align*}
    X_2(HH) &= 2X_2(HT), \quad X_2(TH) = 2X_2(TT), \\
    X_2(HH) &= 100/9, \quad X_2(HT) = 50/9, \\
    X_2(TH) &= 50/9, \quad X_2(TT) = 25/9. \\
    \Delta_1(H) &= \frac{X_2(HH) - X_2(HT)}{S_2(HH) - S_2(HT)} = \frac{25}{54}, \\
    \Delta_1(T) &= \frac{X_2(TH) - X_2(TT)}{S_2(TH) - S_2(TT)} = \frac{25}{27}, \\
    \Delta_0 &= \frac{X_1(H) - X_1(T)}{S_1(H) - S_1(T)} = \frac{5}{9}.
\end{align*}
$$


**Problem**: Given $X_0$ we want to find a random variable $X_N$ without regard to the portfolio process, that maximizes:

$$
\mathbb{E} U(X_N)
$$

subject to:

$$
\tilde{\mathbb{E}} \frac{X_N}{(1 + r)^N} = X_0
$$

**Lemma**: Suppose we have $\Delta_0^*, \Delta_1^*, \dots, \Delta_{N - 1}^*$ is an optimal portfolio process for the optimal investment problem and $X_N^*$ is the corresponding optimal wealth random variable at time $N$. Then $X_N^*$ is optimal for the Maximizing Utility Function problem. Conversely, suppose $X_N^*$ is optimal for the utility function problem. Then there is a portfolio process that starts with initial wealth $X_0$ and has value $X_N^*$ at time $N$, and this portfolio process is optimal for the optimal investment problem.


e.g., Let's take the same Radon-Nikodym derivative from the problem we previously went though with the derivative of $\tilde{\mathbb{P}}$ wrt $\mathbb{P}$. 

$$
\begin{align} Z(HH) &= \frac{\tilde{\mathbb{P}}(HH)}{\mathbb{P}(HH)} = \frac{9}{16}, \quad Z(HT) = \frac{\tilde{\mathbb{P}}(HT)}{\mathbb{P}(HT)} = \frac{9}{8}, \\[8pt] Z(TH) &= \frac{\tilde{\mathbb{P}}(TH)}{\mathbb{P}(TH)} = \frac{9}{8}, \quad Z(TT) = \frac{\tilde{\mathbb{P}}(TT)}{\mathbb{P}(TT)} = \frac{9}{4}. \end{align}
$$

We simplify by using subscripts to denote different values of the state price density $\zeta$.

$$
\begin{align} \zeta_1 &= \zeta(HH) = \frac{Z(HH)}{(1 + r)^2} = \frac{9}{25}, \\[8pt] \zeta_2 &= \zeta(HT) = \frac{Z(HT)}{(1 + r)^2} = \frac{18}{25}, \\[8pt] \zeta_3 &= \zeta(TH) = \frac{Z(TH)}{(1 + r)^2} = \frac{18}{25}, \\[8pt] \zeta_4 &= \zeta(TT) = \frac{Z(TT)}{(1 + r)^2} = \frac{36}{25}. \end{align}
$$

We use notation below to denote the respective probabilities of the possible $\Omega$ sequences:

$$
\begin{align} p_1 &= \mathbb{P}(HH) = \frac{4}{9}, \quad p_2 = \mathbb{P}(HT) = \frac{2}{9}, \\[8pt] p_3 &= \mathbb{P}(TH) = \frac{2}{9}, \quad p_4 = \mathbb{P}(TT) = \frac{1}{9}. \end{align}
$$

We denote the wealth, given a sequence, by:

$$
\begin{align} x_1 &= X_2(HH), \quad x_2 = X_2(HT), \quad x_3 = X_2(TH), \quad x_4 = X_2(TT). \end{align}
$$

Thus, we have the problem:

$$
\begin{align} \text{Maximize} \quad & \sum_{m=1}^{4} p_m \ln x_m, \\[8pt] \text{subject to} \quad & \sum_{m=1}^{4} p_m x_m \zeta_m = X_0. \end{align}
$$

which we can take the log of and expand:

$$
\begin{align} L &= \sum_{m=1}^{4} p_m \ln x_m - \lambda \left( \sum_{m=1}^{4} p_m x_m \zeta_m - X_0 \right). \end{align}
$$

This is clearly a lagrangian, where we can use the lagrangian multiplier and get partials as:

$$
\begin{align} \frac{\partial L}{\partial x_1} &= \frac{4}{9} \left(\frac{1}{x_1} - \lambda \frac{9}{25} \right) = 0, \\[8pt] \frac{\partial L}{\partial x_2} &= \frac{2}{9} \left(\frac{1}{x_2} - \lambda \frac{18}{25} \right) = 0, \\[8pt] \frac{\partial L}{\partial x_3} &= \frac{2}{9} \left(\frac{1}{x_3} - \lambda \frac{18}{25} \right) = 0, \\[8pt] \frac{\partial L}{\partial x_4} &= \frac{1}{9} \left(\frac{1}{x_4} - \lambda \frac{36}{25} \right) = 0. \end{align}
$$

Thus, we get:

$$
\begin{align} x_1 &= \frac{25}{9\lambda}, \quad x_2 = \frac{25}{18\lambda}, \quad x_3 = \frac{25}{18\lambda}, \quad x_4 = \frac{25}{36\lambda}. \end{align}
$$

We can solve for $1 / \lambda$ which can be substituted into our formula:

$$
\begin{align} \frac{4}{9} \frac{9}{25} x_1 + \frac{2}{9} \frac{18}{25} x_2 + \frac{2}{9} \frac{18}{25} x_3 + \frac{1}{9} \frac{36}{25} x_4 &= 4. \end{align} 
$$


$$
\begin{align} \frac{4}{9} \frac{9}{25} \frac{25}{9\lambda} + \frac{2}{9} \frac{18}{25} \frac{25}{18\lambda} + \frac{2}{9} \frac{18}{25} \frac{25}{18\lambda} + \frac{1}{9} \frac{36}{25} \frac{25}{36\lambda} &= 4. \end{align}
$$


$$
\begin{align} \frac{4}{9\lambda} + \frac{2}{9\lambda} + \frac{2}{9\lambda} + \frac{1}{9\lambda} &= 4. \end{align}
$$


$$
\begin{align} \frac{9}{9\lambda} &= 4, \quad \Rightarrow \quad \frac{1}{\lambda} = 4. \end{align}
$$

Our optimal wealth at time 2 is given as,

$$
\begin{align} X_2(HH) &= x_1 = \frac{100}{9}, \\[8pt] X_2(HT) &= x_2 = \frac{50}{9}, \\[8pt] X_2(TH) &= x_3 = \frac{50}{9}, \\[8pt] X_2(TT) &= x_4 = \frac{25}{9}. \end{align}
$$

Now, we can find $\Delta_0, \Delta_1(H), \Delta_1(T)$ as we did following the previous discounting method. We re-write the Radon-Nikodym derivative of $Z$ without reference to the risk-neutral measure,

$$
\mathbb{E} \frac{Z_N X_N}{(1 + r)^N} = X_0 \implies \mathbb{E}_{\zeta} X_N = X_0
$$

In an N-period model, we have $2^N$ possible coin toss sequences $\omega$ which are listed as

$$
\omega^1, \omega^2, \dots, \omega^M
$$

where $M = 2^N$. Thus we formalize this as, given $X_0$ we wish to find $(x_1, x_2, \dots, x_M)$ that maximizes the following summation:

$$
\begin{align} \text{Maximize} \quad & \sum_{m=1}^{M} p_m U(x_m) \\[8pt] \text{subject to} \quad & \sum_{m=1}^{M} p_m x_m \zeta_m = X_0. \end{align}
$$

The lagrangian, as defined specifically, previously, is now generally written as:

$$
\begin{align} L &= \sum_{m=1}^{M} p_m U(x_m) - \lambda \left( \sum_{m=1}^{M} p_m x_m \zeta_m - X_0 \right). \end{align}
$$

With multiplier equations:

$$
\begin{align} \frac{\partial L}{\partial x_m} &= p_m U'(x_m) - \lambda p_m \zeta_m = 0, \quad m = 1, 2, \dots, M. \end{align}
$$


$$
\begin{align} U'(x_m) &= \lambda \zeta_m, \quad m = 1, 2, \dots, M. \end{align}
$$

We can reduce to the above, recalling how $x_m$ and $\zeta_m$ were defined:

$$
\begin{align} X_N &= I \left( \frac{\lambda Z}{(1 + r)^N} \right). \end{align}
$$

