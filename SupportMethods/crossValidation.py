from sklearn.model_selection import cross_validate
import multiprocessing
import numpy as np


def get_scores_from_cross_validation(clf, vector_train, train_y):

    scoring = ['precision_macro', 'recall_macro', 'f1_macro', 'accuracy']
    predicted = cross_validate(clf, vector_train, train_y, cv=10, n_jobs=multiprocessing.cpu_count(), scoring=scoring, return_train_score=False)

    # print("Accuracy: %0.2f (+/- %0.2f)" % (predicted.mean(), predicted.std() * 2))
    # print sorted(predicted.keys())
    # predicted = cross_val_score(clf, vectorTrain, train_y, cv=2, scoring='accuracy')
    # print "Accuracy: ", accuracy_score(train_y, predicted)
    # predicted = cross_val_score(clf, vectorTrain, train_y, cv=2, scoring='precision')
    # print "Precision: ", precision_score(train_y, predicted, average='macro')
    # predicted = cross_val_score(clf, vectorTrain, train_y, cv=2, scoring='recall')
    # print "Recall: ", recall_score(train_y, predicted, average='macro')
    # predicted = cross_val_score(clf, vectorTrain, train_y, cv=2, scoring='f1_macro')
    # print "F-Measure: ", f1_score(train_y, predicted, average='macro')

    # Hold these values to be returned later.
    predicted_accuracy = np.mean(predicted["test_accuracy"])
    predicted_percision = np.mean(predicted["test_precision_macro"])
    predicted_recall = np.mean(predicted["test_recall_macro"])
    prediced_f_measure = np.mean(predicted["test_f1_macro"])

    # DEBUG PRINT!
    print "Accuracy: ", predicted_accuracy, \
        "/ Precision: ", predicted_percision, \
        "/ Recall: ", predicted_recall, \
        "/ F-Measure: ", prediced_f_measure

    return [predicted_accuracy, predicted_percision, predicted_recall, prediced_f_measure]
