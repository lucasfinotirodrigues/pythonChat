# Título 
# Botão iniciar chat
    # Modal
        # Título: Bem vindo ao HashZap
        # Campo de texto: Escreva seu nome no chat
        # Botão: Entrar no chat
            # Sumir com o título e o botão inicial
            # Fechar o modal
            # Criar o chat (Com a mensagem de "Nome entrou no chat")
            # Embaixo do chat 
                #Campo de texto: Digite sua mensagem
                # Botão enviar
                    # Mensagem no chat com o nome do usuário e a mensagem digitada
                    # Finoti: Salve

# Importando o framework
import flet as ft

# Criando função principal

def main(pagina):

    titulo = ft.Text("HashZap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    titulo_modal = ft.Text("Bem-vindo(a) ao HashZap")
    campo_nome = ft.TextField(label="Insira seu nome")

    def enviar_mensagem(evento):
        texto = f"{campo_nome.value}: {texto_mensagem.value}"

        chat.controls.append(ft.Text(texto))

        pagina.pubsub.send_all(texto)


        texto_mensagem.value = ''

        pagina.update()     

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar_mensagem])
    chat = ft.Column()
    
    def entrar_chat(evento):

        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        modal.open = False    

        pagina.add(chat)
        pagina.add(linha_mensagem)

        texto_entrou_chat = f"{campo_nome.value} Entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)
   
        pagina.update()





    botao_entrar= ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    modal = ft.AlertDialog(
        title = titulo_modal,
        content = campo_nome,
        actions = [botao_entrar]
    )

    def abrir_modal(evento):
        pagina.dialog = modal
        modal.open = True
        pagina.update()
        

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_modal)

    pagina.add(titulo)
    pagina.add(botao_iniciar)



ft.app(main, view=ft.WEB_BROWSER)
