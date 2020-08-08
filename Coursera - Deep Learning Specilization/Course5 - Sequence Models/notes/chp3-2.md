# Speech Recognition 

Deep learning have made very accurate speech recognition. 

*See Trigger Word Detection Notebook for code details.*

- Task: Given a audio clip ---> Generate transcript

  - Audio clip is a measure of sound pressure
  - First converted into spectrogram

  ![](imgs/3-8.png)

- In old times, audio was represented with phenomes (hand generated) which is not required in deep learning. 

### What really is an audio recording? 

>What really is an audio recording? 
>
>- A microphone records little variations in air pressure over time, and it is these little variations in air pressure that your ear also perceives as sound. 
>
>- You can think of an audio recording is a long list of numbers measuring the little air pressure changes detected by the microphone. 
>
>- We will use audio sampled at 44100 Hz (or 44100 Hertz). 
>  - This means the microphone gives us 44,100 numbers per second. 
>  - Thus, a 10 second audio clip is represented by 441,000 numbers (= $10 \times 44,100$). 
>
>Spectrogram
>
>- It is quite difficult to figure out from this "raw" representation of audio whether the word "activate" was said. 
>- In  order to help your sequence model more easily learn to detect trigger words, we will compute a *spectrogram* of the audio. 
>- The spectrogram tells us how much different frequencies are present in an audio clip at any moment in time. 
>- If you've ever taken an advanced class on signal processing or on Fourier transforms:
>  - A spectrogram is computed by sliding a window over the raw audio signal, and calculating the most active frequencies in each window using a Fourier transform. 
>  - If you don't understand the previous sentence, don't worry about it.
### Connectionist temporal classification

- Steps:

  1. Use an RNN with equal input and output size. 

  2. In output, repeat many words

  3. Collapse all the words that are not separated by blank.

    ![](imgs/3-9.png)

### Trigger Word Detection 

- Trigger words: detect whether a specific triggered word was uttered. Example: Alexa
- Labels: 0 for before and after trigger words and 1 for trigger words
  ![](imgs/3-10.png)
- Use multiple 1s and 0s instead of only one. 

### References 

1. Connectionist temporal classification labelling unsegmented sequence data with recurrent neural networks 