from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente, ConsultaHistorico

@receiver(post_save, sender=Cliente)
def cliente_post_save(sender, instance, **kwargs):
    """
    Cria um registro no histórico de consultas sempre que um cliente é atualizado.
    """
    if not kwargs.get('created', False):
        ConsultaHistorico.objects.create(
            cnpj=instance.cnpj,
            regime_fiscal=instance.regime_fiscal.nome if instance.regime_fiscal else None,
            tipo_empresa=instance.tipo_empresa.nome if instance.tipo_empresa else None,
            data_inclusao=instance.data_inclusao,
            data_exclusao=instance.data_exclusao,
            escritorio=instance.escritorio.nome if instance.escritorio else None,
        )
