
produtos = []
vendas = []
faturamento = 0


def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")

    nome = input("Nome do produto: ").strip()

    if not nome:
        print("Nome inválido!")
        return

    try:
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))

        if preco <= 0 or quantidade < 0:
            print("Preço ou quantidade inválidos!")
            return

        produto = {
            "nome": nome,
            "preco": preco,
            "estoque": quantidade,
            "vendidos": 0
        }

        produtos.append(produto)

        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Digite valores válidos!")


def listar_produtos():
    print("\n--- PRODUTOS CADASTRADOS ---")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for indice, produto in enumerate(produtos, start=1):
        print(f"\nCódigo: {indice}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']}")
        print(f"Vendidos: {produto['vendidos']}")


def registrar_venda():
    global faturamento

    print("\n--- REGISTRAR VENDA ---")

    if not produtos:
        print("Não existem produtos cadastrados.")
        return

    listar_produtos()

    try:
        codigo = int(input("\nDigite o código do produto: "))

        if codigo < 1 or codigo > len(produtos):
            print("Código inválido!")
            return

        produto = produtos[codigo - 1]

        quantidade = int(input("Quantidade desejada: "))

        if quantidade <= 0:
            print("Quantidade inválida!")
            return

        if quantidade > produto["estoque"]:
            print("Estoque insuficiente!")
            return

        subtotal = produto["preco"] * quantidade

        if subtotal >= 500:
            desconto = subtotal * 0.10
        elif subtotal >= 200:
            desconto = subtotal * 0.05
        else:
            desconto = 0

        total = subtotal - desconto

        produto["estoque"] -= quantidade
        produto["vendidos"] += quantidade

        faturamento += total

        venda = {
            "produto": produto["nome"],
            "quantidade": quantidade,
            "subtotal": subtotal,
            "desconto": desconto,
            "total": total
        }

        vendas.append(venda)

        print("\nVenda realizada com sucesso!")
        print(f"Produto: {produto['nome']}")
        print(f"Quantidade: {quantidade}")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Total: R$ {total:.2f}")

    except ValueError:
        print("Digite um número válido!")


def relatorio_vendas():
    print("\n--- RELATÓRIO DE VENDAS ---")

    if not vendas:
        print("Nenhuma venda registrada.")
        return

    print(f"Quantidade de vendas: {len(vendas)}")
    print(f"Faturamento total: R$ {faturamento:.2f}")

    for indice, venda in enumerate(vendas, start=1):
        print(f"\nVenda {indice}")
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Total: R$ {venda['total']:.2f}")


def produto_mais_vendido():
    print("\n--- PRODUTO MAIS VENDIDO ---")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    mais_vendido = max(produtos, key=lambda produto: produto["vendidos"])

    if mais_vendido["vendidos"] == 0:
        print("Ainda não existem vendas.")
        return

    print(f"Produto: {mais_vendido['nome']}")
    print(f"Unidades vendidas: {mais_vendido['vendidos']}")


def menu():
    while True:
        print("\n========== CONTROLE DE VENDAS ==========")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Registrar venda")
        print("4 - Relatório de vendas")
        print("5 - Produto mais vendido")
        print("6 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            registrar_venda()

        elif opcao == "4":
            relatorio_vendas()

        elif opcao == "5":
            produto_mais_vendido()

        elif opcao == "6":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida! Tente novamente.")


menu()
