from typing import Dict, Any


ENABLE_TEMPLATE_PROCESSING = True
SUPERSET_FEATURE_EMBEDDED_SUPERSET = True
BABEL_DEFAULT_LOCALE = "zh"

# 10 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365 * 10
WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None
SESSION_COOKIE_SAMESITE = "Lax"
PUBLIC_ROLE_LIKE_GAMMA = True
SESSION_COOKIE_SECURE = False

# CORS
ENABLE_CORS = True
HTTP_HEADERS: Dict[str, Any] = {}
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
HTTP_HEADERS = {"X-Frame-Options": "ALLOWALL"}
ENABLE_CORS = True
FEATURE_FLAGS = {"ALERT_REPORTS": True, "EMBEDDED_SUPERSET": True}

# support current_datetime
from datetime import datetime, timedelta


def current_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"'%s'" % current_datetime


#
def shift_datetime(date_interval: int):
    shift_datetime = datetime.now() - timedelta(days=date_interval)
    return f"'%s'" % shift_datetime.strftime("%Y-%m-%d %H:%M:%S")


JINJA_CONTEXT_ADDONS = {
    "current_datetime": current_datetime,
    "shift_datetime": shift_datetime,
}
