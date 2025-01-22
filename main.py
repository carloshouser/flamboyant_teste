# Importações
import streamlit as st
import json
import base64
from constantes import usuarios, estilo, quadros
from territorio import territorios

# Funções Auxiliares


def add_css():
    """
    Adiciona o CSS para personalizar o layout do aplicativo.
    """
    st.markdown(estilo, unsafe_allow_html=True)


def load_json(file_path):
    """
    Carrega dados de um arquivo JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def reset_sessao():
    """
    Reseta a sessão do Streamlit.
    """
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Renderizações


def render_login():
    """
    Renderiza a tela de login.
    """
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.text_input("Usuário").strip()
    senha = st.text_input("Senha", type="password").strip()

    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            st.session_state.update({
                "logado": True,
                "usuario": usuario,
                "pagina": "home"
            })
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")


def render_home():
    """
    Renderiza a página principal com os quadros de anúncios.
    """
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.session_state["usuario"]
    permissoes = usuarios[usuario]["permissoes"]
    st.write(f"Saudações, {usuario}!")

    col1, col2 = st.columns(2)

    def render_quadros(chaves, coluna):
        for chave in chaves:
            if chave in permissoes:
                quadro = quadros[chave]
                if coluna.button(quadro["titulo"], key=f"abrir_{chave}"):
                    st.session_state.update({
                        "pagina": "visualizar",
                        "quadro_atual": chave
                    })
                    st.rerun()

    render_quadros(["a", "b", "c"], col1)
    render_quadros(["d", "e", "f"], col2)

    st.markdown(
        '<a href="https://www.dropbox.com/sh/g7i0hvmnbcd495i/AAC_vF7im3ke8-lvRGfjYQRRa?dl=0" target="_blank" style="margin-top: 20px;">📂 Acessar Designações</a>',
        unsafe_allow_html=True
    )

    if st.button("Sair"):
        reset_sessao()


def render_territorios():
    """
    Renderiza a aba de territórios.
    """
    st.title("Territórios")
    with st.sidebar:
        territorio_selecionado = st.selectbox(
            "Selecione um território", list(territorios.keys()))
        if st.button("Finalizar"):
            reset_sessao()

    arquivo = territorios[territorio_selecionado]
    st.write(arquivo)
    st.subheader(territorio_selecionado)

    with open(arquivo, "rb") as file:
        if arquivo.endswith(".png") or arquivo.endswith(".jpg"):
            st.image(file.read(), use_container_width=True)
        elif arquivo.endswith(".pdf"):
            pdf_base64 = base64.b64encode(file.read()).decode('utf-8')
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{
                    pdf_base64}" width="100%" height="1000px"></iframe>',
                unsafe_allow_html=True
            )


# Configuração Principal
add_css()

if "logado" not in st.session_state:
    render_login()
else:
    tab1, tab2, tab3 = st.tabs(["Quadro", "Eventos", "Territórios"])

    with tab1:
        if st.session_state.get("pagina") == "home":
            render_home()

    with tab2:
        events = load_json('events.json')
        st.subheader("Próximos Eventos")
        for event in events:
            st.markdown(f"### 📅 {event['date']}\n#### **{event['event']}**")
            st.divider()

    with tab3:
        render_territorios()
