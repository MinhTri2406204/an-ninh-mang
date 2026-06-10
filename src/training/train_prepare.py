#import pandas as pd
#import glob

#files=glob.glob("/home/ids/IDS_Project/data/Monday-WorkingHours.pcap_ISCX.csv")
#files=glob.glob("/home/ids/IDS_Project/data/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")

#df=[]

#for f in files:

#    try:
#        x=pd.read_csv(f)

#        df.append(x)

#    except:

#        pass

#data=pd.concat(df)

#print(data.shape)

#data.to_csv("all.csv", index=False)

#print(data.head())

import pandas as pd

#df_benign = pd.read_csv("/home/ids/IDS_Project/data/Monday-WorkingHours.pcap_ISCX.csv")
df = pd.read_csv("/home/ids/IDS_Project/data/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")

#label_col=' Label' if ' Label' in df_attack.columns else 'Label'
df.columns = df.columns.str.strip()
print(df['Label'].value_counts())
df_attack = df[df['Label'] == 'PortScan']
df_benign = df[df['Label'] == 'BENIGN']
df_attack_sampled = df_attack.sample(n=len(df_benign), random_state=42)
data = pd.concat([df_benign, df_attack_sampled], ignore_index=True)

data.to_csv("/home/ids/IDS_Project/data/all.csv", index=False)
