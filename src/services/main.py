# src/main.py

from src.repo.csv_repo import ler_clientes
from src.models.pessoa import Pessoa

clientes = ler_clientes("lista_clientes.csv")
print(f"Clientes carregados: {len(clientes)}")
for cliente in clientes[:5]:
    print(cliente)

# TESTE COM 1 CLIENTE
p = Pessoa(
    nome_completo="André de Bifur Gomes Ribeiro",
    email="andrebifur@testmail.org",
    celular="52127281",
    cpf="940.977.298-28",
    cep="90460-070",
    interesse="Desenvolvimento de Jogos Digitais"
)

p.normalizar_nome()
p.validar_cpf()
p.validar_cep()
p.normalizar_celular()

print("\nTeste de normalização e validação:")
print(f"Nome completo: {p.nome_completo}")
print(f"Primeiro nome: {p.primeiro_nome}")
print(f"Segundo nome: {p.segundo_nome}")
print(f"CPF: {p.cpf}")
print(f"Endereço: {p.endereco}")
print(f"Celular: {p.celular}")
print(f"Observações: {p.observacoes}")



