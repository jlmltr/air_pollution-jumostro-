# Air Pollution ML Prediction Project

Link to the documentation:

## Content:
- Intro
- Initial EDA and useful information
- Preprocessing and pipeline creation
- Baseline model creation
- EDA
- Model creation (Multiple models)
- Model Optimization 
- Stacking models
- Error analysis

--- 
## Preprocessing
 * intorduce ordinal_date
 * introduce wind_speed
 * drop: "angle", "sensor", "ID", "Date", "target_", "water", "_of_wind", "CH4"
 * impute with median
 * log-transform: "L3_cloud_optical_depth", "L3_S02_S02_column_number_density_amf", "wind_speed", "L3_O3_effective_temperature", "L3_N02_N02_slant_column_number_density", "L3_O3_O3_column_number_density", "L3_NO2_tropospheric_NO2_column_density", "L3_NO2_NO2_column_number_density", "L3_H2O_H2O_column_number_desnity", "L3_CLOUD_cloud_base_hight", "L3_CLOUD_surface_albedo",
 "L3_HCHO_tropospheric_HCHO_column_number_density_amf", "L3_CO_CO_column_number_density", "specific_humidity_2m_above_ground", 
 "L3_CLOUD_cloud_top_hight", "target"
