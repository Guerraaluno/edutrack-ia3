import streamlit as st

st.title('Meu Perfil')

st.subheader('Informações Pessoais')

tab_alocar_informa, = st.tabs(["Inserir Dados Pessoais"])

with tab_alocar_informa:
    st.subheader ("Inserir Dados Pessoais")
    with st.form("form_perfil"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        instituicao = st.text_input("Instituição de Ensino")
        tipo_instituicao = st.selectbox("Tipo de Instituição", ["Escola", "Faculdade"])
        if tipo_instituicao == "Escola":
            periodo = st.selectbox("Ano", ["6ºF", "7ºF", "8ºF", "9ºF", "1ºM", "2ºM", "3ºM"])
        elif tipo_instituicao == "Faculdade":
            curso = st.text_input("Curso")
            periodo = st.selectbox("Semestre", ["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º", "9º", "10º", "11º", "12º"])
        
        submitted = st.form_submit_button("Salvar")
        if submitted:
            st.success(f"Perfil atualizado! (Simulação)")