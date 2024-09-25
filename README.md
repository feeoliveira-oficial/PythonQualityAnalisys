🍁 Tim Hortons Review Analysis ☕️

Welcome to the Tim Hortons Review Analysis project! This is a Flask-based web application designed to analyze and visualize customer reviews for Tim Hortons. The app provides an interactive and user-friendly interface to display a rating distribution 📊, a word cloud 🌥️ of frequent terms, and a list of customer comments 📝.

🍁 Tim Hortons Review Analysis ☕️
Welcome to the Tim Hortons Review Analysis project! This is a Flask-based web application designed to analyze and visualize customer reviews for Tim Hortons. The app provides an interactive and user-friendly interface to display a rating distribution 📊, a word cloud 🌥️ of frequent terms, and a list of customer comments 📝.

✨ Features ✨
📊 Rating Distribution: Displays a bar chart representing the distribution of ratings given by customers.
🌥️ Word Cloud: Shows the most common words used in the reviews, excluding common stopwords, in a word cloud format.
📝 Customer Comments: Allows users to toggle visibility of individual customer comments for easy browsing.
🛠️ Technologies Used 🛠️
Flask: A lightweight web framework for Python. 🚀
Pandas: For handling and manipulating datasets. 📑
Matplotlib: For generating visual plots like bar charts. 📈
NLTK: Natural Language Toolkit, used for tokenizing and removing stopwords from text data. ✂️🗣️
WordCloud: To create visually appealing word clouds. 🌥️
Bootstrap: For styling the front-end and making it responsive. 💻🎨
🗂️ Project Structure 📁
app.py: Main Flask application file. 🧑‍💻
static/images/: Directory where generated images (charts and word clouds) are stored. 📂🖼️
templates/index.html: HTML file responsible for rendering the front-end, displaying the charts and customer comments. 🖥️📝
💻 HTML Template Overview 🖼️
The HTML template uses Bootstrap for responsive design and clean, user-friendly styling. It contains:

📊 Rating Distribution Section:

A button to toggle the visibility of the bar chart showing the distribution of ratings.
🌥️ Word Cloud Section:

A button to toggle the visibility of the word cloud generated from customer reviews.
📝 Customer Comments Section:

A button to toggle the visibility of the list of customer comments, making it easier to navigate through feedback.
⚙️ Setup Instructions ⚙️
Prerequisites 📋
Python 3.x installed 🐍
pip for managing Python packages 📦
Installation Steps 🛠️
Clone the repository:

git clone https://github.com/feeoliveira-oficial/PythonQualityAnalisys.git
cd PythonQualityAnalisys
Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Run the Flask app:

python app.py
Open your browser 🌐 and navigate to:

http://127.0.0.1:5000
To see the app in action!

🚪 Endpoints 🚪
/: Displays the list of customer comments. 📝
/rating-distribution: Generates and displays the rating distribution chart. 📊
/word-cloud: Generates and displays the word cloud based on the comments. 🌥️

🖼️ Screenshots 📸
📊 Rating Distribution
🌥️ Word Cloud
