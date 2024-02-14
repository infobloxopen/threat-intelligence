# Databricks notebook source
from cyberlib import data_enrichment as de
from pyspark.sql import functions as sqlfn
import datetime
import os
import pandas as pd
import re

# COMMAND ----------

ROOT_DIR = "/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv"

# Read all csvs from the indicators folder
csv_files = [file for file in os.listdir(ROOT_DIR) if file.endswith(".csv")]

# COMMAND ----------

old_detected_date_column_name = 'detected'
new_detected_date_column_name = 'detected_date'

dataframes = []
for file in csv_files:
    filepath = os.path.join(ROOT_DIR, file)
    original = pd.read_csv(filepath)
    detected_columns = [i for i in original.columns if old_detected_date_column_name in i]
    original = original.drop(detected_columns,axis=1)

    original["indicator"] = original["indicator"].apply(lambda x: x.replace("[.]", "."))

    df2 = spark.createDataFrame(original[["indicator"]])
    df_enriched = (
        de.enrich_with_ikb_data(df2, join_field="indicator")
        .withColumn("submitted", sqlfn.to_date("submitted"))
        .select("indicator", "submitted")
        .withColumnRenamed("submitted", new_detected_date_column_name)
        .toPandas()
    )
    final = original.merge(df_enriched, on='indicator', how='inner')
    final["indicator"] = final["indicator"].apply(lambda x: x.replace(".", "[.]"))

    final.to_csv(filepath, index=False)
    

# COMMAND ----------

to_be_manually_reviewed = []

for file in csv_files:
    filepath = os.path.join(ROOT_DIR, file)
    original = pd.read_csv(filepath)
    print(f"""
          filepath : {filepath}, 
          columns : {[i for i in original.columns]}""")
    data = pd.read_csv(filepath)
    if len(data[data[new_detected_date_column_name].isna()])>0:
        print('Needs manual review')
        to_be_manually_reviewed.append(filepath)

# COMMAND ----------

to_be_manually_reviewed

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ## Add the dates from the filename as detected_dates

# COMMAND ----------

filepaths_to_fix = ['/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv/metacoin_cta_20221109_iocs.csv',
 '/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv/vextrio_cta_20240123_iocs.csv',
 '/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv/decoy_dog_cta_20230714_iocs.csv',
 '/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv/decoy_dog_cta_20230420_iocs.csv',
 '/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv/emotet_cta_20221006_iocs.csv']

for filepath_to_fix in filepaths_to_fix:
    try:
        fix_date = str(datetime.datetime.strptime(re.findall('202\d+',filepath_to_fix)[0],'%Y%m%d').date())
        print(f"filling with {fix_date} date")
    except:
        fix_date = str(datetime.date.today())
        print("filling with todays date")

    to_fix = pd.read_csv(filepath_to_fix)
    to_fix.loc[to_fix[new_detected_date_column_name].isna(),new_detected_date_column_name] = fix_date
    to_fix.to_csv(filepath_to_fix,index=False)

# COMMAND ----------

to_fix = pd.read_csv(filepaths_to_fix[0])

# COMMAND ----------

for i in filepaths_to_fix:
    print(i)
    print(f"NOT fixed : {len(to_fix[to_fix.detected_date.isna()])}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Get rid of the source column
# MAGIC
# MAGIC

# COMMAND ----------

for file in csv_files:
    filepath = os.path.join(ROOT_DIR, file)
    loaded_data = pd.read_csv(filepath)
    if 'source' in loaded_data.columns:
        loaded_data  = loaded_data.drop('source',axis=1)
        print(f"removed source from : {filepath}")
    loaded_data.to_csv(filepath,index=False)

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC # Get rid of the notes and references columns

# COMMAND ----------

for file in csv_files:
    filepath = os.path.join(ROOT_DIR, file)
    loaded_data = pd.read_csv(filepath)
    cols_to_drop = []
    if 'notes' in loaded_data.columns:
        cols_to_drop.append('notes')
    if 'references' in loaded_data.columns:
        cols_to_drop.append('references')
    if cols_to_drop:
        loaded_data = loaded_data.drop(cols_to_drop, axis=1)
        print(f"removed {', '.join(cols_to_drop)} from : {filepath}")
    loaded_data.to_csv(filepath,index=False)


# COMMAND ----------

[
 '/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv/ukraine_russia_legitimate_iocs.csv',
 '/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/csv/ukraine_russia_malicous_suspicious_iocs.csv',
 ]
