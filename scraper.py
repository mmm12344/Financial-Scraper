import requests
from bs4 import BeautifulSoup





def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    rs = requests.get(url=url, headers=headers)
    if rs.status_code != 404:
        return rs.text
    return False

def get_statistics_data(soup1, soup2):
    tbody1 = soup1.select("html body section.mainContainer section.mainContent section.main article.gridLayout section div.table-container table.table tbody")[0]
    tbody2 = soup2.select("html body section.mainContainer section.mainContent section.main article.gridLayout section div.table-container table.table tbody")[0]
    tr_elements1 = tbody1.find_all('tr')
    tr_elements2 = tbody2.find_all('tr')
    data_list = []
    for index in range(0, len(tr_elements1)-1):
        td_elements1 = tr_elements1[index].find_all('td')
        td_elements2 = tr_elements2[index].find_all('td')
        name = td_elements1[0].get_text()
        value1 = td_elements1[1].get_text()
        value2 = td_elements2[1].get_text()
        
        data_list.append([name, value1, value2])
    
    return data_list

def get_financial_data(soup1, soup2):
    table1 = soup1.select("html div#svelte main#nimbus-app section.mainContainer section.mainContent section.main article.gridLayout article section.container div.tableContainer div.table div.tableBody")[0]
    table2 = soup2.select("html div#svelte main#nimbus-app section.mainContainer section.mainContent section.main article.gridLayout article section.container div.tableContainer div.table div.tableBody")[0]
    elements1 = table1.find_all('div', class_='row')
    elements2 = table2.find_all('div', class_='row')
    data_list = []
    for index in range(0, len(elements1)-1):
        columns1 = elements1[index].find_all('div', class_='column')
        name = columns1[0].get_text()
        value1 = columns1[1].get_text()
        
        data_list.append([name, value1, None])
        
    for index in range(0, len(elements2)-1):
        columns2 = elements2[index].find_all('div', class_='column')
        name = columns2[0].get_text()
        value2 = columns2[1].get_text()
        for item in data_list:
            if item[0] == name:
                item[2] = value2
                break
    return data_list

def get_statistics(company1, company2):
    url1 = f"https://finance.yahoo.com/quote/{company1}/key-statistics/"
    url2 = f"https://finance.yahoo.com/quote/{company2}/key-statistics/"
    
    html1 = get_html(url1)
    html2 = get_html(url2)
    if(not html1 or not html2):
        return False
    
    soup1 = BeautifulSoup(html1, features="html.parser")
    soup2 = BeautifulSoup(html2, features="html.parser")
    
    return get_statistics_data(soup1, soup2)


def get_income_statement(company1, company2):
    url1 = f"https://finance.yahoo.com/quote/{company1}/financials/"
    url2 = f"https://finance.yahoo.com/quote/{company2}/financials/"
    
    html1 = get_html(url1)
    html2 = get_html(url2)
    if(not html1 or not html2):
        return False
    
    soup1 = BeautifulSoup(html1, features="html.parser")
    soup2 = BeautifulSoup(html2, features="html.parser")
    
    return get_financial_data(soup1, soup2)


def get_balance_sheet(company1, company2):
    url1 = f"https://finance.yahoo.com/quote/{company1}/balance-sheet/"
    url2 = f"https://finance.yahoo.com/quote/{company2}/balance-sheet/"
    
    html1 = get_html(url1)
    html2 = get_html(url2)
    if(not html1 or not html2):
        return False
    
    soup1 = BeautifulSoup(html1, features="html.parser")
    soup2 = BeautifulSoup(html2, features="html.parser")
    
    return get_financial_data(soup1, soup2)

def get_cash_flow(company1, company2):
    url1 = f"https://finance.yahoo.com/quote/{company1}/cash-flow/"
    url2 = f"https://finance.yahoo.com/quote/{company2}/cash-flow/"
    
    html1 = get_html(url1)
    html2 = get_html(url2)
    if(not html1 or not html2):
        return False
    
    soup1 = BeautifulSoup(html1, features="html.parser")
    soup2 = BeautifulSoup(html2, features="html.parser")
    
    return get_financial_data(soup1, soup2)


    