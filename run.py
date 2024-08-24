import pandas as pd

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

print(train.columns)
print(test.columns)
