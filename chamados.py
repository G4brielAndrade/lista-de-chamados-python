from utils import carregar_chamados, salvar_chamados, gerar_id

def menu():
    print("\n--- Sistema de Chamados ---")
    print("1. Criar novo chamado")
    print("2. Listar chamados")
    print("3. Atualizar status de um chamado")
    print("4. Excluir chamado")
    print("5. Sair")

def criar_chamado(chamados):
    titulo = input("Título do chamado: ")
    descricao = input("Descrição: ")
    chamado = {
        "id": gerar_id(chamados),
        "titulo": titulo,
        "descricao": descricao,
        "status": "Aberto"
    }
    chamados.append(chamado)
    print("Chamado criado com sucesso!")

def listar_chamados(chamados):
    if not chamados:
        print("Nenhum chamado encontrado.")
        return
    for chamado in chamados:
        print(f"ID: {chamado['id']} | Título: {chamado['titulo']} | Status: {chamado['status']}")

def atualizar_status(chamados):
    id = int(input("Digite o ID do chamado: "))
    for chamado in chamados:
        if chamado["id"] == id:
            novo_status = input("Novo status (Aberto, Em andamento, Fechado): ")
            chamado["status"] = novo_status
            print("Status atualizado com sucesso!")
            return
    print("Chamado não encontrado.")

def excluir_chamado(chamados):
    id = int(input("Digite o ID do chamado a excluir: "))
    for chamado in chamados:
        if chamado["id"] == id:
            chamados.remove(chamado)
            print("Chamado excluído com sucesso!")
            return
    print("Chamado não encontrado.")

def main():
    chamados = carregar_chamados()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            criar_chamado(chamados)
        elif opcao == '2':
            listar_chamados(chamados)
        elif opcao == '3':
            atualizar_status(chamados)
        elif opcao == '4':
            excluir_chamado(chamados)
        elif opcao == '5':
            salvar_chamados(chamados)
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
