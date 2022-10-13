
arquivo =open("aula.txt", 'r')


dados = []
contador = 0

for lines in arquivo:
    for letters in lines:
        dados.append(letters) 
        palavra = dados[contador]

        if dados[contador] == ",":
            dados[contador] = ";"
        contador +=1
        
x = "".join(dados)
print(x)



for position in range(len(dados)):
        if dados[contador] == ";" and (dados[contador +1] == " " or dados[contador -1] == " " or dados[contador +1] == "\n"): 
            dados[contador] = ","

        contador +=1

x = "".join(dados)
#print(x)
arquivo = open("novo.txt","w")
arquivo.write(x)
