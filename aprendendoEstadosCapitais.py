estadosLis = ['Bahia','Maranhão','Piauí','Ceará','Rio Grande do Norte',
              'Paraíba','Pernambuco','Alagoas','Sergipe']
capitaisLis = ['Salvador','São Luis','Teresina','Fortaleza'
               ,'Natal','João Pessoa','Recife','Maceió','Aracajú']
aux = None

while(not aux):
    
    palavra = input('Digite um estado:')
    
    if palavra == '0':
        break
    else:
        for i in range(len(estadosLis)):
            if estadosLis[i] == palavra:
                print('\nEstado: '+estadosLis[i]+' Capital: '+capitaisLis[i])
                break
            elif capitaisLis[i] == palavra:
                print('\nEstado: '+estadosLis[i]+' Capital: '+capitaisLis[i])
                break
print('\nObrigado, volte sempre')    