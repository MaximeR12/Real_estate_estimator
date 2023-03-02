from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


df = pd.read_csv("backend/server/estimator/ml/cleaned_prepared_house_data.csv")

y = df['price']
X = df[["sqft_living","bedrooms","zipcode","waterfront", 'bathbed_ratio', 'floors','condition']]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=42)
knn = KNeighborsRegressor(n_neighbors=4)



###############  Variables utilisées  ###################
numeric_features = ["sqft_living","bedrooms","zipcode",'waterfront', 'bathbed_ratio', 'floors', 'condition']
categorial_features = ["zipcode"]

#################  TRANSFORMERS   ######################
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ("minmax", MinMaxScaler())

])
categorical_transformer = OneHotEncoder(sparse_output=True)

################ PREPROCESSING  #######################
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorial_features)
    ])
pipe = Pipeline([
    ('prep', preprocessor),
    ('model', knn)
])
trained_pipe = pipe.fit(X_train,y_train)
import pickle
pickle.dump(pipe, open('backend/server/estimator/ml/knr_model.pkl','wb'))

#####################################################
##################   2 EME MODELE   #################
##############  RANDOM FOREST REGRESSOR  ############
#####################################################
from sklearn.ensemble import RandomForestRegressor


forest = RandomForestRegressor()
trained_forest_pipe = forest.fit(X_train, y_train)
score = trained_forest_pipe.score(X_test, y_test)
print("Score : {:.3%}".format(score)) 

# score plus élevé mais resultats plus longs et qui oscille a +- 1% (logique car randomforest)
# Encore plus long et - performant si utilisation de pipeline avec transformers