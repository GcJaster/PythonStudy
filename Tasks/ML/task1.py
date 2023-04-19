import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, Ridge, RidgeClassifierCV, LassoLars
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


data = pd.read_excel("heart.xlsx")
df = pd.DataFrame(data)
# df.head()
# df.info()


X = df.iloc[:, :].values
y = df['heart disease']

# test = SelectKBest(score_func=chi2, k=4)    # Одномерный отбор признаков
# test.fit(X, y)
# features = test.transform(X)

# pca = PCA(n_components=3)   # Метод главных компонент
# pca.fit(X)
# features = pca.transform(X)
# print(f"Explained Variance: {pca.explained_variance_ratio_}")
# print(features[0:5, :])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=43, stratify=y, shuffle=True)

# Creating Instances of Classifiers
LIN_model = LassoLars(copy_X=True, fit_intercept=True)     # Линейные модели
SVC_model = SVC(kernel="linear", probability=True)          # Метод опорных векторов
KNN_model = KNeighborsClassifier(n_neighbors=5, n_jobs=-1)      # Метод k-ближайших соседей

# Train classifiers
LIN_model.fit(X_train, y_train)
SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)

# Make predictions and save the result
LIN_prediction = LIN_model.predict(X_test)
SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)

def rmse(y, predict):
    return np.sqrt(mean_squared_error(y, predict))


def beautiful_coef(coefs, features_names=data.columns):
    return pd.DataFrame(coefs, index=features_names, columns=['coef']).sort_values('coef', ascending=False)


print('LIN_prediction (RMSE): ', rmse(y_test, LIN_prediction))
print('SVC_prediction (RMSE): ', rmse(y_test, SVC_prediction))
print('KNN_prediction (RMSE): ', rmse(y_test, KNN_prediction))


print('\n', 'LIN: ', '\n', beautiful_coef(LIN_model.coef_))
print('\n', 'SVC: ', '\n', beautiful_coef(SVC_model.coef_[0]))

