from bs4 import BeautifulSoup
import requests as r
import urllib as ur

class Scraping():

    def BMA(self):
        try:
            lista_de_vendas = []
            lista_de_paises = []
            lista_de_compras = []
            num = 0

            DIC = {}

            'link = r.get("https://www.atlantico.ao/pt/particulares/Pages/home.aspx")'
            link2 = ur.request.urlopen("https://www.atlantico.ao/pt/particulares/Pages/home.aspx")

            soup = BeautifulSoup(link2.read(), 'html.parser')

            lista_de_paises = soup.select('.currency')
            lista_de_compras = soup.select('.purchase-value')
            lista_de_vendas = soup.select('.sale-value')
            data_element = soup.select('.updated-information')

            data_text = data_element[0].get_text()
            data_text = data_text.replace(" ","")
            data_text = data_text.replace("\n","")
            data_text = data_text.replace("\r","")

            DIC['Tamanho'] = len(lista_de_compras);
            DIC['Data'] = data_text[data_text.find(':')+1:len(data_text)]

            for x in range(len(lista_de_vendas)):
                DIC[f'{x}'] = {
                    "Moeda":f"{lista_de_paises[x].get_text()}",
                    "Compra":f"{lista_de_compras[x].get_text()}",
                    "Venda":f"{lista_de_vendas[x].get_text()}"
                }
            return DIC
        except:
            resposta = {"Status":"Erro ao conectar-se a Internet!"}
            return resposta
    
    def BNI(self):
        try:
            lista_de_vendas = []
            lista_de_moedas = []
            lista_de_compras = []
            DIC = {}


            link = r.get("https://www.bni.ao/pt/particulares/")
            link2 = ur.request.urlopen("https://www.bni.ao/pt/taxas")

            soup = BeautifulSoup(link.content, 'html.parser')
            soup2 = BeautifulSoup(link2.read(), 'html.parser')

            lista_de_moedas = soup.select('.col-md-7')
            lista_de_compras = soup.select('.buy-value')
            lista_de_vendas = soup.select('.sell-value')
            data_element = soup2.select('tr td:nth-of-type(5)')

            data_text = data_element[0].get_text()
            data_text = data_text.replace(" ","")
            data_text = data_text.replace("\n","")
            data_text = data_text.replace("\r","")

            DIC['Tamanho'] = len(lista_de_compras);
            DIC['Data'] = data_text
            for x in range(len(lista_de_vendas)):
                DIC[f'{x}'] = {
                    "Moeda":f"{lista_de_moedas[x].get_text()}",
                    "Compra":f"{lista_de_compras[x].get_text()}",
                    "Venda":f"{lista_de_vendas[x].get_text()}"
                }
            return DIC
        except:
            resposta = {
                "Status":"Erro ao conectar-se a Internet!"
            }
            return resposta
    
    def BAI(self):
        try:
            lista_de_vendas = []
            lista_de_paises = []
            lista_de_compras = []
            DIC = {}

            link = r.get("https://www.bancobai.ao/pt/cambios-e-valores")
            link2 = r.get("https://www.bancobai.ao/pt/particulares")

            soup = BeautifulSoup(link.content, 'html.parser')
            soup2 = BeautifulSoup(link2.content, 'html.parser')

            conteudo = soup.find('table', class_='table-striped')
            body = conteudo.find('tbody')

            lista_de_paises = body.find_all('div', class_='coin-val')
            lista_de_compras = body.find_all('td', class_='b-right')
            lista_de_vendas = body.select('tr td:nth-of-type(4)')
            data_element = soup2.select('.updated-on')

            data_text = data_element[0].get_text()
            data_text = data_text.replace(" ","")
            data_text = data_text.replace("\n","")
            data_text = data_text.replace("\r","")

            DIC['Tamanho'] = len(lista_de_vendas);
            DIC['Data'] = data_text[data_text.find('m')+1:len(data_text)]
            for x in range(len(lista_de_vendas)):
                DIC[f'{x}'] = {
                    "Moeda":f"{lista_de_paises[x].get_text()}",
                    "Compra":f"{lista_de_compras[x].get_text()}",
                    "Venda":f"{lista_de_vendas[x].get_text()}"
                }
            return DIC
        except:
            resposta = {
                "Status":"Erro ao conectar-se a Internet!"
            }
            return resposta

    def ilustration(self):
        DIC = {}
        DIC['Tamanho'] = 10;
        DIC['Data'] = '12/12/2012'
        DIC['0'] = {
            "Moeda":"AKZ",
            "Compra":"50.000",
            "Venda":"12.000"
        }
        return DIC