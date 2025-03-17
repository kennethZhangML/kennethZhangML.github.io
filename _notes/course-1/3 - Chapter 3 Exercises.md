---
layout: page
title: Chapter 3 Exercises
description: Exercises for Chapter 3 - State Prices.
parent: course-1
importance: 6
permalink: /notes/course-1/chapter-3-exercises/
nav: false
---


**Exercise 3.1**
(i) Since $Z$ is the Radon-Nikodym derivative, by definition, it is strictly continuous under $\mathbb{P}$ meaning that we have $\mathbb{P}(Z > 0) = 1$. By equivalence of measures, we see that $\tilde{\mathbb{P}}$ is absolutely continuous wrt $\mathbb{P}$, so an event that has probability 1 under $\mathbb{P}$ also has probability 1 under $\tilde{\mathbb{P}}$. 
Thus we can conclude that:

$$
\tilde{\mathbb{P}}\left(\frac{1}{Z} > 0 \right) = 1
$$

(ii) We can directly prove this with the definition of expectation under $\tilde{\mathbb{P}}$:

$$
\tilde{\mathbb{E}}X = \int X d \tilde{\mathbb{P}} = \int X Z d\mathbb{P} \implies \tilde{\mathbb{E}} \left[\frac{1}{Z} \right] = \int \frac{1}{Z} d \tilde{\mathbb{P}} \implies \tilde{\mathbb{E}} \left[\frac{1}{Z} \right] = \int \frac{1}{Z} Z d \mathbb{P} = \int 1 d \mathbb{P} = 1 
$$

(iii) For any random variable $Y$, we have:

$$
\mathbb{E} Y = \tilde{\mathbb{E}} \left[\frac{1}{Z} \cdot Y \right]
$$


$$
\tilde{\mathbb{E}}\left[\frac{1}{Z} Y \right] = \int \frac{1}{Z} Y d \tilde{\mathbb{P}} \implies \tilde{\mathbb{E}} \left[\frac{1}{Z} Y \right] = \int \frac{1}{Z} YZ d \mathbb{P} = \int Y d \mathbb{P} = \mathbb{E} Y
$$


**Exercise 3.2**
(i) By definition we have that:

$$
\tilde{\mathbb{P}}(\omega) = Z(\omega) \mathbb{P}(\omega)
$$

For any $A \subseteq \Omega$ and any sample space $\Omega$ we have:

$$
\tilde{\mathbb{P}}(A) = \sum_{\omega \in A} Z(\omega) \mathbb{P}(\omega) \implies \tilde{\mathbb{P}}(\Omega) = \sum_{\omega \in \Omega} Z(\omega) \mathbb{P}(\omega)
$$

Then given $\mathbb{E}[Z] = 1$ we have that:

$$
\tilde{\mathbb{P}}(\Omega) = \mathbb{E}[Z] = 1
$$

(ii) We define the expectation of $\tilde{\mathbb{E}}Y = \mathbb{E}[Z Y]$ as 

$$ \tilde{\mathbb{E}}[Y] = \sum_{\omega \in \Omega} Y(\omega) \tilde{\mathbb{P}}(\omega). $$

After substituting we get:

$$ \tilde{\mathbb{E}}[Y] = \sum_{\omega \in \Omega} Y(\omega) Z(\omega) \mathbb{P}(\omega). $$

Recognizing this as the expectation of $ZY$ under $\mathbb{P}$:

$$ \tilde{\mathbb{E}}[Y] = \mathbb{E}[Z Y]. $$

(iii) By definition we have:

$$ \tilde{\mathbb{P}}(A) = \sum_{\omega \in A} Z(\omega) \mathbb{P}(\omega). $$

If $\mathbb{P}(A) = 0$, then the sum contains only terms where $\mathbb{P}(\omega) = 0$, meaning:

$$ \tilde{\mathbb{P}}(A) = \sum_{\omega \in A} Z(\omega) \cdot 0 = 0. $$

Thus, an event that is impossible under $\mathbb{P}$ is also impossible under $\tilde{\mathbb{P}}$.

(iv) If $\tilde{\mathbb{P}}(A) = 0$, then: 
$$ \sum_{\omega \in A} Z(\omega) \mathbb{P}(\omega) = 0. $$
 Since $Z(\omega) \geq 0$ and $Z(\omega) > 0$ almost surely under $\mathbb{P}$, the only way for this sum to be 0 is if $\mathbb{P}(\omega) = 0$ for all $\omega \in A$. This implies: 
$$ \mathbb{P}(A) = 0. $$

(v) By definition, two probability measures are **equivalent** if they assign probability zero to the same events: 
$$\mathbb{P}(A) = 0 \iff \tilde{\mathbb{P}}(A) = 0.$$
 From **(iii) and (iv)**, we already showed: - If $\mathbb{P}(A) = 0$, then $\tilde{\mathbb{P}}(A) = 0$. - If $\tilde{\mathbb{P}}(A) = 0$ and $\mathbb{P}(Z > 0) = 1$, then $\mathbb{P}(A) = 0$. Thus, $\mathbb{P}$ and $\tilde{\mathbb{P}}$ are equivalent, meaning: 
$$\mathbb{P}(A) = 1 \iff \tilde{\mathbb{P}}(A) = 1.$$

(vi) We need an example where $\mathbb{P}(Z \geq 0) = 1$ but there exists an event $A$ such that: 
$$\tilde{\mathbb{P}}(A) = 0, \quad \text{but} \quad \mathbb{P}(A) > 0.$$
 **Example:** - Let $\Omega = \{ \omega_1, \omega_2 \}$. - Define $\mathbb{P}(\omega_1) = \frac{1}{2}, \mathbb{P}(\omega_2) = \frac{1}{2}$. - Define $Z(\omega_1) = 2, Z(\omega_2) = 0$. Then: 
$$\tilde{\mathbb{P}}(\omega_1) = Z(\omega_1) \mathbb{P}(\omega_1) = 2 \times \frac{1}{2} = 1.$$

$$\tilde{\mathbb{P}}(\omega_2) = Z(\omega_2) \mathbb{P}(\omega_2) = 0 \times \frac{1}{2} = 0.$$
 Now consider the event $A = \{ \omega_2 \}$: - Under $\mathbb{P}$, we have $\mathbb{P}(A) = \frac{1}{2} > 0$. - Under $\tilde{\mathbb{P}}$, we have $\tilde{\mathbb{P}}(A) = 0$. Since $\mathbb{P}(A) > 0$ but $\tilde{\mathbb{P}}(A) = 0$, the measures are **not equivalent**.


**Exercise 3.3**
We are given the stock price model from **Figure 3.1.1** and the actual probabilities: 
$$ p = \frac{2}{3}, \quad q = \frac{1}{3}. $$
 We define the conditional expectation of $ S_3 $ at different times: 
$$ M_n = \mathbb{E}_n[S_3], \quad n = 0,1,2,3. $$
 ### **Step 1: Compute $ M_n $ at each time step** Using the **stock price tree from Figure 3.1.1**, the final stock prices at time $ n=3 $ are: 
$$ S_3(HHH) = 32, \quad S_3(HHT) = S_3(HTH) = S_3(THH) = 8, $$
 
$$ S_3(HTT) = S_3(THT) = S_3(TTH) = 2, \quad S_3(TTT) = 0.5. $$
 Now, we compute the expected values at each node **going backward in time**. At time $ n=2 $, we calculate: 
$$ M_2(HH) = \mathbb{E}[S_3 | HH] = pS_3(HHH) + qS_3(HHT) = \frac{2}{3} (32) + \frac{1}{3} (8) = \frac{64}{3} + \frac{8}{3} = \frac{72}{3} = 24. $$
 
$$ M_2(HT) = \mathbb{E}[S_3 | HT] = pS_3(HTH) + qS_3(HTT) = \frac{2}{3} (8) + \frac{1}{3} (2) = \frac{16}{3} + \frac{2}{3} = \frac{18}{3} = 6. $$
 Similarly, for other nodes: 
$$ M_2(TH) = 6, \quad M_2(TT) = \frac{2}{3} (2) + \frac{1}{3} (0.5) = \frac{4}{3} + \frac{0.5}{3} = \frac{4.5}{3} = 1.5. $$

Using the previous values: 
$$ M_1(H) = \mathbb{E}[M_2 | H] = pM_2(HH) + qM_2(HT) = \frac{2}{3} (24) + \frac{1}{3} (6) = \frac{48}{3} + \frac{6}{3} = \frac{54}{3} = 18. $$
 
$$ M_1(T) = \mathbb{E}[M_2 | T] = pM_2(TH) + qM_2(TT) = \frac{2}{3} (6) + \frac{1}{3} (1.5) = \frac{12}{3} + \frac{1.5}{3} = \frac{13.5}{3} = 4.5. $$

$$ M_0 = \mathbb{E}[M_1] = pM_1(H) + qM_1(T) = \frac{2}{3} (18) + \frac{1}{3} (4.5) = \frac{36}{3} + \frac{4.5}{3} = \frac{40.5}{3} = 13.5. $$

A **martingale** satisfies: 
$$ \mathbb{E}[M_{n+1} | M_n] = M_n. $$
 We verify: - $\mathbb{E}[M_1 | M_0] = 13.5$. - $\mathbb{E}[M_2 | M_1] = M_1$. - $\mathbb{E}[M_3 | M_2] = M_2$. Since all hold, $ M_n $ is indeed a **martingale**.


**Exercise 3.4**
(i) We need to compute: 
$$ \zeta_3(HHH), $$

$$ \zeta_3(HHT) = \zeta_3(HTH) = \zeta_3(THH), $$

$$ \zeta_3(HTT) = \zeta_3(THT) = \zeta_3(TTH), $$

$$ \zeta_3(TTT). $$
 From previous formulas, the state price density is given by: 
$$ \zeta_3(\omega) = \frac{Z_3(\omega)}{(1+r)^3}. $$

(ii) Using the formula for the price at time zero: 
$$ v_0(4,4) = \sum_{\omega \in \Omega} \zeta_3(\omega) V_3(\omega). $$
 This requires the values from part (i). We sum over all states to get: 
$$ v_0(4,4) = \mathbb{E}_0[Z_3 V_3]. $$

(iii) We compute: 
$$ \zeta_2(HT) = \zeta_2(TH). $$
 From the definition: 
$$ \zeta_2(\omega) = \frac{Z_2(\omega)}{(1+r)^2}. $$

(iv) The risk-neutral pricing formula states: 
$$ V_2(HT) = \frac{1}{\zeta_2(HT)} \mathbb{E}_2[\zeta_3 V_3 | HT], $$

$$ V_2(TH) = \frac{1}{\zeta_2(TH)} \mathbb{E}_2[\zeta_3 V_3 | TH]. $$
 Using the values from previous steps, we obtain: 
$$ V_2(HT) = v_2(4,16), \quad V_2(TH) = v_2(4,10). $$
 Finally, we verify: 
$$ V_2(HT) \neq V_2(TH). $$


**Exercise 3.5**
We consider the model from **Exercise 2.9 of Chapter 2**, where the actual probability measure is given by: 
$$ \mathbb{P}(HH) = \frac{4}{9}, \quad \mathbb{P}(HT) = \frac{2}{9}, \quad \mathbb{P}(TH) = \frac{2}{9}, \quad \mathbb{P}(TT) = \frac{1}{9}. $$
(i) The **risk-neutral measure** was computed in **Exercise 2.9** of Chapter 2.
We need to compute: 
$$ Z(HH), \quad Z(HT), \quad Z(TH), \quad Z(TT). $$
Using the definition: 
$$ Z(\omega) = \frac{\tilde{\mathbb{P}}(\omega)}{\mathbb{P}(\omega)}. $$

(ii) We know that $Z_2 = Z$. We now compute: 
$$ Z_1(H), \quad Z_1(T), \quad Z_0. $$
By definition: 
$$ Z_1(H) = \mathbb{E}[Z_2 | H], \quad Z_1(T) = \mathbb{E}[Z_2 | T]. $$
Since $Z_0 = \mathbb{E}[Z] = 1$, we verify: 
$$ Z_0 = 1. $$

(iii) The risk-neutral pricing formula adapted for this model is: 
$$ V_1(H) = \frac{1}{Z_1(H)(1 + r_1(H))} \mathbb{E}_1[Z_2 V_2](H), $$

$$ V_1(T) = \frac{1}{Z_1(T)(1 + r_1(T))} \mathbb{E}_1[Z_2 V_2](T), $$

$$ V_0 = \mathbb{E} \left[ \frac{Z_2}{(1 + r_0)(1 + r_1)} V_2 \right]. $$
 Using the given payoff function: 
$$ V_2 = (S_2 - 7)^+, $$
 we substitute and compute each term.


**Exercise 3.6**
We consider **Problem 3.3.1** in an **$N$-period binomial model** with the utility function: 
$$ U(x) = \ln x. $$
We need to show that the **optimal wealth process** corresponding to the optimal portfolio process is given by: 
$$ X_n = \frac{X_0}{\zeta_n}, \quad n = 0,1,\dots,N, $$
where $\zeta_n$ is the **state price density process** defined in **(3.2.7)**.
From **Problem 3.3.1**, the optimal investment problem seeks to maximize: 
$$ \mathbb{E} [ U(X_N) ] = \mathbb{E} [ \ln X_N ]. $$
Using the first-order condition of the **Lagrangian approach**, we get: 
$$ U'(X_N) = \lambda \zeta_N. $$
Since $U(x) = \ln x$, we have: 
$$ U'(X_N) = \frac{1}{X_N}. $$
Thus, the optimality condition becomes: 
$$ \frac{1}{X_N} = \lambda \zeta_N. $$
Rearranging for $X_N$: 
$$ X_N = \frac{1}{\lambda} \frac{1}{\zeta_N}. $$
From the **budget constraint**: 
$$ \mathbb{E} [ \zeta_N X_N ] = X_0. $$
Substituting $X_N = \frac{1}{\lambda} \frac{1}{\zeta_N}$: 
$$ \mathbb{E} \left[ \zeta_N \cdot \frac{1}{\lambda} \frac{1}{\zeta_N} \right] = X_0. $$
Since $\mathbb{E}[1/\lambda] = 1/\lambda$, we get: 
$$ \frac{1}{\lambda} \mathbb{E} [ 1 ] = X_0. $$
Thus, 
$$ \frac{1}{\lambda} = X_0. $$
 Plugging this back into the expression for $X_N$: 
$$ X_N = \frac{X_0}{\zeta_N}. $$


**Exercise 3.7**
We consider **Problem 3.3.1** in an **$N$-period binomial model** with the utility function: 
$$U(x)=\frac{1}{p}x^p,$$
 where $p<1$ and $p\neq 0$. We need to show that the **optimal wealth at time $N$** is: 
$$X_N=\frac{X_0(1+r)^N Z^{\frac{p-1}{p}}}{\mathbb{E}\left[Z^{\frac{p-1}{p}}\right]},$$
 where $Z$ is the **Radon-Nikodým derivative** of $\tilde{\mathbb{P}}$ with respect to $\mathbb{P}$. ### **Step 1: Solve for Optimal Wealth Process** We aim to maximize: 
$$\mathbb{E} [ U(X_N) ]=\mathbb{E} \left[ \frac{1}{p} X_N^p \right].$$
 Using the **first-order condition** from the **Lagrangian approach**, we get: 
$$U'(X_N)=\lambda Z,$$
 where $U'(x)=x^{p-1}$. Thus, we obtain: 
$$X_N^{p-1}=\lambda Z.$$
 Solving for $X_N$: 
$$X_N=\lambda^{\frac{1}{p-1}} Z^{\frac{1}{p-1}}.$$
From the **budget constraint**: 
$$\mathbb{E} [ Z X_N ] = X_0(1+r)^N.$$
Substituting $X_N$: 
$$\mathbb{E} \left[ Z \lambda^{\frac{1}{p-1}} Z^{\frac{1}{p-1}} \right] = X_0(1+r)^N.$$
 Rewriting: 
$$\lambda^{\frac{1}{p-1}} \mathbb{E} \left[ Z^{\frac{p-1}{p}} \right] = X_0(1+r)^N.$$
 Solving for $\lambda^{\frac{1}{p-1}}$: 
$$\lambda^{\frac{1}{p-1}} = \frac{X_0(1+r)^N}{\mathbb{E} \left[ Z^{\frac{p-1}{p}} \right]}.$$
 Plugging this back into the expression for $X_N$: 
$$X_N = \frac{X_0(1+r)^N Z^{\frac{p-1}{p}}}{\mathbb{E} \left[ Z^{\frac{p-1}{p}} \right]}.$$


**Exercise 3.8**
The **Lagrange Multiplier Theorem** used in **Problem 3.3.5** has hypotheses that were not verified in that solution. The theorem states that if the **gradient of the constraint function**, which in this case is the vector: 
$$(p_1\zeta_1,\dots,p_m\zeta_m),$$
 is not the **zero vector**, then the **optimal solution** must satisfy the Lagrange multiplier equations **(3.3.22)**. Since this **gradient is nonzero**, the hypothesis holds. However, even when this is satisfied, the **theorem does not guarantee** an optimal solution. The **Lagrange multiplier equations** may provide a **minimizer rather than a maximizer**, or the solution could be neither. Thus, we outline a different method to verify that the **random variable** $X_N$ given by **(3.3.25)** maximizes the **expected utility**.

We redefine the **random variable** from **(3.3.25)** as: 
$$X_N^*=I\left(\frac{\lambda}{(1+r)^N}Z\right), \quad (3.6.1)$$
 where **$\lambda$ is the solution** of equation **(3.3.26)**. This allows us to use the notation **$X_N$** for an **arbitrary (not necessarily optimal) random variable** satisfying **(3.3.19)**. We must show: 
$$\mathbb{E}U(X_N)\leq\mathbb{E}U(X_N^*). \quad (3.6.2)$$
Fix $y>0$, and show that the function: 
$$U(x)-yx$$
 is maximized at **$x=I(y)$**. This implies: 
$$U(x)-yx\leq U(I(y))-yI(y) \quad \text{for every } x. \quad (3.6.3)$$
In **(3.6.3)**, replace: - **Dummy variable** $x$ with the **random variable** $X_N$. - **Dummy variable** $y$ with the **random variable**: 
$$\frac{\lambda Z}{(1+r)^N}.$$
 Take **expectations on both sides** and use **(3.3.19)** and **(3.3.26)** to conclude **(3.6.2)**.


**Exercise 3.9**
A wealthy investor provides an initial amount of money $X_0$ for investment over **$N$ periods** in a **binomial model**, under the condition that the portfolio value **never becomes negative**. The investor rewards you if your **final portfolio value** satisfies: 
$$X_N\geq\gamma.$$
 Thus, the objective is to **maximize**: 
$$\mathbb{P}(X_N\geq\gamma).$$
 where $X_N$ is a **portfolio process** satisfying: 
$$X_n\geq0,\quad n=1,2,\dots,N.$$

Following **Problem 3.3.3**, we reformulate the problem as: 
$$\max \mathbb{P}(X_N\geq\gamma),$$
 subject to: 
$$\mathbb{E} \left[\frac{X_N}{(1+r)^N}\right]=X_0,\quad X_n\geq0,\quad n=1,2,\dots,N.$$
Show that if $X_N\geq0$, then **$X_n\geq0$ for all** $n$. **Trivial by induction.** Consider the function: 
$$U(x)=\begin{cases}0,&0\leq x<\gamma,\\1,&x\geq\gamma.\end{cases}$$
 For any fixed $y>0$, show that: 
$$U(x)-yx\leq U(I(y))-yI(y)\quad\forall x\geq0.$$
 where: 
$$I(y)=\begin{cases}\gamma,&0<y\leq\frac{1}{\gamma},\\0,&y>\frac{1}{\gamma}.\end{cases}$$
 If a **solution** $\lambda$ satisfies: 
$$\mathbb{E} \left[ \frac{Z}{(1+r)^N}I\left(\frac{\lambda Z}{(1+r)^N}\right) \right]=X_0,\quad (3.6.4)$$
 then the **optimal $X_N$** is given by: 
$$X_N^*=I\left(\frac{\lambda Z}{(1+r)^N}\right).$$
List the $M=2^N$ **possible coin toss sequences**: 
$$\zeta_1\leq\zeta_2\leq\dots\leq\zeta_M.$$
 Show that assuming a **solution $\lambda$ exists** is equivalent to assuming that **for some $K$**: 
$$\sum_{m=1}^{K} \zeta_m p_m=\frac{X_0}{\gamma}. \quad (3.6.5)$$
