#!/bin/bash
# פריסת אתר "המרחב בנפש" ל-surge.sh — לינק ציבורי קבוע
# הרצה:  bash deploy.sh
set -e

DIR="$(cd "$(dirname "$0")" && pwd)/hamerchav"
DOMAIN="hamerchav-banefesh.surge.sh"

# 200.html כדי שכל נתיב יפנה ל-index (SPA-safe)
cp "$DIR/index.html" "$DIR/200.html" 2>/dev/null || true

echo ""
echo "==============================================="
echo "  פורס את 'המרחב בנפש' ל: https://$DOMAIN"
echo "==============================================="
echo ""
echo "בפעם הראשונה surge יבקש אימייל וסיסמה —"
echo "פשוט המצא סיסמה חדשה (זה יוצר חשבון חינמי)."
echo ""

npx --yes surge "$DIR" "$DOMAIN"

echo ""
echo "✅ בוצע! הלינק לשלוח לבועז:  https://$DOMAIN"
