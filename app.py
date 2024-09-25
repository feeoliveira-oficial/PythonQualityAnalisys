from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
from wordcloud import WordCloud
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

# download the necessaries libraries for NLTK
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# directory to save the images
IMAGE_DIR = 'static/images/'

# dataset
data = {
    'rating': [1, 1, 1, 1, 1, 1, 2, 5, 1, 4, 2, 3, 5, 5, 4, 1, 1, 4, 3, 3, 3, 1, 1, 5, 3, 1, 2, 2, 1, 4, 3, 3, 5, 1, 5],
    'comment': [
        "People don't speak French here.",
        "Amazing service by the people caring and friendly.",
        "Shelter for homeless people.",
        "No effort, I bought the timbits it looks like it's rock.",
        "Not very clean.",
        "On weekends there is only 1 person at the counter…bad service.",
        "Good selection. A bit slow to get food but super friendly service.",
        "Fantastic! Highly recommend.",
        "Nice atmosphere and friendly staff.",
        "It was okay, nothing special.",
        "The staff is very friendly and the service is fast.",
        "Incompetent employees running around like headless chicken.",
        "She handed me my coffee and there was a cockroach on my lid. I asked her to make a new one and she gives me attitude. Clean your restaurant, you nasty people.",
        "I've never seen such a dirty restaurant! Infectious would be the right word. And to have you served in French, well, I wish you good luck or hope the girls are in a good mood!",
        "Hire better staff, had to wait almost 30 mins to get my coffee smh.",
        "Staff who refuse to speak and understand French! Saying “2 diet cokes please”, the waiter pretends not to understand.",
        "Unprofessional staff and so dirty!",
        "Impossible to be served in French. Impatient staff.",
        "There are RATS in this location!",
        "People don't speak French here but it's a cafe in Quebec.",
        "The service was good but I would have preferred to express myself in French. But it doesn't matter otherwise very good and fast service.",
        "Unfortunately, my recent experience at Tim Hortons was quite disappointing. Despite being in Quebec, where French is the official language, we had to communicate with the employees in English.",
        "It is tasteless, toppings were not spread on the pizza, and overall, not worth it.",
        "Took an Iced Latte with Oat Milk and Cane Sugar. I got an Iced Latte with 1 ml of oat milk and no cane sugar. Taste is disgusting. First Tim Hortons I go to that cannot even do a coffee.",
        "I am a fan of Tim Hortons, but their timings at this outlet are disappointing. Despite posting 11 pm closure timings, the staff at their own free will would close any time after 9:45 pm. Today is the 2nd day that I have reached Tim's at 10:15 pm & it's closed.",
        "DO NOT ORDER FROM THIS STORE THROUGH THE APP. Worst place ever. Placed an order for carryout by using the app but once I got there, the store was closed and two employees were wrapping up their shift.",
        "No comments, only rating.",
        "No comments, only rating.",
        "No comments, only rating.",
        "No comments, only rating.",
        "No comments, only rating.",
        "No comments, only rating.",
        "No comments, only rating.",
        "No comments, only rating.",
        "No comments, only rating."
    ]
}

# dataframe creation
df = pd.DataFrame(data)

# remove rows with no comments
df = df[df['comment'] != "No comments, only rating."]

# stopwords definition
stop_words = set(stopwords.words('english'))
additional_stopwords = {"n't", "'s", "…", "’", "``", "''", "'m", "'ve", "'d", "also", "although"}
stop_words = stop_words.union(additional_stopwords)

# Function to generate the most common words
@app.route('/rating-distribution')
def rating_distribution():
    plt.figure(figsize=(10, 8))
    plt.barh(df.index, df['rating'], color='blue')
    plt.xlabel('Rating')
    plt.ylabel('Review Index')
    plt.title('Reviews Distribution by Rating')
    filepath = os.path.join(IMAGE_DIR, 'rating_distribution.png')
    plt.savefig(filepath)
    plt.close()
    return send_file(filepath, mimetype='image/png')

# Function to generate the word cloud
@app.route('/word-cloud')
def word_cloud():
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stop_words).generate(' '.join(df['comment']))
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    filepath = os.path.join(IMAGE_DIR, 'word_cloud.png')
    plt.savefig(filepath)
    plt.close()
    return send_file(filepath, mimetype='image/png')

# main page with the comments
@app.route('/')
def index():
    comments = df['comment'].tolist()  # Colect the comments
    return render_template('index.html', comments=comments)

if __name__ == '__main__':
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    app.run(debug=True, host='0.0.0.0', port=5000)
