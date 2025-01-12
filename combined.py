import dataclasses

import pandas as pd
from tqdm import trange

df_email_detection = pd.read_csv("../Hybrid-Phishing-Detection-Tool/datasets/Phishing_Email.csv")
df_url = pd.read_csv("phishing_site_urls.csv")
df_email_dataset = pd.read_csv("CEAS_08.csv")

df_email_dataset.dropna(inplace=True)
df_url.dropna(inplace=True)
df_email_detection.dropna(inplace=True)

df_email_dataset.reset_index(inplace=True)
df_url.reset_index(inplace=True)
df_email_detection.reset_index(inplace=True)

expected_data = []


def df_email_dataset_to_expected_data(item):
    text = item['subject'] + " " + item['body'] + " " + item['sender']
    label = item['label']

    return {"text": text, "label": label}


def df_email_detection_to_expected_data(item):
    text = item['Email Text']
    label = item['Email Type']
    if item["Email Type"] == 'Safe Email':
        label = 0
    else:
        label = 1

    return {"text": text, "label": label}


def df_url_to_expected_data(item):
    text = item['URL']
    label = 0 if item['Label'] == "good" else 1

    return {"text": text, "label": label}


for data in df_email_dataset.to_dict("records"):
    result = df_email_dataset_to_expected_data(data)
    expected_data.append(result)

for data in df_email_detection.to_dict("records"):
    result = df_email_detection_to_expected_data(data)
    expected_data.append(result)

for data in df_url.to_dict("records"):
    result = df_url_to_expected_data(data)
    expected_data.append(result)

final_df = pd.DataFrame(expected_data)
final_df.to_csv("final_datasets.csv", index=False)



