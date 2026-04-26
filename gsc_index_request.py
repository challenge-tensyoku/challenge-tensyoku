"""
Google Indexing API - URLインデックス申請スクリプト
challenge-tensyoku用
"""

import subprocess
import json
import sys

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
    "https://challenge-tensyoku.com/freeter-nenkin.html",
    "https://challenge-tensyoku.com/freeter-shotoku-zeikin.html",
    "https://challenge-tensyoku.com/seishain-bonus.html",
    "https://challenge-tensyoku.com/tensyoku-age-limit.html",
    "https://challenge-tensyoku.com/tensyoku-mensetsu-shitsumon.html",
    "https://challenge-tensyoku.com/tensyoku-naitei-after.html",
    "https://challenge-tensyoku.com/tensyoku-doki.html",
    "https://challenge-tensyoku.com/freeter-kekkon.html",
    "https://challenge-tensyoku.com/freeter-car-loan.html",
    "https://challenge-tensyoku.com/freeter-baito-chigai.html",
    "https://challenge-tensyoku.com/eigyo-mikeiken.html",
    "https://challenge-tensyoku.com/jimukei-tensyoku.html",
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

def request_indexing(url, token):
    import urllib.request
    data = json.dumps({"url": url, "type": "URL_UPDATED"}).encode()
    req = urllib.request.Request(
        "https://indexing.googleapis.com/v3/urlNotifications:publish",
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
    print(f"取得完了\n")

    success = 0
    failed = 0

    total = len(URLS)
    for i, url in enumerate(URLS, 1):
        print(f"[{i:2d}/{total}] {url.split('/')[-1] or 'index'}", end=" ... ")
        status, body = request_indexing(url, token)
        if status == 200:
            print("OK")
            success += 1
        else:
            print(f"NG ({status}): {body.get('error', {}).get('message', body)}")
            failed += 1

    print(f"\n完了: 成功 {success}件 / 失敗 {failed}件")

if __name__ == "__main__":
    main()
