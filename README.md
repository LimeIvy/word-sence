# ワードセンス

日本語を用いたカードゲームアプリケーションです。

## プロジェクト構成

### Frontend (`/frontend`)
- Next.js 14 + TypeScript + TailwindCSS
- Neonを使用したデータベース連携
- カードゲームのUI/UX

### API (`/API`)
- FastAPIを使用したバックエンドAPI
- 文字合成の処理

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
AUTH_SECRET=
AUTH_GOOGLE_ID=
AUTH_GOOGLE_SECRET=
DATABASE_URL=
```

## 開発

このプロジェクトは以下の技術スタックを使用しています：
- **Frontend**: Next.js 14, TypeScript, TailwindCSS, Shadcn/ui,NextAuth,Drizzle,Neon
- **Backend**: FastAPI, Python
- **Database**: PostgreSQL (Neon)