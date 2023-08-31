from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import numpy as np

class columnDropTransformer():
    def __init__(self, ex_str):
        self.ex_str=ex_str

    def transform(self, X, y=None):
        keep_cols =  [col for col in X.columns if not any([s in col for s in self.ex_str])]
        return X[keep_cols]

    def fit(self, X, y=None):
        return self
    

class ordinalDateTransformer():
    def __init__(self):
        pass

    def transform(self, X, y=None):
        X["ordinal_date"] = X.Date.astype("datetime64[s]").apply(lambda x: x.toordinal())
        return X

    def fit(self, X, y=None):
        return self
    

class windTransformer():
    def __init__(self, columns):
        self.columns=columns

    def transform(self, X, y=None):
        X["wind_speed"] = X.apply(lambda x: np.sqrt(x[self.columns[0]]**2 + x[self.columns[1]]**2), axis=1)
        return X.drop(self.columns, axis=1)

    def fit(self, X, y=None):
        return self
    
class logTransformer():
    def __init__(self, columns):
        self.columns=columns

    def transform(self, X, y=None):
        X[self.columns] = X[self.columns].applymap(lambda x: np.log(x + 1))
        return X
    
    def fit(self, X, y=None):
        return self
    
def get_preprocessor():

    wind_cols = ["u_component_of_wind_10m_above_ground", "v_component_of_wind_10m_above_ground"]
    ex_str = ["angle", "sensor", "ID", "Date", "target_", "water", "_of_wind", "CH4"]
    log_cols = ["L3_CLOUD_cloud_optical_depth", "L3_SO2_SO2_column_number_density_amf", "wind_speed", "L3_O3_O3_effective_temperature", "L3_NO2_NO2_slant_column_number_density", "L3_O3_O3_column_number_density", "L3_CO_H2O_column_number_density", "L3_CLOUD_cloud_base_height", "L3_CLOUD_surface_albedo","L3_HCHO_tropospheric_HCHO_column_number_density_amf", "L3_CO_CO_column_number_density", "specific_humidity_2m_above_ground","L3_CLOUD_cloud_top_height"]

    preprocessor = Pipeline([
        ("ordinal_date", ordinalDateTransformer()),
        ("wind_transform", windTransformer(wind_cols)),
        ("drop_cols", columnDropTransformer(ex_str)),
        ("impute", SimpleImputer(strategy="median")),
        ("logit", logTransformer(log_cols)),
        ("scaling", StandardScaler())
    ])

    return preprocessor