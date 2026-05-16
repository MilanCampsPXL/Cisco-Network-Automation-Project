from ncclient import manager
import os

# Router instellingen (Dinsdag in het lab aanpassen!)
ROUTER_IP = "10.199.65.103" 
USERNAME = "admin"
PASSWORD = "password"

def take_backup():
    # Map waarin we de backup gaan opslaan
    backup_dir = '../Configs'
    backup_file = os.path.join(backup_dir, 'router_running_backup.xml')

    try:
        print(f"Verbinden met {ROUTER_IP} via NETCONF...")
        with manager.connect(host=ROUTER_IP, 
                             port=830, 
                             username=USERNAME, 
                             password=PASSWORD, 
                             hostkey_verify=False) as m:
            
            print("Actieve running-config opvragen van de router via API...")
            # m.get_config haalt de specifieke configuratie op (in dit geval 'running')
            netconf_reply = m.get_config(source='running')
            
            # De opgevraagde XML-data omzetten naar pure tekst
            raw_xml = netconf_reply.data_xml
            
            # Zorgen dat de map bestaat en de backup opslaan
            os.makedirs(backup_dir, exist_ok=True)
            with open(backup_file, 'w') as f:
                f.write(raw_xml)
                
            print(f"💾 Succes! Volledige backup succesvol opgeslagen in: {backup_file}")
            
    except Exception as e:
        print(f"Fout tijdens het maken van de backup: {e}")

if __name__ == "__main__":
    take_backup()
