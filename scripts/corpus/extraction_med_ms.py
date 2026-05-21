from datetime import datetime
from os.path import join

import pandas as pd

today = datetime.now().strftime("%Y%m%d")

date_ref = "20260502"
ref = pd.read_csv(join("results", "ref", f"_ref_files_{date_ref}.csv.gz"))

v_files = ref[ref["corpus_code"] == "MED_MS"]
v_files.to_csv(join("results", "corpus", f"med_ms_files_{today}.csv.gz"), index=False)

dao = pd.read_csv(join("results", "dao", "liste_dao_flat_20260430.csv.gz"))
dao = dao[~dao["nom_fichier_base"].isna()]
v_dao = dao[dao["nom_fichier_base"].str.contains("MED_MS")]
v_dao.to_csv(join("results", "corpus", f"med_ms_dao_{today}.csv.gz"), index=False)
