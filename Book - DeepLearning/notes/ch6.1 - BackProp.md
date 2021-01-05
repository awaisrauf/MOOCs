## Backpropagation and Other Differentiation Algorithms 

- **Forward Propagation** is to give neural network input $x$, propagate it through hidden units until it produces a scalar cost $J(\theta)$. **Backward Propagation (backprop)** is flow of information from cost back to input to compute gradients. A learning algorithm -- like stochastic gradient descent -- can use these gradients to update parameters for learning. This gradient can also be used for any other purposes other than learning as well.
- **Analytical Gradient** computation is straightforward but computationally expensive.  Backprop is simple and inexpensive in comparison. 
- Backprop can compute gradient of any function $\nabla_x f(\vec{x}, \vec{y})$  where $x$ is variable whose derivate is desired and $y$ is an additional set of variables whose derivative can be computed but not desired. Backprop through a network is very general and can be used to compute values such as the Jacobian of a function. 

### Computational Graphs 

- For backprop, we need to think of a network as a computational graph. 
  - Each node in the graph is a variable (scalar, vector, matrix, tensor or even any other type).
  - **Operation** is a simple function of one or more variables (functions, on other hand, can have multiple operations as well). We have a set of allowable variables.  For the sake of simplicity, here we are define an operation to return a single output variable. 
  - If a variable $y$ is computed by applying an operation to a variable $x$ then we draw an edge from $x$ to $y$. 

<img src="C:/Users/Awais/Documents/Huawei/MOOCs/Book - DeepLearning/notes/imgs/52.png" style="zoom:75%;" />

### Chain Rule of Calculus 

- With chain rule, we can compute derivate of functions formed by composing other functions whose derivative is known. Specifically, assume $x \in \mathbb{R}$ and $f, g$ be to functions that map a real number to a real number and $y=g(x)$, $z = f(y)$, then we can compute $\dfrac{dz}{dx}$ with following:
  $$
  \dfrac{dz}{dx} = \dfrac{dz}{dy}.\dfrac{dy}{dx}
  $$

- **Generalization Beyond Scalar**: Let $x \in \mathbb{R^m}$ , $y \in \mathbb{R^n}$ and $g: \mathbb{R^m} \to \mathbb{R}^n$ and $f: \mathbb{R^n} \to \mathbb{R}$, and $y = g(x)$ and  $z = f(g(x))$ then,
  $$
  \dfrac{dz}{dx_i} = \sum_{j=0}^n \dfrac{dz}{dy_j} . \dfrac{dy_i}{dx_i}
  $$
  and in vector notation, 

  

$$
\nabla_\bold{x} z = \bigg(\dfrac{\partial \bold{y}}{ \partial \bold{x} }\bigg)^T \nabla_{\bold{y}} z
$$

​		where $\dfrac{\partial  \boldsymbol{y}}{ \partial \boldsymbol{x} }$ is $n \times m $ Jacobian matrix of $g$. 

- This way,  can compute gradient of any variable w.r.t. $x$ by multiplying Jacobian matrix by gradient. 

- **Generalization to Three Operations**: 

  - Lets assume that $$ \boldsymbol{x} \in \mathbb{R}^n$$, $ \boldsymbol{y_1},  \boldsymbol{y_2} \in \mathbb{R}^{m_1}, \mathbb{R}^{m_2}$ and $z \in \mathbb{R}$ 
  - $ \boldsymbol{y}_1 = f_1( \boldsymbol{x})$, $ \boldsymbol{ \boldsymbol{y}_2} = f_2( \boldsymbol{y_1})$ and $z = f_3( \boldsymbol{y_2})$ and the  overall model is:

  $$
  z = f_3(f_2(f_1( \bold{x})))
  $$

  The derivative:
  $$
  \dfrac{dz}{dx_i} = \sum_{k=0}^{m_2} \sum_{j=0}^{m_1}  \dfrac{dz}{dy_2^{j}} . \dfrac{dy_2^{j}}{dy_1^{k}} .\dfrac{dy_1^{k}}{dx_i} \\ 
  \nabla_{\bold{x}} z = \bigg( \dfrac{\partial \bold{y_2} }{\partial \bold{y_1} } \bigg)^T . \bigg( \dfrac{\partial \bold{y_1} } {\partial \bold{x} } \bigg)^T \nabla_{\bold{y_2}} z
  $$

- BP is now applying this kind of chain rule to all the operations of a computational graph. 

- **Generalization to Tensor**: 



### Recursively Applying the Chain Rule to Obtain Backprop

- Chain rule to write simple algebraic expression for scalar w.r.t any node of the graph is easy, however, evaluating it in computer is need extra considerations. 

- Many expressions are repeated, we need to decide whether to store them or re-compute several times. Storing them would increase memory size and re-computing them would cost extra computation.  Following is an example:

  <img src="C:/Users/Awais/Documents/Huawei/MOOCs/Book - DeepLearning/notes/imgs/53.png" style="zoom:60%;" />

  Suppose that we want to compute $\dfrac{\partial z}{\partial w}$.  The output node is connected with input via following way: $z = f(f(f( w )))$ i.e. $f: \mathbb{R} \to \mathbb{R}$ is used three times or in other words:
  $$
  z = f(y) \\
  y = f(x) \\
  x = f(w)
  $$
  we can compute its gradient via following: 
  $$
  \dfrac{\partial z}{ \partial w} \\ 
  =\dfrac{\partial z}{ \partial y} . \dfrac{\partial y}{ \partial x} \\
  =\dfrac{\partial z}{ \partial y} . \dfrac{\partial y}{ \partial x} . \dfrac{\partial x}{ \partial w} \\
  = f'(y) . f'(x) . f'(w) \\
  = f'(f(f(w))) . f'(f(w)) . f'(w)
  $$



```pseudocode
for i={1, ..., n} do
	u^{i} <- x_i
	

```

