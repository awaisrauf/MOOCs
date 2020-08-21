# Week 3: Vector Space Models

- Represent words as vectors using the principle "You shall know a word by the company it keeps."

- Co-occurence --> Vector Spaces 

- Co-occurance:

  - <u>Word by word design</u>: Number of times a word occur within a specific distance to another word words.
    <img src="imgs/7.png" style="zoom:75%;" />

  - <u>Word by Document</u>: Num of times a word occur in a document.

    ​			    Cat1          Cat 2           Cat 3
    Word1    200           300               399

    Word2    x                y                    z

    We get three vectors from above: [200, x], [300, y] and [399, z]

- Norm can measure distance in this vector space

- Angle between two vectors (cosine simillarity) can tell how a two vectors are directed and how similar two vectors are. 

- Meaningful manipulations in vector spaces of words
  <img src="imgs/8.png" style="zoom:75%;" />

- PCA to see data in lower dimensions. 

  1. Find uncorrelated features and reduce dimension

-  



### References 

Distributed Representations and phrases and their compositionality 

