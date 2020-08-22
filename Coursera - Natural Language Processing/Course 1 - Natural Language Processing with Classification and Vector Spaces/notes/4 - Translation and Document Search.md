# Translation and Document Search 

### Translation 

Translation from one language is to

1. make word embeddings of both languages
2. Find a a way to transform embedding of first language to second language
3. find a word that has closet embedding to this transformation

<img src="imgs/9.png" style="zoom:75%;" />

Mathematically, let's say that $X$ is embeddings of sentence in the first language, $Y$ is embedding that we wish to find and $R$ is a transformation matrix, then we wish to find a transformation matrix $R$ such that $XR \approx Y$. In other words, we want to minimize $||XR-Y||_F^2$. 

- K-nearest neighbors can be used to find closed words from one language to another. 

### Hash Tables

Hash tables are a way to store items in buckets. In Hash tables, first create a formulation to find place for each input and then based on this formulation, we store numbers in different buckets.
<img src="imgs/10.png" style="zoom:75%;" /> 



- To decrease computation requirement of K-Nearest Neighbor, we use Hash Tables. To create a hash table that stores similar inputs in same bucket, we use locality sensitive hashing. 

  > Multiplanes hash functions are based on the idea of numbering every single region that is formed by the intersection of n planes.

- **Locality Sensitive Hashing**: In this type of hasing, we use dot product with given planes to find sign of a vector and then combine these to find a hash value as shown below:
  <img src="imgs/11.png" style="zoom:75%;" />



- **Approximate Nearest Neighbors **: Use hash tables with random planes to find hash value and it will be an approximate nearest neighbors. 
- **Document Search**: We can use this method for document search. We can represent each document as sum of words embeddings it contain. 