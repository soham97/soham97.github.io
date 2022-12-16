---
layout: page
title: Making internet safer
description: Detecting toxicity in social media platforms
img: /assets/img/capsuleintro.jpg
importance: 1
category: language
---
<img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/capsuleintro.jpg' | relative_url }}" alt="" title="example image"/>
<div class="caption">
    Social media
</div>

The Internet has enabled people to communicate and learn from each other. Learning from others and at the same time expressing ones feeling and opinions to others requires a consoling and comforting environment. Online hate, abuse, toxicity shuns people from opening up and taking full advantage of the opportunities that online communication provides. This is observable on social media platforms like Facebook, Twitter, and even Quora. A subtle form of toxicity is observed on Quora in the form of insincere questions. Insincere questions are those founded upon false premises, or that intend to make a statement rather than look for helpful answers.

With respect to label taxonomy, each comment can be classified into buckets:
- safe
- insincere
- toxic
- severe toxic
- obscene
- threat
- insult
- identity hate

Kaggle hosted two challenges for detecting online toxicity. The first one in 2018 was organized by [Jigsaw, Google](https://jigsaw.google.com/) and the second in 2019 was organized by [Quora](https://www.quora.com/about). I was a participant in both the challenges: [Google](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge), [Quora](https://www.kaggle.com/c/quora-insincere-questions-classification).

The solution that my team and I developed consisted of a combination of LSTM/GRU/CNN/Boosting architectures with GLoVe/FastText/Paragram/BPE embeddings and a variety of learning strategies. The main challenges we faced were the text length, usage of slang, misspelling, special characters, and innuendos. Hence a lot of effort went into preprocessing the data. I recommend checking out the challenge pages for the solution descriptions. 

The solution we developed was a combination of all of the above. This includes [Recurrent Capsule Networks](https://ieeexplore.ieee.org/abstract/document/8722433). Recurrent Capsule Networks was the best-performing single model across the competition. The insight behind the model was that the internal data representation of a CNN does not take into account important spatial hierarchies between simple and complex objects which in NLP implies that the presence of words will have more impact on the classification rather than their relative orientation to each other. Moreover, we found that integrating RNN with capsule networks provides improved performance in detecting toxic sarcasm and innuendos. 

The architecture was tested on standard benchmark datasets which cover various text classification tasks such as news categorization and sentiment analysis, to demonstrate the generalizability of the model irrespective of the domain.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/capsuletable.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/capsuletable2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    On the left shows datasets used for model evaluate. On the right, are the results on standard datasets. All numbers are AUC ROC scores.
</div>

In recent times, there have been challenges to tackle social media toxicity in multimodal context. If you find this area interesting, the following dataset is a good place to start: [facebook hateful memes challenge](https://ai.facebook.com/blog/hateful-memes-challenge-and-data-set/)



## References
[1] "Tackling Toxic Online Communication with Recurrent Capsule Networks", Soham Deshmukh, Rahul Rade- CICT 2018 <br>
