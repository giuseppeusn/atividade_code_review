def sao_anagramas(string1, string2):
  #TODO: implementar a lógica
  pass

def encontrar_maior_palavra(texto):
  frase = texto
  lista = frase.split()
  maior = ""
  for palavra in lista:
      if len(palavra) > len(maior):
          maior = palavra
  print(maior)
  pass

encontrar_maior_palavra("o rato roeu a ropa do rei de roma")

  