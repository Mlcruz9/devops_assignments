# Testing locally
# Run PostgreSQL container
docker run -d \
 --name attendance-db \
 -e POSTGRES_PASSWORD=password \
 -e POSTGRES_DB=mydb \
 -p 5432:5432 \
 postgres:15

# Export database connection string
export DB_LINK="postgresql://postgres:password@localhost:5432/mydb"

# cd to src

cd src

# Virtual env

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


## Building with docker bake

-login to ecr 
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 366140438193.dkr.ecr.ap-south-1.amazonaws.com

Docker buildx bake app --push 

## Local demo with tmpfs secrets (no secret manager)

1. Create a local secret file (not committed):
```bash
cp secrets/db_password.txt.example secrets/db_password.txt
```

2. Start services:
```bash
docker compose up --build
```

How it works:
- `./secrets/db_password.txt` is mounted read-only at `/run/local-secrets/db_password.txt`.
- Each container has `tmpfs` at `/run/secrets` (RAM only, not disk).
- Startup script copies the password from `/run/local-secrets/db_password.txt` into `/run/secrets/db_password`.
- PostgreSQL reads `POSTGRES_PASSWORD_FILE=/run/secrets/db_password`.
- App reads `DB_PASSWORD_FILE=/run/secrets/db_password`.
