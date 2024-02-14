# Databricks notebook source
# MAGIC %pip install pymisp

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

MISP_ORG = 'Infoblox'
MISP_ORG_UUID = 'D1C6A726-F132-4DDC-8180-CE3A5B778E65'


# COMMAND ----------

# Function to map CSV types to MISP attribute types
def map_type_to_misp_type(csv_type):
    if csv_type == 'domain':
        return 'domain'
    elif csv_type == 'ip':  # Added ipv4 type conversion
        return 'ip-dst'
    elif csv_type == 'ipv4':  # Added ipv4 type conversion
        return 'ip-dst'
    elif csv_type == 'ipv6':  # Added ipv6 type conversion
        return 'ip-dst'
    elif csv_type == 'sha256':
        return 'sha256'
    elif csv_type == 'url':
        return 'url'
    elif csv_type == 'telfhash':
        return 'filename|sha256'  # Added telfhash type conversion
    elif csv_type == 'email':  # Added email type conversion
        return 'email-src'
    else:
        return None


# COMMAND ----------

import os
import glob
import pymisp
import json
import pandas as pd

# Define MISP configuration
organization_id = MISP_ORG_UUID

# Define the root directory
ROOT_DIR = "/Workspace/Repos/schatzistogias@infoblox.com/opengithub - threat-intelligence/indicators/"
input_subfolder = os.path.join(ROOT_DIR, "csv")
output_subfolder = os.path.join(ROOT_DIR, "misp")

# Get list of CSV files in the 'indicators' folder
csv_files = glob.glob(os.path.join(input_subfolder, '*.csv'))

# Create output folder if it doesn't exist
os.makedirs(output_subfolder, exist_ok=True)

# Create MISPOrganisation object for organization name
misp_org = pymisp.MISPOrganisation()
misp_org.name = MISP_ORG
misp_org.orgc = MISP_ORG_UUID

# Iterate over each CSV file
for csv_filepath in csv_files:
    # Read CSV file using pandas
    csv_data = pd.read_csv(csv_filepath, sep=',', header=0)

    # Convert CSV to MISP event
    misp_event = pymisp.MISPEvent()
    # misp_event.info = 'Your event info'  # Set the event info
    misp_event.orgc = misp_org  # Set organization

    # Set MISP event attributes
    misp_event.info = os.path.basename(csv_filepath)[:-4]

    # Iterate over each row in the CSV data and add attributes to the MISP event
    for index, row in csv_data.iterrows():
        # attribute = pymisp.MISPAttribute()
        a_value = row['indicator'].replace('[.]', '.')  # Set the attribute value
        a_type = map_type_to_misp_type(row['type'])  # Set the attribute type
        if a_type is None:
            print(row['type'])
        # attribute.category = 'Your category'  # Set the attribute category
        misp_event.add_attribute(type=a_type, value=a_value)

    # Convert MISP event to JSON
    misp_json = json.dumps(misp_event.to_json())

    # Save JSON to 'misp' folder with the same filename
    csv_filename = os.path.basename(csv_filepath)
    json_path = os.path.join(output_subfolder, os.path.splitext(csv_filename)[0] + '.json')
    with open(json_path, 'w') as misp_json_file:
        misp_json_file.write(misp_event.to_json(indent=2))

# COMMAND ----------


