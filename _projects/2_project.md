---
layout: page
title:  PM2.5 and the Great Regulatory Vanishing Act - When Pollution Took a Free Pass
description: An introduction to the statistical models used to assess the impact of EPA rollbacks on air quality in California. https://enveurope.springeropen.com/articles/10.1186/s12302-021-00489-9
img: assets/img/pm25-analysis.jpg
importance: 2
category: research
related_publications: true
---

## Overview

This page provides the mathematical derivation used in our analysis of PM2.5 levels in California, following the EPA regulation rollbacks during the COVID-19 pandemic. The goal is to statistically assess the differences in pollution levels before and after the rollbacks, using a combination of **t-tests** and **regression analysis** to evaluate significance.

The study titled "Association of Temporary Environmental Protection Agency Regulation Suspension with Industrial Economic Viability and Local Air Quality in California, United States" investigates the impacts of the 2020 EPA enforcement rollbacks on both the economic health of specific industries and local air quality in California during the COVID-19 pandemic.

To address the first question, the research employed machine learning models to predict weekly employment levels across various industries. The results showed statistically significant declines in employment in industries like oil and manufacturing despite the rollback of regulations, suggesting that these industries did not experience economic recovery.

For the second question, 10 years of PM2.5 air pollution data were analyzed across counties with and without significant industrial activity. The findings indicated that counties with oil refineries showed no improvement in air quality, and in some cases, pollution levels remained similar to historical averages despite the state lockdown.

The paper concludes that the suspension of regulations did not achieve its intended economic benefits and may have allowed industries to maintain previous levels of pollution, raising concerns about the long-term environmental and health impacts of such policy changes.

## Statistical Model: t-test Derivation

We used a paired t-test to compare the means of PM2.5 levels between treatment and control counties. The test statistic for the paired t-test is given by:

$$
t = \frac{\overline{d}}{s_d / \sqrt{n}}
$$

Where:
- $$$\overline{d}$$ is the mean difference between paired observations (pre- and post-rollback PM2.5 levels).
- $$s_d$$ is the standard deviation of the differences.
- $$n$$ is the number of paired observations.

The null hypothesis ($$H_0$$) states that the mean difference in PM2.5 levels between pre- and post-rollback is zero, i.e., $$\overline{d} = 0$$. The alternative hypothesis ($$H_1$$) posits that there is a significant difference, i.e., $$\overline{d} \neq 0$$.

## Polynomial Regression Analysis

To predict future employment and pollution levels, we implemented **polynomial regression**, where the dependent variable $$y$$ (employment levels or PM2.5 values) is modeled as a polynomial function of the independent variable $$x$$ (time in weeks):

$$
y = \beta_0 + \beta_1 x + \beta_2 x^2 + \dots + \beta_n x^n + \epsilon
$$

Where:
- $$\beta_0, \beta_1, \dots, \beta_n$$ are the regression coefficients.
- $$x^n$$ represents the powers of the time variable $$x$$.
- $$\epsilon$$ is the error term.

By fitting the polynomial function to the observed data, we minimized the sum of squared residuals:

$$
S(\beta) = \sum_{i=1}^{n} \left( y_i - \left( \beta_0 + \beta_1 x_i + \dots + \beta_n x_i^n \right) \right)^2
$$

The optimal values of the coefficients $$\beta_0, \beta_1, \dots, \beta_n$$ were obtained using the **least squares method**.

## Conclusion

This mathematical framework was essential in evaluating the impact of the EPA's regulatory rollbacks on both economic and environmental outcomes in California. The results of the paired t-tests, combined with the predictions from polynomial regression models, allowed us to draw meaningful conclusions about the association between industrial activity and air quality.
