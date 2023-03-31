#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e compramos e vendemos commodities:
# - Soja, Milho, Trigo, Petróleo, etc.
# 
# Precisamos pegar na internet, de forma automática, a cotação de todas as commodites e ver se ela está abaixo do nosso preço ideal de compra. Se tiver, precisamos marcar como uma ação de compra para a equipe de operações.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=share_link
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[42]:


get_ipython().system('pip install selenium')


# In[43]:


# Passo a passo:

from selenium import webdriver

# Passo 1: Abrir navegador.

from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://www.google.com.br/")


# In[44]:


# Passo 2: Importar a base de dados.

import pandas as pd

tabela = pd.read_excel("commodities.xlsx")
display(tabela)


# In[45]:


from selenium import webdriver
for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    print(produto)
    produto = produto.replace("ó", "o").replace("ã", "a").replace("ç", "c").replace("ú", "u").replace("é", "e").replace("á", "a")

    navegador = webdriver.Chrome()
    link = f"https://www.melhorcambio.com/{produto}-hoje"

    navegador.get(link)

    preco = navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute('value')
    
    preco = preco.replace(".", "").replace(",", ".")
    print(preco)
    
    tabela.loc[linha, "Preço Atual"] = float(preco)
    
display(tabela)

    
    
    
# Passo 3: Para cada produto na base de dados. 


# In[48]:


tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
display(tabela)


# In[51]:


# Exportar base pro Excel
tabela.to_excel("commodities_new.xlsx", index=False)


# In[ ]:




