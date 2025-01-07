# Hybrid-Phishing-Detection-Tool

A hybrid machine learning and deep learning-based phishing detection tool designed to enhance cybersecurity by identifying phishing attacks with high accuracy. Includes a Streamlit-based user-friendly interface.

---

## 🌟 Overview

Phishing attacks pose significant threats to digital security, targeting personal and corporate information. This project introduces a **hybrid learning model** that combines **machine learning** and **deep learning** to detect phishing attacks with higher accuracy.

---

## 🚀 Features

- ✅ **Hybrid Model**: Combines traditional machine learning algorithms with deep learning methods.
- ✅ **User-Friendly Interface**: Built with **Streamlit**, allowing easy input and analysis of phishing emails.
- ✅ **Dynamic Learning**: Adaptable to evolving phishing techniques using reinforcement and transfer learning.
- ✅ **Performance Metrics**: Evaluated with **accuracy**, **precision**, and **recall**.

---

## 📊 Performance Metrics

| **Algorithm**          | **Accuracy (%)** |
|-------------------------|------------------|
| Logistic Regression     | 92.84           |
| Random Forest           | 93.61           |
| XGBoost                 | 93.41           |
| Naive Bayes             | 91.80           |
| Extra Trees             | **93.89**       |
| Voting Classifier       | **93.65**       |

> **Note**: Deep learning evaluation results are currently under testing.

---

## 🛠️ Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/zgokceaynaci/Phishing-Detection-With-Hybrid-Model.git
   cd Phishing-Detection-With-Hybrid-Model

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the application:
   ```bash
   streamlit run main.py
   
---

## 📂 Datasets

The following datasets were used in this project for training and testing the hybrid phishing detection model:

1. **Phishing Email Dataset**  
   [Kaggle Link](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)

2. **Phishing Site URLs**  
   [Kaggle Link](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)

3. **Phishing Emails Dataset**  
   [Kaggle Link](https://www.kaggle.com/datasets/subhajournal/phishingemails)

---

## ⚠️ Note on Datasets 

The final merged dataset used in this project is **not included** in this repository due to its large size and potential licensing restrictions. ### Dataset Preparation Instructions
1. Download the datasets from the following links: 

- [Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) 
- [Phishing Site URLs](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls) 
- [Phishing Emails Dataset](https://www.kaggle.com/datasets/subhajournal/phishingemails) 

2. Merge the datasets into a single file: - Use tools like **Python** (e.g., pandas) to combine the datasets. - Ensure the merged dataset has consistent formatting (e.g., column names, data types). 

3. Save the merged dataset as `final_dataset.csv` in the `datasets/` folder.

 4. Example code snippet to merge datasets: 
    ```
    python import pandas as pd 

# Load individual datasets 
    ```
    email_dataset = pd.read_csv("datasets/Phishing_Email.csv") 
    site_urls_dataset = pd.read_csv("datasets/phishing_site_urls.csv") 
    phishing_emails_dataset = pd.read_csv("datasets/phishing_emails.csv") 

# Merge datasets (modify as needed) 
    ```
    merged_dataset = pd.concat([email_dataset, site_urls_dataset, phishing_emails_dataset], ignore_index=True) 

# Save the merged dataset 
    ```
    merged_dataset.to_csv("datasets/final_dataset.csv", index=False)

   
---

## 🎯 How It Works
Input: Enter email content in the provided text box.
Processing: The hybrid model analyzes the content using a combination of machine learning and deep learning algorithms.
Output: The tool displays results as either Spam or Not Spam.
🎯 How It Works
Input: Enter email content in the provided text box.
Processing: The hybrid model analyzes the content using a combination of machine learning algorithms (e.g., Logistic Regression, Random Forest) and deep learning techniques (e.g., GloVe embeddings).
Features such as URL patterns, email structures, and behavioral indicators are extracted and analyzed.
Output: The tool classifies the email content and displays results as either:
Spam
Not Spam

This hybrid approach ensures better detection accuracy and adaptability to new phishing attack patterns.

---

## 🌍 Future Enhancements
Real-time phishing detection with API integration.
Expanding detection capabilities to websites and SMS phishing attacks.
Fine-tuning deep learning models for emerging attack patterns.

---

## 📚 References
Zuraiq and Alkasassbeh, Phishing Detection Using ML, 2019.
Alazaidah et al., Hybrid Approaches in Cybersecurity, 2024.
Do et al., Deep Learning in Phishing Detection, 2022.

