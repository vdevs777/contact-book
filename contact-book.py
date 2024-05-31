def adicionar_contato(contatos, informacoes_contato):
  contato = { 
    "nome": informacoes_contato["nome"], 
    "telefone": informacoes_contato["telefone"], 
    "email": informacoes_contato["email"], 
    "favorito": False
  }  
  contatos.append(contato)
  print("Contato %s adicionado com sucesso!" % (contato["nome"]))
  return

def ver_contatos(contatos):
  for indice, contato in enumerate(contatos, start=1):
    favorito = "★" if contato["favorito"] else ""
    print("\n%s. %s %s" % (indice, contato["nome"], favorito))
    print("Telefone: %s" % (contato["telefone"]))
    print("Email: %s" % (contato["email"]))
  return

def editar_contato(contatos, indice, novas_informacoes):
  indice_contato_ajustado = int(indice) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    if novas_informacoes["nome"] != "":
      contatos[indice_contato_ajustado]["nome"] = novas_informacoes["nome"]
    if novas_informacoes["email"] != "":
      contatos[indice_contato_ajustado]["email"] = novas_informacoes["email"]
    if novas_informacoes["telefone"] != "":
      contatos[indice_contato_ajustado]["telefone"] = novas_informacoes["telefone"]
    print("Contato atualizado com sucesso!")
  else: 
    print("Número inválido")
  return

def marcar_contato_como_favorito(contatos, indice):
  indice_contato_ajustado = int(indice) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos) and contatos[indice_contato_ajustado]["favorito"] == False:
    contatos[indice_contato_ajustado]["favorito"] = True
    print("Contato %s marcado como favorito com sucesso!" % (contatos[indice_contato_ajustado]["nome"]))
  elif indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos) and contatos[indice_contato_ajustado]["favorito"] == True:
    contatos[indice_contato_ajustado]["favorito"] = False
    print("Contato %s desmarcado como favorito com sucesso!" % (contatos[indice_contato_ajustado]["nome"]))
  else: 
    print("Número inválido")
  return

def ver_contatos_favoritos(contatos):
  for contato in contatos:
    if contato["favorito"]:
      print("\n%s. %s" % (indice, contato["nome"]))
      print("Telefone: %s" % (contato["telefone"]))
      print("Email: %s" % (contato["email"]))
  return

def deletar_contato(contatos, indice):
  indice_contato_ajustado = int(indice) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos.pop(indice_contato_ajustado)
    print("Contato deletado com sucesso!")
  else:
    print("Número inválido")
  return

contatos = []

while True:
  print("\nLista de contatos")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Editar contato")
  print("4. Marcar/desmarcar contato como favorito")
  print("5. Ver contatos favoritos")
  print("6. Deletar contato")
  print("7. Sair")

  opcao = input("Selecione a opção desejada: ")

  if opcao == "1":
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    informacoes_contato = {"nome": nome, "telefone": telefone, "email": email}
    adicionar_contato(contatos, informacoes_contato)
  if opcao == "2":
    ver_contatos(contatos)
  if opcao == "3":
    ver_contatos(contatos)
    indice = input("Digite o número do contato que você deseja alterar: ")
    nome = input("Digite o novo nome (deixe em branco caso queira manter): ")
    telefone = input("Digite o novo telefone (deixe em branco caso queira manter): ")
    email = input("Digite o novo email (deixe em branco caso queira manter): ")
    novas_informacoes = {"nome": nome, "telefone": telefone, "email": email}
    editar_contato(contatos, indice, novas_informacoes)
  if opcao == "4":
    ver_contatos(contatos)
    indice = input("Digite o número do contato que você deseja marcar ou desmarcar como favorito: ")
    marcar_contato_como_favorito(contatos, indice)
  if opcao == "5":
    ver_contatos_favoritos(contatos)
  if opcao == "6":
    ver_contatos(contatos)
    indice = input("Digite o número do contato que você deseja deletar: ")
    deletar_contato(contatos, indice)
  if opcao == "7":
    break