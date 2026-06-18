from django.db import models

# Create your models here.

class TipoQuarto(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome}"


class StatusReserva(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome}"


class Quarto(models.Model):
    numero = models.CharField(max_length=30)
    tipo_quarto = models.ForeignKey(TipoQuarto, on_delete=models.PROTECT)
    capacidade = models.PositiveSmallIntegerField()
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="valor da diária")
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.numero}"


class Hospede(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, blank=True, default="")
    telefone = models.CharField(max_length=15, blank=True, default="")
    email = models.EmailField(blank=True, default="")

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"


class Reserva(models.Model):
    hospede = models.ForeignKey(Hospede, on_delete=models.PROTECT)
    quarto = models.ForeignKey(Quarto, on_delete=models.PROTECT)
    data_checkin = models.DateTimeField(verbose_name="data de check-in")
    data_checkout = models.DateTimeField(verbose_name="data de check-out")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="valor total")
    status = models.ForeignKey(StatusReserva, on_delete=models.PROTECT)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    cadastrado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.hospede} - {self.quarto} ({self.data_checkin})"


class Hospedagem(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT)
    data_entrada = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="data de entrada",
        help_text="Informe a data de entrada, ex: 2024-12-31 14:00"
    )
    data_saida = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="data de saída",
        help_text="Informe a data de saída, ex: 2025-01-01 11:00"
    )
    finalizada = models.BooleanField(default=False)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    cadastrado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        status = "Finalizada" if self.finalizada else "Em andamento"
        return f"{self.reserva} - {status}"
