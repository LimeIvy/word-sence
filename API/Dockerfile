FROM python:3.10.5-slim

# 作業ディレクトリを設定
WORKDIR /src

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピー
COPY requirements.txt .

# Pythonの依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY api/ ./api/

# モデルファイルをコピー（存在する場合）
COPY wiki_nouns_only.model ./wiki_nouns_only.model

# ポート8000を公開
EXPOSE 8000

# アプリケーションを起動
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]