import pandas as pd
from scipy import stats
import numpy as np

train = pd.read_csv('/Users/Palfrey/Downloads/New Folder With Items/Final Project/Train.csv')
test = pd.read_csv('/Users/Palfrey/Downloads/New Folder With Items/Final Project/Test.csv')

column_rename_dict = {
    'fecho_dato': 'date',
    'ncodpers': 'customer_code',
    'ind_empleado': 'employee_index',
    'pais_residencia': 'country_of_residence',
    'sexo': 'sex',
    'age': 'age',
    'fecha_alta': 'holder_start_date',
    'ind_nuevo': 'new_customer_index',
    'antiguedad': 'seniority',
    'indrel': 'primary',
    'ult_fec_cli_1t': 'last_date_as_primary',
    'indrel_1mes': 'customer_type_at_beginning_of_month',
    'tiprel_1mes': 'customer_relation_type_at_beginning_of_month',
    'indresi': 'residence_index',
    'indext': 'foreigner_index',
    'conyuemp': 'spouse_index',
    'canal_entrada': 'channel',
    'indfall': 'deceased_index',
    'tipodom': 'address_type',
    'cod_prov': 'province_code',
    'nomprov': 'province_name',
    'ind_actividad_cliente': 'activity_index',
    'renta': 'gross_income',
    'segmento': 'segmentation',
    'ind_ahor_fin_ult1': 'saving_account',
    'ind_aval_fin_ult1': 'guarantees',
    'ind_cco_fin_ult1': 'current_accounts',
    'ind_cder_fin_ult1': 'derivada_account',
    'ind_cno_fin_ult1': 'payroll_account',
    'ind_ctju_fin_ult1': 'junior_account',
    'ind_ctma_fin_ult1': 'mas_particular_account',
    'ind_ctop_fin_ult1': 'particular_account',
    'ind_ctpp_fin_ult1': 'particular_plus_account',
    'ind_deco_fin_ult1': 'short_term_deposits',
    'ind_deme_fin_ult1': 'medium_term_deposits',
    'ind_dela_fin_ult1': 'long_term_deposits',
    'ind_ecue_fin_ult1': 'e_account',
    'ind_fond_fin_ult1': 'funds',
    'ind_hip_fin_ult1': 'mortgage',
    'ind_plan_fin_ult1': 'pensions',
    'ind_pres_fin_ult1': 'loans',
    'ind_reca_fin_ult1': 'taxes',
    'ind_tjcr_fin_ult1': 'credit_card',
    'ind_valo_fin_ult1': 'securities',
    'ind_viv_fin_ult1': 'home_account',
    'ind_nomina_ult1': 'payroll',
    'ind_nom_pens_ult1': 'pensions',
    'ind_recibo_ult1': 'direct_debit'
    }
# Rename columns in both DataFrames
train.rename(columns=column_rename_dict, inplace=True)
test.rename(columns=column_rename_dict, inplace=True)

print(train.columns)
print(test.columns)

# Get a summary of the data types and non-null counts
print("Train DataFrame Info:")
print(train.info())
'''
'''
print("\nTest DataFrame Info:")
print(test.info())

"""
Data columns (total 48 columns):
 #   Column                                        Dtype  
---  ------                                        -----  
 0   fecha_dato                                    object 
 1   customer_code                                 int64  
 2   employee_index                                object 
 3   country_of_residence                          object 
 4   sex                                           object 
 5   age                                           object 
 6   holder_start_date                             object 
 7   new_customer_index                            float64
 8   seniority                                     object 
 9   primary                                       float64
 10  last_date_as_primary                          object 
 11  customer_type_at_beginning_of_month           object 
 12  customer_relation_type_at_beginning_of_month  object 
 13  residence_index                               object 
 14  foreigner_index                               object 
 15  spouse_index                                  object 
 16  channel                                       object 
 17  deceased_index                                object 
 18  address_type                                  float64
 19  province_code                                 float64
 20  province_name                                 object 
 21  activity_index                                float64
 22  gross_income                                  float64
 23  segmentation                                  object 
 24  saving_account                                int64  
 25  guarantees                                    int64  
 26  current_accounts                              int64  
 27  derivada_account                              int64  
 28  payroll_account                               int64  
 29  junior_account                                int64  
 30  mas_particular_account                        int64  
 31  particular_account                            int64  
 32  particular_plus_account                       int64  
 33  short_term_deposits                           int64  
 34  medium_term_deposits                          int64  
 35  long_term_deposits                            int64  
 36  e_account                                     int64  
 37  funds                                         int64  
 38  mortgage                                      int64  
 39  pensions                                      int64  
 40  loans                                         int64  
 41  taxes                                         int64  
 42  credit_card                                   int64  
 43  securities                                    int64  
 44  home_account                                  int64  
 45  payroll                                       float64
 46  pensions                                      float64
 47  direct_debit                                  int64  
dtypes: float64(8), int64(23), object(17)
memory usage: 4.9+ GB
None

Test DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 929615 entries, 0 to 929614
Data columns (total 24 columns):
 #   Column                                        Non-Null Count   Dtype  
---  ------                                        --------------   -----  
 0   fecha_dato                                    929615 non-null  object 
 1   customer_code                                 929615 non-null  int64  
 2   employee_index                                929615 non-null  object 
 3   country_of_residence                          929615 non-null  object 
 4   sex                                           929610 non-null  object 
 5   age                                           929615 non-null  int64  
 6   holder_start_date                             929615 non-null  object 
 7   new_customer_index                            929615 non-null  int64  
 8   seniority                                     929615 non-null  int64  
 9   primary                                       929615 non-null  int64  
 10  last_date_as_primary                          1683 non-null    object 
 11  customer_type_at_beginning_of_month           929592 non-null  float64
 12  customer_relation_type_at_beginning_of_month  929592 non-null  object 
 13  residence_index                               929615 non-null  object 
 14  foreigner_index                               929615 non-null  object 
 15  spouse_index                                  104 non-null     object 
 16  channel                                       927534 non-null  object 
 17  deceased_index                                929615 non-null  object 
 18  address_type                                  929615 non-null  int64  
 19  province_code                                 925619 non-null  float64
 20  province_name                                 925619 non-null  object 
 21  activity_index                                929615 non-null  int64  
 22  gross_income                                  929615 non-null  object 
 23  segmentation                                  927367 non-null  object 

dtypes: float64(2), int64(8), object(14)

"""

# Check for missing values in the train DataFrame
print("Missing Values in Train DataFrame:")
print(train.isnull().sum())

# Check for missing values in the test DataFrame
print("\nMissing Values in Test DataFrame:")
print(test.isnull().sum())

'''
Missing Values in Train DataFrame:
fecha_dato                                             0
customer_code                                          0
employee_index                                     27734
country_of_residence                               27734
sex                                                27804
age                                                    0
holder_start_date                                  27734
new_customer_index                                 27734
seniority                                              0
primary                                            27734
last_date_as_primary                            13622516
customer_type_at_beginning_of_month               149781
customer_relation_type_at_beginning_of_month      149781
residence_index                                    27734
foreigner_index                                    27734
spouse_index                                    13645501
channel                                           186126
deceased_index                                     27734
address_type                                       27735
province_code                                      93591
province_name                                      93591
activity_index                                     27734
gross_income                                     2794375
segmentation                                      189368
saving_account                                         0
guarantees                                             0
current_accounts                                       0
derivada_account                                       0
payroll_account                                        0
junior_account                                         0
mas_particular_account                                 0
particular_account                                     0
particular_plus_account                                0
short_term_deposits                                    0
medium_term_deposits                                   0
long_term_deposits                                     0
e_account                                              0
funds                                                  0
mortgage                                               0
pensions                                               0
loans                                                  0
taxes                                                  0
credit_card                                            0
securities                                             0
home_account                                           0
payroll                                            16063
pensions                                           16063
direct_debit                                           0
dtype: int64

Missing Values in Test DataFrame:
fecha_dato                                           0
customer_code                                        0
employee_index                                       0
country_of_residence                                 0
sex                                                  5
age                                                  0
holder_start_date                                    0
new_customer_index                                   0
seniority                                            0
primary                                              0
last_date_as_primary                            927932
customer_type_at_beginning_of_month                 23
customer_relation_type_at_beginning_of_month        23
residence_index                                      0
foreigner_index                                      0
spouse_index                                    929511
channel                                           2081
deceased_index                                       0
address_type                                         0
province_code                                     3996
province_name                                     3996
activity_index                                       0
gross_income                                         0
segmentation                                      2248
dtype: int64

'''
# Convert all columns to numeric, coercing errors to NaN
train = train.apply(pd.to_numeric, errors='coerce')
# Z-score method
z_scores = stats.zscore(train.select_dtypes(include=['float64', 'int64']))
abs_z_scores = np.abs(z_scores)
outliers = (abs_z_scores > 3).all(axis=1)
print("Outliers based on Z-score:", outliers.sum())

# IQR method
Q1 = train.quantile(0.25)
Q3 = train.quantile(0.75)
IQR = Q3 - Q1
outliers = ((train < (Q1 - 1.5 * IQR)) | (train > (Q3 + 1.5 * IQR))).any(axis=1)
print("Outliers based on IQR:", outliers.sum())

'''
Outliers based on Z-score: 0
Outliers based on IQR: 6101444

'''


# Assuming train and test DataFrames are already loaded

# Select only numeric columns from the train DataFrame
numeric_train = train.select_dtypes(include=['number'])

# Select only numeric columns from the test DataFrame
numeric_test = test.select_dtypes(include=['number'])

# Calculate skewness for each numeric column in the train DataFrame
train_skewness = numeric_train.skew()

# Calculate skewness for each numeric column in the test DataFrame
test_skewness = numeric_test.skew()

# Print skewness values
print("Skewness in Train DataFrame:")
print(train_skewness)

print("\nSkewness in Test DataFrame:")
print(test_skewness)

'''
Skewness in Train DataFrame:
fecha_dato                                             NaN
customer_code                                    -0.293747
employee_index                                         NaN
country_of_residence                                   NaN
sex                                                    NaN
age                                               0.804207
holder_start_date                                      NaN
new_customer_index                                3.721909
seniority                                      -597.255999
primary                                          23.373776
last_date_as_primary                                   NaN
customer_type_at_beginning_of_month              51.792897
customer_relation_type_at_beginning_of_month           NaN
residence_index                                        NaN
foreigner_index                                        NaN
spouse_index                                           NaN
channel                                           0.082240
deceased_index                                         NaN
address_type                                      0.000000
province_code                                    -0.124528
province_name                                          NaN
activity_index                                    0.169362
gross_income                                     53.257206
segmentation                                           NaN
saving_account                                   98.858543
guarantees                                      207.809278
current_accounts                                 -0.654378
derivada_account                                 50.354373
payroll_account                                   3.074725
junior_account                                   10.127175
mas_particular_account                            9.991027
particular_account                                2.213494
particular_plus_account                           4.487410
short_term_deposits                              23.647367
medium_term_deposits                             24.475570
long_term_deposits                                4.507626
e_account                                         3.029149
funds                                             7.149396
mortgage                                         12.918353
pensions                                         10.298012
loans                                            19.432099
taxes                                             4.011220
credit_card                                       4.424333
securities                                        6.006428
home_account                                     16.028044
payroll                                           3.915520
pensions                                          3.726945
direct_debit                                      2.228070
dtype: float64

Skewness in Test DataFrame:
customer_code                           -0.327419
age                                      0.830373
new_customer_index                       5.739031
seniority                             -555.491690
primary                                 23.438419
customer_type_at_beginning_of_month    185.543646
address_type                             0.000000
province_code                           -0.124568
activity_index                           0.302309
dtype: float64

'''


# Assuming train and test DataFrames are already loaded

def get_mixed_type_columns(df):
    # Apply a function to get the type of each element
    type_df = df.applymap(type)
    
    # Identify columns with more than one unique type
    mixed_type_columns = [col for col in type_df.columns if len(type_df[col].unique()) > 1]
    
    return mixed_type_columns

# Get columns with mixed data types in the train DataFrame
mixed_type_columns_train = get_mixed_type_columns(train)

# Get columns with mixed data types in the test DataFrame
mixed_type_columns_test = get_mixed_type_columns(test)

# Print the columns with mixed data types
print("Columns with mixed data types in Train DataFrame:")
print(mixed_type_columns_train)

print("\nColumns with mixed data types in Test DataFrame:")
print(mixed_type_columns_test)

'''
DtypeWarning: Columns (5,8,11,15) have mixed types
This includes: age, seniority, customer_type_at_beginning_of_month, and foreigner index
'''
