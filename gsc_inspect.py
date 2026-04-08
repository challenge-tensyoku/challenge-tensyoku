"""
Google Search Console URL Inspection API - インデックス状況チェック
challenge-tensyoku用
"""

import subprocess
import json
import sys
import urllib.request
import time

SITE_URL = "https://challenge-tensyoku.com/"

URLS = [
    "https://challenge-tensyoku.com/",
    "https://challenge-tensyoku.com/freeter-seishain.html",
    "https://challenge-tensyoku.com/kotsotsu-shoshain.html",
    "https://challenge-tensyoku.com/neet-shushoku.html",
    "https://challenge-tensyoku.com/freeter-nenshu-sa.html",
    "https://challenge-tensyoku.com/agent-vs-site.html",
    "https://challenge-tensyoku.com/20dai-freeter-roadmap.html",
    "https://challenge-tensyoku.com/haken-seishain.html",
    "https://challenge-tensyoku.com/mikeiken-shigoto.html",
    "https://challenge-tensyoku.com/mensetsu-taisaku.html",
    "https://challenge-tensyoku.com/20dai-tensyoku-kostu.html",
    "https://challenge-tensyoku.com/rirekisho-kakikata.html",
    "https://challenge-tensyoku.com/freeter-chokin.html",
    "https://challenge-tensyoku.com/shikaku-osusume.html",
    "https://challenge-tensyoku.com/seishain-saishoni.html",
    "https://challenge-tensyoku.com/mensetsu-fukuso.html",
    "https://challenge-tensyoku.com/hitorigurase-seikatsuhi.html",
    "https://challenge-tensyoku.com/tensyoku-shippai.html",
    "https://challenge-tensyoku.com/freeter-eigyo.html",
    "https://challenge-tensyoku.com/tensyoku-kaisuu.html",
    "https://challenge-tensyoku.com/seishain-zeikin.html",
    "https://challenge-tensyoku.com/tensyoku-baito.html",
    "https://challenge-tensyoku.com/freeter-shibo-doki.html",
    "https://challenge-tensyoku.com/tensyoku-riyuu-kotaekata.html",
    "https://challenge-tensyoku.com/daini-shinsotsu-tensyoku.html",
    "https://challenge-tensyoku.com/freeter-nanasai.html",
    "https://challenge-tensyoku.com/freeter-shakaihoken.html",
    "https://challenge-tensyoku.com/kuuhaku-kikan-mensetsu.html",
    "https://challenge-tensyoku.com/jikopr-kakikata.html",
    "https://challenge-tensyoku.com/freeter-agent-osusume.html",
    "https://challenge-tensyoku.com/mensetsu-jikoshoukai.html",
    "https://challenge-tensyoku.com/mikeiken-it-tensyoku.html",
    "https://challenge-tensyoku.com/about.html",
    "https://challenge-tensyoku.com/freeter-naitei.html",
    "https://challenge-tensyoku.com/tensyoku-timing.html",
    "https://challenge-tensyoku.com/freeter-resume-photo.html",
]

def get_access_token():
    result = subprocess.run(
        ["/Users/yamato_o/Downloads/google-cloud-sdk/bin/gcloud", "auth", "application-default", "print-access-token"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("エラー: アクセストークン取得失敗")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()

def inspect_url(url, token):
    data = json.dumps({
        "inspectionUrl": url,
        "siteUrl": SITE_URL,
    }).encode()
    req = urllib.request.Request(
        "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "x-goog-user-project": "project-51d120e2-4c4f-4acd-9d8",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as res:
            return res.status, json.loads(res.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())

def main():
    print("アクセストークン取得中...")
    token = get_access_token()
    print("取得完了\n")

    indexed = []
    not_indexed = []
    errors = []

    total = len(URLS)
    for i, url in enumerate(URLS, 1):
        label = url.split("/")[-1] or "index"
        print(f"[{i:2d}/{total}] {label}", end=" ... ")

        status, body = inspect_url(url, token)

        if status != 200:
            msg = body.get("error", {}).get("message", str(body))
            print(f"エラー ({status}): {msg}")
            errors.append((label, msg))
        else:
            result = body.get("inspectionResult", {})
            index_status = result.get("indexStatusResult", {})
            verdict = index_status.get("verdict", "UNKNOWN")

            if verdict == "PASS":
                coverage = index_status.get("coverageState", "")
                print(f"インデックス済み ({coverage})")
                indexed.append(label)
            else:
                coverage = index_status.get("coverageState", verdict)
                print(f"未インデックス ({coverage})")
                not_indexed.append((label, coverage))

        time.sleep(0.5)  # API負荷軽減

    print(f"\n{'='*50}")
    print(f"インデックス済み: {len(indexed)}件 / {total}件")
    print(f"未インデックス : {len(not_indexed)}件")
    print(f"エラー         : {len(errors)}件")

    if not_indexed:
        print(f"\n【未インデックス一覧】")
        for label, reason in not_indexed:
            print(f"  - {label} ({reason})")

    if errors:
        print(f"\n【エラー一覧】")
        for label, msg in errors:
            print(f"  - {label}: {msg}")

if __name__ == "__main__":
    main()
