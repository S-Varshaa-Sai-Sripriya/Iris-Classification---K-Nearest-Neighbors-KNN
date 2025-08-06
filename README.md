## Iris Classification - K-Nearest Neighbors (KNN)

A lightweight, modular implementation of the K-Nearest Neighbors (KNN) algorithm applied to the classic Iris flower classification problem. Achieved an accuracy of **96.6%** using optimal K selection and preprocessing.

---

## 🌼 Problem Statement: Iris Flower Classification

The **Iris dataset** is a foundational classification problem in machine learning. It contains 150 samples from three species of Iris flowers—**Setosa**, **Versicolor**, and **Virginica**—with four features each:  
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width

The goal is to predict the correct **species** of the flower from its physical measurements.

---

## 🧠 Algorithm: K-Nearest Neighbors (KNN)

**K-Nearest Neighbors** is a non-parametric, instance-based learning algorithm that classifies data points based on the majority label of their **K closest neighbors** in the feature space.

In this project:
- Optimal K value was chosen via cross-validation.
- Euclidean distance was used as the distance metric.
- Data was scaled for distance-based learning.
- Achieved **96.6% classification accuracy** on the test set.

---