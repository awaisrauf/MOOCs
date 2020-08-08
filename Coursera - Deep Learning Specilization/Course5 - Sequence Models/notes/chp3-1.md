## Sequence Models

*For more details: see `1- Neural Machine Translation with Attention.ipynb` in code section.*

- Translate one sentence to other: This is a book.. --> Ya Aik Kitab ha
- Seq2Seq Model: First use a model to get representations and then use another network to get output result. [1, 2]
  ![](imgs/3-1.png)
- Similar architecture also works on image translation 
  Get a latent representation via a CNN ==> give it to an RNN [3, 4, 5]

#### Picking up Most likely sentence 

- Machine translation can be think of as a conditional language model: Find most likely y sentence given x sentence where we get representation of x via an encoder.  
  $P(y^{<1>},..., y^{<n>} | x^{<1>},..., x^{<m>} )$

  - In simple language model, we use random initialization instead on encoder. 

- Model gives most probable output sentences. How to sample good translation from it? Random sampling would not help.
  Solve following:
  $$
  argmax_{y^{<1>},..., y^{n}} P(y^{<1>},..., y^{n}|x) 
  \\ =argmax_y \prod P(y^{<t>} | x, y^{<1>},...., y^{<t-1>})
  $$
  
- **Why not use Greedy Search**: Pick first most likely word then second then third and so on. It does not work because most likely words may not be very useful and targets words in dictionary are large. 

### Beam Search 

- Given a input sequence, find most likely output sequence. 

  1. Give input sequence to encoder and get representation

  2. Input this representation to decoder and get SoftMax output of all possible words and keep $B$ (beam width) most likely words

  3. For each choice in step 1, give decoder fist word and find 
     $$
     P(y^{<1>}, y^{<2>}|x ) = P(y^{<1>}|x ) . P( y^{<2>}|x, y^{<1>} )
     $$
     

     where $P(y^{<1>}|x )$ is output in first step 2 and  $P( y^{<2>}|x, y^{<1>} )$ is output of decoder at current time.

  4. Do step 3 for all B words selected in first step. There will be $B\times len((vocab))$ possibilities.  Again, Select B most likely choices from it.

 ### Refinements in Beam Search 

1. **argmax log**: maximizing product as shown below means multiplying many small numbers. But we can take log of it which will make it finding y that maximizes sum instead multiply.
   $\mathrm{argmax_y} \prod P(y^{<t>} | x, y^{<1>},...., y^{<t-1>})$ is equitant to $\mathrm{argmax_y} \sum_{t=1}^{T_y} log P(y^{<t>} | x, y^{<1>},...., y^{<t-1>})$

2. **Normalize**

    $  score = \dfrac{1}{T_y^\alpha} \mathrm{argmax_y} \sum_{t=1}^{T_y} log P(y^{<t>} | x, y^{<1>},...., y^{<t-1>})$

   where $\alpha=0.7$ works well for practice. 

* **Final Sentence**: How to find $T_y$ or length of sentence. Find sentences of $T_y=1,2,3,...,30$, find probability score with above equation and select with highest probability. 
* **Practical**: Large B means better sentence but more expensive. B=10 is common but in industry B=100, 1000, 3000 can also be seen but returns are diminishing. 

### Error Analysis in Beam Search 

What is causing error? Beam Search or RNN?

- Lets assume translation then 

  - Human : $y^*$
  - Algorithm:  $\hat{y}$

- Compute $P(y^*|x) $ and $P(\hat{y}|x)$ see which is bigger?
  **Case 1**: $P(y^*|x) >  P(\hat{y}|x)$ ==> Beam Search is at fault

  **Case 2**: $P(y^*|x) \leq  P(\hat{y}|x)$ ==> RNN is at fault
  <img src="imgs/3-2.png" style="zoom:75%;" />

  If B is more at fault: get better B other work on RNN more. 

### Bleu Score [6]

How to evaluate answers what output is good? 

 https://en.wikipedia.org/wiki/BLEU



### Attention Model Intuition 

Translation of long sentences is hard because neural  network have to memorize the sentence. This makes long sentence hard. 

Attention module is  a way to assign importance to parts of input sequence while generating current part of output sequence. For instance, to generate translation of a sentence "This is a book.", first word of output translation should give more importance to This than book. 

- For decoder, at each word of the sentence, produce a hidden state and an attention which is based on input sentence. 

### Attention Model 

- **Encoder Decoder**: 
  Input --> Encoder --> Representation --> Decoder --> Output 
  **Attention**:
  Input --> Encoder --> Representation --->
  						|                                           ------>  Decoder --> Output
                   Attention  ---------------------------->  

- In attention module, encoder generates a representation as well activations for each part of input sequence. Decoder takes both the representation and weighted sum of activations to generate output sequence. 
  ![](imgs/3-3.png)

- Encoder-Decoder with Attention
  ![](imgs/3-6.png)

- Attention module
  <img src="imgs/3-7.png" style="zoom:60%;" />

- Attention is calculated as follows:
  $$
  c^{<t'>} = \sum_{t'} \alpha^{<t, t'>} a^{<t>}
  $$

  - $\alpha^{<t, t'>}$: weight for the t-th word in input sequence to generate t'-th word in output sequence.  
  - $c^{<t'>}$: context or attention to generate $t'$ output word. 
  - $a^{<t>}$: activation for word t generated by encoder.

- Weight for each activation or attention is calculated as follows:
  $$
  \alpha^{<t, t'>} = \dfrac{exp(e^{<t, t'>})}{\sum_{t'=1}^{T_x} exp(e^{<t, t'>})}
  $$
  where $e^{<t, t'>}$ is generated by a small neural network with gradient descent. 
  ![](imgs/3-4.png)

- This has quadratic cost.
- Visualization of attention:
  <img src="imgs/3-5.png" style="zoom:75%;" />







#### References 

1. Sequence to Sequence Learning with Neural Networks 
2. Learning phrase representations using RNN encoder-decoder for statistical machine translation 
3. Deep Captioning with multimodal recurrent neural nets
4. Show and tell: Neural Image Caption Generator 
5. Deep Visual Semantic alignments for generating image descriptions.
6. **Readable Important Paper**: A method for automatic evaluation of machine translation 
7. **Influential**: Neural Machine Translation by jointly learn to align and translate 
8. Show Attend and tell: Neural image caption generation with visual attention

