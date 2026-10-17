import os
import streamlit as st
from supabase import create_client, Client

def _get_credential(key_name: str):
    """Retrieve credential first from st.secrets, then from os.environ."""
    # 1. Try streamlit secrets (Streamlit Cloud and local .streamlit/secrets.toml)
    try:
        if hasattr(st, "secrets") and key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass
    # 2. Try environment variables
    return os.getenv(key_name)

SUPABASE_URL = _get_credential("SUPABASE_URL")
SUPABASE_KEY = _get_credential("SUPABASE_KEY")

_client_instance = None

def get_supabase_client() -> Client:
    """Initialize and return the Supabase client safely."""
    global _client_instance
    if _client_instance is not None:
        return _client_instance

    url = _get_credential("SUPABASE_URL")
    key = _get_credential("SUPABASE_KEY")

    if not url or not key:
        msg = (
            "Supabase credentials are missing! Please set SUPABASE_URL and SUPABASE_KEY "
            "in Streamlit Cloud Secrets (or .streamlit/secrets.toml locally)."
        )
        try:
            st.error(f"⚠️ {msg}")
        except Exception:
            pass
        raise ValueError(msg)

    _client_instance = create_client(url, key)
    return _client_instance

class LazySupabaseClient:
    """Proxy object that delays client initialization until first attribute access."""
    def __getattr__(self, name):
        real_client = get_supabase_client()
        return getattr(real_client, name)

supabase: Client = LazySupabaseClient()