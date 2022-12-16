---
layout: page
title: SED in the wild
description: Sound event detection in noisy environments
img: /assets/img/livingroom2.jpg
importance: 1
category: audio
---
Sound event detection aims at processing the continuous acoustic signal and converting it into symbolic descriptions of the corresponding sound events present in a natural environment. 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/hospital.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/livingroom2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    On the left, is a operation room in the hosital and on the right is a living room in a house. Both environment scenes are filled with variety of sounds associated with different event happening.
</div>

<i>Look at the two scenes depicted in the above image, what kind of sounds do you imagine listening in each scene ? </i>

The hospital environment is probably filled with people rushing, instruments clanking, beeping noises, and on the other hand the living room will be filled with tea cups clicking, laughter, TV, maybe someone decided to play the guitar kept in the room. Each environment is filled with a set of rich sounds. These set of sounds can provide information atleast about the event occuring in the scene if not more about the mood, setting etc. Sound event detection system aims to infer this information from such acoustic scenes. Needless to say, it has variety of applications in context-based indexing, retrieval in multimedia databases, unobtrusive monitoring in health care, surveillance and makes product like Amazon echo, Apple home intelligent.

#### Sound event detection in the wild is difficult
- <i>Training data does not represent inference distribution</i>: Sound event detection systems are generally trained on clean data where each audio file contains single or couple events with no background environmental noise. However, when the systems are deployed, they have to make inference in noisy environments like train stations, airports, city etc. 
- <i>Specific applications</i>: Data collected for applications like predicting Remaining Useful Life (RUL) of machines in factories is filled with background factory noises and irrelevant sounds. Getting new data is not only difficult but the collected data will always be noisy.

So in our recent works [1][2] we try to address
#### How to train better SED systems in and for noisy environments with limited data ?

In our experiments we train and evaluate on noisy data. An example of random audio sample from data:

<div class="row">
    <audio controls>
      <source src="/assets/audio/06031_snr0.mp3" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    <div class="caption">
    SNR 0 dB
    </div>
    <audio controls>
      <source src="/assets/audio/06031_snr10.mp3" type="audio/mp3">
    Your browser does not support the audio element.
    </audio>
    <div class="caption">
    SNR 10 dB
    </div>
    <audio controls>
      <source src="/assets/audio/06031_snr20.mp3" type="audio/mp3">
    Your browser does not support the audio element.
    </audio>
    <div class="caption">
    SNR 20 dB
    </div>
</div>
<div class="caption">
    The audio contains sound of drum, coughing and trumpet in real life street setting. The three clips have different Signal to noise ratio (SNR), with SNR 20 db being the cleanest and SNR 0 dB with most noise.
</div>

In our work [1][2], we tackle this from two supplementary approaches:
- <i> Learning better representations/feature detectors </i> for each audio event from such noisy training data. And we learn better representations by using self-supervised auxiliary tasks to aid the primary task of sound event detection. These tasks (eg: mel spectrogram reconstruction) forces the neural network to learn robust representation containing consistent information.
- <i> Improving pooling method used in these networks. </i> We develop two step attention pooling which is interpretable and robust to such noisy training data.

In brief, the networks architecture is as follows:

<img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/mtl.jpg' | relative_url }}" alt="" title="example image"/>
<div class="caption">
    Our proposed self-supervised learning assisted framework for weakly supervised sound event detection. Left figure: the general
    architecture with shared encoder and multiple decoder branches. Shared encoder, primary decoder, auxiliary decoder is represented by g, g2, g4 respectively. Right figure: shows the two step attention pooling function used for primary decoder
</div>

The proposed architecture when evaluated on test data, beats existing benchmarks by 22.3%, 12.8%, 5.9% on 0, 10 and 20 dB SNR
respectively. The performance gains are highest when training data is very noisy (0 dB SNR)

<img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/mtlresults.jpg' | relative_url }}" alt="" title="example image"/>
<div class="caption">
    Sound event detection performance across different SNR
</div>

If you are interested in learning more about Sound event detection, this [reading list](https://github.com/soham97/awesome-sound_event_detection) is a good start.

## References
[1] "Multi-Task Learning for Interpretable Weakly Labelled Sound Event Detection", Soham Deshmukh, Bhiksha Raj, Rita Singh- MS graduate report, [arXiv:2008.07085](https://arxiv.org/abs/2008.07085)

[2] "Improving weakly supervised sound event detection with self-supervised auxiliary tasks", Soham Deshmukh, Bhiksha Raj, Rita Singh- INTERSPEECH 2021, [arXiv:2106.0685](https://arxiv.org/abs/2106.06858)