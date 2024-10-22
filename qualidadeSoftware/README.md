Projeto: Agência Bancária em Python e Automação com Selenium
Este projeto consiste em uma aplicação simples de uma agência bancária desenvolvida em Python utilizando Programação Orientada a Objetos (POO) e Test-Driven Development (TDD). Além disso, inclui automação de testes para o site SauceDemo utilizando Selenium.

Funcionalidades da Agência Bancária
Criação de Clientes e Contas Bancárias
Depósito
Saque
Transferência
Verificação de Saldo
Automação com Selenium
Teste de Login no SauceDemo
Teste de Adição de Itens ao Carrinho
Estrutura do Projeto
bash
Copiar código
agencia_bancaria/
│
├── agencia_bancaria.py   # Código da aplicação bancária
├── test_banco.py         # Código dos testes unitários (TDD)
├── saucedemo_test.py     # Código dos testes de automação com Selenium
└── README.md             # Este arquivo com a documentação
Instalação e Execução
Pré-requisitos
Python 3.x instalado no sistema.
Pip para gerenciamento de pacotes.
Criar um Ambiente Virtual
Recomenda-se criar um ambiente virtual para isolar as dependências do projeto. Siga os passos abaixo para configurar:

Navegue até o diretório do seu projeto:

bash
Copiar código
cd caminho/do/seu/projeto/agencia_bancaria
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

Windows:
bash
Copiar código
venv\Scripts\activate
macOS/Linux:
bash
Copiar código
source venv/bin/activate
Instalação das Bibliotecas Necessárias
Após ativar o ambiente virtual, instale as bibliotecas necessárias usando pip:

Para os testes da aplicação bancária, a biblioteca unittest já está inclusa no Python, então não é necessário instalar nada.

Para os testes de automação do SauceDemo, instale as bibliotecas selenium e webdriver-manager:

bash
Copiar código
pip install selenium webdriver-manager
Execução da Aplicação
Para rodar a aplicação principal, execute:

bash
Copiar código
python agencia_bancaria.py
Para rodar os testes da agência bancária, execute:

bash
Copiar código
python test_banco.py
Para rodar os testes de automação do SauceDemo, execute:

bash
Copiar código
python saucedemo_test.py
Exemplo de Execução
Os testes e a aplicação mostrarão mensagens no console sobre o status das operações, como criação de clientes, depósitos, saques e operações de login no SauceDemo.

Licença
Este projeto está licenciado sob a MIT License.