from django.views.generic import View
from django.shortcuts import render
from supabase import create_client, Client
import os
from dotenv import load_dotenv


load_dotenv()


url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Crea el cliente de Supabase
supabase: Client = create_client(url, key)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Consulta de datos desde Supabase
        data = supabase.table('your_table').select('*').execute()
        context = {
            'data': data['data'],  # Datos obtenidos de Supabase
        }
        return render(request, "Pagina_Principal/index.html", context)