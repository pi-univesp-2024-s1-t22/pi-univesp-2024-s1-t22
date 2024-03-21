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
<<<<<<< HEAD
            <h3>Teste com estilização do django-admin</h3>
            <p>Acesse o <a href="https://pi-univesp-2024-s1-t22.vercel.app/admin">link</a> para ir para a página de login</p>
=======
>>>>>>> 9513f87b7ca98e5966ff6c04877acc072f437a6e
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)