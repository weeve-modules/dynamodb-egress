"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "dynamodb-egress"),
    "MODULE_TYPE": env("MODULE_TYPE", "EGRESS"),
    "EGRESS_URL": env("EGRESS_URL", "http://localhost:8000"),
    "INGRESS_HOST": env("INGRESS_HOST", "0.0.0.0"),
    "INGRESS_PORT": env("INGRESS_PORT", "80"),
    "INGRESS_PATH": env("INGRESS_PATH", "/")
}
