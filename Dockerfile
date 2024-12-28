# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なファイルをコピー
COPY ./app /app
COPY requirements.txt /app/requirements.txt  

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# メインスクリプトを実行
CMD ["python", "main.py"]
