# Setup Guide

## Database

1. Create the database:

   ```sql
   CREATE DATABASE yojanaconnect;
   ```

2. Import schema and data:

   ```bash
   mysql -u root -p yojanaconnect < database/yojanaconnect.sql
   ```

## Backend

Copy `backend/.env.example` to `backend/.env` and set your MySQL credentials.

Start the API server:

```bash
pnpm backend
```

Health check: `GET http://localhost:3000/api/healthz`

## Frontend

The Vite dev server proxies `/api` requests to the backend (default: `http://localhost:3000`).

Start the frontend:

```bash
pnpm frontend
```

Open http://localhost:5173

## Production Build

```bash
pnpm build
```

Frontend output is written to `frontend/dist`.
