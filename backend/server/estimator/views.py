from django.shortcuts import render
from estimator.models import Housing
import pickle
import pandas as pd


def estimate(request):
    loaded_model = pickle.load(open ('estimator/ml/knr_model.pkl', 'rb'))
    if request.method == 'POST':
        form = request.POST
        data = {
            'sqft_living' : int(form.get('surface')),
            'bedrooms' : int(form.get('bedrooms')),
            'bathrooms' : int(form.get('bathrooms')),
            'zipcode' : int(form.get('zipcode')),
            'floors' : int(form.get('floors')),
            'condition' : int(form.get('condition')),
            
            'bathbed_ratio' : int(form.get('bedrooms'))/int(form.get('bathrooms')),
            'waterfront' : 1 if form.get('waterfront') else 0,
        
        }
        df = pd.DataFrame(data, index=[0])
        estimation = str(loaded_model.predict(df)//1)[1:-2]
        estimation = f'{estimation[:-6]} {estimation[-6:-3]} {estimation[-3:]}'
        
        housing = Housing(
            surface = int(form.get('surface')),
            bedrooms = int(form.get('bedrooms')),
            bathrooms = int(form.get('bathrooms')),
            zipcode = int(form.get('zipcode')),
            floors = int(form.get('floors')),
            condition = int(form.get('condition')),
            
            bathbed_ratio = int(form.get('bedrooms'))/int(form.get('bathrooms')),
            waterfront = 1 if form.get('waterfront') else 0,
            estimation = loaded_model.predict(df)
        )
        housing.save()

        return render(request, 'templates/result.html', {'estimation' : estimation})  
    else:
        return render(request, 'templates/estimate.html')

