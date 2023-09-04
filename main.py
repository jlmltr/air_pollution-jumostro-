import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import sys



# ignore warnings
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")



def load_data(path):
    test_data = pd.read_csv(path, index_col=0)   
    return test_data


def fetch_model(path):
    model = pickle.load(open(path, 'rb'))
    return model



def final_prediction(X, model):
    return model.predict(X)



def create_final_table(y_pred, y_test, X_test):
    y_pred_df = pd.DataFrame(y_pred, columns=['predicted_target'])
    y_test_df = pd.DataFrame(y_test)
    X_test_df = pd.DataFrame(X_test)


    output_dict = {
        'place_and_date': X_test_df['Place_ID X Date'].to_list(),
        'real_target': y_test_df['target'].to_list(),
        'predicted_target': y_pred_df['predicted_target'].round(1).to_list()                  
    }

    final_df = pd.DataFrame(data=output_dict)
    final_df.to_csv('./data/predictions.csv')
    print("FINAL PREDICTIONS___________________________________________________________")
    print(final_df.head(10))

    print("SCORES_______________________________________________________")
    print("RMSE: ", mean_squared_error(y_test, y_pred, squared=False))
    print('R SQARE: ', r2_score(y_test, y_pred))



def main():

    file_names = sys.argv[1:]
    X_test = load_data(f"./data/{file_names[0]}.csv")
    y_test = load_data(f"./data/{file_names[1]}.csv")


    final_model = fetch_model("./stacked_model.pkl")

    y_pred = final_prediction(X_test, final_model)

    create_final_table(y_pred, y_test, X_test)

    



if __name__ == '__main__':
    main()
