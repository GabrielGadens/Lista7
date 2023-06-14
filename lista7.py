import csv
class Usuario:
    def __init__(self,nome=None,sobrenome=None,dataNasc=None,cpf=None,nomeDeUsu=None,senha=None):
        self._nome=nome
        self._sobrenome=sobrenome
        self._dataNasc=dataNasc
        self._cpf=cpf
        self._nomeDeUsu=nomeDeUsu
        self._senha=senha
        self._assinaturas=[]

    def adicionarAssinatura(self,assinatura):
        self._assinaturas.append(assinatura)

    def cancelarAssinatura(self,id):
        pass

    def exibirDados(self):
        print('\n',self._nome,self._sobrenome,'\nNasc:',self._dataNasc,'\nCPF:',self._cpf,'\nUsuário:',self._nomeDeUsu,'\nSenha:',self._senha,'\n')
        for i in self._assinaturas:
            print(i.exibirDadosAss())

    def confirmaCPF(self,cpf):
        if cpf == self._cpf:
            return True
        else:
            False
    
    def salvamentoUsuario(self):
        texto= str(str(self._nome)+","+str(self._sobrenome)+","+str(self._dataNasc)+","+str(self._cpf)+","+str(self._nomeDeUsu)+","+str(self._senha)+'\n')
        f = open('Usuarios.csv', 'a')
        f.write(texto)
        f.close()

class Assinatura:
    def __init__(self,tipo=None,preco=None,IdUsu=None,status=None):
        self._tipo=tipo
        self._preco=preco
        self._IdUsu=IdUsu
        self._status=status

    def exibirDadosAss(self):
        return self._tipo+' custa: '+self._preco+'\nId Usuário(CPF): '+self._IdUsu+' status: '+self._status

    def salvamentoAss(self):
        texto= str(str(self._IdUsu)+","+str(self._tipo)+","+str(self._preco)+","+str(self._status)+'\n')
        f = open('Assinaturas.csv', 'a')
        f.write(texto)
        f.close()

    


def serializarUsu():
    usuarios=[]
    f = open('Usuarios.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,(len(tabela))) :
        usuario=Usuario(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4],tabela[i][5])
        usuarios.append(usuario)
    return usuarios

def serializarAss(usuarios):
    assinaturas=[]
    f = open('Assinaturas.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,(len(tabela))) :
        assinatura=Assinatura(tabela[i][1],tabela[i][2],tabela[i][0],tabela[i][3])
        for x in usuarios:
            if tabela[i][3]=='Ativa':
                if x.confirmaCPF(tabela[i][0])==True:
                    x.adicionarAssinatura(assinatura)
                    assinaturas.append(assinatura)
        
    return assinaturas




opcao=0
while opcao!=9:
    usuarios=serializarUsu()
    assinaturas=serializarAss(usuarios)
    for usu in usuarios:
        usu.exibirDados()

    opcao=int(input('1 - Para adicionar Usuário    \n2 - Para adicionar assinatura a um usuário    \n3 - Cancelar assinatura\n'))
    
    if opcao==1:
        nome=input('Digite seu primeiro nome: ')
        sobrenome=input('Digite seu sobrenome: ')
        dataNasc=input('Digite sua data de nascimento no padrão dd/mm/aaaa: ')
        cpf=input('Digite seu cpf: ')
        nomeDeUsu=input('Digite seu Usuário: ')
        senha=input('Digite sua Senha: ')
        cpfJaExiste=False
        for usu in usuarios:
            if usu.confirmaCPF(cpf)==True:
                cpfJaExiste=True
                break
        if cpfJaExiste==False:
            usuario=Usuario(nome,sobrenome,dataNasc,cpf,nomeDeUsu,senha)
            usuarios.append(usuario)
    
    if opcao==2:
        cpf=input('Qual o CPF do responsável pela nova assinatura:')
        tipo=input('Qual tipo de assinatura:')
        valor=input('Qual valor da assinatura:')
        for usu in usuarios:
            if usu.confirmaCPF(cpf)==True:
                assinatura=Assinatura(tipo,valor,cpf,'Ativa')
                usu.adicionarAssinatura(assinatura)
                assinaturas.append(assinatura)
                print('Assinatura incluida com Exito')
                break

    if opcao==3:
        cont=1
        for ass in assinaturas:
            print('ID:',cont,'',ass.exibirDadosAss())
            cont+=1
        idAss=int(input('Qual o ID da assinatura para ser desativada: '))
        del(assinaturas[idAss-1])


    f = open('Usuarios.csv', 'w') #apaga os usuários do arquivo
    f.write('')
    f.close()
    for usu in usuarios: #salva as figurinhas atualizadas
        usu.salvamentoUsuario()
    f = open('Assinaturas.csv', 'w') #apaga as assinaturas do arquivo
    f.write('')
    f.close()
    for ass in assinaturas:
        ass.salvamentoAss()


