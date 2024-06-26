# Movie Genre Prediction
Movie Genre Prediction kicked-off as a final project in the [Le Wagon coding bootcamp](https://www.lewagon.com/tokyo/data-science-course). After the bootcamp, I decided to fork the project and explore other methods to combine machine learning multimodal models.

Huge shoutout to my teammates who worked extremely hard for this project! Would not have finished the project in time for the presentation without their hard work!

### Teammates during bootcamp
* [Jess](https://github.com/chooj202)
* [Yinghui](https://github.com/yinghuing)

#### -- Project Status: Frozen

## System

<img width="690" alt="Screenshot 2024-05-11 at 22 25 59" src="https://github.com/howarudo/movie_genre_prediction/assets/125206676/019b88db-9e76-40e2-8d4d-72e406392dd8">

## Demo

https://github.com/howarudo/movie_genre_prediction/assets/125206676/f6dd0ec3-c1d4-47a0-97c2-a8cc9cc26944

[Video Link In Case Broken](https://drive.google.com/file/d/1ivuj_g4kCCkYvMpdKAxmFdSXPXiTCT1n/view?usp=sharing)

## Introduction

### Methods Used
* Data Engineering with GCP
* Inferential Statistics
* Supervised Machine Learning
* Predictive Modeling

### Technologies
* Pandas, Tensorflow
* Pretrained models (RESNET50, Inception V3, BERT ...)
* Google Cloud Platform (GCR, GCS, Compute Engine ...)
* FastAPI and Streamlit

### Background
There are **two** ways to look at the background of Movie Genre Prediction.

**Business side:**
* Movie distributors such as Warner Bros. distribute their movies without genres tagged. In turn, streaming platforms such as Netflix and Disney+ have to hire "movie experts" to tag the genres. To reduce this long and tiring work, and save resources, we decided to explore the possibilities of using Machine Learning to predict the genres.

**Technical side:**
* Pre-trained Neural Network models such as BERT and ResNet-50 showed remarkable results on identifying features of text and images respectively. And with the rise of these models, numerous researchers have started experimenting on combining these models into one huge model, a multimodal model. Movie Genre Prediction also explores this new field by using movie genres as a target.


### Description
Movie Genre Prediction aims to predict movie genres only by its **Poster** and **Synopsis**. Therefore, fundamentally, Movie Genre Prediction is a **multimodal multilabel classifier**. Multilabel classifiers inherently comes with challenges such as unbalanced dataset and high target dimensionality. Similarly, **multimodal models** also comes with challenges as there is no clear way to best combine these models and is computationally demanding. Hence, Movie Genre Prediction aims to explore and compare the various ways of intergrating independent models while building a cohesive data pipeline to support the computational challenges.

## Getting Started

1. Clone this repo

2. Create a virtual environment for this project with [pyenv](http://github.com/pyenv/pyenv#installation). We recommend a python version of later than 3.10.6
```
pyenv virtualenv <YOUR_PYTHON_VERSION> movie_genre_prediction
pyenv local movie_genre_prediction
pip install --upgrade pip
```

3. Install required libraries
```
make reinstall_package
```

4. Copy .env.sample as .env file and fill in your cloud details
```
cp .env.sample .env
cp .env.yaml.sample .env.yaml
```

5. Load local variables with [direnv](https://github.com/direnv/direnv#getting-started) (Run the code below if you're using zsh)
```
eval "$(direnv hook zsh)"
direnv allow .
```

6. Create a new project in GCP (allow GCR, BQ and other services).
