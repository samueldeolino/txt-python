import time
import os.path

def homeMenu():
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
                    addTask()
                case 2:
                    viewTask()
                case 3:
                    taskUpdate()
                case 4:
                    completeTask()
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

def addTask():
    with open("tarefas.txt", "a") as arquivo_txt:
        tarefa = input("Digite a tarefa: ")
        arquivo_txt.write("[ ] "+tarefa+"\n")
    print(f"Tarefa adicionada: {tarefa}")
    

def viewTask():
    writeValidation()
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    cont = 1
    with open("tarefas.txt", "r") as text_txt:           
        for linha in text_txt.readlines():
            print(f"{cont}. "+ linha, end="")
            cont+=1
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


def taskUpdate():
    writeValidation()
    
    tarefa_num = numberValidation("tarefas.txt", "Escolha o nº da Tarefa: ")

    if tarefa_num is None:
        return

    novoTexto = str(input("Escreva a nova Tarefa: "))

    with open("tarefas.txt", "r") as arquivo_txt:
        arquivoLido = arquivo_txt.readlines()

    arquivoLido[tarefa_num-1] = "[ ] "+novoTexto+"\n"

    with open("tarefas.txt", "w") as arquivo2_txt:
        arquivo2_txt.writelines(arquivoLido)
    print("Tarefa atualizada com sucesso!")



def completeTask():
    writeValidation()    

    tarefa_num = numberValidation("tarefas.txt", "Escreva o número da tarefa que deseja marcar como completada: ")
    if tarefa_num is None:
        return

    with open("tarefas.txt", "r") as arquivo_txt:
        arquivoLido = arquivo_txt.readlines()
    copiaArquivo_lido = arquivoLido[tarefa_num-1]     
    arquivoLido[tarefa_num-1] = "[✓] "+copiaArquivo_lido[4:]

    with open("tarefas.txt", "w") as arquivo2_txt:
        arquivo2_txt.writelines(arquivoLido)
    print("Tarefa atualizada com sucesso!")



def deleteTarefa():
    writeValidation()

    with open("tarefas.txt", "r") as arquivo_txt:
        arquivo_lido = arquivo_txt.readlines() 
    tarefas_nao_concluidas = [linha for linha in arquivo_lido if "[✓]" not in linha]
            
    with open("tarefas.txt", "w") as arquivo2_txt:
        arquivo2_txt.writelines(tarefas_nao_concluidas)
    print("Tarefa concluídas, deletadas com sucesso!")


    
def writeValidation():
    if not os.path.exists("tarefas.txt"):
        print("Nenhuma tarefa existente ainda, adicione para poder vizualizar.")
        return homeMenu()

    with open("tarefas.txt", "r") as arquivo_txt:
        arquivo_lido = arquivo_txt.readlines()
        tam_txt = len(arquivo_lido)
        if  tam_txt == 0:
            print("Não há tarefas cadastradas.\n")
            return homeMenu()


def numberValidation(arquivo, mensagem):

    with open(arquivo, "r") as arquivo_txt:
        tarefas = arquivo_txt.readlines()
        max_tarefas = len(tarefas)
    
    if max_tarefas == 0:
        print("Não há tarefas cadastradas.")
        return None 

    while True:
        try:
            viewTask()
            tarefa_num = int(input(mensagem))
            if tarefa_num < 1 or tarefa_num > max_tarefas:
                print(f"Número da tarefa inexistente. Escolha entre 1 e {max_tarefas}.")
                continue
            return tarefa_num
        except ValueError:
            print("Por favor, insira apenas números.")
