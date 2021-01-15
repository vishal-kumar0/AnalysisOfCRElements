from bs4 import BeautifulSoup
from selenium import webdriver


def getDnaSeq(fr , to):
    driver = webdriver.Firefox()
    driver.get(f"https://www.ncbi.nlm.nih.gov/nuccore/NC_029267.1?report=fasta&from={fr}&to={to}&strand=true")
    
    body = BeautifulSoup(driver.page_source , "html.parser").body

    dnaseq = body.find("div" , {"id" : "viewercontent1"}).string

    idx = dnaseq.find('\n')
    dnaseq = dnaseq[idx:]
    dnaseq = dnaseq.strip()

    print(dnaseq)
    driver.close()

    return dnaseq

