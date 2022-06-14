import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    RocCurveDisplay,
)

# Affiche la matrice de confusion, la courbe précision/recall, et la courbe ROC
def plot_classifier_results(classifier, X, y_true, y_pred = None, y_pred_proba = None):

    _, ax = plt.subplots(1,3,figsize=(24,8))

    if y_pred is None or y_pred_proba is None:
        ConfusionMatrixDisplay.from_estimator(classifier, X, y_true, cmap='BuPu_r', ax=ax[0])
        PrecisionRecallDisplay.from_estimator(classifier, X, y_true, ax=ax[1])
        RocCurveDisplay.from_estimator(classifier, X, y_true, ax=ax[2])

    else:
        ConfusionMatrixDisplay.from_predictions(y_true, y_pred, cmap='BuPu_r', ax=ax[0])
        PrecisionRecallDisplay.from_predictions(y_true, y_pred_proba, ax=ax[1])
        RocCurveDisplay.from_predictions(y_true, y_pred_proba, ax=ax[2])

    plt.show()

# Stock les différentes métriques dans un dictionnaire
def getMetrics(y_true, y_pred, y_pred_proba, training_time, predict_time):
    return {
            "f1 score": metrics.f1_score(y_true, y_pred),
            "accuracy": metrics.accuracy_score(y_true, y_pred),
            "recall": metrics.recall_score(y_true, y_pred),
            "AUC": metrics.roc_auc_score(y_true, y_pred_proba),
            "Training time": training_time,
            "Predict time": predict_time
        }
