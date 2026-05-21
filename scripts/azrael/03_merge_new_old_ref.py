from os.path import join

import pandas as pd

old_ref_date = "20251226"
new_ref_date = "20260502"

ref = pd.read_csv(join("results", "ref", f"_ref_files_{old_ref_date}.csv.gz"))
tmp = pd.read_csv(
    join("results", "ref", f"_ref_files_{new_ref_date}_tmp_s3_dao_oai.csv.gz")
)
tmp = tmp[~tmp["name"].isna()]

m1 = tmp.merge(ref, on=["uuid", "checksum_md5"], how="left")

nc = ["uuid", "checksum_md5"]
nc.extend(list(set(ref.columns) ^ set(tmp.columns)))
new_columns = []
for c in m1.columns:
    if c in nc:
        new_columns.append(c)
    elif c[-2:] == "_x":
        if c == "mix_xSamplingFrequency_x":
            new_columns.append("mix_xSamplingFrequency_new")
        else:
            new_columns.append(c.replace("_x", "_new"))
    elif c[-2:] == "_y":
        new_columns.append(c.replace("_y", "_old"))

m1.columns = new_columns

"""
ref.columns = ['name', 'path', 'size', 'last_content_modification_date',
       'last_metadata_modification_date', 'checksum_md5', 'uuid', 'extension',
       'file_type', 'source2s3', 'conservation_statut', 'finding_aid',
       'unitid', 'osiros_id', 'mix_objectIdentifierValue', 'mix_fileSize',
       'mix_dateTimeCreated', 'mix_formatName', 'mix_byteOrder',
       'mix_compressionScheme', 'mix_imageWidth', 'mix_imageHeight',
       'mix_xSamplingFrequency', 'mix_ySamplingFrequency',
       'mix_samplingFrequencyUnit', 'mix_colorSpace',
       'mix_scanningSoftwareName', 'mix_formatVersion', 'publication_statut',
       'corpus_code', 'oai_set', 's3_key', 's3_uploaded', 's3_uploaded_date',
       's3_bucket']
on découpe le dataframe en segments :
    - ce qui relève de az : 'name', 'path', 'size', 'last_content_modification_date',
           'last_metadata_modification_date', 'checksum_md5', 'uuid', 'extension',
           'file_type', 'source2s3',
    - ce qui relève de s3 : 's3_key', 's3_uploaded', 's3_uploaded_date', 's3_bucket'
    - ce qui relève de oai et dao : 'oai_set', 'finding_aid', 'unitid', 'osiros_id'
    - ce qui relève de mix : 'mix_objectIdentifierValue', 'mix_fileSize', 'mix_dateTimeCreated',
    'mix_formatName', 'mix_byteOrder', 'mix_compressionScheme', 'mix_imageWidth', 'mix_imageHeight',    'mix_xSamplingFrequency', 'mix_ySamplingFrequency',
    'mix_samplingFrequencyUnit', 'mix_colorSpace', 'mix_scanningSoftwareName', 'mix_formatVersion'
    - ce qui relève d'information sur le traitement des fichiers : 'conservation_statut', 'corpus_code', 'publication_statut'
"""

# ce qui relève de az : attention à uuid, extension, file_type, source2s3
len(m1[m1["uuid"].isna()])
len(m1[m1["extension_new"].isna()])
m1.loc[m1["extension_new"].isna(), "extension_new"] = m1.loc[
    m1["extension_new"].isna(), m1["name_new"].str.extract(r".*(\..*)$")
]
