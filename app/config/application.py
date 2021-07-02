"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "INPUT_LABEL": env("INPUT_LABEL", "temperature"),
    "OUTPUT_LABEL": env("OUTPUT_LABEL", "temperature"),
    "OUTPUT_UNIT": env("OUTPUT_UNIT", "Celsius"),
    "AWS_ACCESS_KEY_ID": env("AWS_ACCESS_KEY_ID", ""),
    "AWS_SECRET_ACCESS_KEY": env("AWS_SECRET_ACCESS_KEY", ""),
    "REGION": env("REGION", ""),
    "TABLE": env("TABLE", ""),
}
