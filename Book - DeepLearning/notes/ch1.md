# Chapter 1: Introduction 

### Challenge for AI

- Computers easily solved many problems that were intellectually difficult for humans but straightforward for humans.
- Computers can't easily solve problems that are easy for humans to do but hard to formally describe. 
- Solution: To learn from experience by building hierarchy of concepts so that humans don't have to formally describe them. 

### Types of AI

 There are two ways of AI: hardcoded where knowledge is hardcoded by humans and machine learning where computer learn from experience i.e. patterns from raw data. 

![](imgs/1-3.png)

### Representation of Input data

-  Machine learning algorithms are heavily influenced by the representation of the data. There are two ways for this: either hardcode features of input and give it to algorithm or design an algorithm that first learns how to represent the data (automatically learns features).

- > Many artificial intelligence tasks can be solved by designing the right set of
  > features to extract for that task, then providing these features to a simple machine
  > learning algorithm  For many tasks, however, it is difficult to know what features should be extracted.  

### Representation Learning

- In feature design, **our goal is to separate the factors (sources of influence) of variation that explain the observed data**. We want to disentangle factors of variation and discard ones that are not useful.

  >we use the word “factors” simply to refer to separate sources of influence; the factors are usually not combined by multiplication. Such factors are often not quantities that are directly observed. Instead, they may exist as either unobserved objects or unobserved forces in the physical world that affect observable quantities.
  > They may also exist as constructs in the human mind that provide useful simplifying
  >explanations or inferred causes of the observed data. They can be thought of as
  >concepts or abstractions that help us make sense of the rich variability in the data.  

  > A major source of difficulty in many real-world artificial intelligence applications
  > is that many of the factors of variation influence every single piece of data we are
  > able to observe. The individual pixels in an image of a red car might be very close
  > to black at night. The shape of the car’s silhouette depends on the viewing angle.
  > Most applications require us to disentangle the factors of variation and discard the
  > ones that we do not care about.  

- Deep learning solves the problem of representation by learning hierarchy of concepts in sequential manner.

  >Deep learning solves this central problem in representation learning by introducing representations that are expressed in terms of other, simpler representations. Deep learning enables the computer to build complex concepts out of simpler concepts.   

  

### Progress in Deep Learning

- Dataset sizes are increasing:
  ![](imgs/1-4.png)

- Progress of deep learning is driven by many factors like larger datasets, big models etc. However, even the largest models are smaller than even very small animals. 

- Many parts of deep learning are influenced or motivated by research in neuroscience but neuroscience is not main influencer now. 

- ANNs have smaller number of neurons compare to even small animals but much higher number of connections per neurons compare to even larger animals like humans as shown in following figures. 

  ![](imgs\1-1.PNG)![](imgs\1-2.PNG)
  
