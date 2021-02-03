# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.
# %pip install cufflinks

# Commented out IPython magic to ensure Python compatibility.
#A partir do plotly versão 4.0, todas as funcionalidades relacionadas ao Chart Studio foram movidas para a chart_studiobiblioteca. 
#https://plotly.com/python/v4-migration/#online-features-plotlyplotly-moved-to-chartstudio-package
# %pip install chart-studio

import pandas as pd
import cufflinks as cl

#https://chart-studio.plotly.com/settings/api
#import plotly.tools as tls
#A partir do plotly versão 4.0, todas as funcionalidades relacionadas ao Chart Studio foram movidas para a chart_studiobiblioteca. 
#https://plotly.com/python/v4-migration/#online-features-plotlyplotly-moved-to-chartstudio-package
#from chart_studio.plotly import plot, iplot
import chart_studio

#https://plotly.com/python/getting-started-with-chart-studio/
chart_studio.tools.set_credentials_file(username='giovanebmr', api_key='cK2EmejarWAwyyYW9PN7')

#colocando o gráfico no modo de compartilhamento privado
chart_studio.tools.set_config_file(world_readable=False, sharing='private')

caminho = '/content/df_vendas_novo.csv'
data = pd.read_csv(caminho)
data.columns = ['Data Venda','Data Envio','ID Loja','ID Produto','ID Cliente','No. Venda','Custo Unitário','Preço Unitário','Quantidade','Valor Desconto','Valor Venda','Produto','Fabricante','Marca','Classe','Cor','custo','lucro','Tempo de envio']

df = data[['Valor Venda','lucro','Quantidade']]

"""# **Criando um gráfico de linhas com DataFrame Pandas**"""

layout = {
    'title':'Gráfico de um DataFrame',
    'xaxis':{'title':'eixo X'},
    'yaxis':{'title':'eixo Y'}
}

df.iplot(filename='grafico-de-linhas-plotly', layout=layout)