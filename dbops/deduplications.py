from connection import db_connection

conn = db_connection()
cursor = conn.cursor()

list_base_names_in_stage = [
    't_affluent_recovery_aff_black_20211229',
    't_affluent_recovery_aff_platinum_20211229',
    't_maste0140_dbm041_interesse_mass_20210610',
    't_maste0140_dbm042_regional_affluent_20210710'
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
                query_deduplicate = f"""delete from stg.{base_in_deduplication[0]} where customer_id in (select customer_id from stg.{base_for_deduplicate[0]};"""
                print(query_deduplicate)

def self_deduplicate_values(list_base_names: list):
    for base in list_base_names:
        self_deduplicate_query = f"""delete from stg.{base} dm where exists (select email from stg.{base} ss where dm.email = ss.email and dm.customer_id < ss.customer_id);"""
        print(self_deduplicate_query)


self_deduplicate_values(list_base_names_in_stage)
deduplicate_between_bases(get_list_bases_sorted(list_base_names_in_stage))