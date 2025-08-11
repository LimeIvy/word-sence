# JP Card Game

日本語のカードゲームアプリケーションです。

## プロジェクト構成

### Frontend (`/frontend`)
- Next.js 14 + TypeScript + TailwindCSS
- Supabaseを使用したデータベース連携
- カードゲームのUI/UX

### API (`/API`)
- FastAPIを使用したバックエンドAPI
- カードゲームのロジック処理
- データベース操作

## セットアップ

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### API
```bash
cd API
pip install -r requirements.txt
uvicorn api.main:app --reload
```

## 環境変数

### Frontend
`.env.local`ファイルを作成し、以下を設定：
```
DATABASE_URL=your_supabase_database_url
```

### API
`.env`ファイルを作成し、必要に応じて環境変数を設定

## 開発

このプロジェクトは以下の技術スタックを使用しています：
- **Frontend**: Next.js 14, TypeScript, TailwindCSS, Supabase
- **Backend**: FastAPI, Python
- **Database**: PostgreSQL (Supabase)

## ライセンス

MIT License
