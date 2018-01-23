from bs4 import BeautifulSoup
from lxml import html
import requests
import regex

def main():
    endereco = input("Digite o endereco: ")
    string = input("digite termo")
    for i in range(10):
        response = requests.get(endereco)

        web = html.fromstring(response.content)



        html_sem_tags = BeautifulSoup(response.text, 'html.parser')
        result = regex.search(".........."+string+"......",html_sem_tags.text)
        print(result)
        if result is None:
            for links in web.xpath('//a/@href'):
                if "http" in links:
                    endereco = links
                    break
        else:
            print(result)
            break







def imprime_dados(response):
    print(response.status_code)
    print(response.headers)
    print(response.text.__sizeof__())




if __name__ == '__main__':
    main()