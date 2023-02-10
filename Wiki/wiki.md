# **Multi-objective least squares and applications**

## Introduction

This is an introductory article designed to introduce readers with some basic programming background to the multi-objective least squares problem. The Table of Contents:

* Preliminaries
* Multi-objective least squares
* Regularized data fitting
* Estimation


## Preliminaries

Before we start, we will quickly review some fundamental concepts that we need later on.

## Multi-objective least squares

In a multi-objective least squares problem, we want to seek one $x$ that minimizes a linear combination of $n$ objectives at the same time.

$$J_1 = ||A_1x-b_1||^2, J_2 = ||A_2x-b_2||^2, ..., J_n = ||A_nx-b_n||^2$$

For example, a weighted least squares problem can be formulated with the above definitions.

$$ \textnormal{minimize} \quad J = \lambda_1||A_1x-b_1||^2 + ... + \lambda_n||A_nx-b_n||^2$$

In general, the coefficients $\lambda_1, ..., \lambda_n$ are positive values, and they express the relative importance of different objectives. An extreme example is $\lambda_1 = 1, \lambda_{2}, ..., \lambda_{n} = 0$, which simplifies this problem to a single-objective least squares problem.

### Solution of weighted least squares

Assuming all $\lambda$s are all positive, we can slightly rewrite the objective.

$$ \begin{aligned}
\textnormal{minimize} \quad J &= \lVert\sqrt{\lambda_{1}}A_1x-\sqrt{\lambda_1}b_1 \rVert^2 + ... + \lVert\sqrt{\lambda_{n}}A_nx-\sqrt{\lambda_n}b_n \rVert^2\\
&= \sum_{k=1}^{n} \lVert\sqrt{\lambda_{k}}A_kx-\sqrt{\lambda_k}b_k \rVert^2\\
&= \lVert 
\begin{bmatrix}
\sqrt{\lambda_{1}}A_1 \\
\sqrt{\lambda_{2}}A_2 \\
:\\
:\\
\sqrt{\lambda_{n}}A_n
\end{bmatrix} x - 
\begin{bmatrix}
\sqrt{\lambda_{1}}b_1 \\
\sqrt{\lambda_{2}}b_2 \\
:\\
:\\
\sqrt{\lambda_{n}}b_n
\end{bmatrix} \rVert^2
\end{aligned}
$$

We can see that in the final form, it looks exactly like a least squares problem. However, if the stacked matrix has linearly dependent columns, we have multiple solutions. Also note that we do not enforce all matrices $A$ to be full column rank, i.e. have linearly independent columns.

Hence the solution to the above least squares problem can be derived from a single-objective least squares problem.

$$\hat{x} = (\lambda_1A_1^TA_1+...+\lambda_kA_k^TA_k)^{-1}(\lambda_1A_1^Tb_1+...+\lambda_kA_k^Tb_k)$$

## Regularized data fitting

### Why do we need regularization?

Let's look at a simple linear (linear in parameters!) regression problem.

We have data points $(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), (x^{(3)}, y^{(3)}), ..., (x^{(N)}, y^{(N)})$ and model
 $$\hat{f}(x)=\theta_1f_1(x)+...+\theta_pf_p(x)$$

If $\hat{f}_k(x)$ is a high-order polynomial of x, then a large $\theta_k$ will amplify the perturbations in $x$. This will result in a large variance in $\hat{f}(x)$, hence an overfitted model. We will later see how this is useful in image deblurring.

Now, our problem becomes two-fold: 
1) We want to fit the model $\hat{f}(x)$ to data points $(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), (x^{(3)}, y^{(3)}), ..., (x^{(N)}, y^{(N)})$, i.e. minimize the difference between our prediction and ground-truth.
2) We want to keep $\theta_1, \theta_2, ..., \theta_p$ small to avoid over-fitting.

We can easily formulate this problem into a multi-objective least squares problem.

$$J_1(\theta) = \sum_{k=1}^{N}(\hat{f}(x^{(k)}) - y^{(k)})^2,\quad J_2(\theta) = \sum_{j=1}^{p}\theta_j^2$$

Depending on the strength of regularization, we can toggle the value of a regularization coefficient $\lambda$. That is,

$$\textnormal{minimize} \quad J_1(\theta) + \lambda J_2(\theta) = \sum_{k=1}^{N}(\hat{f}(x^{(k)}) - y^{(k)})^2 + \lambda \sum_{j=1}^{p}\theta_j^2$$



<figure>
    <img src="../Images/projection.png"
         alt="Elephant at sunset">
    <figcaption> Fig.1 Projection</figcaption>
</figure>

Projection of $\vec{x}$ onto $\vec{u}$ (green vector in fig.1)?

$$ \begin{aligned}
\lVert \vec{x} \rVert \cos\theta &= \frac{\lVert \vec{x} \rVert \lVert \vec{u} \rVert \cos\theta} {\lVert \vec{u} \rVert} \\
&= \frac{\vec{x}^\intercal \vec{u}}{\lVert \vec{u} \rVert}
\end{aligned}
$$


### Heading 3

$A \cup B$

<p align="center">
<img src="https://www.raspberrypi.org/app/uploads/2018/03/RPi-Logo-Reg-SCREEN-199x250.png" alt="Raspberry pi" style="width:20%; border:0;">
</p>


$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
a & b & c
\end{bmatrix}
$$



```r
norm = function(x) {
  sqrt(x%*%x)
}
norm(1:4)
```