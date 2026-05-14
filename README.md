# Cisco Network Automation Project 🚀

Dit project is ontwikkeld voor de PE van Network Automation. Het doel is om een Cisco IOS-XE device te configureren middels **NETCONF** en **Python**, waarbij GitHub fungeert als de **Single Source of Truth**.

## 📂 Project Structuur
- `Configs/`: Bevat de XML-templates voor de interface configuraties (YANG-gebaseerd).
- `Scripts/`: Bevat het Python-script (`deploy_config.py`) dat gebruik maakt van `ncclient`.

## 🛠️ Technologieën
- **Taal:** Python 3.x
- **Protocol:** NETCONF (Poort 830)
- **Library:** `ncclient`
- **Omgeving:** Docker (YANG Suite voor analyse)
- **Versiebeheer:** Git / GitHub

## 🚀 Hoe te gebruiken
1. Clone de repository:
   `git clone https://github.com/MilanCampsPXL/Cisco-Network-Automation-Project.git`
2. Installeer de benodigde packages:
   `pip install ncclient`
3. Pas de IP-gegevens in `Scripts/deploy_config.py` aan naar de lab-router.
4. Run het script:
   `python Scripts/deploy_config.py`

## 👨‍💻 Troubleshooting (PE Bewijslast)
Tijdens dit project is er uitvoerig gedebugged op:
- Docker container orchestratie (CRLF vs LF issues).
- Handmatige SSL-certificaat generatie via OpenSSL voor Nginx TLS-terminatie.
- YANG-model analyse via de Cisco YANG Suite.
