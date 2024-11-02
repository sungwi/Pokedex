import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemonkawasaki.settings')

application = get_wsgi_application()

# WhiteNoiseを利用して静的ファイルを提供する
from django.conf import settings
application = WhiteNoise(application, root=settings.STATIC_ROOT)

# Vercel互換性のため
app = application