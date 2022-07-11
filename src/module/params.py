from os import getenv

PARAMS = {
    "AWS_ACCESS_KEY_ID": getenv("AWS_ACCESS_KEY_ID", ""),
    "AWS_SECRET_ACCESS_KEY": getenv("AWS_SECRET_ACCESS_KEY", ""),
    "REGION": getenv("REGION", ""),
    "TABLE": getenv("TABLE", ""),
}
