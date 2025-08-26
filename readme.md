**🌳 Decision Tree Pass/Fail Predictor**

This project uses a Decision Tree Classifier to predict whether a student will Pass or Fail an exam based on study-related features.
It is also deployed as an interactive Streamlit web app for real-time predictions.

**👉Try it Live** https://yuvashri-25-ml-project-1-app-x5qjoz.streamlit.app/

**📌 Project Overview**

The objective of this project is to:

Train a Decision Tree model on student performance data

Predict Pass/Fail outcomes

Provide an interactive Streamlit web app for testing inputs

Visualize model behavior with plots and decision tree graph

**📂 Dataset**

The dataset includes the following features:

📖 Hours Studied

😴 Sleep Hours

🏫 Attendance Percentage

🎯 Pass/Fail Label

📄 Example dataset file: student_exam_tree.csv


**🖥️ Streamlit Web App**

The Streamlit web app allows users to input Hours Studied, Sleep Hours, and Attendance %.
Based on these inputs, the trained Decision Tree model predicts whether the student will Pass or Fail.



**📊 Visualizations**

1️⃣ Decision Tree Visualization
The trained Decision Tree splits data mainly on Attendance and Hours Studied to decide pass/fail outcomes.



**📊 Model Evaluation**

The Decision Tree is evaluated using:

✅ Accuracy
✅ Precision
✅ Recall
✅ F1-score
✅ Confusion Matrix

**[📝 Future Enhancements]**

Add more features (assignment marks, quiz scores, etc.)
Compare performance with other ML models (Logistic Regression, Random Forest, SVM)
Improve interpretability using SHAP values
Enhance UI with more interactive plots in Streamlit
