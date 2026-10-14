import subprocess
import requests

def checar_ping(host):
    comando = ['ping', '-n', '1', host]
    try:
        resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if resultado.returncode == 0:
            return True
    except subprocess.CalledProcessError:
        return False

def checar_http(host):
    try:
        resposta = requests.get(host, timeout=5)
        if resposta.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        return False
if __name__ == '__main__':
    teste_host = "127.0.0.1" # DNS do Google (quase sempre online)
    teste_url = "https://www.google.com"
    
    print(f"Testando Ping em {teste_host}: {'ONLINE' if checar_ping(teste_host) else 'OFFLINE'}")
    print(f"Testando HTTP em {teste_url}: {'ONLINE' if checar_http(teste_url) else 'OFFLINE'}")