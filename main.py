import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
import joblib

def load_data(path):
    test_data = pd.read_csv(path)   
    return test_data


def fetch_model(path):
    model = pickle.load(open(path, 'rb'))
    return model


def final_prediction(X, model):
    return model.predict(X)



def main():

    X_test = load_data("./X_train.csv")
    final_model = fetch_model("./final_model.csv")
    y_pred = final_prediction(X_test, final_model)

    print(y_pred)


if __name__ == '__main__':
    main()    


    