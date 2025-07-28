# 🍎 SystemFruits

Sistema de compras de frutas em terminal com geração de recibo em PDF. Idealizado para simular uma experiência de e-commerce simples com funcionalidades como login, carrinho de compras, cupons de desconto e formas de pagamento variadas.

## 📋 Funcionalidades

- ✅ Login com usuário e senha
- 🛒 Carrinho de compras com adição, edição e remoção de itens
- 💸 Aplicação de cupons de desconto e pagamento com ajuste por método
- 🧾 Geração automática de recibo em PDF com detalhes da compra
- 📊 Sistema com cálculo de subtotal, desconto, juros e total final

## 🖥️ Tecnologias Utilizadas

- **Python 3.x**
- **ReportLab** – geração de arquivos PDF

## 🚀 Como Executar

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-usuario/SystemFruits.git
   cd SystemFruits
   ```
- Instale as dependências:

```bash
pip install reportlab
```

- Execute o sistema:

```bash
python systemfruits.py
```

- O recibo será salvo como recibo_compra.pdf.

## 🧠 Fluxo do Sistema
** Usuário realiza login com credenciais válidas.

** Escolhe as frutas e adiciona ao carrinho.

** Pode editar/remover frutas antes de finalizar.

** Aplica cupons, escolhe forma de pagamento e finaliza compra.

** Um recibo é gerado automaticamente com todos os detalhes.

## 🧾 Exemplo de Recibo Gerado

===============================
      RECIBO DE COMPRA
        SYSTEMFRUITS
===============================

Cliente: admin
Data: 28/07/2025
Hora: 11:42

Itens Comprados:
- Maçã: 3 x R$ 2.00 = R$ 6.00
- Banana: 2 x R$ 1.50 = R$ 3.00
- Morango: 1 x R$ 4.00 = R$ 4.00

-------------------------------
Subtotal: R$ 13.00
Desconto (Cupom: BEMVINDO10): -R$ 1.30
Juros (Cartão de crédito): +R$ 0.65
-------------------------------
Total a Pagar: **R$ 12.35**
Forma de Pagamento: Cartão de crédito

-------------------------------
Obrigado por comprar conosco!
Volte sempre! 
===============================



## 🎯 Objetivos do Projeto
Este projeto foi criado com fins didáticos para praticar:

- Lógica de programação

- Manipulação de arquivos PDF com Python

- Estruturação de sistemas de terminal com múltiplos fluxos

- Princípios básicos de controle de estoque e automação de recibos

## 🔐 Login de Teste
** Usuário: admin

** Senha: 1234



## 📂 Estrutura de Arquivos

```bash
SystemFruits/
├── systemfruits.py
├── recibo_compra.pdf
├── README.md
└── requirements.txt
```


👨‍💻 Autor
Desenvolvido por [Moisés/github.com/Devmoises79].

📃 Licença
Este projeto está sob a licença MIT.
