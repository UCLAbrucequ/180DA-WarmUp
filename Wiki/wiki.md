# **Image Deblurring with Multi-objective least squares**

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

$$ \textnormal{minimize} \;\; J = \lambda_1||A_1x-b_1||^2 + ... + \lambda_n||A_nx-b_n||^2$$

Let's look at an example!

```Matlab
% MATLAB script
T=6;
a,b=rand(T);
m=tril(a,-1);
n=tril(b,-1);
A_1=m+m'+eye(T).*rand(T);
A_2=n+n'+eye(T).*rand(T);  %generate two 6x6 full rank matrices
```

In general, the coefficients $\lambda_1, ..., \lambda_n$ are positive values, and they express the relative importance of different objectives. An extreme example is $\lambda_1 = 1, \lambda_{2}, ..., \lambda_{n} = 0$, which simplifies this problem to a single-objective least squares problem.

### Solution of weighted least squares

Assuming all $\lambda$s are all positive, we can slightly rewrite the objective.

$$ \begin{aligned}
\textnormal{minimize} \;\; J &= \lVert\sqrt{\lambda_{1}}A_1x-\sqrt{\lambda_1}b_1 \rVert^2 + ... + \lVert\sqrt{\lambda_{n}}A_nx-\sqrt{\lambda_n}b_n \rVert^2\\
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

### Projections



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