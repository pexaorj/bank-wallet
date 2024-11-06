# Usar a imagem base do Python
FROM python:3.9-slim

# Defina a versão da aplicação como argumento do build
ARG APP_VERSION="unknown"

# Defina a variável de ambiente APP_VERSION para ser usada no código
ENV APP_VERSION=$APP_VERSION

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt ./

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app.py ./
COPY config.py ./
COPY models.py ./
COPY templates/ ./templates/

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"]