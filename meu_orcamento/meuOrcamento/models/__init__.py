from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

PRIVILEGIO = { (1, 'Administrador'), (2, 'Usuário'), }
TIPO_ORCAMENTO = { (1, 'Receita'), (2, 'Despesa'), }

from .Categoria import Categoria
from .Orcamento import Orcamento
from .Perfil import Perfil
