# Função que faz a conexão
def client():
    import pymongo
    # Link de conexão com o banco de dados na nuvem
    stringConnection = "mongodb+srv://engenharia:dbR4zr7MfU8bdig7@cluster0.1e19e.mongodb.net/test"
    myClient = pymongo.MongoClient(stringConnection)
    myDb = myClient["base_dados"]     # Definindo o banco
    return myDb

# Função de inserção de um cliente
def cadastroCliente(document):
    db = client()
    cliente = db["clientes"]         # Definindo o documento
    cliente.insert_one(document)    # Inserindo um documento

# Função de inserção de um funcioanrio
def cadastroFuncionario(document):
    db = client()
    funcionario = db["funcionarios"]
    funcionario.insert_one(document)


def buscarCliente(user, password):
    db = client()
    funcionario = db["loginCliente"]
    row = funcionario.find_one({ 'user': user, 'password': password })
    if row == None:
        return False
    else:
        return True
  

def buscarFuncionario(user, password):
    db = client()
    funcionario = db["funcionarios"]
    row = funcionario.find_one({ 'UserName': user, 'Password': password })
    if row == None:
        return False
    else:
        return True


def inserirVaga(document):
    db = client()
    vagas = db["vagas"]
    vagas.insert_one(document)


def listarVagasDB():
    db = client()
    vagas = db["vagas"]
    return vagas.find().limit(20)


def vagasDB(indice):
    db = client()
    vagas = db["vagas"]
    return vagas.find_one({ 'Vaga': indice })


def updateVaga(row, status:str):
    query = {"Vaga": row["Vaga"], "Status": row["Status"]}
    newQuery = { "$set": { "Status": status }}
    db = client()
    vagas = db["vagas"]   
    vagas.update_one(query, newQuery) 
