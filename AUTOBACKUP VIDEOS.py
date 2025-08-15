import os
import subprocess
import time
from datetime import datetime


def baixar(plataforma, link, pasta):
    print(f"[{datetime.now()}] Baixando de {plataforma}...")
    subprocess.run([
        "yt-dlp",
        "-P", pasta,
        "-o", "%(upload_date)s_%(title)s.%(ext)s",
        "--download-archive", os.path.join(pasta, "baixados.txt"),
        link
    ])

# Pastas 
PASTAS = {
    "youtube": os.path.join(os.getcwd(), "YouTube"),
    "tiktok": os.path.join(os.getcwd(), "TikTok"),
    "instagram": os.path.join(os.getcwd(), "Instagram")
}

LINKS = {
     "youtube": "https://www.youtube.com/@Matiass270",
    "tiktok": "COLE_AQUI_O_LINK_DO_TIKTOK",
    "instagram": "COLE_AQUI_O_LINK_DO_INSTAGRAM"
}


for pasta in PASTAS.values():
    if not os.path.exists(pasta):
        os.makedirs(pasta)

# Loop 
while True:
    for plataforma, link in LINKS.items():
        baixar(plataforma, link, PASTAS[plataforma])
    print(f"[{datetime.now()}] Aguardando próxima verificação...")
    time.sleep(3600)  # Espera 1 hora antes de checar de novo
