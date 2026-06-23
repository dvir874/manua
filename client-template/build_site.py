"""
Kore — Site Builder
מקבל config.json ומייצר אתר מוכן לפריסה
שימוש: python3 build_site.py config.json
"""

import json
import sys
import os
import shutil
from datetime import datetime

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "index.html")


def build(config_path):
    with open(config_path, encoding="utf-8") as f:
        config = json.load(f)

    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        html = f.read()

    config["YEAR"] = str(datetime.now().year)

    # Phone formatting
    phone = config.get("PHONE", "")
    digits = "".join(c for c in phone if c.isdigit())
    if digits.startswith("0"):
        config["PHONE_INTL"] = "972" + digits[1:]
    else:
        config["PHONE_INTL"] = digits

    # Replace all placeholders
    missing = []
    import re
    placeholders = re.findall(r'\{\{([^}]+)\}\}', html)
    for key in set(placeholders):
        if key in config:
            html = html.replace("{{" + key + "}}", str(config[key]))
        else:
            missing.append(key)

    if missing:
        print(f"⚠️  חסרים שדות: {', '.join(sorted(missing))}")

    # Output folder
    business_slug = config.get("BUSINESS_NAME", "site").replace(" ", "-")
    out_dir = os.path.join(os.path.dirname(__file__), "output", business_slug)
    os.makedirs(out_dir, exist_ok=True)

    out_file = os.path.join(out_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ אתר נוצר: {out_file}")
    print(f"📁 תיקייה: {out_dir}")
    print(f"🚀 כדי לפרוס: גרור את התיקייה ל-netlify.com/drop")
    return out_dir


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("שימוש: python3 build_site.py config.json")
        sys.exit(1)
    build(sys.argv[1])
