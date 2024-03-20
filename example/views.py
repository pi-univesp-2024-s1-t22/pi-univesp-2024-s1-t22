# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <h2>Aplicativo para o projeto integrador da univesp, ano 2024, primeiro semestre, grupo 22</h2>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)