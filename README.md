# Movie Genre Prediction
Movie Genre Prediction kicked-off as a final project in the [Le Wagon coding bootcamp](https://www.lewagon.com/tokyo/data-science-course). After the bootcamp, I decided to fork the project and explore other methods to combine machine learning models on multimodal models.

Huge credits to my teammates who worked extremely hard for this project! Would not have finished the project in time for the presentation without their hard work!

### Teammates during bootcamp
* [Jess](https://github.com/chooj202)
* [Yinghui](https://github.com/yinghuing)

#### -- Project Status: Active

## Introduction

### Methods Used
* Data Engineering with GCP
* Inferential Statistics
* Machine Learning
* Predictive Modeling

### Technologies
* Pandas, Tensorflow
* Matplotlib
* Google Cloud Platform (GCR, GCS, Compute Engine etc.)
* FastAPI and Streamlit

### Background
There are **two** ways to look at the background of Movie Genre Prediction.

**Business side:**
* Movie distributors such as Warner Bros. distribute their movies without genres tagged. In turn, streaming platforms such as Netflix and Disney+ has to hire "movie experts" to tag the genres. To reduce this long and mundane chore, we decided to explore the possibilities of using Machine Learning to predict the genres.

**Technical side:**
* Pre-trained Neural Network models such as BERT and ResNet-50 showed remarkable results on identifying features of text and images respectively. And with the rise of these models, numerous researchers has started experimenting on combining these models into one huge model, a multimodal model. Movie Genre Prediction also explores this new field by using movie genres as a target.


### Description
Movie Genre Prediction aims to predict movie genres only by its **Poster** and **Synopsis**. Therefore, fundamentally, Movie Genre Prediction is a **multimodal multilabel classifier**. Multilabel classifiers inherently comes with challenges such as unbalanced dataset and high target dimensionality. Similarly, multimodal models also comes with challenges as there is no clear way to best combine these models and is computationally demanding. Hence, Movie Genre Prediction aims to explore and compare the various ways of intergrating independent models while building a cohesive data pipeline to support the computational challenges.

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*

3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*

5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](link)
* [Notebook/Markdown/Slide DeckTitle](link)
* [Blog Post](link)


## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).
* Our slack channel is `#datasci-projectname`
* Feel free to contact team leads with any questions or if you are interested in contributing!
