from flask import Flask, render_template
from monitor import checar_ping , checar_http
from database import criar_tabela, listar_dispositivos, listar_dispositivos, salvar_log

app = Flask(__name__)
criar_tabela()


@app.route('/')
def home():
    lista_final = []
    dispositivos = listar_dispositivos()
    for disp_tuple in dispositivos:
        dispositivo = {
            'id': disp_tuple[0],
            'nome': disp_tuple[1],
            'host': disp_tuple[2],
            'url': disp_tuple[3]
        }
        if checar_ping(dispositivo['host']):
            ping_status = 'ONLINE'
        else:
            ping_status = 'OFFLINE'
        if checar_http(dispositivo['url']):
            http_status = 'ONLINE'
        else:
            http_status = 'OFFLINE'
        salvar_log(dispositivo['nome'], ping_status, http_status)
        lista_final.append(dispositivo)
        dispositivo['ping_status'] = ping_status
        dispositivo['http_status'] = http_status
    return render_template('index.html', dispositivos=lista_final )
if __name__ == '__main__':
    app.run(debug=True)
