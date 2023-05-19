from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
model=pickle.load(open('House_price.pickle','rb'))
final=pd.read_csv('final.csv')
len_location= len(sorted(final['location'].unique()))
predict_file=pd.read_csv('predict.csv')

@app.route('/', methods=['GET'])
def something():
    return render_template('index.html')

@app.route('/about_us', methods=['GET'])
def something2():
    return render_template('about_us.html')


@app.route('/predict',methods=['GET'])
def index():

    locations=sorted(final['location'].unique())
    print(locations)
    print(len(locations))
    # locations.insert(0,'Select Location')
    return render_template('predict.html',locations=locations)



@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    location=request.form.get('location')
    area=request.form.get('area')
    bhk=request.form.get('bhk')
    bathrooms=request.form.get('bathrooms')

    if location=="other":
        x = np.zeros(len_location + 2)
        x[0] = area
        x[1] = bhk
        x[2] = bathrooms
    else:
        loc_index = np.where(predict_file.columns == location)[0][0]
        loc_index=loc_index-1
        x = np.zeros(len_location+2)
        x[0] = area
        x[1] = bhk
        x[2] = bathrooms
        if loc_index >= 0:
            x[loc_index] = 1

    print(model.predict([x])[0])
    return str(round(model.predict([x])[0] *100000,2))


if __name__=='__main__':
    app.run(debug=True)