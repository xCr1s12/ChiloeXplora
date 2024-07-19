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

class CucaoView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        
        # Realiza la consulta a Supabase
        if query:
            # Consulta los datos basados en el término de búsqueda
            response = supabase.table('notas_cucao').select('*').ilike('campo_de_busqueda', f'%{query}%').execute()
            results = response['data']
        else:
            results = []

        context = {
            'query': query,
            'results': results,  # Agrega los resultados al contexto
        }
        return render(request, "Notas_Cucao/notas_cucao.html", context)
