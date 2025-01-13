""" Prediction Script for Cloud  Deployment """
import pickle
import pandas as pd

with open("knn_model.bin",'rb') as f_in1:
    knn = pickle.load(f_in1)

with open("gb_model.bin",'rb') as f_in2:
    gb = pickle.load(f_in2)

def predict(data):
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
    return result


def lambda_handler(event,context):
    data= event['data']
    result = predict(data)
    return result

