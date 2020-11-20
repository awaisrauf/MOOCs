# Machine Learning Basics 

[TOC]



- Deep learning is a specific kind of machine learning and :

  > Machine learning is essentially a form of applied statistics with increased emphasis on the use of computers to statistically estimate complicated functions and a decreased emphasis on proving confidence intervals around these functions.

-  A computer program is said to learn from Experience E on class of Task T if it improves on Performance Metric P with the experience. 

- >From a scientific and philosophical point of view, machine learning is interesting because developing our understanding of it entails developing our understanding of the principles that underlie intelligence.  

### Task (T)

A task in ML is how machine learning algorithm should process an example. The process of learning is not task. Learning is the ability to attaining the ability to perform the task T. 

- #### Classification 
  To which category in $k$ categories do an input belong. In other words, we want to learn a function $y=f(x)$: $f: x \in \R^n \to {1,2,..., k}$. The algorithm may output category or distribution over categories. 

- #### Classification with Missing Inputs 
When each part of input vector $x$ is not guaranteed to have at inference time. This often happens in medical diagnosis where it is either expensive or invasive to get all the input. Two possible ways:

	1. learn functions for all the possible missing functions 
	2. to learn probability over all the input variables and then marginalizing it for missing variables

- #### Regression 
	 Prediction of a numerical value for an input: $f: \R^n \to R$

- #### Transcription 
	To convert a relatively unstructured input to structured textual output. For example, OCR: Image to Numbers or Audio to spoken words

- #### Machine Translation 
	Converting an input language to an output language.

- #### Structured Output 
	Where output is vector where elements have relationship between themselves. Example: machine translation, transcription, pixel wise segmentation. 

	>These tasks are called structured output tasks because the program must output several values that are all tightly interrelated. For example, the words produced by an image captioning program must form a valid sentence.  

- #### Anomaly Detection 
	Sifting through the input and finding unusual or atypical behavior. 

- #### Synthesis and Sampling 
	To create examples similar to those in training data. 
	
> This is a kind of structured output task, but with the added qualification that there is no single correct output for each input, and we explicitly desire a large amount of variation in the output, in order for the output to seem more natural and realistic. 

- #### Imputation of Missing Values 
	To predict missing values in input $x\in \R^n$

- #### Denoising 
	To get clean  $x\in \R^n$ from a corrupted input $\tilde{x}\in \R^n$. In other words, to learn distribution $p(x|\tilde{x}) $.

- #### Density Estimation 
	Given training data $\R^n \to \R$, we are required to find $p_{model}$. In this task, we have to learn structure of the data. By learning $p_{model}$, we can, in principle, also tackle other task as well like finding missing values. 
	
	>In practice, density estimation does not always enable us to solve all these related tasks, because in many cases the required operations on p(x) are computationally intractable.

### Performance Measure (P)

Machine learning systems require a performance measure to calculate how well model is doing. For classification, it is accuracy or error rate also called 0-1 loss. In can be different for other tasks. We use a held out set of data (called test) to see performance of a model on unseen data. 

In many tasks it is not very straight forward to measure the performance. For instance, in regression, how should we penalize model output? Then, it depends on the application. 

### Experience (E)

Machine learning algorithms learn from experience which is dataset i.e. examples of the task that we want to learn. In this way, we can divide algorithms into two:

1. supervised where we have both $(x,y)$ i.e. input and and labels, formally, we want to learn $p(y|x)$
2. Unsupervised: Where we only have input i.e. $x$ and we estimate distribution $p(x)$. 

However, lines between both of these are blurry as we can formulate unsupervised task for $\vec{x} \in \R^n$ as following using chain rule;
$$
p(\vec{x}) = \Pi_i^n p(x_i|x_{i-1})
$$
  And  we can use unsupervised learning to learn $p(x,y)$ and use Bayes' Rule for conditional distribution. 
$$
p(y|x) = \dfrac{p(x,y)}{\sum_{\hat{y}} p(x,\hat{y})}
$$
We can describe dataset by  design matrix where each row has one example and each column has one feature. For instance, Iris data contains 150 examples with 4 features so design matrix is: $X\in \R^{150\times 4}$. If all x are not equal in size, we can not represent data as matrix. In that case, we use set notation: $\{x^1, x^2, ...., x^n\}$.

## Capacity, Overfitting and Underfitting 

### Generalization 

In machine learning, we are interested in performance of a model on held out dataset after training on a train set. This is called generalizability of the model - the gap between the train and test error.
$$
\text{generlization} = \text{error}_{train} - \text{error}_{test}
$$


- For generalization, we make i.i.d. assumption about the data that all the data points are independent from each other and sampled from same underlying distribution also called data generating distribution. Both train and test set comes from the same distribution. 
- For a randomly chosen model, expected train and test error are equivalent. 
- For a model being trained, we wish to decrease its training error and gap between training and test error. This arises problem of underfitting and overfitting i.e. model can not decrease train error sufficiently and where a model is unable to reduce the gap. 

Generalizability mainly depends on two things: capacity of the model and number of training examples. 

### Capacity and Generalization 

We can control train and test error by changing capacity of the model. Capacity of a model is difficult to quantify, and it is also limited by many factors like optimization algorithm etc.

- Capacity of a model can be changed  by changing hypothesis space from which optimization function can pick models. 
- The choice of capacity of the model is dependent on both task and number of data points. 
- **Effective capacity** of a model is dependent on hypothesis space as well as the optimization program. 
- Statistical theory provide different ways to calculate capacity of a model. 
- **VC Dimension**: A binary measure, maximum  $m$ for which a model can classify $m$ examples ($x$) arbitrarily. 
- **Statistical Bounds for Justification of ML**:   generalization gap increases with the capacity of a model and shrinks with number of examples. 
- **Limitation in Deep Learning:** Statistical bounds presents a intellectual justification for ml, however they are rarely used in deep learning as it is difficult to calculate capacity. 
- **Occur Razor Principle**: Among the competing hypotheses that explain a phenomenon, we should choose the simplest one. 
- Although simpler models are better, we still need complex enough models that can decrease training error. 
- Error of a ml model 
  <img src="imgs/40.png" style="zoom:75%;" />\

**Non-parametric models** :A model that is dependent on parameters (like weights in linear regression), is parametric model. We can also have non-parametric models. For instance nearest neighbor where we store all the examples and at test time find the $\arg \min ||x - X_{i,:}||p$  i.e. the label of closet example in train set. 

A non- parametric model can get least possible error given the training data. 

**Ideal Model**: Ideal model is an oracle that knows the probability distribution that genrerates the data. It still can have errors due to the noise. This error is called Bayes Error and error of model is bounded by Bayes Error. 

### No Free Lunch Theorem 

Learning theory says that we can generalize well from finite set of examples. This is in contradiction with basic logic because to infer a rule over all members of a set, we need to know each member of the set. The learning theory, however, promises to find rules in probable sense i.e. the rule works for most of members. 

No free lunch theorem of ml describes that : 

> averaged over all possible data-generating distributions, every classification algorithm has the  same error rate when classifying previously unobserved points. In other words, in some sense, no machine learning algorithm is universally any better than any other. The most sophisticated algorithm we can conceive of has the same average performance (over all possible tasks) as merely predicting that every point belongs to the same class.  

**The goal of ml research**

> This means that the goal of machine learning research is not to seek a universal learning algorithm or the absolute best learning algorithm. Instead, our goal is to understand what kinds of distributions are relevant to the “real world” that an AI agent experiences, and what kinds of machine learning algorithms perform well on data drawn from the kinds of data-generating distributions we care about.

### Regularization 

The `No Free Lunch Theorem of Machine Learning` tells us that we should create our algorithms for specific tasks. We do this by aligning our algorithm with the learning task. One way to do is by increasing or decreasing the capacity. However, we can also do it by regularization which is adding a preference in the space of hypothesis functions. 

In general, regularization is any modification in the learning program that reduces generalization error without reducing train error. It can be described as:
$$
J(w) = MSE(w, x) + \Omega(w, x)
$$

> Regularization is one of the central concerns of the field of machine learning, rivaled in its importance only by optimization.  

>The philosophy of deep learning in general and this book in particular is that a wide range of tasks (such as all the intellectual tasks that people can do) may all be solved effectively using very general-purpose forms of regularization.  

## Hyperparameters and Validation Sets

Hyperparameters are the settings that control the behavior of the algorithm. Hyperparameters are often not found using training dataset for two reasons:

1.  are difficult to optimize
2. are difficult to learn from training dataset i.e. finding model capacity hyper parameter from training set means it will always choose maximum value and overfit training data

For hyperparameter optimization, we hold out a part of training set as validation set and use them for the selection of hyperparameter. 

We should not choose hyperparameters from test set. Test set should be used for generalization error. 

> In practice, when the same test set has been used repeatedly to evaluate performance of different algorithms over many years, and especially if we consider all the attempts from the scientific community at beating the reported state-of-the-art performance on that test set, we end up having optimistic evaluations with the test set as well. *Benchmarks can thus become stale and then do not reflect the true field performance of a trained system*. Thankfully, the community tends to move on to new (and usually more ambitious and larger) benchmark datasets  

### Cross Validation 

For small datasets, it is difficult to create a validation set and found true performance. To mitigate this, we can use cross validation which process of using parts of data as train and validation set repeatedly.

 For k-fold cross validation, we partition the data into k-fold, use one set as validation and others as trainset. We repeat this process for k times and find validation error as avg over all k-validations errors. 

## Estimators, Bias and Variance 

### Point Estimator

point estimator is single best prediction of parameter. Given m i.i.d. points, a point estimator or `statistic` is any function of the data as follows:
$$
\hat{\theta}_m = g(x^{(1)}, x^{(2)}, ..., x^{(m)})
$$
Where we assume that $\theta$ is true, fixed and unknown value of it while $\hat{\theta}$ is random variable and an estimate. 

A point estimation of relationship between two variables are often described in terms of **function estimator**:
$$
y = f(x) + \epsilon 
$$
where $\epsilon$ is the part of function that can not be explained based on $x$. 

A function estimator is similar to point estimator in function space. 

### Properties of Estimators 

#### Bias 

Bias is defined as 
$$
bias(\hat{\theta}_m) = \mathbb{E}(\hat{\theta}_m) - \theta
$$
An unbiased estimator: $bias(\hat{\theta}_m) =  0 \implies  \mathbb{E}(\hat{\theta}_m) = \theta$.

An asymptotically unbiased estimator: $\lim_{m\to0} bias(\hat{\theta}_m) = 0$.

#### Variance 

Variance of an estimator is how much we expect the estimator to change as we resample the data from the underlying distribution. It is defined as $Var(\hat{\theta}_m)$. It can also be described as standard error $SE(\hat{\theta}_m)$. 

>The expected degree of variation in any estimator is a source of error that we want to quantify.  

The SE of a mean estimator is given by:
$$
SE(\hat{\mu}_m)  = \dfrac{\sigma}{\sqrt{m}}
$$
We  often use this in machine learning. Since we report  mean estimate of error of ml algorithms, we can compute confidence interval for it. From CLT, we know that mean is normally distributed so we can define 95 % confidence interval of mean as:
$$
\hat{u}_m = 1.96 \pm SE(\hat{\mu}_m)
$$
And we say that an algorithm A is better than B iff, upper limit of confidence interval for A is higher than lower limit of confidence interval of B. 

#### Tradeoff Between Bias and Variance 

How can we deicide between bias and variance? Mean square error is often used for this purpose which has both bias and variance term and reducing MSE decreases both. It is defined as:
$$
MSE(\theta) = \mathbb{E}[(\hat{\theta}_m) - \theta)^2]
\\ = bias(\hat{\theta}_m) - var(\hat{\theta}_m)
$$
Bias and variance tradeoff is tightly linked with generalization and capacity. 

<img src="imgs/41.png" style="zoom:75%;" />

#### Consistency 

We want our estimator to converge to true value as number of data points increases. More formally:
$$
p\lim_{m\to\infty} \hat{\theta}_m = \theta
$$
where $p\lim$ is limit in probability i.e. for any arbitrarily small $\epsilon$, we want 
$$
P(|\hat{\theta}_m - \theta| > \epsilon) \to 0 \text{ as } m \to \infty
$$
it is also called weak consistency. Strong consistency is when above term is equal to 0. 

Consistency means bias introduced by data diminishes as data points increases. However, a unbiased estimator don't have to be consistent. 



## Maximum Likelihood Function 

Where do the estimator come from? One of the method to come up with an estimator is maximum likelihood function.

Suppose that we have i.i.d. data $\mathbb{X} = \{x^1, ...x^m \} \sim p_{data}(x)$  and we want to estimate it with a parametric family of distributions  $p_{model}(x; \theta)$ over a space $\theta$, or in other words we want to estimate $\theta$ given the data. We can formally write it as: 
$$
\theta_{ML} = \arg \max_{\theta} p_{model}(x; \theta)
\\ = \arg \max_{\theta}\Pi_{i=1}^m p_{model}(x^{(i)}; \theta)
\\= \arg \max_{\theta} \sum_{i=1}^m \log p_{model}(x^{(i)}; \theta)
\\= \arg \max_{\theta} \mathbb{E}_{x\sim p_{data}}  \log p_{model}(x; \theta)
$$
Here we have gone from dot product to log of summation because argmax for both are same. 

So we can interpret it as decreasing the discrepancy between model distribution and empirical distribution $p_{data}$ defined by training data. We can also write this objective in terms of KL divergence: 
$$
KL (p_{data} || p_{model} ) = \mathbb{E}_{x\sim p_{data}} [\log p_{data}(x) - \log p_{model}(x; \theta) ]
$$
Since we want to minimize this KL divergence and minimization is not dependent on first term ( since when we are training, we only minimize $p_{model}$), so this becomes minimization of following:
$$
- \mathbb{E} [\log p_{model}(x;\theta)]
$$
 That's why maximum likelihood is also called minimization of negative likelihood. Minimizing log likelihood is exactly equal to minimizing kl divergence between two distributions.
>Any loss consisting of a negative log-likelihood is a cross entropy between the empirical distribution defined by the training set and the probability distribution defined by model. **For example, mean squared error is the cross-entropy between the empirical distribution and a Gaussian model.**  

$\theta$ is same regardless of maximum likelihood or negative log likelihood. 

### Conditional Maximum Likelihood

We can easily extend above mentioned framework for conditional distribution estimation as follows:
$$
\hat{\theta}_{ML} = \arg \max_{\theta} P(Y|X; \theta)
$$

### Properties of Maximum Likelihood

- ML estimator can be showed to be the best estimator asymptotically, as as number of examples increases to infinity in terms of its rate of convergence.
- Under certain conditions, it is consistent i.e $\hat{\theta} \to \theta$ as $m\to \infty$. The conditions are:
  - True distribution $p_{data}$ lie within family of distributions by $p_{model}$
  - True distribution must correspond to exactly one $\theta$ . 
- A way to compute how close we are to real $\theta$ is to compute MSE on data. Cramer Rao bound shows that   maximum likelihood is the best consistent estimator. 





## Stochastic Gradient Descent 

Gradient descent is slow. How? The loss function of ml models is per-class based:
$$
J(\theta) = \mathbb{E}_{(x,y)\sim \hat{p}_{data}} =  L(x,y ; \theta)
\\ = \dfrac{1}{m} \sum_{i=1}^m L(x^{(i)}, y^{(i)}, \theta)
$$
where $L$ is per-class loss function defined as $-\log p(y|x; \theta)$,  gradient becomes:
$$
\nabla_{\theta} J(\theta) = \dfrac{1}{m} \sum_{i=1}^m \nabla_{\theta} L(x^{(i)}, y^{(i)}, \theta)
$$
This makes gradient descent an $O(m)$ complexity algorithm which is computationally expensive. 

**Insight**: offered by Stochastic gradient descent is that gradient is an expectation so we can estimate with small batch size like $\Beta = \{x^{(0)}, ..., x^{(m^{'})}\}$. Therefore, estimate of $g$ becomes:
$$
\vec{g} = \dfrac{1}{m^{'}} \sum_{i=1}^{m^{'}} \nabla_{\theta} L(x^{(i)}, y^{(i)}, \theta)
$$
 and stochastic gradient update becomes:
$$
\vec{\theta} = \vec{\theta} - \epsilon \vec{g}
$$

> The optimization algorithm may not be guaranteed to arrive at even a local minimum in a reasonable amount of time, but it often finds a very low value of the cost function quickly enough to be useful.  

Apart form deep learning, SGD is also used to train linear models with billions of examples. Before that, kernel trick was used which has a cost of $O(m^2)$.

## Building Machine Learning Algorithms

Most deep learning algorithms can be described as having three components:

1. Data i.e. $\bold{X}, y$
2. A model i.e. linear models
3. A cost function i.e. negative log likelihood
4. An optimizer procedure like stochastic gradient descent 

#### Example 1: Linear Regression 

For example, linear regression consists of data $\bold{X}, y$, a cost function like following:
$$
J(\bold{w}, b) = - \mathbb{E}_{X,y \sim \hat{p}_{data}} \log p_{model}(y|x)
$$
Where our model is $p_{model}(y|x) = \mathcal{N}(y;x^Tw+b, 1)$. It is optimized by solving this where gradient is zero and using normal equations. 

> The cost function typically includes at least one term that causes the learning process to perform statistical estimation. The most common cost function is the negative log-likelihood, so that minimizing the cost function causes maximum likelihood estimation.  

Cost function can also include some kind of regularization i.e. 
$$
J(\bold{w}, b) = \lambda ||w||^2_2 - \mathbb{E}_{X,y \sim \hat{p}_{data}} \log p_{model}(y|x)
$$
We can get an analytical solution for this. However, for non-linear cases, it is hard to get close form so we solve it using iterative optimization like gradient descent. 

#### Example 2: Unsupervised Case - PCA 

Similar formulation can also be used for un-supervised case where the data is only $\bold{X}$,  and cost function can be described as:
$$
J(\bold{w}, b) = \mathbb{E}_{X,y \sim p_{data}}||x-r(x)||_2^2
$$
where $r(x) = w^Txw$ is reconstruction function.

If we can not actually evaluate cost function, we can approximate it as long as we have some way of approximating its gradient. 

## Challenges Motivating Deep Learning Research 

 The simple ML algorithms don't succeed in AI tasks such as or recognizing speech or objects. DL is mainly focused on solving these AI tasks. Generalizing to new examples becomes exponentially more difficult in higher dimensions, traditional mechanisms of ML fail to are insufficient to learn complex functions in higher spaces and they often impose higher costs.

### Curse of Dimensionality 

As the number of input dimension increases, so does the possible configurations that this variable can take. This makes generalizing in higher spaces exponentially more difficult compare to smaller dimensions as required data points increases. 

<img src="imgs/42.png" style="zoom:75%;" />

*We have one variable for which we are interested to distinguish 10 regions of interest. In one dimensional example, we need 10 samples, for instance, to compute the value of target. However, in 2D, we need to track 10x10 regions and in 3D, we need 10x10x10. In general, we would require $O(v^d)$ regions and examples for v regions and d dimensions.*

### Local constancy and Smoothness Regularization 

In order to generalize well, ML models are guided by prior believes on what kind of functions they should learn. For instance, we can regularize a model's parameters to bias it to have smaller weights. On such prior is smoothness or local constancy. This can be achieved by multiple ways, however what it requires it to learn a function $f$  that should not change in small region:

$f(x+\epsilon) \approx f(x)$,

i.e. if we know good answer to $f(x)$, it is probably good in the neighborhood of $x$.

For instance, k-nearest neighbor matches input to samples nearest sample in the training. Similarly, kernel methods compute similarity of $k(u, v)$ and tree algorithms divide input space into k leave regions. These kind of algorithm require at least $O(k)$ examples to distinguish $O(k)$ regions in the input space and much more to generalize  well and smoothness becomes important. 

Is it possible to learn a complex function that has many more regions to distinguish than examples? This can not be done via smoothness requirement. And, the function may not be smooth in higher dimensions or it may be smooth in a different ways. So the question is: can we learn a complex function efficiently that generalizes well without requiring for us to have $O(k)$ examples? The answer: yes, in DL we need $O(k)$ samples to distinguish between $O(2^k)$ regions by having some assumptions on data generating distribution and we can generalize non-locally. 

ML algorithms also incorporate other beliefs such as structure etc. However, in higher dimensions, it is much more difficult to incorporate such beliefs manually as these are way more complex. The core assumption in DL: data was generated by composition of may features at multiple level of Hierarchies. 

#### Manifold Learning 

A manifold is connected points. It is defined in terms of neighborhood points of a point. It is locally Euclidian space. In terms of ML, it is set of points for which we can learn without smaller degree of freedom or in lower dimensions.

##### Probability Mass is Highly Concentrated 

If we assume interesting variations along all of $R^n$, then ML algorithms are hopeless. ML algorithms surmount this by considering that interesting data points lie only on collection of manifolds with interesting variations in the output of the learned functions occur only in the directions that lie on the manifold and everywhere else it is invalid inputs. Interesting things happen when we move from one manifold to another. 
<img src="imgs/43.png" style="zoom:75%;" />
*One dimensional manifold in two dimensional space.*

Manifold hypothesis may not be correct always but it is for AI related tasks. We have tow kinds of observations for this hypothesis: 

1.  inputs for AI-related tasks such as images, audios. language etc can not occur at random i.e. uniform noise can never resemble them in practice.  An example is in this sense is that we never see any faces if randomly sample an image from $R^n$ or we don't see any useful sentence if we make them by choosing words at random; 

2. Examples are connected to each other. We can intuitively traverse through a manifold by applying transformation like in images we can apply brightness to get different kinds of coloring etc.

	>In the case of images, we can certainly think  of many possible transformations that allow us to trace out a manifold in image space: we can gradually dim or brighten the lights, gradually move or rotates objects in the image, gradually alter the colors on the surfaces of objects, and so forth.  

If data lies on low-dimensional manifolds, it is better for ML algo to represent the data in terms of coordinates on these manifolds rather than coordinates in the original $R^n$ space.  Like when giving direction of way, we don't give coordinates of 3D space rather coordinates of specific points of the roads. 





