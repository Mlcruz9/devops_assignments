import os

variable_which_i_wont_use = "this is a variable which i wont use"


def _read_file_secret(path):
    if not path:
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return None


class Config:
    _db_link = os.getenv("DB_LINK")
    _db_password = _read_file_secret(os.getenv("DB_PASSWORD_FILE")) or os.getenv(
        "DB_PASSWORD"
    )

    SQLALCHEMY_DATABASE_URI = _db_link or (
        "postgresql://{user}:{password}@{host}:{port}/{db}".format(
            user=os.getenv("DB_USER", "postgres"),
            password=_db_password or "",
            host=os.getenv("DB_HOST", "db"),
            port=os.getenv("DB_PORT", "5432"),
            db=os.getenv("DB_NAME", "mydb"),
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
