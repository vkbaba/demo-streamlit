## demo-streamlit
streamlit とFastAPI を使ったデモアプリです。

## ローカルでのデプロイ
### 1. リポジトリのクローン
```bash
$ git clone
$ cd demo-streamlit
```

### 2. requirements.txt のインストール
```bash
$ pip install -r requirements.txt
```

### 3. ローカルでの起動
ターミナルを2つ開き、それぞれで以下のコマンドを実行します。
```bash
$ uvicorn main:app --reload
```
```bash
$ streamlit run streamlit_app.py
```

### 4. ブラウザでの確認
ブラウザで以下のURLにアクセスします。
```
http://localhost:8501
```

## クラウドでのデプロイ
今回はStrealit Cloud にStreamlitアプリを、Fly.io にFastAPIアプリをデプロイします。

### 1. Fly.io へのFastAPI アプリのデプロイ
```bash
$ fly login
$ fly launch --no-deploy
```
`? Would you like to copy its configuration to the new app? (y/N)`
はy を選択します。もしEnter でそのまま進めてしまったり、N を選択してしまった場合は、fly.toml の internal_port が8080 に変更になっている可能性があるため、 internal_port = 8000 に戻してください。

その後、アプリをデプロイします。デフォルトで可用性機能が有効になっていると、無料ユーザーでは2台目のVM のデプロイ時にエラーが発生するため、`--ha=false`で無効にします。

```bash
$ fly deploy --ha=false
```

### 2. Streamlit Cloud へのデプロイ
クローンしたリポジトリを自分のGitHub リポジトリにプッシュします（直接Fork しても構いません）。Git のSSH などの設定は、キカガクのPython アプリケーション開発コース Streamlit 実践 の記載をそのまま実施してください。やることは、新規リポジトリの作成、作成した新しいリポジトリをリモートリポジトリとして設定、プッシュです。

```bash
(リポジトリの作成後)
$ git remote set-url origin [新しいリポジトリのURL]
$ git push -u origin master
```

Streamlit Cloud にログインし、GitHubからリポジトリを選択します。注意点として、Advanced Settings でURL fly.io で払い出されたURL に変更します。

![Alt text](image.png)