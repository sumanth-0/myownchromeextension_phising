from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from flask_cors import CORS
import joblib,os

app = Flask(__name__)
CORS(app)


#with open('phishing.pkl', 'rb') as f:
 #   model = pickle.load(f)

phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')
    if text is not None:
        #text_transformed = vectorizer.transform([text])
        
        X_predict = []
        X_predict.append(str(text))
        y_predict = phish_model_ls.predict(X_predict)
        if  y_predict == 'bad' :
            prediction = 0
        else :
            prediction=1
            
        

        return jsonify({'prediction': int(prediction)})
    else:
        return jsonify({'error': 'Input text not provided.'})

if __name__ == '__main__':
    app.run(debug=True)
