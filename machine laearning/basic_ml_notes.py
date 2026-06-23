# ============================================================
#                    MACHINE LEARNING NOTES
#                         22 June
# ============================================================


# ------------------------------------------------------------
# WHAT IS MACHINE LEARNING?
# ------------------------------------------------------------
# Machine Learning is the science of getting computers to act
# like humans do and improve their learning over time autonomously,
# by feeding them data and information in the form of observations
# and real-world interactions.


# ------------------------------------------------------------
# HOW IS ML DIFFERENT FROM TRADITIONAL PROGRAMMING?
# ------------------------------------------------------------
# Traditional Programming : Data + Code  → Output
# Machine Learning        : Data + Output → Code (Model)
#
# Machine learning is an automatic process.
# The machine understands with the help of data — data is like fuel for a machine.


# ------------------------------------------------------------
# 3 TYPES OF MACHINE LEARNING
# ------------------------------------------------------------

# 1. SUPERVISED LEARNING
#    - Data is labelled (input + correct output pairs are provided).
#    - The model learns the mapping from inputs to outputs.
#
#    Supervised learning has 2 types:
#
#    A) REGRESSION
#       - Used when the output/label is a continuous numerical value.
#       - Answers the question: "How much?" or "How many?"
#       - Use when: predicting prices, temperatures, scores, salaries, etc.
#
#       Examples:
#       - Linear Regression      : Predicts a value using a straight line relationship.
#                                  e.g., Predicting house price based on size.
#       - Polynomial Regression  : Fits a curve instead of a straight line.
#                                  e.g., Predicting growth rate over time.
#       - Ridge / Lasso Regression: Linear regression with regularization to reduce overfitting.
#
#    B) CLASSIFICATION
#       - Used when the output/label is a category or class.
#       - Answers the question: "Which class does this belong to?"
#       - Use when: spam detection, disease diagnosis, image recognition, etc.
#
#       Examples:
#       - Logistic Regression    : Despite the name, used for binary classification (0 or 1).
#                                  e.g., Email is spam or not spam.
#       - Decision Tree          : Splits data into branches based on feature conditions.
#                                  e.g., Approving or rejecting a loan application.
#       - Random Forest          : An ensemble of many Decision Trees working together.
#                                  - More accurate and less prone to overfitting than a single tree.
#                                  - e.g., Predicting whether a patient has a disease.
#       - Support Vector Machine : Finds the best boundary (hyperplane) between classes.
#         (SVM)                    e.g., Classifying handwritten digits.
#       - K-Nearest Neighbors    : Classifies a data point based on its K closest neighbors.
#         (KNN)                    e.g., Recommending products similar to ones a user liked.
#       - Naive Bayes            : Uses probability (Bayes theorem) to classify data.
#                                  e.g., Sentiment analysis (positive/negative review).
#
#    QUICK GUIDE — Regression vs Classification:
#    ┌─────────────────────────────┬──────────────────────────────────┐
#    │       REGRESSION            │         CLASSIFICATION           │
#    ├─────────────────────────────┼──────────────────────────────────┤
#    │ Output is a number          │ Output is a category/label       │
#    │ e.g., Price = ₹45,000       │ e.g., Spam / Not Spam            │
#    │ e.g., Temperature = 36.6°C  │ e.g., Cat / Dog / Bird           │
#    │ Metric: MAE, RMSE, R²       │ Metric: Accuracy, Precision, F1  │
#    └─────────────────────────────┴──────────────────────────────────┘

# 2. UNSUPERVISED LEARNING
#    - Data is unlabelled.
#    - The model finds hidden patterns or groupings on its own.

# 3. REINFORCEMENT LEARNING
#    - A learning agent is present that improves by interacting with an environment.
#    - Learning is based on rewards (positive feedback) and penalties (negative feedback).


# ------------------------------------------------------------
# ML LIFECYCLE
# ------------------------------------------------------------
# 1. Data Collection   – Gather raw data from various sources.
# 2. Data Preparation  – Clean and format the data.
# 3. Data Wrangling    – Transform and organize data for analysis.
# 4. Data Modeling     – Choose an appropriate algorithm/model.
# 5. Model Training    – Train the model on the prepared data.
# 6. Model Verification – Evaluate model performance on test data.
# 7. Model Deployment  – Deploy the model to production for real-world use.


# ------------------------------------------------------------
# AI vs ML vs DL
# ------------------------------------------------------------

# ARTIFICIAL INTELLIGENCE (AI)
#    The science and engineering of making computers capable of performing
#    tasks that typically require human intelligence.
#
#    Two types:
#    1. Applied AI (Weak AI)
#       - Examples: Alexa, Siri
#       - Performs specific tasks like playing music, weather prediction,
#         acting as a personal assistant.
#       - Requires human involvement.
#
#    2. Generalized AI (Strong AI)
#       - Behaves exactly like a human with no human involvement.
#       - Example: a fully autonomous coffee-making machine.
#       - Still largely theoretical/in research.

# MACHINE LEARNING (ML)
#    - A subset of AI.
#    - Enables computers to learn from data without being explicitly programmed.

# DEEP LEARNING (DL)
#    - A subset of ML.
#    - Concerned with algorithms inspired by the structure and function of the human brain.
#    - In computing terms, these are called Neural Networks.
#    - With the help of neural networks, a machine can learn things,
#      gain knowledge, and make decisions.


# ------------------------------------------------------------
# FEATURES AND LABELS
# ------------------------------------------------------------

# FEATURE (Input)
#    - Every column in the dataset is a feature.
#    - These are the input variables used to make predictions.

# LABEL (Output)
#    - The output/result we get after training the model.
#    - Also called the target variable.


