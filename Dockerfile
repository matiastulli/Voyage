FROM python:3.11.6
WORKDIR /usr/src/app

EXPOSE 3001

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV DOTENV_PATH=/usr/src/app/.env
CMD ["/bin/bash", "/usr/src/app/entrypoint.sh"]