from ncclient import manager
import sys

# Gegevens van de router (Dinsdag aanpassen aan het lab!)
ROUTER_IP = "192.168.x.x" 
USERNAME = "admin"
PASSWORD = "password"

def deploy():
    # We lezen de XML in (normaal haal je dit uit de Configs map)
    with open('../Configs/interface_description.xml', 'r') as f:
        config_data = f.read()

    try:
        # Verbinding maken met de router via NETCONF (Poort 830)
        with manager.connect(host=ROUTER_IP, 
                             port=830, 
                             username=USERNAME, 
                             password=PASSWORD, 
                             hostkey_verify=False) as m:
            
            print(f"Verbinden met {ROUTER_IP}...")
            response = m.edit_config(target='running', config=config_data)
            print("Status: Configuratie succesvol verzonden!")
            
    except Exception as e:
        print(f"Fout tijdens deployment: {e}")

if __name__ == "__main__":
    deploy()
