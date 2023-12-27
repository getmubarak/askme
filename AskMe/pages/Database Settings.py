import streamlit as st

def check_db_configured_status():
    if not st.session_state.get("DB_USER"):
        return
    if not st.session_state.get("DB_PASSWORD"):
        return
    if not st.session_state.get("DB_HOST"):
        return
    if not st.session_state.get("DB_DATABASE"):
        return

    st.session_state["database_configured"] = True
    print('Database Configured Successfully!')


st.markdown("1. Enter your Database 🔑 below\n")



db_user = st.text_input(
    "User",
    placeholder="user name here",
    value=st.session_state.get("DB_USER", ""))

db_password = st.text_input(
    "Password",
    type="password",
    placeholder="your password here",
    value=st.session_state.get("DB_PASSWORD", ""))

db_host = st.text_input(
    "Host",
    placeholder="Host here",
    value=st.session_state.get("DB_HOST", ""))

db_database = st.text_input(
    "Database",
    placeholder="Database here",
    value=st.session_state.get("DB_DATABASE", ""))

if db_user:
    st.session_state["DB_USER"] = db_user

if db_password:
    st.session_state["DB_PASSWORD"] = db_password

if db_host:
    st.session_state["DB_HOST"] = db_host

if db_database:
    st.session_state["DB_DATABASE"] = db_database

check_db_configured_status()

if not st.session_state.get("database_configured"):
    st.error("Please configure your database")
else:
    st.markdown("Datbase Configured!")

    