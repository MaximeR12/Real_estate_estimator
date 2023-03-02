import pandas as pd
import numpy as np
df = pd.read_csv('backend/server/estimator/ml/cleaned_house_data.csv')


# Création d'une nouvelle valeur de ratio entre le nombre de chambre et le nombre de sdb
df['bathbed_ratio'] = (df.bedrooms / df.bathrooms).round(2)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(subset="bathbed_ratio", how="all", inplace=True)

#remplacement du yr_built par yr_renovated si le bien a été rénové
#df.loc[df["yr_renovated"]!=0, "yr_built"] = (df.yr_built + df.yr_renovated)/2
#contre productif, score moins precis

#sauvegarde sur un ficher csv modifié pour garder l'original
df.to_csv('backend/server/estimator/ml/cleaned_prepared_house_data.csv')