# Usa a imagem oficial do Python 3.11
FROM python:3.11-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando padrão para rodar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
