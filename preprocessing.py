from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn import set_config
set_config(transform_output='pandas')
import numpy as np
import pandas as pd

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
        X2 = X.copy(deep=True)
        X2["ordinal_date"] = X2.Date.astype("datetime64[s]").apply(lambda x: x.toordinal())
        return X2

    def fit(self, X, y=None):
        return self
    

class windTransformer():
    def __init__(self, columns):
        self.columns=columns

    def transform(self, X, y=None):
        X2 = X.copy()
        X2["wind_speed"] = X2.apply(lambda x: np.sqrt(x[self.columns[0]]**2 + x[self.columns[1]]**2), axis=1)
        return X2.drop(self.columns, axis=1)

    def fit(self, X, y=None):
        return self
    
class logTransformer():
    def __init__(self, columns):
        self.columns=columns

    def transform(self, X, y=None):
        X2 = X.copy()
        X2[self.columns] = X2[self.columns].applymap(lambda x: np.log(x + 1))
        return X2
    
    def fit(self, X, y=None):
        return self
    
class polynomialTransformer():
    def __init__(self):
        pass

    def transform(self, X, y=None):        
        trans = PolynomialFeatures(degree=2, interaction_only=True)
        transformed = trans.fit_transform(X)
        X = pd.DataFrame(transformed)
        return X
    
    def fit(self, X, y=None):
        return self
    
    
def get_preprocessor_poly():

    wind_cols = ["u_component_of_wind_10m_above_ground", "v_component_of_wind_10m_above_ground"]
    ex_str = ["angle", "sensor", "ID", "Date", "target_", "water", "_of_wind", "CH4"]
    log_cols = ["L3_CLOUD_cloud_optical_depth", "L3_SO2_SO2_column_number_density_amf", "wind_speed", "L3_O3_O3_effective_temperature", "L3_NO2_NO2_slant_column_number_density", "L3_O3_O3_column_number_density", "L3_CO_H2O_column_number_density", "L3_CLOUD_cloud_base_height", "L3_CLOUD_surface_albedo","L3_HCHO_tropospheric_HCHO_column_number_density_amf", "L3_CO_CO_column_number_density", "specific_humidity_2m_above_ground","L3_CLOUD_cloud_top_height"]

    preprocessor = Pipeline([
        ("ordinal_date", ordinalDateTransformer()),
        ("wind_transform", windTransformer(wind_cols)),
        ("drop_cols", columnDropTransformer(ex_str)),
        ("impute", SimpleImputer(strategy="median")),
        ("logit", logTransformer(log_cols)),
        ("scaling", StandardScaler()),
        ("polynomial", polynomialTransformer()),
    ])
    return preprocessor


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
        ("scaling", StandardScaler()),
    ])
    return preprocessor