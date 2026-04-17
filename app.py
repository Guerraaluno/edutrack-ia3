import os
import streamlit as st

from subjects_service import (
    create_subject,
    delete_subject,
    get_subjects,
    update_subject,
)

# Configuração da Página (Título na aba do navegador)
st.set_page_config(page_title="EduTrack AI", page_icon="🎓")

# Título Principal
st.title("🎓 EduTrack AI")

# Sidebar (Menu Lateral)
st.sidebar.header("Menu")
menu_option = st.sidebar.radio("Navegar", ["Dashboard", "Disciplinas", "Tarefas"])

if menu_option == "Dashboard":
    st.write("Bem-vindo ao seu assistente acadêmico!")
    st.info("Conecte ao Xano para ver seus dados reais.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Disciplinas Ativas", "0")
    col2.metric("Tarefas Pendentes", "0")

elif menu_option == "Disciplinas":
    st.subheader("Minhas Disciplinas")

    xano_base_url = os.getenv("XANO_BASE_URL", "")
    if xano_base_url:
        st.info(f"Conectado ao backend Xano em {xano_base_url}")
    else:
        st.warning(
            "XANO_BASE_URL não está configurado. Usando armazenamento local em subjects_data.json."
        )

    try:
        subjects = get_subjects()
    except Exception as exc:
        st.error(f"Erro ao carregar disciplinas: {exc}")
        subjects = []

    active_count = sum(1 for subject in subjects if subject.get("active", True))
    col1, col2 = st.columns(2)
    col1.metric("Disciplinas Ativas", active_count)
    col2.metric("Total de Disciplinas", len(subjects))

    with st.form("create_subject"):
        new_name = st.text_input("Nome da disciplina")
        new_description = st.text_area("Descrição (opcional)")
        new_active = st.checkbox("Ativa", value=True)
        submitted = st.form_submit_button("Adicionar disciplina")

        if submitted:
            if not new_name.strip():
                st.error("Por favor informe o nome da disciplina.")
            else:
                try:
                    create_subject(new_name.strip(), new_description.strip(), new_active)
                    st.success("Disciplina criada com sucesso.")
                    st.experimental_rerun()
                except Exception as exc:
                    st.error(f"Falha ao criar disciplina: {exc}")

    if subjects:
        st.markdown("### Disciplinas cadastradas")

        for subject in subjects:
            subject_id = subject.get("id")
            if subject_id is None:
                continue

            with st.expander(subject.get("name", "Disciplina sem nome")):
                current_name = st.text_input(
                    "Nome",
                    value=subject.get("name", ""),
                    key=f"name-{subject_id}",
                )
                current_description = st.text_area(
                    "Descrição",
                    value=subject.get("description", ""),
                    key=f"description-{subject_id}",
                )
                current_active = st.checkbox(
                    "Ativa",
                    value=subject.get("active", True),
                    key=f"active-{subject_id}",
                )

                cols = st.columns([3, 1])
                with cols[0]:
                    if st.button("Salvar alterações", key=f"save-{subject_id}"):
                        try:
                            update_subject(
                                subject_id,
                                current_name.strip(),
                                current_description.strip(),
                                current_active,
                            )
                            st.success("Disciplina atualizada com sucesso.")
                            st.experimental_rerun()
                        except Exception as exc:
                            st.error(f"Falha ao atualizar disciplina: {exc}")

                with cols[1]:
                    if st.button("Excluir disciplina", key=f"delete-{subject_id}"):
                        try:
                            delete_subject(subject_id)
                            st.success("Disciplina excluída com sucesso.")
                            st.experimental_rerun()
                        except Exception as exc:
                            st.error(f"Falha ao excluir disciplina: {exc}")
    else:
        st.info("Nenhuma disciplina cadastrada ainda.")

elif menu_option == "Tarefas":
    st.subheader("Gerenciamento de Tarefas")
    st.checkbox("Exemplo: Estudar Streamlit")
