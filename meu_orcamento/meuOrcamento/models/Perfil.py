from meuOrcamento.models import *

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    privilegio = models.IntegerField(choices=PRIVILEGIO, default=2)
    orcamento = models.ManyToManyField(Orcamento, blank=True, related_name='orcamentos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self) -> str:
        return '{}'.format(self.usuario.username)


    @receiver(post_save, sender=User)
    def criar_usuario(sender, instance, created, **kwargs):
        try:
            if created:
                Perfil.objects.create(usuario=instance)
        except:
            pass


    @receiver(post_save, sender=User)
    def salvar_usuario(sender, instance, created, **kwargs):
        try:
            if created:
                instance.perfil.save(usuarior=instance)
        except:
            pass