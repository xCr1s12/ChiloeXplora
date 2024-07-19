from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Carga las variables de entorno
load_dotenv()

# Obtén las variables de entorno
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Verifica que las variables no estén vacías
if not supabase_url or not supabase_key:
    raise ValueError("Las variables de entorno SUPABASE_URL y SUPABASE_KEY deben estar configuradas")

# Crea el cliente de Supabase
supabase: Client = create_client(supabase_url, supabase_key)
