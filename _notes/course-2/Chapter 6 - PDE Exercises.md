---
layout: page
title: Chapter 4 - Partial Differential Equations Exercises
description: Notes on Partial Differential Equations and its applications.
parent: course-2
importance: 9
permalink: /notes/course-2/chapter-4-PDEs-exercises/
nav: false
---

**Exercise 6.1**

Consider the stochastic differential equation  

$$
dX(u) = (a(u) + b(u)X(u))\,du + (\gamma(u) + \sigma(u)X(u))\,dW(u),
$$
  
where $W(u)$ is a Brownian motion relative to a filtration $\mathcal{F}(u)$, $u \geq 0$, and we allow $a(u)$, $b(u)$, $\gamma(u)$, and $\sigma(u)$ to be processes adapted to this filtration. Fix an initial time $t \geq 0$ and an initial position $x \in \mathbb{R}$. Define  

$$
Z(u) = \exp\left\{ \int_t^u \sigma(v)\,dW(v) + \int_t^u \left( b(v) - \frac{1}{2}\sigma^2(v) \right)\,dv \right\},
$$
  

$$
Y(u) = x + \int_t^u \frac{a(v) - \sigma(v)\gamma(v)}{Z(v)}\,dv + \int_t^u \frac{\gamma(v)}{Z(v)}\,dW(v).
$$


**(i)** Show that $Z(t) = 1$ and  

$$
dZ(u) = b(u)Z(u)\,du + \sigma(u)Z(u)\,dW(u), \quad u \geq t.
$$


Let  

$$
f(u) = \int_t^u \sigma(v)\,dW(v) + \int_t^u \left( b(v) - \frac{1}{2}\sigma^2(v) \right)\,dv,
$$
  
so that $Z(u) = \exp(f(u))$. Applying Itô’s formula:

$$
dZ(u) = Z(u)\,df(u) + \frac{1}{2}Z(u)\,d[f](u),
$$

where  
- $df(u) = \sigma(u)\,dW(u) + \left(b(u) - \frac{1}{2}\sigma^2(u)\right)\,du$,  
- $d[f](u) = \sigma^2(u)\,du$.  

Then,  

$$
\begin{align*}
dZ(u) &= Z(u)\left[\sigma(u)\,dW(u) + \left(b(u) - \frac{1}{2}\sigma^2(u)\right)\,du \right] + \frac{1}{2}Z(u)\sigma^2(u)\,du \\
&= Z(u)\left[b(u)\,du + \sigma(u)\,dW(u)\right].
\end{align*}
$$


Also, since the integrals in the exponential defining $Z(u)$ start at $t$, we have:

$$
Z(t) = \exp(0) = 1.
$$


**(ii)** By its very definition, $Y(u)$ satisfies $Y(t) = x$, and  

$$
dY(u) = \frac{a(u) - \sigma(u)\gamma(u)}{Z(u)}\,du + \frac{\gamma(u)}{Z(u)}\,dW(u), \quad u \geq t.
$$


Now define $X(u) = Y(u)Z(u)$ and apply the product rule for Itô calculus:

$$
dX(u) = Y(u)\,dZ(u) + Z(u)\,dY(u) + dY(u)\,dZ(u).
$$


Substitute:
- $dZ(u) = b(u)Z(u)\,du + \sigma(u)Z(u)\,dW(u)$,  
- $dY(u) = \frac{a(u) - \sigma(u)\gamma(u)}{Z(u)}\,du + \frac{\gamma(u)}{Z(u)}\,dW(u)$,  
- The cross term is:

$$
dY(u)\,dZ(u) = \frac{\gamma(u)}{Z(u)}\,dW(u) \cdot \sigma(u)Z(u)\,dW(u) = \gamma(u)\sigma(u)\,du.
$$


Putting everything together:

$$
\begin{align*}
dX(u) &= Y(u)\left[b(u)Z(u)\,du + \sigma(u)Z(u)\,dW(u)\right] \\
&\quad + Z(u)\left[\frac{a(u) - \sigma(u)\gamma(u)}{Z(u)}\,du + \frac{\gamma(u)}{Z(u)}\,dW(u)\right] \\
&\quad + \gamma(u)\sigma(u)\,du \\
&= b(u)Y(u)Z(u)\,du + \sigma(u)Y(u)Z(u)\,dW(u) \\
&\quad + (a(u) - \sigma(u)\gamma(u))\,du + \gamma(u)\,dW(u) + \gamma(u)\sigma(u)\,du \\
&= (a(u) + b(u)X(u))\,du + (\gamma(u) + \sigma(u)X(u))\,dW(u),
\end{align*}
$$

since $X(u) = Y(u)Z(u)$.

Also, $X(t) = Y(t)Z(t) = x \cdot 1 = x$, so the initial condition is satisfied.

Hence, $X(u) = Y(u)Z(u)$ solves the stochastic differential equation and satisfies the initial condition.



**Exercise 6.2 (No-arbitrage derivation of bond-pricing equation)**

Suppose the interest rate is given by the stochastic differential equation  

$$
dR(t) = \alpha(t, R(t))\,dt + \gamma(t, R(t))\,dW(t),
$$
  
where $W(t)$ is a Brownian motion under a probability measure $\mathbb{P}$ (not necessarily risk-neutral). The price of a $T$-maturity zero-coupon bond at time $t$ is given by a function $f(t, R(t), T)$.

Assume that $f_r(t, r, T) \neq 0$ and define  

$$
\beta(t, r, T) = -\frac{1}{f_r(t, r, T)}\left[ -r f(t, r, T) + f_t(t, r, T) + \frac{1}{2}\gamma^2(t, r) f_{rr}(t, r, T) \right].
$$


Then the PDE for $f$ is  

$$
f_t(t, r, T) + \beta(t, r, T) f_r(t, r, T) + \frac{1}{2}\gamma^2(t, r) f_{rr}(t, r, T) = r f(t, r, T).
$$


---

**(i)** Consider two maturities $0 \leq T_1 \leq T_2$, and a portfolio that holds at time $t \leq T_1$:
- $\Delta_1(t)$ units of the bond maturing at $T_1$,
- $\Delta_2(t)$ units of the bond maturing at $T_2$,

and finances this position by investing or borrowing at the interest rate $R(t)$. Let $X(t)$ denote the value of the portfolio. Then:

$$
d(D(t)X(t)) = 
\Delta_1(t)D(t)\left[ -R(t)f(t, R(t), T_1) + f_t(t, R(t), T_1) + \alpha(t, R(t))f_r(t, R(t), T_1) + \frac{1}{2}\gamma^2(t, R(t))f_{rr}(t, R(t), T_1) \right]\,dt \\
+ \Delta_2(t)D(t)\left[ -R(t)f(t, R(t), T_2) + f_t(t, R(t), T_2) + \alpha(t, R(t))f_r(t, R(t), T_2) + \frac{1}{2}\gamma^2(t, R(t))f_{rr}(t, R(t), T_2) \right]\,dt \\
+ D(t)\gamma(t, R(t))\left[\Delta_1(t)f_r(t, R(t), T_1) + \Delta_2(t)f_r(t, R(t), T_2)\right]\,dW(t).
$$


Grouping terms and substituting the definition of $\beta(t, r, T)$:

$$
= \Delta_1(t)D(t)\left[\alpha(t, R(t)) - \beta(t, R(t), T_1)\right]f_r(t, R(t), T_1)\,dt \\
+ \Delta_2(t)D(t)\left[\alpha(t, R(t)) - \beta(t, R(t), T_2)\right]f_r(t, R(t), T_2)\,dt \\
+ D(t)\gamma(t, R(t))\left[\Delta_1(t)f_r(t, R(t), T_1) + \Delta_2(t)f_r(t, R(t), T_2)\right]\,dW(t).
$$


This is equation (6.9.4) from the textbook.

---

**(ii)** Define the sign function:

$$
\text{sign}(x) = 
\begin{cases}
1 & \text{if } x > 0, \\
0 & \text{if } x = 0, \\
-1 & \text{if } x < 0,
\end{cases}
$$
  
and let

$$
S(t) = \text{sign}\left\{ [\beta(t, R(t), T_2) - \beta(t, R(t), T_1)] f_r(t, R(t), T_1) f_r(t, R(t), T_2) \right\}.
$$


Set the portfolio weights as:
- $\Delta_1(t) = S(t) f_r(t, R(t), T_2)$,
- $\Delta_2(t) = -S(t) f_r(t, R(t), T_1)$.

Substitute into the drift term of $d(D(t)X(t))$:

$$
D(t)\left[
\Delta_1(t)\left(\alpha(t, R(t)) - \beta(t, R(t), T_1)\right)f_r(t, R(t), T_1) +
\Delta_2(t)\left(\alpha(t, R(t)) - \beta(t, R(t), T_2)\right)f_r(t, R(t), T_2)
\right].
$$


This becomes:

$$
S(t)D(t)\left[ f_r(t, R(t), T_2)\left(\alpha - \beta_1\right)f_r(t, R(t), T_1) - f_r(t, R(t), T_1)\left(\alpha - \beta_2\right)f_r(t, R(t), T_2) \right] = S(t)D(t)(\beta_2 - \beta_1)f_r(t, R(t), T_1)f_r(t, R(t), T_2).
$$


Since $S(t)$ has the same sign as the expression in the brackets, this term is strictly positive unless $\beta(t, R(t), T_1) = \beta(t, R(t), T_2)$. Hence, there is an arbitrage unless $\beta(t, r, T)$ is independent of $T$. Since $T_1$ and $T_2$ are arbitrary, we conclude:

$$
\beta(t, r, T) = \beta(t, r).
$$


---

**(iii)** Now let $T > 0$ be given and consider a portfolio that only invests in the $T$-maturity bond. Then:

$$
d(D(t)X(t)) = \Delta(t)D(t)\left[ -R(t)f + f_t + \alpha f_r + \frac{1}{2}\gamma^2 f_{rr} \right]\,dt + D(t)\Delta(t)\gamma f_r\,dW(t),
$$

where all functions are evaluated at $(t, R(t), T)$. This is equation (6.9.5).

If $f_r(t, r, T) = 0$ but the drift term above is non-zero, then there is an arbitrage opportunity. Therefore, in the case $f_r = 0$, we must have:

$$
f_t(t, r, T) + \frac{1}{2}\gamma^2(t, r) f_{rr}(t, r, T) = r f(t, r, T),
$$

as in equation (6.9.6).

Hence, even if $f_r = 0$, the bond pricing PDE still holds.

---

**Conclusion:** If zero-coupon bond markets are arbitrage-free, then for all $t, r, T$ such that $f_r(t, r, T) \neq 0$, the function $\beta(t, r, T)$ defined in (6.9.2) must not depend on $T$. Therefore, the bond price $f(t, r, T)$ satisfies:

$$
f_t + \beta(t, r)f_r + \frac{1}{2}\gamma^2 f_{rr} = r f,
$$

which is equation (6.5.4).  

Under the measure $\widetilde{\mathbb{P}}$ defined by:

$$
\widetilde{W}(t) = W(t) + \int_0^t \frac{1}{\gamma(u, R(u))}\left[\alpha(u, R(u)) - \beta(u, R(u))\right]du,
$$

$\widetilde{W}(t)$ is a Brownian motion, and the SDE for $R(t)$ becomes the risk-neutral one, so $\widetilde{\mathbb{P}}$ is risk-neutral.



**Exercise 6.3 (Solution of Hull-White model)**

This exercise solves the ODEs (6.5.8) and (6.5.9) to produce the solutions $C(t, T)$ and $A(t, T)$ given in (6.5.10) and (6.5.11).

---

**(i)** Use equation (6.5.8) with $s$ replacing $t$. The equation is:

$$
\frac{\partial C(s, T)}{\partial s} = -1 + b(s)C(s, T).
$$


Multiply both sides by $\exp\left(-\int_0^s b(v)\,dv\right)$:

$$
\exp\left(-\int_0^s b(v)\,dv\right) \frac{\partial C(s, T)}{\partial s} = -\exp\left(-\int_0^s b(v)\,dv\right) + b(s)C(s, T)\exp\left(-\int_0^s b(v)\,dv\right).
$$


This is the same as:

$$
\frac{d}{ds}\left[ \exp\left(-\int_0^s b(v)\,dv\right) C(s, T) \right] = -\exp\left(-\int_0^s b(v)\,dv\right).
$$


So we have shown:

$$
\frac{d}{ds}\left[ e^{-\int_0^s b(v)\,dv} C(s, T) \right] = -e^{-\int_0^s b(v)\,dv}.
$$


---

**(ii)** Integrate both sides from $s = t$ to $s = T$:

$$
\int_t^T \frac{d}{ds} \left[ e^{-\int_0^s b(v)\,dv} C(s, T) \right] ds = -\int_t^T e^{-\int_0^s b(v)\,dv}\,ds.
$$


The left-hand side becomes:

$$
e^{-\int_0^T b(v)\,dv} C(T, T) - e^{-\int_0^t b(v)\,dv} C(t, T).
$$


Using $C(T, T) = 0$, we have:

$$
- e^{-\int_0^t b(v)\,dv} C(t, T) = -\int_t^T e^{-\int_0^s b(v)\,dv}\,ds.
$$


Multiplying both sides by $-1$:

$$
C(t, T) = e^{\int_0^t b(v)\,dv} \int_t^T e^{-\int_0^s b(v)\,dv}\,ds.
$$


This is equation (6.5.10).

---

**(iii)** Replace $t$ by $s$ in (6.5.9):

$$
\frac{\partial A(s, T)}{\partial s} = -\frac{1}{2}\sigma^2(s) C^2(s, T).
$$


Integrate from $s = t$ to $s = T$ and use $A(T, T) = 0$:

$$
A(T, T) - A(t, T) = -\int_t^T \frac{1}{2}\sigma^2(s) C^2(s, T)\,ds.
$$


Then:

$$
A(t, T) = \int_t^T \frac{1}{2}\sigma^2(s) C^2(s, T)\,ds.
$$


This is equation (6.5.11).



**Exercise 6.4 (Solution of Cox-Ingersoll-Ross model)**

This exercise solves the ODEs (6.5.14) and (6.5.15) to produce the solutions $C(t, T)$ and $A(t, T)$ given in (6.5.16) and (6.5.17).

---

**(i)** Define the function

$$
\varphi(t) = \exp\left( \frac{1}{2}\sigma^2 \int_t^T C(u, T)\,du \right).
$$


Differentiate:
- First, show

$$
C(t, T) = -\frac{2\varphi'(t)}{\sigma^2 \varphi(t)},
$$

- Then, differentiate $C(t, T)$:

$$
C'(t, T) = -\frac{2\varphi''(t)}{\sigma^2 \varphi(t)} + \frac{2\varphi'^2(t)}{\sigma^2 \varphi^2(t)} = -\frac{2\varphi''(t)}{\sigma^2 \varphi(t)} + \frac{1}{2} \sigma^2 C^2(t, T).
$$


This gives equations (6.9.8) and (6.9.9).

---

**(ii)** Use equation (6.5.14):

$$
C'(t, T) = b C(t, T) - 1 + \frac{1}{2}\sigma^2 C^2(t, T).
$$


Substitute $C(t, T) = -\frac{2\varphi'(t)}{\sigma^2 \varphi(t)}$ and plug into the equation above. After simplification, the condition for equality is:

$$
\varphi''(t) - b\varphi'(t) - \frac{1}{2}\sigma^2 \varphi(t) = 0.
$$


This is equation (6.9.10).

---

**(iii)** This is a second-order linear ODE with constant coefficients. The general solution is:

$$
\varphi(t) = a_1 e^{\lambda_1 t} + a_2 e^{\lambda_2 t},
$$

where $\lambda_{1,2}$ are the roots of the characteristic equation:

$$
\lambda^2 - b\lambda - \frac{1}{2}\sigma^2 = 0.
$$


---

**(iv)** Solving the characteristic equation:

$$
\lambda = \frac{1}{2}b \pm \gamma, \quad \text{where } \gamma = \frac{1}{2}\sqrt{b^2 + 2\sigma^2}.
$$


So the general solution is:

$$
\varphi(t) = \frac{c_1}{\frac{1}{2}b + \gamma} e^{-(\frac{1}{2}b + \gamma)(T - t)} - \frac{c_2}{\frac{1}{2}b - \gamma} e^{-(\frac{1}{2}b - \gamma)(T - t)}.
$$


This is equation (6.9.11).

---

**(v)** Differentiate $\varphi(t)$:

$$
\varphi'(t) = c_1 e^{-(\frac{1}{2}b + \gamma)(T - t)} - c_2 e^{-(\frac{1}{2}b - \gamma)(T - t)}.
$$


Use $C(T, T) = 0$ in the formula for $C(t, T)$:

$$
C(t, T) = -\frac{2\varphi'(t)}{\sigma^2 \varphi(t)} \Rightarrow c_1 = c_2.
$$


---

**(vi)** Plug $c_1 = c_2$ into $\varphi(t)$:

$$
\varphi(t) = c_1 e^{-\frac{1}{2}b(T - t)} \left[ \frac{\frac{1}{2}b - \gamma}{\frac{1}{4}b^2 - \gamma^2} e^{-\gamma(T - t)} - \frac{\frac{1}{2}b + \gamma}{\frac{1}{4}b^2 - \gamma^2} e^{\gamma(T - t)} \right].
$$


Simplify the expression:

$$
\varphi(t) = \frac{2c_1}{\sigma^2} e^{-\frac{1}{2}b(T - t)}\left[ b\sinh(\gamma(T - t)) + 2\gamma \cosh(\gamma(T - t)) \right],
$$


$$
\varphi'(t) = -2c_1 e^{-\frac{1}{2}b(T - t)} \sinh(\gamma(T - t)) \gamma.
$$


Then:

$$
C(t, T) = -\frac{2\varphi'(t)}{\sigma^2 \varphi(t)} = \frac{2\gamma \sinh(\gamma(T - t))}{\sigma^2 \left[ b\sinh(\gamma(T - t)) + 2\gamma \cosh(\gamma(T - t)) \right]},
$$


which matches equation (6.5.16).

---

**(vii)** From (6.5.15) and (6.9.8):

$$
A'(t, T) = \frac{2a \varphi'(t)}{\sigma^2 \varphi(t)}.
$$


Replace $t$ by $s$ and integrate from $s = t$ to $s = T$:

$$
A(t, T) = \int_t^T \frac{2a \varphi'(s)}{\sigma^2 \varphi(s)}\,ds.
$$


This matches equation (6.5.17).


**Exercise 6.5 (Two-dimensional Feynman-Kac)**

---

**(i)** With $g(t, x_1, x_2)$ and $f(t, x_1, x_2)$ defined by (6.6.1) and (6.6.2), we want to show that:
- $g(t, X_1(t), X_2(t))$ and
- $e^{-rt}f(t, X_1(t), X_2(t))$

are martingales.

This follows from the fact that both $g$ and $f$ solve their respective PDEs and that the SDEs for $X_1(t)$ and $X_2(t)$ are Markovian. If the discounted process $e^{-rt}f(t, X_1(t), X_2(t))$ has zero drift (i.e., the $dt$ term vanishes), then it is a martingale under the risk-neutral measure.

---

**(ii)** Assume $W_1(t)$ and $W_2(t)$ are independent Brownian motions. Apply Itô’s formula to $g(t, X_1(t), X_2(t))$:

Let the dynamics be:

$$
dX_1(t) = \beta_1(t)\,dt + \gamma_{11}(t)\,dW_1(t) + \gamma_{12}(t)\,dW_2(t), \\
dX_2(t) = \beta_2(t)\,dt + \gamma_{21}(t)\,dW_1(t) + \gamma_{22}(t)\,dW_2(t).
$$


Then the Itô formula gives:

$$
dg = g_t\,dt + g_{x_1}\,dX_1 + g_{x_2}\,dX_2 + \frac{1}{2}g_{x_1x_1}(dX_1)^2 + \frac{1}{2}g_{x_2x_2}(dX_2)^2 + g_{x_1x_2}\,dX_1 dX_2.
$$


Using independence, $dW_1 dW_2 = 0$, and computing $(dX_i)^2$:
- $(dX_1)^2 = \gamma_{11}^2\,dt + \gamma_{12}^2\,dt$,
- $(dX_2)^2 = \gamma_{21}^2\,dt + \gamma_{22}^2\,dt$,
- $dX_1 dX_2 = \gamma_{11}\gamma_{21}\,dt + \gamma_{12}\gamma_{22}\,dt$.

Setting the drift term to zero leads to:

$$
g_t + \beta_1 g_{x_1} + \beta_2 g_{x_2} + \frac{1}{2}(\gamma_{11}^2 + \gamma_{12}^2)g_{x_1x_1} + \frac{1}{2}(\gamma_{21}^2 + \gamma_{22}^2)g_{x_2x_2} + (\gamma_{11}\gamma_{21} + \gamma_{12}\gamma_{22})g_{x_1x_2} = 0,
$$


which is PDE (6.6.3).

Now apply Itô’s formula to $e^{-rt}f(t, X_1(t), X_2(t))$ and set $dt$ term to zero:

$$
f_t - r f + \beta_1 f_{x_1} + \beta_2 f_{x_2} + \frac{1}{2}(\gamma_{11}^2 + \gamma_{12}^2)f_{x_1x_1} + \frac{1}{2}(\gamma_{21}^2 + \gamma_{22}^2)f_{x_2x_2} + (\gamma_{11}\gamma_{21} + \gamma_{12}\gamma_{22})f_{x_1x_2} = 0,
$$


which gives the Feynman-Kac PDE (6.6.4).

---

**(iii)** Now assume:

$$
dW_1(t)dW_2(t) = \rho\,dt,
$$

so the Brownian motions are correlated. Then:
- $dX_1 dX_2$ contains cross terms:

$$
dX_1 dX_2 = \gamma_{11}\gamma_{21}\,dt + \gamma_{12}\gamma_{22}\,dt + \rho(\gamma_{11}\gamma_{22} + \gamma_{12}\gamma_{21})\,dt.
$$


Thus the mixed second-order term becomes:

$$
g_{x_1x_2}\left( \gamma_{11}\gamma_{21} + \gamma_{12}\gamma_{22} + \rho(\gamma_{11}\gamma_{22} + \gamma_{12}\gamma_{21}) \right).
$$


Putting everything together, the PDE for $g$ becomes:

$$
\begin{aligned}
g_t + \beta_1 g_{x_1} + \beta_2 g_{x_2} 
&+ \left( \frac{1}{2}\gamma_{11}^2 + \rho \gamma_{11} \gamma_{12} + \frac{1}{2} \gamma_{12}^2 \right) g_{x_1x_1} \\
&+ (\gamma_{11}\gamma_{21} + \rho\gamma_{11}\gamma_{22} + \rho\gamma_{12}\gamma_{21} + \gamma_{12}\gamma_{22}) g_{x_1x_2} \\
&+ \left( \frac{1}{2}\gamma_{21}^2 + \rho \gamma_{21} \gamma_{22} + \frac{1}{2} \gamma_{22}^2 \right) g_{x_2x_2} = 0,
\end{aligned}
$$


which is equation (6.9.13).

Similarly, for $f$, include the $-rf$ term:

$$
\begin{aligned}
f_t + \beta_1 f_{x_1} + \beta_2 f_{x_2} 
&+ \left( \frac{1}{2}\gamma_{11}^2 + \rho \gamma_{11} \gamma_{12} + \frac{1}{2} \gamma_{12}^2 \right) f_{x_1x_1} \\
&+ (\gamma_{11}\gamma_{21} + \rho\gamma_{11}\gamma_{22} + \rho\gamma_{12}\gamma_{21} + \gamma_{12}\gamma_{22}) f_{x_1x_2} \\
&+ \left( \frac{1}{2}\gamma_{21}^2 + \rho \gamma_{21} \gamma_{22} + \frac{1}{2} \gamma_{22}^2 \right) f_{x_2x_2} = r f,
\end{aligned}
$$


which is equation (6.9.14).




**Exercise 6.6 (Moment-generating function for Cox-Ingersoll-Ross process)**

---

**(i)** Let $X_j(t)$ solve the Ornstein-Uhlenbeck SDE:

$$
dX_j(t) = -\frac{b}{2}X_j(t)\,dt + \frac{\sigma}{2}dW_j(t).
$$


To solve this, use integrating factor $e^{\frac{b}{2}t}$:

$$
\frac{d}{dt}\left( e^{\frac{b}{2}t} X_j(t) \right) = \frac{\sigma}{2} e^{\frac{b}{2}t} \frac{dW_j(t)}{dt}.
$$


Then:

$$
X_j(t) = e^{-\frac{b}{2}t} \left[ X_j(0) + \frac{\sigma}{2} \int_0^t e^{\frac{b}{2}u} dW_j(u) \right],
$$


which is equation (6.9.16).

Now show $X_j(t)$ is normal with:
- Mean:

$$
\mathbb{E}[X_j(t)] = e^{-\frac{b}{2}t}X_j(0),
$$


- Variance:

$$
\text{Var}(X_j(t)) = e^{-bt} \cdot \left( \frac{\sigma^2}{4} \int_0^t e^{bu}\,du \right) = \frac{\sigma^2}{4b}\left( 1 - e^{-bt} \right),
$$


which gives equation (6.9.17).

---

**(ii)** Define:

$$
R(t) = \sum_{j=1}^d X_j^2(t).
$$


Apply Itô’s lemma to $X_j^2(t)$:

$$
dX_j^2(t) = 2X_j(t)\,dX_j(t) + (dX_j(t))^2 = -bX_j^2(t)\,dt + \frac{\sigma^2}{4}\,dt + \sigma X_j(t)\,dW_j(t).
$$


Then:

$$
dR(t) = \sum_{j=1}^d dX_j^2(t) = \left( -b R(t) + \frac{d\sigma^2}{4} \right)dt + \sigma \sum_{j=1}^d X_j(t)\,dW_j(t),
$$


Let $a = \frac{d\sigma^2}{4}$ and define:

$$
B(t) = \sum_{j=1}^d \int_0^t \frac{X_j(s)}{\sqrt{R(s)}}\,dW_j(s).
$$


Then:

$$
dR(t) = (a - bR(t))\,dt + \sigma \sqrt{R(t)}\,dB(t),
$$


which is the CIR process in equation (6.9.19). Since $B(t)$ is constructed as a stochastic integral of orthonormal components, by Lévy’s theorem, $B(t)$ is a Brownian motion — this is equation (6.9.20).

---

**(iii)** Suppose $R(0) > 0$ is given, and define:

$$
X_j(0) = \sqrt{\frac{R(0)}{d}}.
$$


Then all $X_j(t)$ are independent and identically distributed normal random variables with:
- Mean:

$$
\mu(t) = \mathbb{E}[X_j(t)] = e^{-\frac{b}{2}t} \sqrt{\frac{R(0)}{d}},
$$


- Variance:

$$
v(t) = \text{Var}(X_j(t)) = \frac{\sigma^2}{4b}(1 - e^{-bt}),
$$


so $X_j(t) \sim \mathcal{N}(\mu(t), v(t))$.

---

**(iv)** Since $R(t) = \sum_{j=1}^d X_j^2(t)$ is a sum of squares of i.i.d. normal variables with nonzero mean, it follows a **noncentral chi-squared distribution**. To compute the MGF of $R(t)$, first compute the MGF of $X_j^2(t)$:

$$
\mathbb{E}[e^{uX_j^2(t)}] = \frac{1}{\sqrt{1 - 2v(t)u}} \exp\left( \frac{u\mu^2(t)}{1 - 2v(t)u} \right), \quad \text{for all } u < \frac{1}{2v(t)},
$$


which is equation (6.9.21), using completion of the square and integration of the normal density.

---

**(v)** Since $R(t) = \sum_{j=1}^d X_j^2(t)$, and the $X_j^2(t)$ are i.i.d., the moment-generating function of $R(t)$ is:

$$
\mathbb{E}[e^{uR(t)}] = \left( \frac{1}{1 - 2v(t)u} \right)^{d/2} \exp\left( \frac{u e^{-bt} R(0)}{1 - 2v(t)u} \right).
$$


Using $d = \frac{4a}{\sigma^2}$, this becomes:

$$
\mathbb{E}[e^{uR(t)}] = \left( \frac{1}{1 - 2v(t)u} \right)^{2a/\sigma^2} \exp\left( \frac{u e^{-bt} R(0)}{1 - 2v(t)u} \right),
$$


valid for all $u < \frac{1}{2v(t)}$, which is equation (6.9.22).



**Exercise 6.7 (Heston stochastic volatility model)**

---

**(i)** Show that $e^{-rt}c(t, S(t), V(t))$ is a martingale under $\widetilde{\mathbb{P}}$.

Using Itô’s formula on $c(t, S(t), V(t))$ where $S(t)$ and $V(t)$ follow (6.9.23) and (6.9.24), and applying the product rule to $e^{-rt}c(t, S(t), V(t))$, we require the drift of this process to be zero. Setting the $dt$ term to zero gives the PDE:

$$
c_t + rsc_s + (a - bv)c_v + \frac{1}{2}s^2vc_{ss} + \rho\sigma svc_{sv} + \frac{1}{2}\sigma^2vc_{vv} = rc,
$$

which is equation (6.9.26).

---

**(ii)** Suppose $f(t, x, v)$ and $g(t, x, v)$ satisfy the PDEs:

$$
f_t + \left( r + \frac{1}{2}v \right) f_x + (a - bv + \rho\sigma v)f_v + \frac{1}{2}vf_{xx} + \rho\sigma vf_{xv} + \frac{1}{2}\sigma^2 v f_{vv} = 0, \tag{6.9.32}
$$


$$
g_t + \left( r - \frac{1}{2}v \right) g_x + (a - bv)g_v + \frac{1}{2}vg_{xx} + \rho\sigma vg_{xv} + \frac{1}{2}\sigma^2 v g_{vv} = 0. \tag{6.9.33}
$$


Then, define

$$
c(t, s, v) = s f(t, \log s, v) - e^{-r(T - t)} K g(t, \log s, v). \tag{6.9.34}
$$


Show that $c(t, s, v)$ satisfies (6.9.26).

To verify this, apply the chain rule:
- $c_s = f + s f_x$,  
- $c_{ss} = \frac{1}{s}f_x + f_{xx} + s f_{xx}$,  
- $c_t = s f_t - re^{-r(T - t)}K g - e^{-r(T - t)}K g_t$,  
- $c_v = s f_v - e^{-r(T - t)}K g_v$,  
- $c_{sv}, c_{vv}$ likewise follow from applying product/chain rule.

Then substitute into the LHS of (6.9.26) and simplify using (6.9.32) and (6.9.33).

---

**(iii)** Let $(X(t), V(t))$ solve:

$$
dX(t) = \left(r + \frac{1}{2}V(t)\right)dt + \sqrt{V(t)}\,dW_1(t), \tag{6.9.35}
$$


$$
dV(t) = (a - bV(t) + \rho\sigma V(t))dt + \sigma \sqrt{V(t)}\,dW_2(t). \tag{6.9.36}
$$


Define:

$$
f(t, x, v) = \mathbb{E}^{t,x,v}[\mathbb{I}_{\{X(T) \geq \log K\}}]. \tag{6.9.37}
$$


Using Feynman-Kac, $f$ solves (6.9.32) with terminal condition:

$$
f(T, x, v) = \mathbb{I}_{\{x \geq \log K\}}. \tag{6.9.38}
$$


---

**(iv)** Now let $(X(t), V(t))$ follow:

$$
dX(t) = \left(r - \frac{1}{2}V(t)\right)dt + \sqrt{V(t)}\,dW_1(t), \tag{6.9.39}
$$


$$
dV(t) = (a - bV(t))dt + \sigma \sqrt{V(t)}\,dW_2(t). \tag{6.9.40}
$$


Define:

$$
g(t, x, v) = \mathbb{E}^{t,x,v}[\mathbb{I}_{\{X(T) \geq \log K\}}]. \tag{6.9.41}
$$


Then $g$ satisfies (6.9.33) and boundary condition:

$$
g(T, x, v) = \mathbb{I}_{\{x \geq \log K\}}. \tag{6.9.42}
$$


---

**(v)** Since $f$ and $g$ satisfy their PDEs and terminal conditions as shown, the function

$$
c(t, s, v) = s f(t, \log s, v) - e^{-r(T - t)}K g(t, \log s, v)
$$


satisfies the PDE (6.9.26) and boundary condition (6.9.27):

$$
c(T, s, v) = (s - K)^+.
$$



**Exercise 6.8 (Kolmogorov backward equation)**

We are given the SDE:

$$
dX(u) = \beta(u, X(u))\,du + \gamma(u, X(u))\,dW(u).
$$


Let $p(t, T; x, y)$ denote the transition density of $X(T)$ given $X(t) = x$. We want to show that $p$ satisfies the **Kolmogorov backward equation**:

$$
- p_t(t, T; x, y) = \beta(t, x)p_x(t, T; x, y) + \frac{1}{2}\gamma^2(t, x)p_{xx}(t, T; x, y). \tag{6.9.43}
$$


We use the **Feynman-Kac Theorem**, which says for any $h(y)$,

$$
g(t, x) = \mathbb{E}^{t,x}[h(X(T))] = \int_0^\infty h(y) p(t, T; x, y)\,dy \tag{6.9.44}
$$

satisfies the PDE:

$$
g_t(t, x) + \beta(t, x) g_x(t, x) + \frac{1}{2}\gamma^2(t, x) g_{xx}(t, x) = 0. \tag{6.9.45}
$$


Now differentiate under the integral in (6.9.44):
- $g_t = \int h(y) p_t\,dy$,
- $g_x = \int h(y) p_x\,dy$,
- $g_{xx} = \int h(y) p_{xx}\,dy$.

Substitute into (6.9.45):

$$
\int_0^\infty h(y)\left[ p_t + \beta p_x + \frac{1}{2} \gamma^2 p_{xx} \right]\,dy = 0.
$$


Since this holds for all $h(y)$, we conclude:

$$
p_t + \beta p_x + \frac{1}{2}\gamma^2 p_{xx} = 0 \quad \Rightarrow \quad -p_t = \beta p_x + \frac{1}{2}\gamma^2 p_{xx},
$$


which is equation (6.9.43).

---

**Exercise 6.9 (Kolmogorov forward equation)**

Again, consider:

$$
dX(u) = \beta(u, X(u))\,du + \gamma(u, X(u))\,dW(u). \tag{6.9.46}
$$


Let $p(t, T; x, y)$ be the transition density. We aim to show that $p$ satisfies the **Kolmogorov forward (Fokker-Planck) equation**:

$$
\frac{\partial}{\partial T}p(t, T; x, y) = -\frac{\partial}{\partial y}[\beta(T, y)p(t, T; x, y)] + \frac{1}{2} \frac{\partial^2}{\partial y^2}[\gamma^2(T, y)p(t, T; x, y)]. \tag{6.9.47}
$$


---

**(i)** Let $h_b(y)$ be a test function with compact support on $(0, b)$, satisfying $h_b(0) = h_b'(0) = h_b(b) = h_b'(b) = 0$.

Apply Itô’s lemma to $h_b(X(u))$:

$$
dh_b(X(u)) = h_b'(X(u))\,dX(u) + \frac{1}{2}h_b''(X(u))\,\gamma^2(u, X(u))\,du.
$$


Take expectation and integrate from $t$ to $T$:

$$
\mathbb{E}[h_b(X(T))] = h_b(x) + \mathbb{E}\left[ \int_t^T h_b'(X(u)) \beta(u, X(u))\,du + \frac{1}{2} \int_t^T h_b''(X(u)) \gamma^2(u, X(u))\,du \right].
$$


---

**(ii)** Replace $\mathbb{E}[h_b(X(T))]$ using the transition density:

$$
\int_0^b h_b(y) p(t, T; x, y)\,dy = h_b(x) + \int_t^T \int_0^b \beta(u, y) p(t, u; x, y) h_b'(y)\,dy\,du + \frac{1}{2} \int_t^T \int_0^b \gamma^2(u, y) p(t, u; x, y) h_b''(y)\,dy\,du. \tag{6.9.48}
$$


---

**(iii)** Apply integration by parts in the $y$ variable to the RHS:

$$
\int_0^b h_b(y)p(t, T; x, y)\,dy = h_b(x) - \int_t^T \int_0^b \frac{\partial}{\partial y}[\beta(u, y)p(t, u; x, y)] h_b(y)\,dy\,du + \frac{1}{2} \int_t^T \int_0^b \frac{\partial^2}{\partial y^2}[\gamma^2(u, y)p(t, u; x, y)] h_b(y)\,dy\,du. \tag{6.9.49}
$$


---

**(iv)** Differentiate (6.9.49) w.r.t. $T$:

$$
\int_0^b h_b(y) \left[
\frac{\partial}{\partial T}p(t, T; x, y)
+ \frac{\partial}{\partial y}[\beta(T, y)p(t, T; x, y)]
- \frac{1}{2}\frac{\partial^2}{\partial y^2}[\gamma^2(T, y)p(t, T; x, y)]
\right]\,dy = 0. \tag{6.9.50}
$$


---

**(v)** Since $h_b(y)$ is arbitrary, the integrand must be zero:

$$
\frac{\partial}{\partial T}p(t, T; x, y)
+ \frac{\partial}{\partial y}[\beta(T, y)p(t, T; x, y)]
- \frac{1}{2}\frac{\partial^2}{\partial y^2}[\gamma^2(T, y)p(t, T; x, y)] = 0,
$$


which is equation (6.9.47), the Kolmogorov forward equation.



**Exercise 6.10 (Implying the volatility surface)**

We are given the SDE:

$$
dS(u) = rS(u)\,du + \sigma(u, S(u))S(u)\,d\widetilde{W}(u),
$$

and define the transition density $\widetilde{p}(t, T; x, y)$ of $S(T)$ given $S(t) = x$.

According to Exercise 6.9, this satisfies the **Kolmogorov forward equation**:

$$
\frac{\partial}{\partial T} \widetilde{p}(t, T; x, y) = -\frac{\partial}{\partial y} \left( r y \widetilde{p}(t, T; x, y) \right) + \frac{1}{2} \frac{\partial^2}{\partial y^2} \left( \sigma^2(T, y) y^2 \widetilde{p}(t, T; x, y) \right). \tag{6.9.51}
$$


Define the time-zero price of a European call as:

$$
c(0, T, x, K) = e^{-rT} \int_K^\infty (y - K) \widetilde{p}(0, T; x, y)\,dy. \tag{6.9.52}
$$


Differentiate this in $T$:

$$
c_T(0, T, x, K) = -r c(0, T, x, K) + e^{-rT} \int_K^\infty (y - K) \frac{\partial}{\partial T} \widetilde{p}(0, T; x, y)\,dy. \tag{6.9.53}
$$


---

**(i)** Use integration by parts to show:

$$
- \int_K^\infty (y - K) \frac{\partial}{\partial y} (ry \widetilde{p}(0, T; x, y))\,dy = \int_K^\infty r y \widetilde{p}(0, T; x, y)\,dy. \tag{6.9.54}
$$


Assuming the boundary term vanishes:

$$
\lim_{y \to \infty} (y - K) r y \widetilde{p}(0, T; x, y) = 0. \tag{6.9.55}
$$


---

**(ii)** Now compute:

$$
\frac{1}{2} \int_K^\infty (y - K) \frac{\partial^2}{\partial y^2} \left( \sigma^2(T, y) y^2 \widetilde{p}(0, T; x, y) \right)\,dy.
$$


Integrate by parts **twice**, applying (6.9.57) and (6.9.58) which ensure boundary terms vanish:

$$
\frac{1}{2} \int_K^\infty (y - K) \frac{\partial^2}{\partial y^2} \left( \sigma^2(T, y) y^2 \widetilde{p} \right)\,dy = \frac{1}{2} \sigma^2(T, K) K^2 \widetilde{p}(0, T; x, K). \tag{6.9.56}
$$


---

**(iii)** Plug everything back into equation (6.9.53):

Start with:

$$
c_T(0, T, x, K) = -r c(0, T, x, K) + e^{-rT} \int_K^\infty (y - K) \frac{\partial}{\partial T} \widetilde{p}(0, T; x, y)\,dy,
$$

and use (6.9.51), (6.9.54), (6.9.56) to get:

$$
c_T(0, T, x, K) = e^{-rT} r K \int_K^\infty \widetilde{p}(0, T; x, y)\,dy + \frac{1}{2} e^{-rT} \sigma^2(T, K) K^2 \widetilde{p}(0, T; x, K),
$$


Note:
- $\int_K^\infty \widetilde{p} = \frac{\partial}{\partial K} c(0, T, x, K)$,
- $\widetilde{p}(0, T; x, K) = \frac{\partial^2}{\partial K^2} c(0, T, x, K)$.

So:

$$
c_T(0, T, x, K) = -r K c_K(0, T, x, K) + \frac{1}{2} \sigma^2(T, K) K^2 c_{KK}(0, T, x, K). \tag{6.9.59}
$$


---

This is the final equation. Under the assumption $c_{KK}(0, T, x, K) \neq 0$, we can solve (6.9.59) for $\sigma^2(T, K)$ in terms of:
- $c_T(0, T, x, K)$,
- $c_K(0, T, x, K)$,
- $c_{KK}(0, T, x, K)$,

which are quantities that can be inferred from observable option prices.

