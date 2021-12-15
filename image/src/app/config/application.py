"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "AWS_ACCESS_KEY_ID": env("AWS_ACCESS_KEY_ID", ""),
    "AWS_SECRET_ACCESS_KEY": env("AWS_SECRET_ACCESS_KEY", ""),
    "REGION": env("REGION", ""),
    "TABLE": env("TABLE", ""),
}
