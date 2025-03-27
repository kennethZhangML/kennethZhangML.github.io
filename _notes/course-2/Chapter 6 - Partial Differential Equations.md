---
layout: page
title: Chapter 6 - Partial Differential Equations
description: Notes on Partial Differential Equations and its applications.
parent: course-2
importance: 8
permalink: /notes/course-2/chapter-4-PDEs/
nav: false
---


A **Stochastic Differential Equation** is of the form,


$$
dX(u) = \beta(u, X(u)) du + \gamma(u, X(u)) dW(u)
$$


where:
- $\beta(u, x)$ is the drift function, and
- $\gamma(u, x)$ is the diffusion function
We assume initial condition $X(t) = x$ where $t \ge 0$. We wish to find the stochastic process $X(T)$ for $T \ge t$ that satisfies:


$$
\begin{align*}
X(t) = x,\\
X(T) = X(t) + \int_t^T \beta(u, X(u))du + \int_t^T \gamma(u, X(u)) dW(u)
\end{align*}
$$


There exists a unique $X(T)$ for $T \ge t$ but can be difficult to determine because it appears on both the RHS and LHS. Generally, a $1$-dimensional linear SDE can be solved explicitly, 


$$
dX(u) = (a(u) + b(u) X(u))du + (\gamma(u) + \sigma(u)X(u))dW(u)
$$


where $a(u), b(u), \sigma(u), \gamma(u)$ are non-random functions of time. These functions need not be non-random for the equation above to be solvable, however, the randomness we can only permit is on the RHS of the equation in the SDE form at the top. The randomness inherent in the solution $X(u)$ and in driving the Brownian motion $W(u)$. 

**e.g., Geometric Brownian Motion**
For the GBM SDE,


$$
dS(u) = \alpha S(u) du + \sigma S(u) dW(u)
$$


We have already established that it has solution,


$$
S(t) = S(0) \exp \left\{\sigma W(t) + \left(\alpha - \frac{1}{2}\sigma^2 \right) t \right\} \Longleftrightarrow S(T) = S(0) \exp \left\{\sigma W(T) + \left(\sigma - \frac{1}{2}\sigma^2 \right)T \right\}
$$


Taking $S(T) / S(t)$, we can obtain,


$$
\frac{S(T)}{S(t)} = \exp\left\{\sigma (W(T) - W(t)) + \left(\alpha - \frac{1}{2}\sigma^2 \right) (T - t) \right\}
$$


If the initial condition is given at time $t$ rather than at time $0$, and is $S(t) = x$, then,


$$
S(T) = x \exp \left\{\sigma(W(T) - W(t)) + \left(\alpha - \frac{1}{2}\sigma^2 \right)(T -t) \right\}
$$


Using $S(t) = x$ shows that $S(T)$ only depends on the path of the BM between $t$ and $T$. 


**e.g., Hull-White Interest Rate Model**


$$
dR(u) = (a(u) - b(u)R(u))du + \sigma(u)d\tilde{W}(u)
$$


where,
- $a(u), b(u), \sigma(u)$ are non-random positive functions of $u$ time variable
- $\tilde{W}(u)$ is a Brownian motion under risk-neutral probability measure $\tilde{\mathbb{P}}$
- Let $r$ be a dummy variable with $\beta(u, r) = a(u) - b(u)r, \gamma(u, r) = \sigma(u)$
We can solve this by computing the SDE to compute,


$$
\begin{align*}
d\left(e^{\int_0^u b(v)\,dv} R(u)\right) 
&= e^{\int_0^u b(v)\,dv} \left( b(u)R(u)\,du + dR(u) \right) \\
&= e^{\int_0^u b(v)\,dv} \left( \alpha(u)\,du + \sigma(u)\,d\widetilde{W}(u) \right).
\end{align*}
$$


Integrating both sides from $t$ to $T$ with initial conditions $R(t) = r$, we get,


$$
\begin{align*}
e^{\int_0^T b(v)\,dv} R(T) 
&= r e^{\int_0^t b(v)\,dv} 
+ \int_t^T e^{\int_0^u b(v)\,dv} \alpha(u)\,du 
+ \int_t^T e^{\int_0^u b(v)\,dv} \sigma(u)\,d\widetilde{W}(u), \\
R(T) 
&= r e^{-\int_t^T b(v)\,dv} 
+ \int_t^T e^{-\int_u^T b(v)\,dv} \alpha(u)\,du 
+ \int_t^T e^{-\int_u^T b(v)\,dv} \sigma(u)\,d\widetilde{W}(u).
\end{align*}
$$


where we then solved for $R(T)$. Note the RHS does not involve the interest rate process $R(u)$ apart from $R(t) = r$. By using the Ito integral and the property that the integral with $\sigma(u)$ is normally distributed with mean 0 and variance defined by theorem, under the risk-neutral measure, we can therefore write our mean as,


$$
\begin{align*}
r e^{-\int_t^T b(v)\,dv} 
+ \int_t^T e^{-\int_u^T b(v)\,dv} \alpha(u)\,du
\end{align*}
$$


and variance as,


$$
\begin{align*}
\int_t^T e^{-2\int_u^T b(v)\,dv} \sigma^2(u)\,du
\end{align*}
$$



**e.g., Cox-Ingersoll-Ross Interest Rate model**
The interest rate is given by the SDE,


$$
dR(u) = (a - bR(u))du + \sigma \sqrt{R(u)}d\tilde{W}(u)
$$


For some initial condition $R(t) = r$, although there is no formula for $R(T)$, there is only one solution to this DE, which can be approximated by MC simulation. Unlike the Hull-White model, the interest rate in the CIR model cannot take negative values. When the interest rate approaches zero, the term $\sigma \sqrt{R(u)} d\tilde{W}(u)$ also approaches 0. Thus, with disappearing volatility, the behaviour of the interest rate near zero depends on the drift term $a - bR(u)$ with $a > 0$ when $R(u) = 0$ The positive drift inhibits the interest rate from crossing 0 into negative territory. 


**Markov Property**
For $0 \le t \le T$ and let $h(y)$ be a Borel-measurable function, then let's denote,


$$
g(t, x) = \mathbb{E}^{t, x} h(X(T))
$$


be the expectation of $h(X(T))$ and $X(T)$ is the solution with the SDE of original form with initial condition $X(t) = x$. Assume that $\mathbb{E}^{t, x} |h(X(T))| < \infty$. Note: $g(t, x)$ is not random and is in fact, ordinary and is actually Borel-measurable. 

$g(t, x)$ can be computed numerically by starting at $X(t) = x$ and simulating the SDE. 

**Euler Method**
Using the **Euler method** (MC Method), we can a small positive step size $\delta$ and set,


$$
X(t + \delta) = x + \beta(t, x)\delta + \gamma(t, x)\sqrt{\delta} \epsilon_1
$$


where $\epsilon_1$ is a standard normal r.v., then we can set,


$$
X(t + 2\delta) = X(t + \delta) + \beta(t + \delta, X(t + \delta)) \delta + \gamma(t + \delta, X(t + \delta)) \sqrt{\delta}\epsilon_2
$$


assuming that $\delta$ satisfies the following,


$$
\frac{T - t}{\delta} \in \mathbb{Z}
$$


After repeating the process above many times, we can compute the average of $h(X(T))$ over all these simulations to get an approximate value for $g(t, x)$. If one were to begin with a different time $t$ and initial value $x$, then one would get a different answer. 

---



$$
\begin{align*}
&\textbf{Input:} \\
&\quad \text{Initial value } x,\ \text{Initial time } t,\ \text{Terminal time } T,\ \text{Step size } \delta, \\
&\quad \text{Drift function } \beta(t, x),\ \text{Diffusion function } \gamma(t, x),\ \text{Number of simulations } M \\
&N \leftarrow \frac{T - t}{\delta} \\
&\textbf{For } m = 1 \text{ to } M: \\
&\quad X \leftarrow x \\
&\quad t_{\text{curr}} \leftarrow t \\
&\quad \textbf{For } i = 1 \text{ to } N: \\
&\qquad \epsilon \sim \mathcal{N}(0, 1) \\
&\qquad X \leftarrow X + \beta(t_{\text{curr}}, X)\,\delta + \gamma(t_{\text{curr}}, X)\,\sqrt{\delta}\,\epsilon \\
&\qquad t_{\text{curr}} \leftarrow t_{\text{curr}} + \delta \\
&\quad \text{Store } h(X) \text{ as } \text{payoff}_m \\
&\textbf{Estimate:} \quad g(t, x) \approx \frac{1}{M} \sum_{m=1}^M \text{payoff}_m
\end{align*}
$$



---
**Theorem**
$X(u)$ is a solution to an SDE of the form defined previously with initial condition given at time $0$. Then for $0 \le t \le T$, we have,


$$
\mathbb{E}[h(X(T))|\mathcal{F}(t)] = g(t, X(t))
$$


- the idea is to replace $X(t)$ by $x$ in order to hold it constant and compute $g(t, x)$
- value of $X(T)$ is determined by value of $X(t)$ and is thus $\mathcal{F}(t)$ measurable
- the only relevant piece of information when computing $\mathbb{E}[h(X(T)) | \mathcal{F}(t)]$ is $X(t)$
Thus, $X(t)$ is a **Markov Process.**

---

**Partial Differential Equations**
SDEs and PDEs are related. Moreover, when a PDE is solved usually numerically, it produces a function $g(t, x)$. The Euler method described above is an example of a method of determining this function that converges slowly and gives the function value for only one pair $(t, x)$. In the case of the one-dimensional $x$ being considered here and give $g(t, x)$ for all value of $(t, x)$, the algorithm(s) converge quickly. 

**Theorem: Feymann-Kac**
Take the SDE:


$$
dX(u) = \beta(u, X(u))du + \gamma(u, X(u))dW(u)
$$


$h(y)$ is a Borel-measurable function. Fix $T > 0$ and let $t \in [0, T]$ be given. Then we define,


$$
g(t, x) = \mathbb{E}^{t, x}h(X(T))
$$


assuming that $\mathbb{E}^{t, x} |h(X(T))| < \infty$ for all $(t, x)$. Then $g(t, x)$ satisfies the PDE,


$$
g_t(t, x) + \beta(t, x) g_x(t, x) + \frac{1}{2}\gamma^2(t, x) g_{xx}(t, x) = 0
$$


and the terminal condition,


$$
g(T, x) = h(x)\quad\text{for all }x
$$



**Lemma**
$X(u)$ is a SDE with initial condition given at time $0$. $h(y)$ is a Borel-measurable function and we fix $T > 0$ and let $g(t, x)$ be given. Then the stochastic process,


$$
g(t, X(t)),\quad 0 \le t \le T
$$


is a martingale. 

**Proof**
Letting $0 \le s \le t \le T$ be given, and we get,


$$
\begin{align*}
\mathbb{E}[h(X(T)) \mid \mathcal{F}(s)] &= g(s, X(s)), \\
\mathbb{E}[h(X(T)) \mid \mathcal{F}(t)] &= g(t, X(t)).
\end{align*}
$$


Using the iterated conditioning trick in the first equation and taking conditional expectations of the second equation, we can get the following,


$$
\begin{align*}
\mathbb{E}[g(t, X(t)) \mid \mathcal{F}(s)] 
&= \mathbb{E}[\mathbb{E}[h(X(T)) \mid \mathcal{F}(t)] \mid \mathcal{F}(s)] \\
&= \mathbb{E}[h(X(T)) \mid \mathcal{F}(s)] \\
&= g(s, X(s)).
\end{align*}
$$



**Proof of Theorem**


$$
\begin{align*}
dg(t, X(t)) 
&= g_t\,dt + g_x\,dX + \frac{1}{2} g_{xx}\,dX\,dX \\
&= g_t\,dt + \beta g_x\,dt + \gamma g_x\,dW + \frac{1}{2} \gamma^2 g_{xx}\,dt \\
&= \left[ g_t + \beta g_x + \frac{1}{2} \gamma^2 g_{xx} \right] dt + \gamma g_x\,dW \\
0 &= g_t(t, X(t)) + \beta(t, X(t)) g_x(t, X(t)) + \frac{1}{2} \gamma^2(t, X(t)) g_{xx}(t, X(t)) \\
0 &= g_t(t, x) + \beta(t, x) g_x(t, x) + \frac{1}{2} \gamma^2(t, x) g_{xx}(t, x)
\end{align*}
$$


$X(t)$ is the solution the SDE starting at time $0$. Since $g(t, X(t))$ is a martingale, the $dt$ term is also zero. Any positivity at any time would given $g(t, X(t))$ a tendency to rise. Otherwise, if it were negative $g(t, X(t))$ would have a tendency to fall. Then, setting up the $dt$ term to zero, and putting the argument $(t, X(t))$ back, we get the 2nd last equation along every path, therefore arriving at the last equation at every point $(t, x)$ that can be reached by $(t, X(t))$. We found the martingale, took the differential and set the $dt$ term equal to zero. 

**Theorem**
Consider the SDE:


$$
dX(u) = \beta(u, X(u))du + \gamma(u, X(u)) dW(u)
$$


$h(y)$ is Borel-measurable and $r$ is constant. Fix $T > 0$ and let $t \in [0, T]$ be given, then define,


$$
f(t, x) = \mathbb{E}^{t, x}[e^{-r(T - t)}h(X(T))]
$$


assuming the expectation finiteness principle for all $t, x$. Then $f(t, x)$ satisfies, the PDE,


$$
f_t(t, x) + \beta(t, x)f_x(t, x) + \frac{1}{2}\gamma^2(t, x) f_{xx}(t, x) = rf(t, x)
$$


with the terminal condition,


$$
f(T, x) = h(x),\quad\text{for all }x
$$



**Proof**


$$
\begin{align*}
f(t, X(t)) &= \mathbb{E} \left[ e^{-r(T-t)} h(X(T)) \mid \mathcal{F}(t) \right] \\
\mathbb{E} \left[ f(t, X(t)) \mid \mathcal{F}(s) \right] 
&= \mathbb{E} \left[ \mathbb{E} \left[ e^{-r(T-t)} h(X(T)) \mid \mathcal{F}(t) \right] \mid \mathcal{F}(s) \right] \\
&= \mathbb{E} \left[ e^{-r(T-t)} h(X(T)) \mid \mathcal{F}(s) \right] \\
f(s, X(s)) &= \mathbb{E} \left[ e^{-r(T-s)} h(X(T)) \mid \mathcal{F}(s) \right] \\
e^{-rt} f(t, X(t)) &= \mathbb{E} \left[ e^{-rT} h(X(T)) \mid \mathcal{F}(t) \right] \\
d\left( e^{-rt} f(t, X(t)) \right) 
&= e^{-rt} \left[ -rf\,dt + f_t\,dt + f_x\,dX + \frac{1}{2} f_{xx} dX\,dX \right] \\
&= e^{-rt} \left[ -rf + f_t + \beta f_x + \frac{1}{2} \gamma^2 f_{xx} \right] dt + e^{-rt} \gamma f_x\,dW
\end{align*}
$$


$X(t)$ is the solution to the SDE starting at time $0$. However, it is not the case that $f(t, X(t))$ is a martingale. However the 2nd to 3rd line is indeed not the same as the 4th line, if $0 \le s \le t \le T$, because we're discounting different terms. To get the martingale property from iterated conditioning, we need the r.v., being estimated not depending on $t$, the time of the conditioning. Thus the 5th line completes the discounting process and now, we can apply iterated conditioning to show that $e^{-rt}f(t, X(t))$ is a martingale. 

---

**e.g., Options on a GBM**
$h(S(T))$ is a payoff at time $T$ of a derivative security whose underlying asset is a GBM,


$$
dS(u) = \alpha S(u) du + \sigma S(u) dW(u) \implies dS(u) = rS(u) du + \sigma S(u) \tilde{W}(u)
$$


Assume that $\sigma, r$ the interest rate are constant, and that the stock price is Markov and the payoff is a function of the stock price alone. According to the risk-neutral pricing formula, the price of the derivative security can be written as,


$$
V(t) = \tilde{\mathbb{E}}[e^{-r(T - t)} h(S(T)) | \mathcal{F}(t)]
$$


There is a function $v(t, x)$ such that $V(t) = v(t, S(t))$ and must satisfy the PDE, 


$$
v_t(t, x) + rxv_x(t, x) + \frac{1}{2} \sigma^2 x^2 v_{xx}(t, x) = rv(t, x)
$$


When the underlying follows a GBM, the above is the right pricing formula for a European call, put, FC, and any option that has payoff for some function of $S(T)$ at time $T$. 

Let's consider when $\sigma$ is now a function of the time and stock price, then the stock price would no longer be a GBM and the BS-Merton formula no longer applies. Thus, we can still solve for the option price by solving the PDE where the now constant $\sigma^2$ is replaced by, $\sigma^2(t, x)$,


$$
v_t(t, x) + rxv_{x}(t, x) + \frac{1}{2}\sigma^2(t, x) x^2 v_{xx}(t, x) = rv(t, x)
$$


---

**Remark**
If we assume constant volatility, the parameter $\sigma$ that makes the theoretical option price given by the BS-Merton equation agree with the market price, the **implied volatility** is different for options having different strikes. 
- Implied volatility is generally a convex function of the strike price 
- also called the **volatility smile**

**Non-constant** volatility is the **Constant Elasticity of Variance** model in which $\sigma(t, x) = \sigma x^{\delta - 1}$ depends on $x$ but not $t$. $\delta \in (0, 1)$ is chosen so that the model gives a good fit to option prices across different strikes at a single expiration date. The stock price follows the SDE,


$$
dS(t) = rS(t) dt + \sigma S^{\delta} (t) d\tilde{W}(t)
$$


where $\sigma S^{\delta - 1}(t)$ is a decreasing function of the stock price. We wish to account for different volatilities implied by options expiring at different dates as well as different strikes, so, we allow $\sigma$ to depend on $t$ as well as $x$ (the stock price). We call this the **volatility surface**.

---

**Interest Rate Models**
Models for the interest rate $R(t)$ are called short-rate models as $R(t)$ is the interest rate for short-term borrowing. When the interest is determined by only one SDE it is said to have one-factor. However, these such models fail to capture the complicated yield curve behaviour and tend to produce parallel shifts in the yield curve but not change in the slope/curvature. 

**Discount Process:**


$$
D(t) = e^{- \int_0^2 R(s) ds}
$$


**Money Market Account price process:**


$$
\frac{1}{D(t)} = e^{\int_0^t R(s) ds}
$$


which is the value at time $t$ of one unit of currency invested in the money market account at time $0$ and continuously rolled over at the short-term interest rate, $R(s), s\ge 0$. Thus we have the DE,


$$
dD(t) = -R(t) D(t) dt,\quad d\left(\frac{1}{D(t)} \right) = \frac{R(t)}{D(t)} dt
$$


---

**Zero Coupon Bond**
For a zero coupon bond $B(t, T)$ that pays 1 dollar at maturity date $T$, the risk-neutral pricing formula tells us that the discounted price of this bond should be a martingale under the risk-neutral measure, which gives for $0 \le t \le T$,


$$
D(t)B(t, T) = \tilde{\mathbb{E}}[D(T) | \mathcal{F}(t)] \implies D(t) B(t, T) = \tilde{\mathbb{E}}\left[e^{- \int_t^T R(s) ds} | \mathcal{F}(t)\right] 
$$


the zero-coupon bond pricing formula given on the RHS of the implies arrow. When a ZCB price is computed, we have the yield defined between times $t$ and $T$, which is,


$$
Y(t, T) = -\frac{1}{T - t} \log B(t, T)
$$


or equivalently,


$$
B(t, T) = e^{-Y(t, T)(T - t)}
$$


The yield $Y(t, T)$ is the constant rate of continuously compounding interest between $t$ and $T$ that is consistent with the bond price $B(t, T)$. Since $R$ is given by a SDE and is Markov, we have that $B(t, T) = f(t, R(t))$. The only relevant part of the path of $R$ before $t$ is its value at time $t$, so the bond price $B(t, T)$ must be a function of the time $t$ of $R(t)$. 

For $f(t, r)$, some unknown function for which we want to find the PDE for, we find a martingale, take its differential and set the $dt$ term equal to zero. i.e., $D(t) B(t, T) = D(t) f(t, R(t))$,


$$
\begin{align*}
d\left(D(t) f(t, R(t))\right) 
&= f(t, R(t))\,dD(t) + D(t)\,df(t, R(t)) \\
&= D(t) \left[ -R f\,dt + f_t\,dt + f_r\,dR + \frac{1}{2} f_{rr}\,dR\,dR \right] \\
&= D(t) \left[ -R f + f_t + \beta f_r + \frac{1}{2} \gamma^2 f_{rr} \right] dt + D(t)\,\gamma f_r\,d\widetilde{W}.
\end{align*}
$$


which gives us the PDE, with terminal condition $f(T, r) = 1$ for all $r$,


$$
f_t(t, r) + \beta(t, r) f_r(t, r) + \frac{1}{2}\gamma^2 (t, r) f_rr(t, r) = rf(t, r)
$$


because the value of the bond a maturity has its face value of 1.

---

**e.g., Hull-White Interest rate model**
The evolution of the interest rate is given by,


$$
dR(t) = (a(t) - b(t)R(t))dt + \sigma(t) d \tilde{W}(t)
$$


where $a(t), b(t), \sigma(t)$ are non-random positive functions of time, and the ZCB price becomes,


$$
\begin{align*}
f_t(t, r) 
+ \left(a(t) - b(t) r\right) f_r(t, r) 
+ \frac{1}{2} \sigma^2(t) f_{rr}(t, r) 
= r f(t, r).
\end{align*}
$$


We have an initial guess which is then verified that the solution is of form,


$$
\begin{align*}
f(t, r) = e^{-r C(t, T) - A(t, T)}
\end{align*}
$$


We fix $T$ for the non-random functions $C(t, T)$ and $A(t, T)$ which are to be determined. In this case, the yield is given by,


$$
\begin{align*}
Y(t, T) = -\frac{1}{T - t} \log f(t, r) 
= \frac{1}{T - t} \left( r C(t, T) + A(t, T) \right)
\end{align*}
$$


For the Hull-White model, we have a special case of these models call affine-yield models,


$$
\begin{align*}
f_t(t, r) &= \left( -r C'(t, T) - A'(t, T) \right) f(t, r), \\
f_r(t, r) &= -C(t, T)\, f(t, r), \\
f_{rr}(t, r) &= C^2(t, T)\, f(t, r)
\end{align*}
$$


Taking the derivatives of $C(t, T)$ and $A(t, T)$ gives us the PDE,


$$
\begin{align*}
\left[
\left( -C'(t, T) + b(t) C(t, T) - 1 \right) r 
- A'(t, T) - a(t) C(t, T) 
+ \frac{1}{2} \sigma^2(t) C^2(t, T)
\right] f(t, r) = 0
\end{align*}
$$


The term that multiplies $r$ must be zero, otherwise changing values of $r$ will gives us different values on the LHS which may not always be equal. Thus, we get the ODE,


$$
C'(t, T) = b(t)C(t, T) - 1
$$


which we set to zero to get,


$$
\begin{align*}
A'(t, T) = -a(t) C(t, T) + \frac{1}{2} \sigma^2(t) C^2(t, T).
\end{align*}
$$


We also see that the terminal condition holds for all $r$ implying that $C(T, T) = A(T, T) = 0$. These terminal conditions provide enough information to determine the functions $A(t, T)$ and $C(t, T)$ for $0 \le t \le T$ and thus we get them as,


$$
\begin{align*}
C(t, T) &= \int_t^T e^{-\int_t^s b(v)\,dv} \,ds, \\
A(t, T) &= \int_t^T \left( a(s) C(s, T) - \frac{1}{2} \sigma^2(s) C^2(s, T) \right) ds.
\end{align*}
$$


Thus, we have an explicit formula for the Hull-White model,


$$
\begin{align*}
B(t, T) = e^{-R(t) C(t, T) - A(t, T)}
\end{align*}
$$



---

**Multi-Dimensional Feynman-Kac Theorems**
Let's say we have a number of differential equations and the number of Brownian motions entering those differential equations can be both be larger than one and do NOT need to be the same. For the sake of simplicity, we can take the following example.

$W(t) = (W_1(t),W_2(t))$ be a 2-dim BM. Consider the SDEs,


$$
\begin{align*}
dX_1(u) &= \beta_1\left(u, X_1(u), X_2(u)\right) du 
+ \gamma_{11}\left(u, X_1(u), X_2(u)\right) dW_1(u) \\
&\quad + \gamma_{12}\left(u, X_1(u), X_2(u)\right) dW_2(u), \\
dX_2(u) &= \beta_2\left(u, X_1(u), X_2(u)\right) du 
+ \gamma_{21}\left(u, X_1(u), X_2(u)\right) dW_1(u) \\
&\quad + \gamma_{22}\left(u, X_1(u), X_2(u)\right) dW_2(u).
\end{align*}
$$


Let's say there is a Borel-measurable function, for the solution to the SDE pair above is Markov, $h(y_1, y_2)$ is given, and given initial condition $(t, x_1, x_2)$, for $0 \le t \le T$, we define,


$$
\begin{align*}
g(t, x_1, x_2) &= \mathbb{E}^{t, x_1, x_2} \left[ h\left(X_1(T), X_2(T)\right) \right], \\
f(t, x_1, x_2) &= \mathbb{E}^{t, x_1, x_2} \left[ e^{-r(T - t)} h\left(X_1(T), X_2(T)\right) \right].
\end{align*}
$$


Then, we can get,


$$
\begin{align*}
g_t + \beta_1 g_{x_1} + \beta_2 g_{x_2} 
+ \frac{1}{2} (\gamma_{11}^2 + \gamma_{12}^2) g_{x_1 x_1} 
+ (\gamma_{11} \gamma_{21} + \gamma_{12} \gamma_{22}) g_{x_1 x_2} 
+ \frac{1}{2} (\gamma_{21}^2 + \gamma_{22}^2) g_{x_2 x_2} 
= 0,
\end{align*}
$$


and,


$$
\begin{align*}
f_t + \beta_1 f_{x_1} + \beta_2 f_{x_2} 
+ \frac{1}{2} (\gamma_{11}^2 + \gamma_{12}^2) f_{x_1 x_1} 
+ (\gamma_{11} \gamma_{21} + \gamma_{12} \gamma_{22}) f_{x_1 x_2} 
+ \frac{1}{2} (\gamma_{21}^2 + \gamma_{22}^2) f_{x_2 x_2} 
= r f.
\end{align*}
$$


The above also satisfy the terminal conditions, 


$$
g(T, x_1, x_2) = f(T, x_1, x_2) = h(x_1, x_2),\quad\text{for all }x_1, x_2
$$



e.g., Asian Option
We define the discounted option price and apply Ito's lemma,


$$
\begin{align*}
d&\left(e^{-rt}v(t, S(t), Y(t))\right)\\
&= e^{-rt} \left[
    -rv\,dt + v_t\,dt + v_x\,dS + v_y\,dY 
    + \frac{1}{2} v_{xx}\,dS\,dS + v_{xy}\,dS\,dY + \frac{1}{2} v_{yy}\,dY\,dY
\right]
\end{align*}
$$


then plug in the dynamics of $S(t), Y(t)$ into the equation above,


$$
\begin{align*}
&= e^{-rt} \left[
    -rv + v_t + v_x \left( rS\,dt + \sigma S\,d\widetilde{W} \right)
    + v_y S\,dt + \frac{1}{2} v_{xx} \sigma^2 S^2\,dt
\right] \\
&= e^{-rt} \left[
    -rv + v_t + rS v_x + S v_y + \frac{1}{2} \sigma^2 S^2 v_{xx}
\right] dt 
+ e^{-rt} \sigma S v_x\,d\widetilde{W}
\end{align*}
$$


Then, we can write the final differential for the discounted option value,


$$
\begin{align*}
d\left(e^{-rt}v(t, S(t), Y(t))\right)
&= e^{-rt} \left[
    -rv + v_t + rS v_x + S v_y + \frac{1}{2} \sigma^2 S^2 v_{xx}
\right] dt 
+ e^{-rt} \sigma S v_x\,d\widetilde{W}
\end{align*}
$$


Given this is a martingale, the $dt$ term must be 0,


$$
\begin{align*}
v_t + r x v_x + x v_y + \frac{1}{2} \sigma^2 x^2 v_{xx} = r v
\end{align*}
$$


