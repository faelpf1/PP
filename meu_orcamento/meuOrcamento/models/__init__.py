from django.db import models
from django.contrib.auth.models import User

TIPO_ORCAMENTO = { (1, 'Receita'), (2, 'Despesa'), }

from .Categoria import Categoria
from .Orcamento import Orcamento

