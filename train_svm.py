# script to train VBL-VA001

from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pandas as pd

path = r'D:\Kuliah\SMT 6\Pembelajaran Mesin\VBL-VA001-master\data\feature_VBL-VA001.csv'
x = pd.read_csv(path, header=None)

path = r'D:\Kuliah\SMT 6\Pembelajaran Mesin\VBL-VA001-master\data\label_VBL-VA001.csv'
y = pd.read_csv(path, header=None)

# make 1D array to avoid warning
y = pd.Series.ravel(y)


X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, shuffle=True
)

print("Shape of Train Data : {}".format(X_train.shape))
print("Shape of Test Data : {}".format(X_test.shape))

# Setup arrays to store training and test accuracies
c_svm = np.arange(1, 100)
train_accuracy = np.empty(len(c_svm))
test_accuracy = np.empty(len(c_svm))

for i, k in enumerate(c_svm):
    # Setup a knn classifier with c_svm
    svm = SVC(C=k)
    # Fit the model
    svm.fit(X_train, y_train)
    # Compute accuracy on the training set
    train_accuracy[i] = svm.score(X_train, y_train)
    # Compute accuracy on the test set
    test_accuracy[i] = svm.score(X_test, y_test)

# Generate plot
# plt.title('Varying number of SVM')
plt.plot(c_svm, test_accuracy, label='Testing Accuracy')
plt.plot(c_svm, train_accuracy, label='Training accuracy')
plt.legend()
plt.xlabel('C')
plt.ylabel('Accuracy')
plt.show()
# np.savetxt('scm_c.txt', test_accuracy)
# plt.savefig('acc_svm.pdf')

# print optimal C and max test accuracy
print(f"Optimal C: {np.argmax(test_accuracy)}")
print(f"Max test accuracy: {max(test_accuracy)}")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Prediksi pada data uji
y_pred = svm.predict(X_test)

# Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

# Menghitung presisi (menggunakan metode macro)
precision = precision_score(y_test, y_pred, average='macro')
print("Precision: ", precision)

# Menghitung recall (menggunakan metode macro)
recall = recall_score(y_test, y_pred, average='macro')
print("Recall: ", recall)

# Menghitung F1-score (menggunakan metode macro)
f1 = f1_score(y_test, y_pred, average='macro')
print("F1-score: ", f1)
