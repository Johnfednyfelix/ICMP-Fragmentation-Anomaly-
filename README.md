# ICMP-Fragmentation-Anomaly

## 🚀 Purpose
This project simulates a fragmented ICMP Echo Request with a deliberate anomaly: the **middle fragment is skipped**, which prevents proper reassembly at the destination. This setup is ideal for testing how systems, firewalls, or network monitoring tools handle **incomplete or evasive packet sequences**.

## 🖼️ Topology / Diagram
Target host (e.g., MacBook) is reachable on the same LAN. Script is executed from a Windows 11 machine using Python + Scapy.

```
[Windows 11 Scapy Host] ───> [Target: 192.168.1.248 (MacBook)]
                   ICMP Echo Fragments #1 and #3 only
```

## ⚙️ How It Works
- Payload of 4000 bytes is split into 3 pieces manually.
- Only **fragment 1** (offset=0, MF=1) and **fragment 3** (offset=370, MF=0) are sent.
- Fragment 2 is intentionally omitted.
- Reassembly fails silently; **no Echo Reply** is ever returned.

## 🧪 Example Run
```bash
python broken_icmp_fragments.py
```

Expected output:
```
.
Sent 1 packets.
.
Sent 1 packets.
```

Wireshark (on target) will show:
- Two incomplete fragments
- IP ID: 12345 (same for both)
- No ICMP Echo Reply
- Fragmentation reassembly failure

## 🛠️ Setup Instructions
1. Install Scapy:
```bash
pip install scapy
```
2. Update the target IP in the script (`target = "192.168.1.248"`).
3. Run the script from Command Prompt:
```bash
python broken_icmp_fragments.py
```

## ⚠️ Error Handling / Edge Cases
- Make sure Scapy is installed and allowed through Windows Firewall.
- The target host must be online and reachable.
- Requires admin or elevated permissions to send raw packets on some systems.

## 🔁 How to Extend
- Send all three fragments to observe successful reassembly.
- Skip other fragments (first or last) to test alternative failure modes.
- Adapt for UDP, DNS, or TCP payloads for protocol-specific evasion tests.

## 🧾 Version History
- v1.0: Initial ICMP fragment gap simulation

## 🧠 Author
John Felix  
GitHub: [https://github.com/Johnfednyfelix]  
LinkedIn: [https://www.linkedin.com/in/johnfelix/]
