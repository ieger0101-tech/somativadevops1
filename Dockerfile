# Usa uma imagem oficial do Python
FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do seu repositório para dentro do container
COPY . .

# Comando para rodar sua aplicação
CMD ["python", "main.py"]
