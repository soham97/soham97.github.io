---
layout: page
title: Audio concepts from language
description: Learning audio concepts from natural language supervision
img: /assets/img/clap_applications.jpg
importance: 1
category: audio
---
[Audio Analytics](https://www.microsoft.com/en-us/research/project/audio-analytics/) focuses on analyzing and understanding audio signals. This technology has a variety of applications in context-based indexing, retrieval in multimedia databases, unobtrusive monitoring in health care, surveillance, and makes products like Amazon Echo, and Apple home intelligent.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/clap_applications.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    Applications of audio analytics technology
</div>

The north star goal of the audio analytics technology is to achieve human ear understanding and performance. To achieve this goal, the mainstream Machine Learning (ML) approaches for audio understanding break the human hearing into smaller tasks such as sound event detection, acoustic scene classification, emotion recognition, etc. Creating ML models for the smaller task requires defining a unique label ontology, followed by data collection and model training phase. This time-consuming process has to be repeated for each task. 

Therefore in our recent work [1], we ask the question *"Can we learn audio concepts directly from natural language supervision?"*. We introduce Contrastive Language-Audio Pretraining (CLAP :clap:), which learns to connect language and audio by jointly learning a multimodal space using contrastive learning. 

The benefits of the proposed natural language learning supervision are:
- **Foundation Model.** This learning framework allows the training of a foundation audio model for audio for a large web corpus of audio-text pairs. The trained foundation model can then power multiple downstream audio tasks with little or no finetuning on the target domain. An equivalent example of such models can be found in the field of computer vision (Open AI CLIP, Microsoft Florence) and language (BERT, PaLM, GPT3) 
- **Zero-Shot capability.** The current large-scale pre-trained models still require an additional layer of finetuning on the target dataset. This includes Self-Supervised Learning (SSL) models for Speech and Audio. However, CLAP does not require the additional step of finetuning required on the target dataset. The model enables Zero-Shot (ZS) predictions and takes input audio and yields a prediction score for any class typed by the user.

To show the potential of audio-text supervision we collect 128k audio-text pairs from audio captioning and sound event datasets. Some examples of what the audio-text pairs look like are below:
<div class="row">
    <audio controls>
      <source src="/assets/audio/Media1.mp3" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    <div class="caption">
    String instrument playing one tone repeatedly before voilin joins to create melody
    </div> <br>
    <audio controls>
      <source src="/assets/audio/Media2.mp3" type="audio/mp3">
    Your browser does not support the audio element.
    </audio>
    <div class="caption">
    An insect buzzing in the foreground as birds chirps in the background
    </div>
    <audio controls>
      <source src="/assets/audio/Media3.mp3" type="audio/mp3">
    Your browser does not support the audio element.
    </audio>
    <div class="caption">
    A campfire crackles as the flame burns branches and leaves
    </div>
</div>
<div class="caption">
    Three randomly sampled audio-text pairs
</div>

For training, CLAP jointly trains an audio and a text encoder to learn the (dis)similarity of audio and text pairs in a batch using contrastive learning. At testing time, the pretrained encoders are used to extract audio embeddings from the testing audio and text embeddings from the class labels. Zero-Shot linear classification is achieved by computing cosine similarity between the embeddings. 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/clap.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    Training and Zero-Shot evaluation of CLAP
</div>

Once CLAP is trained, it can be used to provide Zero-Shot inference in a few lines of code. We evaluate CLAP's ZS performance across 16 datasets from 8 domains as downstream tasks. We also evaluate CLAP in the traditional supervised setup on the downstream dataset. This traditional setup is shown as *CLAP (Best)* in the table below:
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/clap_zs.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    CLAP (ZS) Zero-Shot outperforms the literature. CLAP (Best) is the best performance among our supervised setups.
Higher is better for all numbers, DCASE17 employs F1, FSD50K and AudioSet employs mAP, everything else uses accuracy
</div>

The paper [1] covers the analysis of results, ablation studies for training, and the effects of prompt tuning.

Overall, CLAP shows excellent promise. I am personally excited to see the upcoming research in this direction and the emergence of new audio applications powered by such models.

Twitter conversations about CLAP:
{% twitter https://twitter.com/_akhaliq/status/1536495422683893765 %}

## References
[1] Benjamin Elizalde, Soham Deshmukh, Mahmoud Al Ismail, Huaming Wang, "CLAP: Learning Audio Concepts from Natural Language Supervision," ArXiv 2022

