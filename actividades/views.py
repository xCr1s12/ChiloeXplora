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

class Actividad(View):
    def get(self, request, *args, **kwargs):
        # Consulta de datos desde Supabase
        # Ajusta la consulta según tus necesidades
        data = supabase.table('your_table').select('*').execute()
        
        context = {
            'data': data['data'],  # Datos obtenidos de Supabase
        }
        
        return render(request, "Actividades/actividades.html", context)