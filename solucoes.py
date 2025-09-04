def sao_anagramas(string1, string2):
  #TODO: implementar a lógica
  pass

def encontrar_maior_palavra(texto):
  lista = texto.split()
  maior = ""
  for palavra in lista:
      if len(palavra) > len(maior):
          maior = palavra
  print(maior)
  