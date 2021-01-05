# Regularization for Deep Learning 

## Parameter Norm Penalties 

Objective function for a a general parameter regularization can be expressed as:
$$
J_{R}(\mathcal{\boldsymbol{w}}, X, y) = J(w, X, y) + \alpha \Omega(w)
$$
Incorporating $L^2$ regularization: $\dfrac{\alpha}{2} \| w \|_2^2$;

 
$$
J_{R}(\mathcal{\boldsymbol{w}}, X, y) = J(w, X, y) + \dfrac{\alpha}{2} w^Tw
$$

#### Effect on One Gradient Descent Step

To understand its effect on learning, let's take its gradient:

$\nabla_w J_R(w) = \nabla_w J(w) + \alpha w $

Now the updated gradient descent step:
$$
w \leftarrow w - \epsilon (\alpha w - \nabla_w J(w)) \\
w \leftarrow (w - \epsilon \alpha w) - \nabla_w J(w) \\
w \leftarrow ( 1 - \epsilon \alpha )w - \nabla_w J(w)
$$
So $L^2$ regularization multiplicatively shrink weights at each step i.e. if we have $\epsilon=0.1, \alpha=0.5$, then gradient descent update will be subtracted from$0.95w$: $w \leftarrow 0.95w - \nabla_w J(w) $. 

#### Effect on Overall Training 

To see its effect on overall training, we need to see what kind of $w$ we will get after $L^2$ regularization compare to no regularization. Assume that $w^\star = \arg \min_w J$. Let's do quadratic approximation of original $J(w)$ in the neighborhood of $w^\star$ by Taylor series:

 
$$
\hat{J}(w) = J(w^\star) + \dfrac{1}{2!} (\nabla_w J(w-w^\star)) + \dfrac{1}{3!} (w - w^\star)^TH(w-w^\star) \\ 
\text{since $w^\star = \arg \min_w J$, $\nabla_w J = 0$; } \\
= J(w^\star) + (w-w^\star)^TH(w-w^\star) \\ 
\text{taking graident}\\
\nabla_w \hat J(w) = 0 + H(w-w^\star)
$$
The minima of $\hat{J}$ occurs when $\nabla \hat J (w) = 0$. To see the effect of regularization, let's assume that $w^R$ be the location of minima after regularization. Adding gradient of regularization, we get the minima at: 


$$
\alpha w^R + H(w^R-w^\star) = 0
$$
Solving this for $w^R$, we get: 
$$
w^R = (H+\alpha I)^{-1} Hw^\star
$$
Since $H$ is hessian, it is real and symmetric, there we can decompose into: $H = Q \Delta Q^T$, where $Q$ is orthogonal matrix representing eigen vectors of $H$.
$$
w^R = (Q\Lambda Q^T + \alpha I)^{-1} Q\Lambda Q^T w^\star \\ 
w^R = [Q (\Lambda +\alpha I)Q^T]^{-1} Q \Lambda Q^T w^\star \\
\text{since Q is orthogonal $Q^{-1}=Q$;}\\
w^R = [Q (\Lambda + \alpha I)^{-1}Q^T]Q\Lambda Q^T w^\star \\
\text{since Q is orthogonal: $QQ^T = I$} \\
w^R = Q(\Lambda + \alpha I)^{-1} \Lambda Q^T w^\star \\
$$
We can rewrite this as $w^R = Q \Lambda^R Q^T w^\star$, where $\Lambda^R = (\Lambda + \alpha I)^{-1}\Lambda$. This equation shows that regularization scales  $w^\star$ along the axis defined by eigen vectors of Hessian. 

To further see this effect, let's open $\Lambda^R$:
$$
\Lambda^R = (\Lambda + \alpha I)^{-1} \Lambda = 
\begin{bmatrix}
\lambda_1+\alpha & 0 & ... & 0 \\
0 & \lambda_2 +\alpha & ....& 0 \\
.. & ..& .. & .. \\
0 & 0 & ... & \lambda_n+\alpha
\end{bmatrix}^{-1} \begin{bmatrix}
\lambda_1 & 0 & ... & 0 \\
0 & \lambda_2 & ....& 0 \\
.. & ..& .. & .. \\
0 & 0 & ... & \lambda_n
\end{bmatrix}
\\
\text{$\Lambda$ is diagonal matrix so it's inverse is inverse of it's diagonal entries}\\
= \begin{bmatrix}
\dfrac{\lambda_1}{\lambda_1+\alpha} & 0 & ... & 0 \\
0 & \dfrac{\lambda_2}{\lambda_2+\alpha} & ....& 0 \\
.. & ..& .. & .. \\
0 & 0 & ... & \dfrac{\lambda_n}{\lambda_n+\alpha}
\end{bmatrix} \\
$$
This means that  the $i$-th eigen vector is of Hessian is scaled by $\dfrac{\lambda_i}{\lambda_i + \alpha}$.  

To further understand the effect of this, think of a matrix-vector multiplication. When we apply a matrix on vector, it stretches or expands the space. With eigen values, we can understand the this effect along the axis defined by eigen vectors.  

Now, if $\lambda_i >> \alpha$, scaling of $\alpha$ won't h have that much effect on $\lambda_i$ i.e. if $\lambda_i = 50, \alpha=1 \implies \dfrac{50}{50+0.1} \approx 1$ ; but if $\lambda_i << \alpha$ then the regularization will shrink the eigen value close to zero i.e. $\lambda_i = 0.001, \alpha=1 \implies \dfrac{0.001}{1+0.001} = 0.00099 $

