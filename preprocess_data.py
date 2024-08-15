import json
import pandas as pd

with open('../data/captured_data.json') as f:
    traffic_data = json.load(f)

with open('../data/circuit_data.json') as f:
    circuit_data = json.load(f)

traffic_df = pd.DataFrame(traffic_data)
circuit_df = pd.DataFrame(circuit_data)

merged_data = pd.merge(traffic_df, circuit_df, left_on='src_ip', right_on='path', how='left')

merged_data.dropna(subset=['src_ip', 'dst_ip'], inplace=True)

merged_data['src_ip'] = merged_data['src_ip'].apply(lambda x: x.strip())
merged_data['dst_ip'] = merged_data['dst_ip'].apply(lambda x: x.strip())

merged_data['vpn_usage'] = merged_data['vpn_usage'].apply(lambda x: 1 if x == 'Yes' else 0)

merged_data['packet_length'] = merged_data['payload'].apply(lambda x: len(x) if x else 0)

merged_data['timestamp'] = pd.to_datetime(merged_data['timestamp'])
merged_data['inter_arrival_time'] = merged_data['timestamp'].diff().fillna(pd.Timedelta(seconds=0)).dt.total_seconds()

features = merged_data[['src_ip', 'dst_ip', 'src_port', 'dst_port', 'packet_length', 'inter_arrival_time']]
labels = merged_data['vpn_usage']

features.to_csv('../data/features.csv', index=False)
labels.to_csv('../data/labels.csv', index=False)
