from django.urls import path
from .views import *
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView
)

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="website/form.html",
        extra_context={
            "titulo": "Autenticação de Usuário",
            "botao": "Entrar"
        }
    ), name="login"),

    path("logout/", LogoutView.as_view(), name="logout"),

    path("alterar-senha/", PasswordChangeView.as_view(
        template_name="website/form.html",
        extra_context={
            "titulo": "Alterar Senha",
            "botao": "Alterar"
        }
    ), name="alterar_senha"),

    path("", Index.as_view(), name="pagina_inicial"),
    path("sobre/", Sobre.as_view(), name="sobre"),
    path("contato/", Contato.as_view(), name="contato"),

    path("tipoquartos/cadastrar/", TipoQuartoCreate.as_view(), name="tipoquarto_create"),
    path("tipoquartos/listar/", TipoQuartoList.as_view(), name="tipoquarto_list"),
    path("tipoquartos/editar/<int:pk>/", TipoQuartoUpdate.as_view(), name="tipoquarto_update"),
    path("tipoquartos/excluir/<int:pk>/", TipoQuartoDelete.as_view(), name="tipoquarto_delete"),
    path("tipoquartos/ver/<int:pk>/", TipoQuartoDetail.as_view(), name="tipoquarto_detail"),

    path("statusreservas/cadastrar/", StatusReservaCreate.as_view(), name="statusreserva_create"),
    path("statusreservas/listar/", StatusReservaList.as_view(), name="statusreserva_list"),
    path("statusreservas/editar/<int:pk>/", StatusReservaUpdate.as_view(), name="statusreserva_update"),
    path("statusreservas/excluir/<int:pk>/", StatusReservaDelete.as_view(), name="statusreserva_delete"),
    path("statusreservas/ver/<int:pk>/", StatusReservaDetail.as_view(), name="statusreserva_detail"),

    path("quartos/cadastrar/", QuartoCreate.as_view(), name="quarto_create"),
    path("quartos/listar/", QuartoList.as_view(), name="quarto_list"),
    path("quartos/editar/<int:pk>/", QuartoUpdate.as_view(), name="quarto_update"),
    path("quartos/excluir/<int:pk>/", QuartoDelete.as_view(), name="quarto_delete"),
    path("quartos/ver/<int:pk>/", QuartoDetail.as_view(), name="quarto_detail"),

    path("hospedes/cadastrar/", HospedeCreate.as_view(), name="hospede_create"),
    path("hospedes/listar/", HospedeList.as_view(), name="hospede_list"),
    path("hospedes/editar/<int:pk>/", HospedeUpdate.as_view(), name="hospede_update"),
    path("hospedes/excluir/<int:pk>/", HospedeDelete.as_view(), name="hospede_delete"),
    path("hospedes/ver/<int:pk>/", HospedeDetail.as_view(), name="hospede_detail"),

    path("reservas/cadastrar/", ReservaCreate.as_view(), name="reserva_create"),
    path("reservas/listar/", ReservaList.as_view(), name="reserva_list"),
    path("reservas/editar/<int:pk>/", ReservaUpdate.as_view(), name="reserva_update"),
    path("reservas/excluir/<int:pk>/", ReservaDelete.as_view(), name="reserva_delete"),
    path("reservas/ver/<int:pk>/", ReservaDetail.as_view(), name="reserva_detail"),

    path("hospedagens/cadastrar/", HospedagemCreate.as_view(), name="hospedagem_create"),
    path("hospedagens/listar/", HospedagemList.as_view(), name="hospedagem_list"),
    path("hospedagens/editar/<int:pk>/", HospedagemUpdate.as_view(), name="hospedagem_update"),
    path("hospedagens/excluir/<int:pk>/", HospedagemDelete.as_view(), name="hospedagem_delete"),
    path("hospedagens/ver/<int:pk>/", HospedagemDetail.as_view(), name="hospedagem_detail"),
]
