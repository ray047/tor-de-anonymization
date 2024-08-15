from scapy.all import sniff, IP, TCP
import json

captured_data = []

def capture_packets(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"Captured Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            data = {
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "src_port": src_port,
                "dst_port": dst_port,
                "payload": packet[TCP].payload.load if packet[TCP].payload else None
            }
            captured_data.append(data)

sniff(filter="tcp", prn=capture_packets, count=100)

with open('../data/captured_data.json', 'w') as f:
    json.dump(captured_data, f, indent=4)
