import pandas as pd
df = pd.read_csv("/home/ids/IDS_Project/data/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")
df.columns = df.columns.str.strip()
print(df['Label'].value_counts())
df_attack = df[df['Label'] == 'PortScan']
df_benign = df[df['Label'] == 'BENIGN']
df_attack_sampled = df_attack.sample(n=len(df_benign), random_state=42)
data = pd.concat([df_benign, df_attack_sampled], ignore_index=True)
data.to_csv("/home/ids/IDS_Project/data/all.csv", index=False)
