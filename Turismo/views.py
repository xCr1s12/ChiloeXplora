from django.shortcuts import render
from django.views.generic import View
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de Supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Crea el cliente de Supabase
supabase: Client = create_client(url, key)

class TurismoListViews(View):
    def get(self, request, *args, **kwargs):
        # Consulta los lugares recomendados desde Supabase
        response = supabase.table('lugares_recomendados').select('*').execute()
        lugares_recomendados = response['data']

        context = {
            'lugares_recomendados': lugares_recomendados,  # Datos obtenidos de Supabase
        }
        return render(request, "Lugares_Recomendados/Recomendados.html", context)
