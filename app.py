from flask import Flask, render_template, redirect, request
from monitor import checar_ping , checar_http
from database import criar_tabela, listar_dispositivos, listar_dispositivos, salvar_log, adicionar_dispositivo, excluir_tabela

app = Flask(__name__)
criar_tabela()

@app.route('/remover/<int:id>', methods=['POST'])
def remover(id):
    excluir_tabela(id)
    return redirect('/')
@app.route('/add', methods=['POST'])
def adicionar():
    nome=request.form.get('nome')
    host=request.form.get('host')
    url=request.form.get('url')
    adicionar_dispositivo(nome, host, url)
    return redirect('/')
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
        res_ping = checar_ping(dispositivo['host'])
        if res_ping:
            ping_status = f"ONLINE ({res_ping})"if isinstance(res_ping, str) else "ONLINE"


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
