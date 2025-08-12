# 🍎 SystemFruits

Sistema de compras de frutas via terminal, com autenticação de usuário, gerenciamento de estoque, aplicação de cupons, escolha de forma de pagamento e geração automática de recibo em PDF. Ideal para simular um e-commerce simples com fluxos reais de compra.

---

## 📋 Funcionalidades

- ✅ Login seguro com usuário e senha (fluxo reinicia em caso de erro)
- 🛒 Carrinho de compras com adição, edição e remoção de frutas
- 📦 Controle dinâmico de estoque atualizado durante a compra
- 💸 Aplicação de cupons de desconto (ex: DESCONTO10, DESCONTO20)
- 💳 Formas de pagamento: Pix (5% de desconto), Crédito (10% de acréscimo), Débito (sem alteração)
- 🧾 Geração automática de recibo em PDF detalhando a compra
- 🧪 Testes automatizados para validação da autenticação do sistema

---

## 🖥️ Tecnologias Utilizadas

- **Python 3.x**  
- **ReportLab** – para geração dos arquivos PDF  
- **unittest** – framework para testes automatizados (built-in no Python)

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/Devmoises79/System-Fruits.git
cd System-Fruits
```

- Instale as dependências:

```bash
pip install reportlab
```

Execute o sistema:

```bash

python frutas.py
```

- Faça login com as credenciais válidas:

* Usuário: Admin01 | Senha: Adm123

* Usuário: User01 | Senha: User123

* Siga o fluxo para adicionar frutas ao carrinho, aplicar cupom, escolher forma de pagamento e gerar recibo.

# 🧪 Rodando os Testes Automatizados
Para validar a autenticação, rode:

```bash
python -m unittest test.py
```

* Certifique-se de que o arquivo test.py está no mesmo diretório e que as funções de autenticação estão importáveis para os testes.

# 🧠 Fluxo do Sistema
- Solicita usuário e senha (fluxo reinicia em caso de erro)

- Mostra frutas disponíveis e permite adicionar ao carrinho

- Permite editar e remover itens do carrinho

- Aplica cupom de desconto se informado

- Solicita forma de pagamento e aplica desconto ou acréscimo

- Gera recibo detalhado em PDF com resumo da compra

# 🧾 Exemplo de Recibo Gerado

```ruby
Recibo de Compra - SystemFruits

Cliente: Admin01
Itens comprados:
- Maçã: 3 x R$ 4.00 = R$ 12.00
- Banana: 2 x R$ 5.00 = R$ 10.00

Subtotal: R$ 22.00
Desconto aplicado: R$ 2.20
Ajuste (Pix): -R$ 0.99
Total Final: R$ 18.81
```

* Obrigado por comprar no SystemFruits!

# 📂 Estrutura do Projeto

```bash
System-Fruits/
├── frutas.py             # Código principal do sistema
├── test.py  # Testes automatizados para autenticação
├── recibo_<cliente>.pdf  # Recibos gerados automaticamente
├── README.md             # Documentação do projeto     
```

#🔐 Credenciais de Teste

* Usuário	Senha

- Admin01	Adm123
- User01	User123

# 👨‍💻 Autor
* Desenvolvido por Moisés.

# 📃 Licença
* Este projeto está sob a licença MIT.