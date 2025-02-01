# 🎥 YouTube Recommendation System

## 📝 Overview
This project implements a **YouTube Recommendation System** using **Collaborative Filtering** based on **Cosine Similarity**. It uses a dataset of YouTube channel names and a similarity matrix to recommend YouTubers similar to the selected one.

## 📂 Dataset
- **📌 Source:** YouTube Channel Data (Custom dataset)
- **📑 Files:**
  - `yt_dict.pkl`: Contains YouTube channel details (name, description, etc.).
  - `similarity_matrix.pkl`: Contains a similarity matrix based on cosine similarity between channels.
- **📊 Data Preprocessing:**
  - Cleaned and preprocessed the YouTube dataset to ensure it contains valid channel names and details.
  - Calculated cosine similarity between YouTube channels to measure similarity.

## 🏆 Recommendation Techniques
### 🔹 **Collaborative Filtering-Based Recommendation**
- Used **Cosine Similarity** to recommend YouTube channels that are similar to a given channel.
- **Example Output** (for a selected YouTube channel):
  ```bash
  Recommendations for 'Tech with Tim':
  - Python Programming Tutorials
  - Code Bullet
  - The Coding Train
  - FreeCodeCamp
  - CS50
  - Traversy Media
  - Dev Ed
  - Sentdex
  - Programming Knowledge
🔬 Implementation Steps
Load and Preprocess Data

Loaded the dataset (yt_dict.pkl).
Loaded the similarity matrix (similarity_matrix.pkl).
Collaborative Filtering:

Created a recommendation function to find similar YouTube channels using cosine similarity.
Implemented a UI using Streamlit to display recommended channels interactively.
Display Results:

Displayed the recommended channels in a user-friendly layout using Streamlit’s layout components.
Save Models Using Pickle

python
Copy
Edit
import pickle
pickle.dump(yts_dict, open('yt_dict.pkl', 'wb'))
pickle.dump(similarity, open('similarity_matrix.pkl', 'wb'))
🛠️ Installation & Usage
📌 Requirements
Ensure you have the following Python libraries installed:

bash
Copy
Edit
pip install pandas streamlit scikit-learn
▶️ Running the Code
To run the YouTube Recommendation System:

bash
Copy
Edit
streamlit run youtube_recommendation_system.py
🎯 Future Enhancements
Integrate Deep Learning Models (Neural Collaborative Filtering, Autoencoders) for improved recommendations.
Deploy the system as a Web App using Flask or Streamlit.
Implement a Hybrid Recommendation System combining collaborative and content-based filtering.
📬 Contact & Support
Connect with me for feedback or contributions:

|||

🚀 Developed by Nadeem Akhtar | 📅 Copyright © 2024
