from bs4 import BeautifulSoup
import lxml

def read_file():
    file=open('customers_report.txt')
    data=file.read()
    file.close()
    return data

soup=BeautifulSoup(read_file(), 'lxml')
all_divs= soup.find_all('div', attrs={'class':"crux-body-copy"})
main_url="https://www.consumersreport.org"


products_list_with_links={div.a.string:div.a['href'] for div in all_divs}
for key,value in products_list_with_links.items():
    print(key,'   -->', main_url+value) 