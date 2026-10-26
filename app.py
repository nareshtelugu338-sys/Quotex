import os, json, urllib.parse, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

API_BASE = "https://otcharts.com"
PORT = int(os.environ.get("PORT", "8000"))
KEY = os.environ.get("OTCHARTS_API_KEY", "").strip()

def api_get(path):
    if not KEY:
        raise RuntimeError("సర్వర్‌లో OTCHARTS_API_KEY సెట్ చేయలేదు.")
    req = urllib.request.Request(API_BASE + path, headers={
        "Authorization": "Bearer " + KEY,
        "Accept": "application/json",
        "User-Agent": "QuotexSignalPWA/1.0"
    })
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))

class Handler(BaseHTTPRequestHandler):
    def send_bytes(self, status, data, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)
    def send_json(self, status, obj):
        self.send_bytes(status, json.dumps(obj, ensure_ascii=False).encode(), "application/json; charset=utf-8")
    def do_GET(self):
        u=urllib.parse.urlparse(self.path)
        if u.path == "/api/status":
            self.send_json(200, {"ok": bool(KEY), "message": "API key సెట్ అయింది" if KEY else "సర్వర్‌లో API key సెట్ చేయండి"})
            return
        if u.path == "/api/symbols":
            try:
                self.send_json(200, api_get("/v1/symbols?venue=quotex"))
            except Exception as e: self.send_json(502, {"error": str(e)})
            return
        if u.path == "/api/candles":
            q=urllib.parse.parse_qs(u.query)
            symbol=q.get("symbol", [""])[0]
            tf=q.get("tf", ["60"])[0]
            if not symbol or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_#.-/" for c in symbol):
                self.send_json(400, {"error":"చెల్లని symbol"}); return
            if tf not in ("60","300"):
                self.send_json(400, {"error":"M1=60 లేదా M5=300 మాత్రమే"}); return
            try:
                path="/v1/candles?"+urllib.parse.urlencode({"venue":"quotex","symbol":symbol,"tf":tf,"limit":"100"})
                self.send_json(200, api_get(path))
            except Exception as e: self.send_json(502, {"error": str(e)})
            return
        if u.path == "/" or u.path == "/index.html":
            try:
                with open("public/index.html","rb") as f: self.send_bytes(200,f.read(),"text/html; charset=utf-8")
            except Exception: self.send_json(500,{"error":"public/index.html missing"})
            return
        if u.path in ("/manifest.json","/sw.js","/icon.svg"):
            name="public"+u.path
            typ={"manifest.json":"application/manifest+json","sw.js":"application/javascript","icon.svg":"image/svg+xml"}[u.path[1:]]
            try:
                with open(name,"rb") as f: self.send_bytes(200,f.read(),typ)
            except Exception: self.send_json(404,{"error":"not found"})
            return
        self.send_json(404,{"error":"not found"})
    def log_message(self, fmt, *args):
        print("%s - %s"%(self.address_string(),fmt%args))

if __name__ == "__main__":
    print("Quotex Signal PWA server on port", PORT)
    print("API key configured:", bool(KEY))
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
