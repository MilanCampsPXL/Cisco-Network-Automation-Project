from ncclient import manager
import os

# Gegevens van jouw specifieke lab-router
ROUTER_IP = "10.199.65.103" 
USERNAME = "admin"
PASSWORD = "password"

def push_full_config():
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
            
            # Stap 1: Lock de candidate datastore (Task 22)
            print("Locking candidate datastore...")
            m.lock(target='candidate')
            
            try:
                print("Configuratie stagen in de candidate datastore (Task 36)...")
                # We pushen de configuratie specifiek naar 'candidate' in plaats van 'running'
                m.edit_config(target='candidate', config=full_config_data)
                
                print("Wijzigingen valideren en plegen (Commit naar running)...")
                # Pas als dit lukt, wordt het definitief actief
                m.commit()
                print("🚀 Volledige deployment succesvol afgerond!")
                
            except Exception as eval_error:
                print(f"⚠️ Fout tijdens staging/validation: {eval_error}")
                print("Fout gedetecteerd! Wijzigingen in de candidate weggooien (discard-changes)...")
                # Foutafhandeling eist discard-changes volgens Task 36
                m.discard_changes()
                
            finally:
                # Altijd netjes unlocken
                print("Unlocking candidate datastore...")
                m.unlock(target='candidate')
            
    except Exception as e:
        print(f"Fout tijdens de NETCONF-sessie: {e}")

if __name__ == "__main__":
    push_full_config()
