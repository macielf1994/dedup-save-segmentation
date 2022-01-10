from connection import db_connection

conn = db_connection()
cursor = conn.cursor()

list_base_names_in_stage = [
    't_affluent_recovery_aff_black_20211229',
    't_affluent_recovery_aff_platinum_20211229'
    ]

def get_list_bases_vol_sorted_in_dict(list_base_names: list):
    base_names_vol_dict = {}
    for base in list_base_names:
        base_select = f"select count(customer_id) from stg.{base}"
        cursor.execute(base_select)

        count_rows_base = list(cursor)[0][0]
        base_names_vol_dict.update({base: count_rows_base})

    sort_by_count_vol_bases = sorted(base_names_vol_dict.items(), key=lambda base_count: base_count[1], reverse=True)
    
    return sort_by_count_vol_bases

dict_bases_and_vol = get_list_bases_vol_sorted_in_dict(list_base_names_in_stage)

print(dict_bases_and_vol)