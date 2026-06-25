from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    TipoQuarto,
    StatusReserva,
    Quarto,
    Hospede,
    Reserva,
    Hospedagem
)
class HospedagemForm(forms.ModelForm):
    class Meta:
        model = Hospedagem
        fields = ["reserva", "data_entrada", "data_saida", "finalizada"]
        widgets = {
            "data_entrada": forms.DateInput(attrs={"type": "date"}),
            "data_saida": forms.DateInput(attrs={"type": "date"}),
        }

class Index(TemplateView):
    template_name = "website/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_hospedes"] = Hospede.objects.count()
        context["total_hospedagens"] = Hospedagem.objects.count()
        context["total_quartos"] = Quarto.objects.count()
        context["total_reservas"] = Reserva.objects.count()
        return context


class Sobre(TemplateView):
    template_name = "website/sobre.html"


class Contato(TemplateView):
    template_name = "website/contato.html"


#################### Views para TipoQuarto ####################


class TipoQuartoCreate(LoginRequiredMixin, CreateView):
    model = TipoQuarto
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("tipoquarto_list")
    extra_context = {
        "titulo": "Cadastro de Tipo de Quarto",
        "botao": "Cadastrar"
    }


class TipoQuartoUpdate(LoginRequiredMixin, UpdateView):
    model = TipoQuarto
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("tipoquarto_list")
    extra_context = {
        "titulo": "Edição de Tipo de Quarto",
        "botao": "Salvar"
    }


class TipoQuartoDelete(LoginRequiredMixin, DeleteView):
    model = TipoQuarto
    template_name = "website/form.html"
    success_url = reverse_lazy("tipoquarto_list")
    extra_context = {
        "titulo": "Excluir Tipo de Quarto",
        "botao": "Excluir"
    }


class TipoQuartoList(LoginRequiredMixin, ListView):
    model = TipoQuarto
    template_name = "website/listas/tipoquartos.html"


class TipoQuartoDetail(LoginRequiredMixin, DetailView):
    model = TipoQuarto
    template_name = "website/ver/tipoquarto.html"


#################### Views para StatusReserva ####################


class StatusReservaCreate(LoginRequiredMixin, CreateView):
    model = StatusReserva
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("statusreserva_list")
    extra_context = {
        "titulo": "Cadastro de Status de Reserva",
        "botao": "Cadastrar"
    }


class StatusReservaUpdate(LoginRequiredMixin, UpdateView):
    model = StatusReserva
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("statusreserva_list")
    extra_context = {
        "titulo": "Edição de Status de Reserva",
        "botao": "Salvar"
    }


class StatusReservaDelete(LoginRequiredMixin, DeleteView):
    model = StatusReserva
    template_name = "website/form.html"
    success_url = reverse_lazy("statusreserva_list")
    extra_context = {
        "titulo": "Excluir Status de Reserva",
        "botao": "Excluir"
    }


class StatusReservaList(LoginRequiredMixin, ListView):
    model = StatusReserva
    template_name = "website/listas/statusreservas.html"


class StatusReservaDetail(LoginRequiredMixin, DetailView):
    model = StatusReserva
    template_name = "website/ver/statusreserva.html"


#################### Views para Quarto ####################


class QuartoCreate(LoginRequiredMixin, CreateView):
    model = Quarto
    fields = ["numero", "tipo_quarto", "capacidade", "valor_diaria", "disponivel"]
    template_name = "website/form.html"
    success_url = reverse_lazy("quarto_list")
    extra_context = {
        "titulo": "Cadastro de Quartos",
        "botao": "Cadastrar"
    }


class QuartoUpdate(LoginRequiredMixin, UpdateView):
    model = Quarto
    fields = ["numero", "tipo_quarto", "capacidade", "valor_diaria", "disponivel"]
    template_name = "website/form.html"
    success_url = reverse_lazy("quarto_list")
    extra_context = {
        "titulo": "Edição de Quartos",
        "botao": "Salvar"
    }


class QuartoDelete(LoginRequiredMixin, DeleteView):
    model = Quarto
    template_name = "website/form.html"
    success_url = reverse_lazy("quarto_list")
    extra_context = {
        "titulo": "Excluir Quarto",
        "botao": "Excluir"
    }


class QuartoList(LoginRequiredMixin, ListView):
    model = Quarto
    template_name = "website/listas/quartos.html"

class QuartoDetail(LoginRequiredMixin, DetailView):
    model = Quarto
    template_name = "website/ver/quarto.html"


#################### Views para Hospede ####################


class HospedeCreate(LoginRequiredMixin, CreateView):
    model = Hospede
    fields = ["nome", "cpf", "telefone", "email"]
    template_name = "website/form.html"
    success_url = reverse_lazy("hospede_list")
    extra_context = {
        "titulo": "Cadastro de Hóspedes",
        "botao": "Cadastrar"
    }


class HospedeUpdate(LoginRequiredMixin, UpdateView):
    model = Hospede
    fields = ["nome", "cpf", "telefone", "email"]
    template_name = "website/form.html"
    success_url = reverse_lazy("hospede_list")
    extra_context = {
        "titulo": "Edição de Hóspedes",
        "botao": "Salvar"
    }


class HospedeDelete(LoginRequiredMixin, DeleteView):
    model = Hospede
    template_name = "website/form.html"
    success_url = reverse_lazy("hospede_list")
    extra_context = {
        "titulo": "Excluir Hóspede",
        "botao": "Excluir"
    }


class HospedeList(LoginRequiredMixin, ListView):
    model = Hospede
    template_name = "website/listas/hospedes.html"


class HospedeDetail(LoginRequiredMixin, DetailView):
    model = Hospede
    template_name = "website/ver/hospede.html"


#################### Views para Reserva ####################


class ReservaCreate(LoginRequiredMixin, CreateView):
    model = Reserva
    fields = ["hospede", "quarto", "data_checkin", "data_checkout", "valor_total", "status"]
    template_name = "website/form.html"
    success_url = reverse_lazy("reserva_list")
    extra_context = {
        "titulo": "Cadastro de Reservas",
        "botao": "Cadastrar"
    }

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class ReservaUpdate(LoginRequiredMixin, UpdateView):
    model = Reserva
    fields = ["hospede", "quarto", "data_checkin", "data_checkout", "valor_total", "status"]
    template_name = "website/form.html"
    success_url = reverse_lazy("reserva_list")
    extra_context = {
        "titulo": "Edição de Reservas",
        "botao": "Salvar"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class ReservaDelete(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = "website/form.html"
    success_url = reverse_lazy("reserva_list")
    extra_context = {
        "titulo": "Excluir Reserva",
        "botao": "Excluir"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class ReservaList(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = "website/listas/reservas.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class ReservaDetail(LoginRequiredMixin, DetailView):
    model = Reserva
    template_name = "website/ver/reserva.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


#################### Views para Hospedagem ####################


class HospedagemCreate(LoginRequiredMixin, CreateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "website/form.html"
    success_url = reverse_lazy("hospedagem_list")
    extra_context = {
        "titulo": "Cadastro de Hospedagens",
        "botao": "Cadastrar"
    }

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class HospedagemUpdate(LoginRequiredMixin, UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "website/form.html"
    success_url = reverse_lazy("hospedagem_list")
    extra_context = {
        "titulo": "Edição de Hospedagens",
        "botao": "Salvar"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class HospedagemDelete(LoginRequiredMixin, DeleteView):
    model = Hospedagem
    template_name = "website/form.html"
    success_url = reverse_lazy("hospedagem_list")
    extra_context = {
        "titulo": "Excluir Hospedagem",
        "botao": "Excluir"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class HospedagemList(LoginRequiredMixin, ListView):
    model = Hospedagem
    template_name = "website/listas/hospedagens.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class HospedagemDetail(LoginRequiredMixin, DetailView):
    model = Hospedagem
    template_name = "website/ver/hospedagem.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)
