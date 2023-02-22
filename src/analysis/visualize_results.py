import matplotlib.pyplot as plt
import numpy as np

def analyze_results(y_true, y_pred, classes):
    """
    Analyzes the results of a machine learning model and generates visualizations to help users understand the model's performance.

    Args:
        y_true (numpy.ndarray): True labels for the test data.
        y_pred (numpy.ndarray): Predicted labels for the test data.
        classes (list): List of class names.

    Returns:
        None
    """
    # Generate a confusion matrix to show the distribution of predicted labels
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title='Confusion matrix',
           ylabel='True label',
           xlabel='Predicted label')
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()

    # Generate a classification report to show precision, recall, and f1-score for each class
    cr = classification_report(y_true, y_pred, target_names=classes)
    print(cr)
