from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ---------------------- Dados de Login ----------------------
print("------ Bem-vindo ao SystemFruits ------")

senha = input("Digite a senha: ")
usuario = input("Agora, digite o nome de usuário: ")

if (usuario == "Admin01" and senha == "Adm123") or (usuario == "User01" and senha == "User123"):
    print("Acesso autorizado!\n")
    
    # ---------------------- Função para escolher frutas ----------------------
    def escolher_frutas():
        frutas_disponiveis = {
            "Pera": {"preco": 8.00, "estoque": 20},
            "Banana": {"preco": 5.00, "estoque": 30},
            "Maçã": {"preco": 4.00, "estoque": 25},
            "Uva": {"preco": 6.00, "estoque": 15},
            "Laranja": {"preco": 2.00, "estoque": 50},
            "Melancia": {"preco": 12.00, "estoque": 10},
            "Maracujá": {"preco": 8.00, "estoque": 12},
            "Morango": {"preco": 10.00, "estoque": 10},
            "Manga": {"preco": 4.00, "estoque": 18}
        }

        carrinho = {}

        while True:
            print("\n--- Frutas Disponíveis ---")
            for fruta, info in frutas_disponiveis.items():
                print(f"{fruta}: R$ {info['preco']:.2f} | Estoque: {info['estoque']}")

            escolha = input("\nDigite a fruta, 'editar', 'remover' ou 'sair': ").capitalize()

            if escolha == "Sair":
                break
            elif escolha == "Editar":
                item = input("Qual fruta deseja editar? ").capitalize()
                if item in carrinho:
                    nova_qtd = int(input("Nova quantidade: "))
                    if nova_qtd <= frutas_disponiveis[item]["estoque"]:
                        carrinho[item] = nova_qtd
                        print(f"{item} atualizado para {nova_qtd} unidades.")
                    else:
                        print("Estoque insuficiente.")
                else:
                    print("Fruta não está no carrinho.")
            elif escolha == "Remover":
                item = input("Qual fruta deseja remover? ").capitalize()
                if item in carrinho:
                    del carrinho[item]
                    print(f"{item} removido do carrinho.")
                else:
                    print("Fruta não está no carrinho.")
            elif escolha in frutas_disponiveis:
                qtd = int(input(f"Quantas unidades de {escolha}? "))
                if qtd <= frutas_disponiveis[escolha]["estoque"]:
                    carrinho[escolha] = carrinho.get(escolha, 0) + qtd
                    frutas_disponiveis[escolha]["estoque"] -= qtd
                    print(f"{qtd} unidade(s) de {escolha} adicionadas ao carrinho.")
                else:
                    print("Quantidade acima do estoque disponível.")
            else:
                print("Comando ou fruta inválido.")

        return carrinho, frutas_disponiveis

    # ---------------------- Aplicar cupom ----------------------
    def aplicar_cupom(total):
        cupom = input("\nDigite o cupom de desconto (ou Enter para ignorar): ").upper()
        if cupom == "DESCONTO10":
            print("Cupom aplicado: 10% de desconto.")
            return total * 0.10
        elif cupom == "DESCONTO20":
            print("Cupom aplicado: 20% de desconto.")
            return total * 0.20
        elif cupom:
            print("Cupom inválido.")
        return 0

    # ---------------------- Forma de pagamento ----------------------
    def escolher_pagamento(total):
        forma = input("\nForma de pagamento (Pix / Crédito / Débito): ").lower()
        ajuste = 0
        if forma == "pix":
            ajuste = -total * 0.05
            print("5% de desconto no Pix.")
        elif forma == "crédito" or forma == "credito":
            ajuste = total * 0.10
            print("10% de acréscimo no crédito.")
        elif forma == "débito" or forma == "debito":
            print("Pagamento no débito: sem alteração.")
        else:
            print("Forma não reconhecida. Considerando Débito.")
        return forma.capitalize(), ajuste

    # ---------------------- Gerar recibo PDF ----------------------
    def gerar_recibo_pdf(nome_cliente, carrinho, frutas, total, desconto, ajuste, total_final, forma_pagamento):
        nome_arquivo = f"recibo_{nome_cliente}.pdf"
        c = canvas.Canvas(nome_arquivo, pagesize=A4)
        largura, altura = A4

        y = altura - 50
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "Recibo de Compra - SystemFruits")
        y -= 40

        c.setFont("Helvetica", 12)
        c.drawString(50, y, f"Cliente: {nome_cliente}")
        y -= 20
        c.drawString(50, y, "Itens comprados:")

        y -= 20
        for fruta, qtd in carrinho.items():
            preco = frutas[fruta]["preco"]
            subtotal = qtd * preco
            c.drawString(60, y, f"{fruta}: {qtd} x R$ {preco:.2f} = R$ {subtotal:.2f}")
            y -= 20

        y -= 10
        c.drawString(50, y, f"Subtotal: R$ {total:.2f}")
        y -= 20
        c.drawString(50, y, f"Desconto aplicado: R$ {desconto:.2f}")
        y -= 20
        c.drawString(50, y, f"Ajuste ({forma_pagamento}): R$ {ajuste:.2f}")
        y -= 20
        c.drawString(50, y, f"Total Final: R$ {total_final:.2f}")
        y -= 30
        c.drawString(50, y, "Obrigado por comprar no SystemFruits!")
        c.save()
        print(f"\nRecibo gerado: {nome_arquivo}")

    # ---------------------- Resumo final ----------------------
    def mostrar_resumo(carrinho, frutas):
        print("\n--- Resumo da Compra ---")
        total = 0
        for fruta, qtd in carrinho.items():
            preco = frutas[fruta]["preco"]
            subtotal = qtd * preco
            print(f"{fruta}: {qtd} x R$ {preco:.2f} = R$ {subtotal:.2f}")
            total += subtotal

        desconto = aplicar_cupom(total)
        total_com_desconto = total - desconto

        forma_pagamento, ajuste = escolher_pagamento(total_com_desconto)
        total_final = total_com_desconto + ajuste

        print(f"\nTotal a pagar: R$ {total_final:.2f}")

        nome_cliente = input("\nDigite o nome do cliente para gerar o recibo: ").strip()
        gerar_recibo_pdf(nome_cliente, carrinho, frutas, total, desconto, ajuste, total_final, forma_pagamento)

    # ---------------------- Execução ----------------------
    carrinho, frutas_disponiveis = escolher_frutas()
    if carrinho:
        mostrar_resumo(carrinho, frutas_disponiveis)
    else:
        print("Nenhum item no carrinho. Compra cancelada.")

else:
    print("Acesso negado. Tente novamente.")
