# https://hub.docker.com/_/python
FROM python:3.10-slim-bullseye

# 作業ディレクトリの設定
WORKDIR /app
# 依存関係ファイルをコンテナにコピー
COPY requirements.txt requirements.txt

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコンテナにコピー
COPY ./main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]