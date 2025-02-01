📊 Global YouTube Statistics Analysis 📹
This project focuses on analyzing global YouTube statistics, such as the most subscribed YouTubers, video views, and the distribution of YouTubers by channel type, category, and country.

📑 Table of Contents
📈 Overview
📊 Data Insights
Top YouTubers by Subscribers
Top YouTubers by Video Views
Distribution by Channel Type
Distribution by Category
Distribution by Country
⚙️ Technologies Used
🛠️ How to Use
🧑‍💻 Contributing
📄 License
📈 Overview
This analysis leverages a dataset of 995 YouTubers with attributes such as subscribers, video views, uploads, country, category, and more. Various visualizations have been created using tools like Matplotlib, Seaborn, and Plotly.

🧐 Key Questions
Who are the top 10 YouTubers by subscribers? 📺
Which categories are most popular among YouTubers? 🎮
Where are YouTubers located across the globe? 🌍
How do YouTubers distribute across different channel types? 🎬
📊 Data Insights
1. Top YouTubers by Subscribers
📊 The analysis highlights the Top 10 YouTubers by subscribers. The rankings are visualized using bar graphs and pie charts.

T-Series 📌: 245M Subscribers
YouTube Movies 🎥: 170M Subscribers
MrBeast 🍔: 166M Subscribers
2. Top YouTubers by Video Views
🌍 The Top 10 YouTubers by video views are also visualized. This gives insight into which channels attract the most viewers.

T-Series 📌: 228B Views
Cocomelon 🍼: 164B Views
SET India 🎬: 148B Views
3. Distribution by Channel Type
📅 The distribution of YouTubers by channel type shows the different categories such as Entertainment, Music, Nonprofit, and more.

Most common types: Entertainment 🎭, Music 🎶
Least common type: Nonprofit 🧑‍🤝‍🧑
4. Distribution by Category
📊 Categories such as Entertainment, Music, People & Blogs, and Comedy dominate the YouTube landscape.

Top category: Entertainment 🎬
Least common category: Education 📚
5. Distribution by Country
🌎 The distribution of YouTubers by country reveals a high concentration in countries like the United States, India, and Brazil.

🇺🇸 United States
🇮🇳 India
🇧🇷 Brazil
⚙️ Technologies Used
Python 🐍
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Plotly
Jupyter Notebooks 📓 for data analysis
Label Encoding 🔠 for categorical data preprocessing
🛠️ How to Use
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/YouTube-Statistics-Analysis.git
Install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Open the Jupyter notebook and start exploring the data!

bash
Copy
Edit
jupyter notebook
🧑‍💻 Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🛠️ Features

- **🔍 Recommendation**: Get similar YouTube channels based on a selected channel.
- **💬 Interactive**: Choose a YouTube channel from the dropdown and get top 9 recommended channels.
- **📊 View Counter**: Keeps track of the total number of views for the app.
- **🔗 External Links**: Quick access to the developer's **LinkedIn**, **GitHub**, **Kaggle**, and **Personal Website**.

## 🚀 Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.x
- Streamlit
- Pandas
- Pickle

### 📦 Install Dependencies

Run the following command to install required libraries:

```bash
pip install streamlit pandas pickle-mixin
🏃 How to Run
Clone this repository or download the files.
Ensure you have the following pickle files in the same directory as the app:
yt_dict.pkl: Contains YouTube channel data.
similarity_matrix.pkl: Contains the pre-computed cosine similarity matrix for the channels.
In the project directory, run:
bash
Copy
Edit
streamlit run app.py
Visit http://localhost:8501 in your browser to interact with the app.
✨ Functionality
YouTube Channel Dropdown: Select a YouTube channel from the list.
🔄 Get Recommendations: Click on the 'Get Recommend' button to receive 9 recommended YouTube channels.
👁️ View Count: Displays the total number of views.
🌐 External Links: Links to the developer’s LinkedIn, GitHub, Kaggle, and Personal Website.
🌍 Links
🔗 LinkedIn
🐱 GitHub
📊 Kaggle
🌐 Personal Website
