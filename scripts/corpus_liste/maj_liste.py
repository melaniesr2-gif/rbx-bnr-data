from os.path import join

import pandas as pd

ref_date = "20260502"
old_ref_date = "20251226"

ref = pd.read_csv(join("results", "ref", f"_ref_files_{ref_date}.csv.gz"))
c = ref.groupby(["corpus_code"])["uuid"].count().reset_index()

l = pd.read_csv(join("data", "corpus_liste", "bnr_corpus.csv"))
