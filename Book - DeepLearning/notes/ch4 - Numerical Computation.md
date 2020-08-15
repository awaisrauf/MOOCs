# Numerical Computation

- ML algorithms uses numerical computations (iterative process of solving problems) instead of symbolic one. This can be tricky for real numbers because of the limited precision offered by digital computers. 
- Problems tackled: optimization and solution of linear equations 

### Underflow and Overflow

- Limited memory in digital computers mean we can not precisely represent real numbers. This make us approximate which causes rounding errors. Rounding errors can be serious problems if they happen multiple times and can cause an algorithm to fail

- **Underflow**: When a small number is rounded to zero. The problem is some functions may cause issues e.g. division by zero is not permitted in many programs. 

- **Overflow**: When a large number is approximated with $-\infty$ or $\infty$. 

- **Example**: Softmax function used for probability distribution of multinuli random variables: 
  $$
  Softmax(x_i) = \dfrac{e^{x_i}}{\sum_{j=1}^{n} e^{x_j}}
  $$
  Problem: for even fairly large number, exp can be very large which causes overflow. One solution is to perform softmax on $z=x-\max_ix_i$ since adding scalar from input vector in softmax does not change its result.

### Poor Conditioning 

- **Conditioning**: How much a function changes by changing it input. If a function changes rapidly, rounding errors can change results significantly. 

- **Condition Number**: Quantifies conditioning of a function. 

  >  the **condition number** of a function measures how much the output value of the function can change for a small change in the input argument. T

### Gradient Based Optimization 

- Many problems involve optimization which is finding a point that minimizes or maximizes a function. Let's say that we have a function $y=f(x)$, and we want to find $x^*=argmin_x f(x)$, where $f(x)$ is called objective function. Finding maxima is same as finding minimum of $-f(x)$.

- Derivative of a function $f(x)$ tells us how we should make a small change in $x$ that reflects in $f(x)$ i.e. $f(x+\epsilon) \approx f(x) + \epsilon \nabla_xf(x)$. Therefore, derivative is useful for optimization as it tell us how to change $x$ to decrease $f(x)$.

- If we want to find an x that minimizes $f(x)$, we should find $\hat{x}=x+\epsilon$ such that $f(\hat{x})\leq f(x)$ .

- A point where $f(x)=0$ is called critical point and there are three types of it; minima, maxima and saddle point. 

- A function may have many local critical points i.e. points

  >A local minimum is a point where f(x) is lower than at all neighboring points, so it is no longer possible to decrease f(x) by making infinitesimal steps.  

  >In the context of deep learning, we optimize functions that may have many local minima that are not optimal and many saddle points surrounded by very flat regions.  sually settle for finding a value of f that is very low but not necessarily minimal in any formal sense.  

  <img src="imgs/35.png" style="zoom:75%;" />

- **Directional derivative**: In higher dimensions, partial derivative $\partial_{x_1} f$ tells us how making small change in $x_1$ direction changes the function. The directional derivative is the derivative of a function with respect to a particular unit vector $\vec{u}$ where $\vec{u}$ defines the direction. Directional derivative is defined as $\dfrac{\partial f}{\partial \alpha}(f(x+\alpha \vec{u})) = \vec{u}^T\nabla f$. 
  For more: [link](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/gradient-and-directional-derivatives/v/directional-derivative)

- **Gradient Descent from Directional Derivative**: Then, our goal is to find a direction in which the function changes the fastest i.e.
  $$
  \text{argmin}_{\vec{u} } \vec{u}^T\nabla f = \text{argmin}_{\vec{u}}||\vec{u}||_2  ||\nabla f||_2 cos \theta = cos \theta
  $$
  where $\theta$ is angle between directional vector and gradient. This minimizes when angle between gradient and directional vector is -180 i.e. the directional of fastest change in $f(x)$ is opposite to direction of gradient. This gives rise to steepest descent or gradient descent which proposes to change $x$ in following way:
  $$
  x^{'} = x - \epsilon \nabla f
  $$
  

- There are a number of ways to choose $\epsilon$: one is to evaluate $f(x)$ for several $\epsilon$ and use one that has minimum objective function value. This is called line search. 

#### Beyond Gradient 

**Jacobian**: If a function has multiple inputs and outputs ($f: \mathbb{R}^n \to \mathbb{R}^m$), then we can also have multiple partial derivatives i.e. $J_{i,j} = \dfrac{\partial }{\partial x_j} f(x)_i$

**Second Derivative**: Derivative of a derivative $\dfrac{\nabla^2f}{\nabla x^2}$. It tell us curvature of a function. In terms of optimization, it tell us how much improvement in objective function we should expect when we change $x$ by $\epsilon$.

>The second derivative tells us how the first derivative will change as we vary the input. This is important because it tells us whether a gradient step will cause as much of an improvement as we would expect based on the gradient alone.  

**Hessian**: When we input is vector, second derivative is a matrix defined as 

<img src="imgs/36.png" style="zoom:75%;" />

For most deep learning, Hessian is real and symmetric which means we can decompose it into eigenvalues and eigen vectors. 

- Hessian in a specific direction $\vec{d}$ is given by $\vec{d}H^T\vec{d}$. 	

- when $\vec{d}$ is eigen vector, Hessian is in this direction is given by eigen value. 

- > The maximum eigenvalue determines the maximum second derivative, and the minimum eigenvalue determines the minimum second derivative.  

**What does second derivative tell us?**: Second derivative tell us how good we should expect gradient descent to perform for small changes. To see this, lets use Taylor series expansion of a function around a value $x^{(0)}$:

<img src="imgs/37.png" style="zoom:75%;" />

New point by gradient descent is $x^{(0)} - \epsilon g$, and Taylor series expansion:

<img src="imgs/38.png" style="zoom:75%;" />

- When $g^THg$ is zero or negative, gradient descent update changes the function forever. 
- When $g^THg$ is positive, gradient descent update may make us go to other direction, for this case, best epsilon can be found by solving:

$$
\epsilon^* = \dfrac{g^Tg}{g^THg}
$$

When $g$ aligns with eigen vector, it is the worst case and $\epsilon^* = \dfrac{1}{\lambda_{max}}$ .

- In multiple directions, second derivative is different along different directions for a point. Condition number of Hessian at this points measures how much derivatives differ from each other. 
- A poor conditioning number of Hessian means derivatives differ a lot from each other. Which means that going along some directions means fast changes while on other directions, changes are slow.  Gradient descent is unaware of it so it can not explore preferentially in some directions compare to others.  Which makes it hard to find learning rate ($\epsilon$).
- Hessian tells us something about the learning rate? A well conditioned heassian means we can use larger learning rates?

