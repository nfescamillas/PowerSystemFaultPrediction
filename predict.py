""" Prediction Script for Local Deployment """
import pickle
from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd


with open("knn_model.bin",'rb') as f_in1:
    knn = pickle.load(f_in1)

with open("gb_model.bin",'rb') as f_in2:
    gb = pickle.load(f_in2)


app = Flask('PowerSystemFault_Prediction')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        print("Received data:", data)  # Debugging step

        # Convert input data to a DataFrame
        X = pd.DataFrame([data])

        # Predict
        y_pred = knn.predict(X)

        if y_pred == 1.0:
            y_pred_class = gb.predict(X)
        else:
            y_pred_class = 0

        y_pred_class =int(y_pred_class[0])

        match y_pred_class:
            case 0:
                y_pred_final= 'No fault detected'
            case 11:
                y_pred_final= 'Phase A,B and Ground Fault'
            case 15:
                y_pred_final= 'All Phases and Ground Fault'
            case 9:
                y_pred_final= 'Phase A and Ground Fault'
            case 7:
                y_pred_final= 'Phase A,B,C and Ground Fault'
            case 6:
                y_pred_final= 'Phase B and C Fault'
            case _:
                y_pred_final= 'Not in the database'

        # Prepare and send response
        result = {'Power System Fault' :int(y_pred[0]),
                'Fault Location': y_pred_final} 
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
    