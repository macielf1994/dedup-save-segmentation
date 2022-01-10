from connection import db_connection

conn = db_connection()
cursor = conn.cursor()

list_base_names_in_stage = [
    't_affluent_recovery_aff_black_20211229',
    't_affluent_recovery_aff_platinum_20211229'
    ]

def get_list_bases_sorted(list_base_names: list):
    base_names_vol_dict = {}
    for base in list_base_names:
        base_select = f"select count(customer_id) from stg.{base}"
        cursor.execute(base_select)

        count_rows_base = list(cursor)[0][0]
        base_names_vol_dict.update({base: count_rows_base})

    sort_by_count_vol_bases = sorted(base_names_vol_dict.items(), key=lambda base_count: base_count[1], reverse=True)
    
    return sort_by_count_vol_bases

def deduplicate_between_bases(dict_sorted_bases: dict):
    for base_in_deduplication in dict_sorted_bases:
        new_list_for_compare = list(dict_sorted_bases)
        for base_for_deduplicate in new_list_for_compare:
            if base_in_deduplication[0] != base_for_deduplicate[0]:
                print(f'{base_in_deduplication[1]} deduplicate {base_for_deduplicate[1]}')
        

deduplicate_between_bases(get_list_bases_sorted(list_base_names_in_stage))