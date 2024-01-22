from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl

nav = webdriver.Chrome()
nav.get("https://www.kalunga.com.br/busca/1?q=teclado")

# //tag[@atributo='valor']

titulos = nav.find_elements(By.XPATH, "//h2[@class='blocoproduto__title mb-0 mt-2 pb-2 pb-lg-3']")
precos = nav.find_elements(By.XPATH, "//span[@class='blocoproduto__text blocoproduto__text--bold blocoproduto__price']")

workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')
sheetProdutos = workbook['produtos']
sheetProdutos['A1'].value = 'Nome'
sheetProdutos['B1'].value = 'Preço'

for titulo, preco in zip(titulos, precos):
    sheetProdutos.append([titulo.text, preco.text])
workbook.save('produtos.xlsx')