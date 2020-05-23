# Reddit-Flair-Detector
A Reddit Flair Detector which detects and classifies the type of flair of a post on the [subreddit india](https://www.reddit.com/r/india/) based on five ML algorithms, namely Naive-Bayes, Linear Support Vector Machine, Logistic Regression, Random Forest, and Mulyi-Layer Perceptron Classifier.


## Files And Directories
```Data``` contains database instance of raw data,its csv and the resulting data after cleaning and pre processing.

```Finalized_Model``` contains the finalized ML model which gave the maximum accuracy during testing.

```Scripts``` contains the the files used pre-deployment, that is, the code used for scraping reddit posts and training the model.

```Project_Reddit_Flair.ipynb``` contains the Jupyter Notebook to collect ```r/india``` data, pre-process it, train the models and test them using the mearsures including accuracy, precision, recall, f1-score, and support measures based on different features of flairs.

```flask_app.py``` is the main python file which contains the flask web application for Heroku servers.

```graph.html```, ```index.html```, ```post.html```, ```result.html```  These all were the HTML files which were required to make the Web Application.

```Procfile``` is the file required to connect the web app to Heroku usiing Heroku CLI.

```nltk.txt``` contains 'stopwords' to be downloaded from the shell.

```requirements.txt``` lists all the dependencies required to run the project.


## Working
The user enters the url of the required post. The app takes the url, extracts various features from it and tries to predict the flair by applying the finalized model.


## Execution on localhost

1. Open the terminal.

2. Clone the repository ```git clone https://github.com/AshuKV/Reddit-Flair-Predictor.git```.

3.  Create a virtual environment by the command ```virtualenv -p python3 env```.

4. Activate the ```env``` virtual environment by executing the following command: ```source env/bin/activate```.

5. Inside the cloned directory, Enter command ```pip install -r requirements.txt```.

6. Go inside the Web directory and execute command ```python3 flask_app.py```, which will start the server. 

7. Hit the ```IP Address``` on a web browser to use the app.


## Dependencies

```requirements.txt``` contains the list of all the dependencies.


## Approach

The data was collected using the praw library in Python. The codebase is located in the ```Scripts```. Only top ten comments were considered along with their authors. Total 50 posts were considered for data analysis for each of the 12 flairs considered as a part of the project.

The data includes ```title```, ```comments```, ```body```, ```url```,  ```author```, ```score```, ```id```, ```time-created``` and ```number of comments```. For ```comments```, only top level comments are considered in dataset and no sub-comments are present. The ```title```, ```comments``` and ```body``` were cleaned by removing bad symbols and stopwords using ```nltk```. Basically five types of standalone features were considered for training namely:
1. ```Title```
2. ```Comments```
3. ```Urls```
4. ```Body```
5. Combining ```Title```, ```Comments``` and ```Urls``` as one feature.

After the data collection, and going through various literatures available for Natural Language Processing and various ML  classifiers, I got across [this](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568) article which explained everything, from the data pre-processing to data analysis for text classification. The data was cleaned using textcleaning.py ```Scripts```, which I saved in a csv file.

After cleaning the data, various ML algorithms were trained with training and testing dataset in the ratio 7:3. Basically five ML algorithms were used:
 1. Naive Bayes
 2. Linear Suport Vector Machine
 3. Logistic Regression
 4. Random Forest
 5. Multi Layer Perceptron
 
Training and Testing on the dataset showed the Logistic Regression showed the best accuracy of 66% when trained on the combination of ```Title``` +  ```Comments``` + ```Url``` feature. The best model was saved using ```pickle``` library, which was used further for prediction of the flair from the URL of the post using the web app.


## Deployment

A flask app was made with these routes - ```/``` the home route, ```/action_page``` for displaying the predicted flair, and ```/stats``` for statistics, later which was deployed to Heroku servers using the ```flask_app.py```,  ```Procfile```, ```.gitignore``` and ```requirement.txt``` files.
