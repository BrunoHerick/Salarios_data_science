# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as grafico

# Atualizado em junho/2022

arquivo = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/dataScienceSalaries/ds_salaries.csv")

""" dois020us = arquivo[arquivo["work_year"] == 2020]
#dois020us = dois020us[dois020us["company_location"] == "US"]
dois020us = dois020us.sample(30)

dois021us = arquivo[arquivo["work_year"] == 2021]
#dois021us = dois021us[dois021us["company_location"] == "US"]
dois021us = dois021us.sample(30)

dois022us = arquivo[arquivo["work_year"] == 2022]
#dois022us = dois022us[dois022us["company_location"] == "US"]
dois022us = dois022us.sample(30)

mediaUS_2020 = np.mean(dois020us["salary_in_usd"])
mediaUS_2021 = np.mean(dois021us["salary_in_usd"])
mediaUS_2022 = np.mean(dois022us["salary_in_usd"])

varianciaUS_2020 = np.var(dois020us["salary_in_usd"])
varianciaUS_2021 = np.var(dois021us["salary_in_usd"])
varianciaUS_2022 = np.var(dois022us["salary_in_usd"])

mediaDasVarianciasUSanos = np.mean([varianciaUS_2020,varianciaUS_2021,varianciaUS_2022])
varianciaDasMediasUSanos = np.var([mediaUS_2020,mediaUS_2021,mediaUS_2022])

# f tabelado = 3.101 para 2,87 (cálculo feito para a variáve anos)
razaoF = ((varianciaDasMediasUSanos*30)/mediaDasVarianciasUSanos)
#print(razaoF) """

#===============================company_size============================
""" pequena = arquivo[arquivo["company_size"] == "S"]
medium = arquivo[arquivo["company_size"] == "M"]
grande = arquivo[arquivo["company_size"] == "L"]

#pequena = pequena[pequena["company_location"] == "US"]
#medium = medium[medium["company_location"] == "US"]
#grande = grande[grande["company_location"] == "US"]

#print(len(pequena))
#print(len(medium))
#print(len(grande))

pequena = pequena.sample(31)
medium = medium.sample(31)
grande = grande.sample(31)

#print(pequena["salary_in_usd"].describe())
#print(medium["salary_in_usd"].describe())
#print(grande["salary_in_usd"].describe())

#grafico.boxplot([pequena["salary_in_usd"],medium["salary_in_usd"],grande["salary_in_usd"]])
#grafico.grid()
#grafico.show()

mediaPequena = np.mean(pequena["salary_in_usd"])
mediaMedium = np.mean(medium["salary_in_usd"])
mediaGrande = np.mean(grande["salary_in_usd"])

varianciaPequena = np.var(pequena["salary_in_usd"])
varianciaMedium = np.var(medium["salary_in_usd"])
varianciaGrande = np.var(grande["salary_in_usd"])

mediaDasVarianciasTamanho = np.mean([varianciaPequena,varianciaMedium])
varianciaDasMediasTamanho = np.var([mediaPequena,mediaMedium])

# f tabelado = 3.101 para 2.87
razaoFtamanho = ((varianciaDasMediasTamanho*31)/mediaDasVarianciasTamanho)
#print(razaoFtamanho) """

#===========================remoto=presencial======================
""" print(arquivo["remote_ratio"].value_counts())

remoto = arquivo[arquivo["remote_ratio"] == 100]
hibrido = arquivo[arquivo["remote_ratio"] == 50]
presencial = arquivo[arquivo["remote_ratio"] == 0]

#remoto = remoto[remoto["company_location"] == "US"]
#hibrido = hibrido[hibrido["company_location"] == "US"]
#presencial = presencial[presencial["company_location"] == "US"]

remoto = remoto.sample(99)
hibrido = hibrido.sample(99)
presencial = presencial.sample(99)

#print(len(remoto))
#print(len(hibrido))
#print(len(presencial))

mediaRemoto = np.mean(remoto["salary_in_usd"])
mediaHibrido= np.mean(hibrido["salary_in_usd"])
mediaPresencial = np.mean(presencial["salary_in_usd"])

varianciaRemoto = np.var(remoto["salary_in_usd"])
varianciaHibrido= np.var(hibrido["salary_in_usd"])
varianciaPresencial = np.var(presencial["salary_in_usd"])

mediaDasVarianciasRemoto = np.mean([varianciaHibrido,varianciaPresencial])
varianciaDasMediasRemoto = np.var([mediaHibrido,mediaPresencial])

# f tabelado = 3.159 para 2.57
razaoFremoto = ((varianciaDasMediasRemoto*99.0)/mediaDasVarianciasRemoto)
print(razaoFremoto)

#grafico.boxplot([remoto["salary_in_usd"],hibrido["salary_in_usd"],presencial["salary_in_usd"]])
#grafico.grid()
#grafico.show() """

#=================QUESTÕES===============
# 1 - Houve diferença de salários das profissões de data science entre os anos de 2020, 2021 e 2022 nos EUA e em todo mundo ? Resposta: não houvem diferenças significativas de salários nos EUA ou no mundo entre os anos de 2020, 2021 e 2022.

# 2 - Existe diferença de salários entre as empresas de tamanho small, medium e large nos EUA e em todo mundo. Resposta: não existem diferenças de salários entre as empresas de tamanho S e M ou M e L nos EUA, porém existe uma diferença significativa de salário entre as empresas de tamanho S e M considerando todos os outros países da pesquisa.

# 3 - Existe diferença de salários entre as vagas de trabalho remoto nos EUA e em todo mundo. Resposta: Os salários são os mesmos para quem trabalha presencialmente ou remoto nos EUA, porém são diferentes entre quem trabalha de forma remota ou hibrida considerando todos os outros países da pesquisa.

# Experience level = EN Entry-level / Junior MI Mid-level / Intermediate SE Senior-level / Expert EX Executive-level / Director.
# employment_type = PT Part-time, FT Full-time, CT Contract, FL Freelance
# remote_ratio = the overall amount of work done remotely, possible values are as follows: 0 No remote work (less than 20%) 50 Partially remote 100 Fully remote (more than 80%)
# company_size = the average number of people that worked for the company during the year: S less than 50 employees (small) M 50 to 250 employees (medium) L more than 250 employees (large)