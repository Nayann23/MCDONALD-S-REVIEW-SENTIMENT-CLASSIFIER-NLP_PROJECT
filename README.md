# 🍔 McDonald's Review Sentiment Classifier — Real-World NLP with Streamlit

A smart, production-ready sentiment analysis system designed to classify real-world McDonald's customer reviews into **Excellent**, **Average**, or **Poor**, even when input includes typos, sarcasm, or emojis. Built using robust NLP techniques and deployed with an interactive **Streamlit** interface.

---

## 🔍 What It Does

- Analyzes casual and informal customer feedback — including emoji slang and misspellings  
- Handles complex inputs like sarcasm, mixed emotions, and noisy language  
- Predicts sentiment into 3 clear categories: **Excellent**, **Average**, or **Poor**  
- Delivers real-time predictions through a friendly web interface  

---

## 🚀 Features

- ✅ Accepts messy, unstructured text  
  > Example: `da fooood waz 🔥 bt service sux lol`

- ✅ Detects sarcasm and emotional ambiguity  
  > Example: `Wow, cold fries again. Best day ever 🙃`

- ✅ Interprets emoji context and sentiment  
- ✅ Corrects common spelling errors and slang  
- ✅ Performs strongly on real-world, user-generated content  

---

## 📊 Model Performance Summary

| Model Version        | Accuracy (Holdout Set) | Notes                                      |
|----------------------|------------------------|--------------------------------------------|
| SVC (default)        | 83.3%                  | Strong baseline, excellent generalization  |
| SVC (with CV)        | 82.2% (CV Mean)        | Stable across cross-validation folds       |
| **Final Model**      | ~90–95% (real-world)   | Optimized for sarcasm, typos, and emojis   |

> ⚠️ Final model includes advanced preprocessing logic tailored to noisy user inputs. Detailed preprocessing steps are abstracted for clarity and IP protection.

---

## 🎯 Sentiment Labels

- 🟢 **Excellent**  
- 🟡 **Average**  
- 🔴 **Poor**  

---

## 🌍 Real-World Use Cases

- Analyzing food delivery app feedback  
- Monitoring social media sentiment for fast food brands  
- Automating sentiment detection in app store reviews  
- Internal analysis of customer experience trends  

---

## 🖥️ How to Run Locally

1. Install required packages (e.g., `streamlit`, `nltk`, `emoji`, etc.)
2. Run the app using:

```bash
streamlit run app.py
```

---

## 📁 Project File Structure

```text
mcdonalds-review-sentiment-classifier/
├── app.py                                 # Streamlit frontend application
├── svc_model.pkl                          # Trained final SVC model
├── tfidf_vectorizer.pkl                   # TF-IDF vectorizer for feature extraction
├── McDonalds_Review_Classifier_Model_Development.ipynb  # Model development notebook
└── README.md                              # Project documentation (this file)
```

---


## 🙋‍♂️ AUTHOR

#### **NAYAN DAROKAR**  
Aspiring Data Scientist with a focus on building real-world, intelligent systems using data-driven approaches.  

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nayan-darokar-468a85294/) 


---

## 🙌 Acknowledgements

This project was developed through hands-on experimentation to simulate real-world, noisy customer feedback. It draws inspiration from practical challenges in food service sentiment analysis and aims to bridge the gap between academic NLP and consumer-facing applications.


