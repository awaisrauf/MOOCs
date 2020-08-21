# Week 1: Welcome to NLP

### How to represent words 

Sentence: [W1, W2, W3, ... Wn]

1. **One Hot**: Each word as one-hot vector, each word's dim = Vocab size

2. **Frequency based** : Count appearance of each word in the data. 

   ![](imgs/1.png)

      Representation: NegFreq of words appearing in class 1, ...n
   	![](imgs/2.png)

   ### Preprocessing 

   1. Remove Stop Words
   2. Stemming: Convert words to their roots 
   3. Lowercase

   ### Logistic Regression 

   $$
   h(x, \theta) = \dfrac{1}{1+e^{-\theta x}}
   $$

   

# Week 2: Naive Bayes 

- It uses Bayes Rule

$$
P(y|x) = \dfrac{P(x|y)P(y)}{P(x)}
$$

- This is how we will calculate conditional probabilities: 

  <img src="imgs/3.png" style="zoom:75%;" />

- Applying Naive Baye's: Finding ratio of conditional probabilities. 
  <img src="imgs/4.png" style="zoom:75%;" />

- **Laplacian Smoothing **: To avoid zeros and thereby probability being zero, we add 1 for each frequency.
  <img src="imgs/5.png" style="zoom:75%;" />
-  To avoid numerical unstability, we use log: 
  <img src="imgs/6.png" style="zoom:75%;" />
- 