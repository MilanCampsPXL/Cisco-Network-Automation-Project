from ncclient import manager
import os

# Router instellingen (Dinsdag in het lab aanpassen!)
ROUTER_IP = "192.168.x.x" 
USERNAME = "admin"
PASSWORD = "password"

def push_full_config():
    # Pad naar je volledige XML config bestand
    config_path = '../Configs/full_router_config.xml'
    
    if not os.path.exists(config_path):
        print(f"Fout: Kan het bestand {config_path} niet vinden!")
        return

    with open(config_path, 'r') as f:
        full_config_data = f.read()

    try:
        print(f"Verbinden met {ROUTER_IP} via NETCONF (poort 830)...")
        with manager.connect(host=ROUTER_IP, 
                             port=830, 
                             username=USERNAME, 
                             password=PASSWORD, 
                             hostkey_verify=False) as m:
            
            print("Volledige configuratie pushen naar de router...")
            # 'edit_config' met target 'running' voert de XML live uit
            response = m.edit_config(target='running', config=full_config_data)
            
            print("🚀 Succes! De volledige configuratie is toegepast.")
            print(f"Router response: {response}")
            
    except Exception as e:
        print(f"Fout tijdens het pushen van de configuratie: {e}")

if __name__ == "__main__":
    push_full_config()
