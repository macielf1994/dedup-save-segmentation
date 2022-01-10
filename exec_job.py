from dbops.deduplications import DeduplicateBases

deduplications_config = {
    'list_base_names' : [
    't_affluent_recovery_aff_black_20211229',
    't_affluent_recovery_aff_platinum_20211229',
    't_maste0140_dbm041_interesse_mass_20210610',
    't_maste0140_dbm042_regional_affluent_20210710'
    ]
}


DeduplicateBases(deduplications_config)