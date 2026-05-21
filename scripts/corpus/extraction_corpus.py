from datetime import datetime
from os.path import join

import pandas as pd

today = datetime.now().strftime("%Y%m%d")

date_ref = "20260502"
print("Chargement des fichiers de données")
ref = pd.read_csv(join("results", "ref", f"_ref_files_{date_ref}.csv.gz"))
dao = pd.read_csv(join("results", "dao", "liste_dao_flat_20260430.csv.gz"))
dao = dao[~dao["nom_fichier_base"].isna()]

corpus_codes = ['MED_AFF',
'MED_AVI',
'MED_CHA',
#'MED_CP',
'MED_DIL',
'MED_EPH',
'MED_FAN',
'MED_FLR',
'MED_FOO',
'MED_IMA',
'MED_JOU',
'MED_LAI',
'MED_LET',
'MED_MAR',
'MED_MON',
#'MED_MS',
'MED_NPT',
'MED_PAR',
'MED_PBI',
'MED_PER',
'MED_PHD',
'MED_PHO',
'MED_PLA',
'MED_PUB',
'MED_VAI',
'MED_VDM',
'MED_VID']

for corpus_code in corpus_codes :
    print(f"Traitement du corpus {corpus_code}")
    v_files = ref[ref["corpus_code"] == corpus_code]
    v_files.to_csv(join("results", "corpus", f"{corpus_code}_files_{today}.csv.gz"), index=False)
    print(f"-- {len(v_files)} fichiers")
    
    v_dao = dao[dao["nom_fichier_base"].str.contains(corpus_code)]
    v_dao.to_csv(join("results", "corpus", f"{corpus_code}_dao_{today}.csv.gz"), index=False)
    print(f"-- {len(v_dao)} dao")