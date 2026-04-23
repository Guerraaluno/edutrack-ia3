import streamlit as st

st.title('Cartas de Estudo')

st.info('Aqui você pode criar e organizar suas cartas de estudo para revisão rápida.')

container_carta = st.container()

with container_carta:
    with st.form("form_carta"):
        nome = st.text_input("Nome da Carta")
        descrição = st.text_input("Descrição")
        resposta = st.text_input("Resposta")

        submitted = st.form_submit_button("Salvar")
        if submitted:
            st.success(f"Carta Feita! (Simulação)")