import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from google.colab import drive
plt.rcParams["figure.max_open_warning"] = 100

dados = pd.read_csv('/UserBehavior/UserBehaviorDataset.csv', sep = ",")

os_counts = dados['Operating System'].value_counts()
device_counts = dados['Device Model'].value_counts()
gender_counts = dados['Gender'].value_counts()
gender_dataUsage = dados.groupby('Gender')['Data Usage (MB/day)'].mean()
mean_by_gender = dados.groupby('Gender')['Screen On Time (hours/day)'].mean()

#FIGURA 1
media_consumo = dados.groupby('Number of Apps Installed')['Data Usage (MB/day)'].mean()
fig1 = plt.figure(figsize=(8, 5))
plt.plot(media_consumo.index, media_consumo.values, marker='o', linestyle='-', color='b')
plt.title('Consumo Médio de MB por Número de Apps Baixados')
plt.xlabel('Número de Apps Baixados')
plt.ylabel('Consumo Médio de MB')
plt.grid(True)
plt.show()

#FIGURA 2
media_consumo = dados.groupby('Age')['Data Usage (MB/day)'].mean()
fig2 = plt.figure(figsize=(8, 5))
plt.plot(media_consumo.index, media_consumo.values, marker='o', linestyle='-', color='b')
plt.title('Consumo Médio de MB por Idade')
plt.xlabel('Age')
plt.ylabel('Consumo Médio de MB')
plt.grid(True)
plt.show()

#FIGURA 3
horas_no_celular = dados.groupby('Age')['Screen On Time (hours/day)'].mean()
fig3 = plt.figure(figsize=(8, 5))
plt.plot(horas_no_celular.index, horas_no_celular.values, marker='o', linestyle='-', color='b')
plt.title('Tempo na Tela Médio por Idade')
plt.xlabel('idade')
plt.ylabel('Tempo na Tela')
plt.grid(True)
plt.show()

#FIGURA 4
tempo_por_dado = dados.groupby('Screen On Time (hours/day)')['Data Usage (MB/day)'].mean()
fig4 = plt.figure(figsize=(8, 5))
plt.plot(tempo_por_dado.index, tempo_por_dado.values, marker='o', linestyle='-', color='b')
plt.title('Uso de Dados e Tempo na Tela')
plt.xlabel('Tempo na tela')
plt.ylabel('Uso de Dados')
plt.grid(True)
plt.show()

#FIGURA 5
contagem_modelos = dados['Device Model'].value_counts()
fig5 = plt.figure(figsize=(8, 8))
plt.pie(contagem_modelos, labels=contagem_modelos.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Modelos de Celulares')
plt.show()

#TABELA FAIXA ETÁRIA X MODELO
bins = [18, 25, 30, 40, 50, 60]
labels = ['18-25', '25-30', '30-40', '40-50', '50-60']
dados['Age Group'] = pd.cut(dados['Age'], bins=bins, labels=labels, right=False)
favorite_models = dados.groupby('Age Group', observed=False)['Device Model'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else 'N/A')
favorite_models_df = favorite_models.reset_index()
favorite_models_df.columns = ['Age Group', 'Favorite Device Model']

#FIGURA 6
dados['consumo_de_energia'] = dados['Battery Drain (mAh/day)'] / dados['App Usage Time (min/day)']
lista= dados.groupby('Device Model')['consumo_de_energia'].mean()
fig6 = plt.figure(figsize=(10, 6))
lista.plot(kind='bar', color='skyblue')
plt.title('Consumo Médio de Bateria por Hora por Modelo')
plt.xlabel('Modelo do Celular')
plt.ylabel('Consumo Médio (mAh/hora)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#FIGURA 7
screen_time_by_model = dados.groupby('Device Model')['Screen On Time (hours/day)'].mean().sort_values(ascending=False)
fig7 = plt.figure(figsize=(10, 6))
screen_time_by_model.plot(kind='bar', color='skyblue')
plt.title('Tempo Médio de Tela Ligada por Modelo de Celular')
plt.xlabel('Modelo de Celular')
plt.ylabel('Tempo de Tela Ligada (horas/dia)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#FIGURA 8
tempo_de_uso = dados.groupby('Device Model')['App Usage Time (min/day)'].mean().sort_values(ascending=False)
fig8 = plt.figure(figsize=(10, 6))
tempo_de_uso.plot(kind='bar', color='skyblue')
plt.title('Tempo Médio de Uso por Modelo de Celular')
plt.xlabel('Modelo de Celular')
plt.ylabel('Tempo de uso')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#FIGURA 9
battery_usage_by_os = dados.groupby('Operating System')['Battery Drain (mAh/day)'].mean().sort_values(ascending=False)
fig9 = plt.figure(figsize=(10, 6))
battery_usage_by_os.plot(kind='bar', color='lightcoral')
plt.title('Consumo Médio de Bateria por Sistema Operacional')
plt.xlabel('Sistema Operacional')
plt.ylabel('Consumo de Bateria (mAh/dia)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#FIGURA 10
data_usage_by_os = dados.groupby('Operating System')['Data Usage (MB/day)'].mean().sort_values(ascending=False)
fig10 = plt.figure(figsize=(10, 6))
data_usage_by_os.plot(kind='bar', color='lightblue')
plt.title('Consumo Médio de Dados por Sistema Operacional')
plt.xlabel('Sistema Operacional')
plt.ylabel('Consumo de Dados (MB/dia)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#FIGURA 11
dados['consumo por genero'] = dados['Battery Drain (mAh/day)'] / dados['Screen On Time (hours/day)']
consumo = dados.groupby('Gender')['Battery Drain (mAh/day)'].mean()
fig11, ax = plt.subplots()
consumo.plot(kind='bar', color=['skyblue', 'lightgreen'], ax=ax)
ax.set_title('Consumo de Bateria e Gênero')
ax.set_xlabel('Gênero')
ax.set_ylabel('Consumo de Bateria (mAh/dia)')
ax.set_xticks(range(len(consumo.index)))
ax.set_xticklabels(consumo.index, rotation=0)
plt.show()

#FIGURA 12
dados_classes = [
    ["Classe 1", "Leve", "Uso mínimo", "Idosos"],
    ["Classe 2", "Ocasional", "Uso baixo", "Básico"],
    ["Classe 3", "Moderado", "Uso equilibrado", "Casual"],
    ["Classe 4", "Frequente", "Uso moderado", "Profissionais"],
    ["Classe 5", "Intenso", "Uso alto", "Influenciadores"]
]
fig12, ax = plt.subplots(figsize=(8, 4))
ax.axis('tight')
ax.axis('off')
tabela = ax.table(cellText=dados_classes,
                  colLabels=["Classe", "Tipo", "Características", "Exemplo"],
                  loc='center',
                  cellLoc='center',
                  rowLoc='center')
tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.auto_set_column_width(col=list(range(len(dados_classes[0]))))
plt.title("Classes de Comportamento de Usuários", fontsize=14, pad=20)
plt.show()

#FIGURA 13
media_bateria = dados.groupby('User Behavior Class')['Battery Drain (mAh/day)'].mean()
fig13, ax = plt.subplots(figsize=(8, 5))
ax.bar(media_bateria.index, media_bateria.values, color='skyblue')
ax.set_title('Média de Consumo de Bateria por Tipo de Usuário', fontsize=14)
ax.set_xlabel('Tipo de Usuário', fontsize=12)
ax.set_ylabel('Consumo Médio de Bateria (mAh/dia)', fontsize=12)
plt.show()

#FIGURA 14
media_t = dados.groupby('User Behavior Class')['Screen On Time (hours/day)'].mean()
fig14, ax = plt.subplots(figsize=(8, 5))
ax.bar(media_t.index, media_t.values, color='skyblue')
ax.set_title('Média de Tempo de Tela por Tipo de Usuário', fontsize=14)
ax.set_xlabel('Tipo de Usuário', fontsize=12)
ax.set_ylabel('Tempo de Tela (horas/dia)', fontsize=12)
plt.show()

#FIGURA 15
media_dad = dados.groupby('User Behavior Class')['Data Usage (MB/day)'].mean()
fig15, ax = plt.subplots(figsize=(8, 5))
ax.bar(media_dad.index, media_dad.values, color='skyblue')
ax.set_title('Média de Uso de Dados por Tipo de Usuário', fontsize=14)
ax.set_xlabel('Tipo de Usuário', fontsize=12)
ax.set_ylabel('Uso de Dados Médio (MB/dia)', fontsize=12)
plt.show()

#FIGURA 16
media_d = dados.groupby('User Behavior Class')['App Usage Time (min/day)'].mean()
fig16, ax = plt.subplots(figsize=(8, 5))
ax.bar(media_d.index, media_d.values, color='skyblue')
ax.set_title('Média de Uso de App por Tipo de Usuário', fontsize=14)
ax.set_xlabel('Tipo de Usuário', fontsize=12)
ax.set_ylabel('tempo de uso', fontsize=12)
plt.show()

#STREAMLIT
#TÍTULO E APRESENTAÇÃO DO DATASET
st.write("# Uso de Dispositivos Móveis e Comportamento do Usuário")

st.write("""
**GRUPO:**  
Adan Vinícius da Silva Gonçalves Simões - 124008542  
Igor Coelho de Carvalho - 124132870  
Luiz Gustavo Camporês - 124050638  
Ricardo Augusto de Borba - 124012274
""")

st.write("**Dataset utilizado:** *https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset*")

st.dataframe(dados)

#EXPLORANDO O DATASET
st.write("### Explorando um pouco o Dataset")

st.write("Vamos agora explorar um pouco mais do Dataset escolhido.")

st.write("""Primeiramente, vamos analisar, das pessoas contidas no Dataset, a qual gênero pertencem:
Assim, conforme a tabela abaixo, podemos perceber que, das pessoas que estamos analisando, temos 364 
homens e 336 mulheres.""")
st.table(gender_counts.reset_index().rename(columns={'count': 'Total Users'}))

st.write("""Agora, vamos analisar qual é o sistema operacional mais presente em nosso Dataset:
Conforme a tabela abaixo, podemos perceber que a maior parte das pessoas analisadas usa o sistema
 operacional Android, com um total de 554 usuários contra 146 usuários do sistema operacional iOS.""")
st.table(os_counts.reset_index().rename(columns={'count': 'Total Users'}))

st.write("""De acordo com a tabela acima, podemos perceber que os usuários analisados possuem mais 
aparelhos com o sistema operacional Android. Assim, é correto afirmar que, ao compararmos os aparelhos 
analisados, teremos um número maior de aparelhos Android. Isso é confirmado pela tabela abaixo, que mostra
a quantidade de usuários para cada modelo de aparelho.""")
st.table(device_counts.reset_index().rename(columns={'count': 'Total Users'}))

st.write("""Abaixo, apresentamos uma tabela que mostra a média da relação entre o gênero e o uso de dados 
por dia. Conforme a tabela, os homens usam, em média, 944 MB/dia, enquanto as mulheres usam 914 MB/dia..""")
st.table(gender_dataUsage.reset_index())

st.write("""Por fim, apresentamos uma tabela que mostra o tempo médio de tela ligada, dividido por gênero. 
Conforme a tabela, pode-se perceber que os homens analisados apresentam uma média de 5,28 horas por dia 
de tempo de tela ligada, enquanto as mulheres apresentam uma média de 5,26 horas por dia.""")
st.table(mean_by_gender.reset_index().rename(columns={'Screen On Time (hours/day)': 'Average Hours'}))

#GRÁFICOS
st.write("### Gráficos e análises do Dataset")

st.write("""Nesta parte, implementaremos alguns gráficos com base no Dataset escolhido para extrair 
informações de forma mais clara. Primeiramente, apresentamos um gráfico que mostra o Consumo Médio 
de MB por Número de Apps Baixados.""")
st.pyplot(fig1)
st.write("""Analisando o gráfico gerado, podemos notar que, de modo geral, conforme o número de Apps 
baixados aumenta, o consumo médio de internet também cresce.""")

st.pyplot(fig2)
st.write("""Para este segundo gráfico, temos uma representação que relaciona a idade com o consumo 
de internet. Analisando-o, podemos observar que ele é extremamente irregular, dificultando a extração 
precisa de informações.""")

st.pyplot(fig3)
st.write("""Neste terceiro gráfico, podemos notar que ele também é irregular. No entanto, seu formato 
acompanha o gráfico de idade e consumo de internet. Ou seja, as idades que mais consomem internet são 
as mesmas que apresentam maior consumo de dados, o que faz sentido. Agora, apresentamos um gráfico que 
compara o tempo de tela com o consumo de MB/dia.""")

st.pyplot(fig4)
st.write("""Assim, podemos concluir que, de fato, quanto maior o tempo de uso, maior é o consumo de dados.""")

st.write("""Agora, apresentamos um gráfico que mostra a distribuição dos modelos de celulares, ou seja, quais 
são os mais utilizados pelos usuários do Dataset.""")
st.pyplot(fig5)

st.write("""Com o gráfico acima, surge a dúvida: qual modelo de celular é o mais querido ou preferido em cada 
faixa etária? Para responder a isso, criamos a tabela abaixo, que apresenta essa informação.""")
st.write("Tabela com os modelos mais usados em cada faixa etária:")
st.table(favorite_models_df)

st.write("""Agora, realizaremos análises mais aprofundadas sobre os modelos de celulares presentes no Dataset. 
Primeiramente, apresentamos um gráfico que mostra o consumo médio de bateria por hora para cada modelo.""")
st.pyplot(fig6)
st.write("""Podemos estimar qual modelo de celular consome mais bateria com base no número de minutos de uso 
de aplicativos. Assim, é possível calcular quantos mAh por minuto cada modelo necessita para funcionar. Contudo, 
esse raciocínio pressupõe que os usos de aplicativos sejam, em média, semelhantes entre todos os usuários. Ou seja, 
que um usuário médio de iPhone utilize seu dispositivo de maneira similar a um usuário de Xiaomi. Embora essa forma 
de calcular o consumo médio de bateria por modelo possa não ser totalmente precisa, uma discrepância significativa 
entre os modelos analisados pode indicar diferenças no consumo de bateria. Analisando o gráfico, percebemos que o 
consumo entre os aparelhos é bem próximo.""")

st.write("""Após a análise acima, apresentamos agora um gráfico que mostra o tempo médio de tela ligada por modelo 
de celular analisado.""")
st.pyplot(fig7)

st.write("""Agora, apresentamos um gráfico que mostra o tempo médio de uso por modelo de celular.""")
st.pyplot(fig8)
st.write("""Observe que, de certa forma, a quantidade de tempo com a tela ligada é proporcional ao tempo de uso, e 
vice-versa. Embora isso possa parecer óbvio, significa que a razão entre o tempo de uso dos aplicativos e o tempo de 
tela ligada é constante.""")

st.write("""Comparando agora o consumo médio de bateria por sistema operacional, podemos notar, ao analisar o gráfico 
abaixo, que o sistema operacional iOS consome mais bateria que o Android.""")
st.pyplot(fig9)

st.write("""Agora, comparamos graficamente o consumo médio de dados por sistema operacional.""")
st.pyplot(fig10)
st.write("""Como podemos observar, em média, o iOS consome mais dados. Vale lembrar que, tanto nesta análise quanto na 
anterior, estamos realizando apenas um levantamento inicial, considerando uma distribuição homogênea e uniforme das 
necessidades dos usuários. Ou seja, assumimos que um usuário de um modelo X utiliza seu dispositivo da mesma forma e 
no mesmo tempo que um usuário de um modelo Y.""")

st.write("""Agora, apresentamos um gráfico que mostra a relação entre o consumo de bateria e o gênero. Conforme o gráfico, 
podemos notar que ambos os gêneros apresentam consumos de bateria bem similares.""")
st.pyplot(fig11)

st.write("""Observe que, até agora, consideramos que todos os usuários possuem um comportamento uniforme. Isso faz sentido 
ao analisarmos de forma macroscópica. Contudo, sabemos que esse raciocínio pode não ser totalmente preciso. No entanto, 
neste dataset, existe a categoria de comportamento do usuário. Veja um breve resumo de como ela funciona:""")
st.pyplot(fig12)
st.write("""Sendo assim, confirmaremos se os usuários estão ranqueados de forma correta. Ou seja, verificaremos se, quanto 
maior o número do usuário, maior é o consumo de dados, bateria, tempo em aplicativos e tempo de tela ligada.""")

st.pyplot(fig13)
st.pyplot(fig14)
st.pyplot(fig15)
st.pyplot(fig16)
st.write("""Para finalizar, podemos observar que, em todas as análises acima, de fato, quanto maior o número do tipo de 
usuário, maior é o consumo.""")
