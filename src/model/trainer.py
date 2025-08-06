import numpy as np
from src.model.knn import KNNClassifier
from src.dataWrangling.load_data import load_iris_data
from src.dataWrangling.split_data import split_train_test
from src.evaluation.metrics import accuracy
from utils.logger import logger

def train():
    logger.info("Loading data...")
    X, y = load_iris_data()
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    logger.info("Training model...")
    model = KNNClassifier(k=3)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    acc = accuracy(y_test, predictions)
    logger.info(f"Accuracy: {acc:.4f}")

if __name__ == "__main__":
    train()