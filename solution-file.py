import json

def ler_json():
    with open('data.json', 'r', encoding='utf8') as f:
        return json.load(f)


def estrutura_json(establishments, products, categories):
    saidaJson = []
    for estabelecimento in reversed(establishments):
        estabelecimento_nome = estabelecimento['name']
        media_produtos = format(media_avg(products, estabelecimento), '.2f')
        saidaJson.append({f'establishment {estabelecimento_nome}': {'avgPrice': media_produtos }})
        for produto in products:
            for i in estabelecimento['productsId']:
                if i == produto['id']:
                    categoria_nome = categoria_comida(categories, produto)
                    produto_nome = produto['name']
                    preco = (float(produto['price']) / 100)
                    preco = format(preco, '.2f')
                    saidaJson.append({f'category {categoria_nome}' : {f'product {produto_nome}': {'price': preco }}})
                    salva_json(saidaJson)


def media_avg(products, estabelecimento):
    valores = []
    for produto in products:
        for i in estabelecimento['productsId']:
            if i == produto['id']:
                preco = (int(produto['price']) / 100)
                valores.append(preco)
                tam = len(valores)
                soma_total = sum(valores)
                media = soma_total/tam
    return media


def categoria_comida(categories, produto):
    for categoria in categories:
        for id in produto['categoriesId']:
            if id == categoria['id']:
                categoria_nome = (categoria['name'])
                return categoria_nome


def salva_json(lista_j):
    with open('saida.json', 'w', encoding='utf-8') as saida:
        json.dump(lista_j, saida, ensure_ascii=False, indent=4)


dataJsonData = ler_json()
establishments = dataJsonData['establishments']
products = dataJsonData['products']
categories = dataJsonData['categories']
estrutura_json(establishments, products, categories)

