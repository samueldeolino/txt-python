import time
import os.path

def Menu_initial():
    while True:
        print("\nMenu do Gerenciador de Tarefas: ")
        print("1. Adicionar Tarefa")
        print("2. Ver Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Completar Tarefa")
        print("5. Deletar Tarefa Concluídas")
        print("6. Sair")
        try:
            number_choice = int(input("Digite sua escolha: "))
            match number_choice:
                case 1:
                    Add_Tarefa()
                case 2:
                    viewTarefas()
                case 3:
                    updateTarefa()
                case 4:
                    completTarefa()
                case 5:
                    deleteTarefa()
                case 6:
                    print("Encerrando o programa...")
                    time.sleep(1)
                    exit()
                case _:
                    print("Opção inválida! Tente novamente.")
        except ValueError: 
            print(f"\nError: {ValueError}\nEscolha uma opção válida!")
        except KeyboardInterrupt:
            print("\nPrograma encerrado.")
            exit()

def Add_Tarefa():
    with open("tarefas.txt", "a") as arquivo_txt:
        tarefa = input("Digite a tarefa: ")
        arquivo_txt.write("[ ] "+tarefa+"\n")
    print(f"Tarefa adicionada: {tarefa}")
    

def viewTarefas():
    validationWrite()
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    cont = 1
    with open("tarefas.txt", "r") as text_txt:           
        for linha in text_txt.readlines():
            print(f"{cont}. "+ linha, end="")
            cont+=1
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


def updateTarefa():
    validationWrite()
    while True:
        try:
            with open("tarefas.txt", "r") as arquivo_txt:
                arquivoLIDO = arquivo_txt.readlines()
                tam_txt = len(arquivoLIDO)
            viewTarefas()
            tarefa_num = int(input("Escolha o nº da Tarefa: "))
            tarefa_num -= 1
            if tarefa_num < 0 or tarefa_num >= tam_txt:
                print("Número da tarefa Inexistente")
                return updateTarefa()
            break
        except ValueError:
            print(f"{ValueError} Insira apenas números.")

    novoTexto = str(input("Escreva a nova Tarefa: "))

    with open("tarefas.txt", "r") as arquivo_txt:
        arquivoLido = arquivo_txt.readlines()

    arquivoLido[tarefa_num] = "[ ] "+novoTexto+"\n"

    with open("tarefas.txt", "w") as arquivo2_txt:
        arquivo2_txt.writelines(arquivoLido)
    print("Tarefa atualizada com sucesso!")



def completTarefa():
    validationWrite()
    viewTarefas()
    
    with open("tarefas.txt", "r") as arquivo_txt:
        arquivoLido = arquivo_txt.readlines()
    while True:
            try:    
                tarefa_num = int(input("Escreva o número da tarefa que deseja marcar como completada: "))
                if tarefa_num < 1 or tarefa_num > len(arquivoLido):
                    print("Número da tarefa inexistente. Tente novamente.")
                    viewTarefas()
                    continue
                break
            except ValueError:
                print("Por favor, insira apenas números.")   

    copiaArquivo_lido = arquivoLido[tarefa_num-1]     
    arquivoLido[tarefa_num-1] = "[✓] "+copiaArquivo_lido[4:]

    with open("tarefas.txt", "w") as arquivo2_txt:
        arquivo2_txt.writelines(arquivoLido)
    print("Tarefa atualizada com sucesso!")



def deleteTarefa():
    validationWrite()

    with open("tarefas.txt", "r") as arquivo_txt:
        arquivo_lido = arquivo_txt.readlines() 
    tarefas_nao_concluidas = [linha for linha in arquivo_lido if "[✓]" not in linha]

    """for linhas in arquivo_lido:
            print(linhas.find("✓"))
            if linhas.find("✓"):
                del arquivo_lido[number_linha]
            number_linha +=1"""
            
    with open("tarefas.txt", "w") as arquivo2_txt:
        arquivo2_txt.writelines(tarefas_nao_concluidas)
    print("Tarefa concluídas, deletadas com sucesso!")


    
def validationWrite():
    if not os.path.exists("tarefas.txt"):
        print("Nenhuma tarefa existente ainda, adicione para poder vizualizar.")
        return Menu_initial()

    with open("tarefas.txt", "r") as arquivo_txt:
        arquivo_lido = arquivo_txt.readlines()
        tam_txt = len(arquivo_lido)
        if  tam_txt == 0:
            print("Não há tarefas cadastradas.\n")
            return Menu_initial()


def validationNumber():
    with open("tarefas.txt", "r") as arquivo_txt:
        arquivoLido = arquivo_txt.readlines()
    while True:
            try:    
                tarefa_num = int(input("Escolha o nº da tarefa: "))
                if tarefa_num < 1 or tarefa_num > len(arquivoLido):
                    print("Número da tarefa inexistente. Tente novamente.")
                    viewTarefas()
                    continue
                break
            except ValueError:
                print("Por favor, insira apenas números.") 
    return arquivoLido