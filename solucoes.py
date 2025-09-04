def sao_anagramas(string1, string2):
  v1 =sorted(string1.lower())
  v2 =sorted(string2.lower())
  if v1==v2:
    print(True)
  else:
    print(False)


def encontrar_maior_palavra(texto):
  lista = texto.split()
  maior = ""
  for palavra in lista:
      if len(palavra) > len(maior):
          maior = palavra
  print(maior)
  
