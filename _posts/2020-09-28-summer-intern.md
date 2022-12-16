---
layout: post
title: Summer 2020 at Microsoft
date: 2020-08-20 11:12:00-0400
description: Using machine learning in industry and how that defers from academia.
categories: data-science intern microsoft
---
<p align="center">
<img src="{{site.baseurl}}/assets/img/msft_logo.png" alt="theme"
width="100%"/>
</p>
<br>
I interned at Yammer, Microsoft as Data & Applied Scientist Intern from May 18th to August 7th 2020 at their San Francisco Office. [Yammer](https://en.wikipedia.org/wiki/Yammer) is a social network for workplace specifically aimed at organization-wide communication and comes under the office 365 bundle. The intern situated in California got converted to virtual internship due to COVID-19.

I worked on improving and scaling Yammer’s recommendation model both home feed recommendation and group recommendation models. This involved performing analysis and using the insight from analysis to improving models either from features perspective or data or adding entire new models in the mix. I can’t indulge in the details due to NDA, nor do I want to bore you with the % improvement numbers that work for recruiters. Instead, I thought I would make this about <b><i>using/applied machine learning in industry and how that defers from academia.<b><i> 

In applied machine learning roles, there is also a focus on scalability, latency of deployed models apart from usual goal of improving machine learning models. The below insights are from developing and deploying recommendation models for social platform Yammer.

## 1. Data matters more than the choice of model
Social media sites generate a lot of data, the scale is atleast 100s of TBs. The usual methods of training on entire data are not feasible. So data needs to be subsampled before being fed into the ML model. The type of subsampling you use has a great influence on the performance of the model and can lead to score bloating if incorrect subsampling is used. The type of subsampling to be chosen depends on understanding the product usage and type of recommendations the user wants. For example, the MSFT data is completely different than the EY data on Yammer and there are no interactions between users among those networks. So intelligent heuristic is required to reducing data to be trained on. Similar consideration also applies while prediction. For each user, it’s not possible to evaluate on all the threads, so how do you construct the potential thread pool for evaluation has a great impact on the content being served to users. ‘Garbage-in and Garbage-out’ is a real thing in data science and at every conjunction either at infrastructure or feature engineering or modelling one should make sure that appropriate data is being used both in terms of data distribution and assumptions about data being made.

## 2. Interpretability is important 
Serving recommendations to the users is not the end of the job. Your users will ask why they are seeing XYZ post and debugging would is hell for black box models which lack attribution to data point features. For example: Why users A consistently sees posts about or related to XYZ while he clearly likes posts related to ABC. Having at least some interpretability in the model helps in identifying common bugs at the backend side as well, like some features getting very high importance which might be associated to incorrect joins or data leakage when computing that features and so on. This wouldn’t be possible if we use high performance model which has zero visibility to probe into it.  Generally, this boils down to tradeoff between interpretability and performance of the model. Rule of thumb, choose interpretable models anytime over a model which gives slightly better scores but is entirely blackbox. 

## 3. Infrastructure can support or hinder		 
The type of models you can build will be restricted to available infrastucture. This is due to obvious reasons like though you want to serve the best threads/content possible to users, however each request needs to have ceiling latency and should not blow the dollar roof due to excessive syncing between predictions and training. Hence, the type of infrastructure you have plays a major role in deciding the model and what can go into production. So I definitely recommend looking into the infrastructure side of things to appreciate what they do and also there are quick gains to be made in modelling by doing some quick changes at the infrastructure side. Some major choices I have seen here are whether to go with batch predictions or near real-time architecture, syncing times between training and predictions and so on. There are many articles on infrastructure design choices and there subsequent downstream impacts and they are worth looking into.

## 4. Results should be reproducible
In academia, the main focus is building machine learning models to achieve benchmark performance. Sometimes, this leaves model reproducibility in back seat. THowever, in industry, you want the results of the model developed to be absolutely reproducible and should be able to consistently produce high performance in production. This ensures consistent monetary gains for the company and more importantly it builds confidence in customers to get consistent relevant content served by Yammer. The two pillars of reproducibility and reproducibility should be enforced throughout the ML system right from data logging, ETL, generating features, model training to generating predictions. In real-time systems like Yammer, there is another problem of data drift and how validation data might not represent the current real-time stream data. It's a topic for another day I guess 😄 

## 5. Documentation
Having good documentation about the infrastructure, models and analytics side of things will determine the velocity of the team. Ideally, you want documentation with every A/B test and experiment that was tried, what they did, whether they failed or succeed and then a post-dive in of possible why it didn’t succeed. Thought this increases time in the short run but in the long run you would look back and see this as the best thing you invested in. Also it helps setup new employees and interns for success and quicker onboarding.

## 6. Final thoughts
I had a great time learning about what goes into productionising ML models and seeing your deployed model positively impact 15M monthly active users is an experience in itself. Another thing I would like to add here is that the ML models form only a small part of the whole ML infrastructure, and a data scientist should also focus on ‘adding business value and improving customer experience’ rather than focusing only on building bigger and complex ML model.
