import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


data = pd.read_excel('heart.xlsx')
df = pd.DataFrame(data)

df.head()

X = df.iloc[:, :-1].values
y = df['heart disease']


DTC_model = DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=None,
                                   max_features='sqrt', max_leaf_nodes=None,
                                   min_impurity_decrease=0.0,
                                   min_samples_leaf=1, min_samples_split=2,
                                   min_weight_fraction_leaf=0.0, random_state=17,
                                   splitter='best')

RF_model = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                  max_depth=None, max_features='sqrt', max_leaf_nodes=None,
                                  min_impurity_decrease=0.0,
                                  min_samples_leaf=2, min_samples_split=2,
                                  min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=-1,
                                  oob_score=False, random_state=17, verbose=0, warm_start=False)

DTC_model.fit(X, y)
RF_model.fit(X, y)


DTC_feat_imp = pd.DataFrame(DTC_model.feature_importances_,
                            index=df.iloc[:, :-1].columns,
                            columns=['importance']).sort_values('importance', ascending=False)

RF_feat_imp = pd.DataFrame(RF_model.feature_importances_,
                           index=df.iloc[:, :-1].columns,
                           columns=['importance']).sort_values('importance', ascending=False)

print(DTC_feat_imp, RF_feat_imp, sep='\n\n')

kf = KFold(shuffle=True, random_state=27, n_splits=4)

DTC_score = cross_val_score(estimator=DTC_model, X=X, y=y, cv=kf, scoring="accuracy")
print('\n', "DTC score: ", DTC_score)
print(' DTC_score mean: ', DTC_score.mean())


RF_score = cross_val_score(estimator=RF_model, X=X, y=y, cv=kf, scoring="accuracy")
print('\n', "RF score: ", RF_score)
print(' RF_score mean: ', RF_score.mean())
