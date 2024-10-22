from reactpy import component, html, run, hooks
from base_dados import obras

@component
def galeria():
    indice_obra, set_indice_obra= hooks.use_state(0)

    

    def obra_anterior(evento):
        set_indice_obra(indice_obra - 1)
    def obra_proxima(evento):
        set_indice_obra(indice_obra + 1)

    if indice_obra >= len(obras):
        set_indice_obra(len(obras) - 1)
    elif indice_obra < 0 :
        set_indice_obra (0)

    obra = obras[indice_obra]
    nome = obra['name']
    artista = obra['artist']
    descricao = obra['description']
    imagem_url = obra['url']

    componente = html.div(
        html.h3(nome), #nome
        html.img({'src': imagem_url, 'style':{'height':'200px'}}), #foto
        html.p(descricao), #descrição
        html.p(f'Artista :{artista}'), #nome: Artista
        html.button({'on_click': obra_anterior},'Anterior'),  #anterior
        html.button({'on_click': obra_proxima},'Próxima'), #próximo
        html.p(f'Obra {indice_obra} de {len(obras)}'), #obra 2/9
    )
    return componente

@component
def app():
    pagina = html.div(
        html.h1('Obras de Arte'),
        galeria(),
    )
    return pagina

run(app)