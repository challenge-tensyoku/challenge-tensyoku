# Google Search Console 手動インデックス申請手順書
## チャレンジ転職（challenge-tensyoku）

作成日：2026-04-04  
対象サイト：https://challenge-tensyoku.github.io/challenge-tensyoku/

---

## 全体の流れ

1. Search Consoleにログイン・プロパティ確認
2. サイト所有権の確認（メタタグ検証）
3. サイトマップ送信
4. URLインデックス申請（25ページ）

---

## 対象URLリスト（全25ページ）

| # | URL |
|---|-----|
| 1 | https://challenge-tensyoku.github.io/challenge-tensyoku/ |
| 2 | https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-seishain.html |
| 3 | https://challenge-tensyoku.github.io/challenge-tensyoku/kotsotsu-shoshain.html |
| 4 | https://challenge-tensyoku.github.io/challenge-tensyoku/neet-shushoku.html |
| 5 | https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-nenshu-sa.html |
| 6 | https://challenge-tensyoku.github.io/challenge-tensyoku/agent-vs-site.html |
| 7 | https://challenge-tensyoku.github.io/challenge-tensyoku/20dai-freeter-roadmap.html |
| 8 | https://challenge-tensyoku.github.io/challenge-tensyoku/haken-seishain.html |
| 9 | https://challenge-tensyoku.github.io/challenge-tensyoku/mikeiken-shigoto.html |
| 10 | https://challenge-tensyoku.github.io/challenge-tensyoku/mensetsu-taisaku.html |
| 11 | https://challenge-tensyoku.github.io/challenge-tensyoku/20dai-tensyoku-kostu.html |
| 12 | https://challenge-tensyoku.github.io/challenge-tensyoku/rirekisho-kakikata.html |
| 13 | https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-chokin.html |
| 14 | https://challenge-tensyoku.github.io/challenge-tensyoku/shikaku-osusume.html |
| 15 | https://challenge-tensyoku.github.io/challenge-tensyoku/seishain-saishoni.html |
| 16 | https://challenge-tensyoku.github.io/challenge-tensyoku/mensetsu-fukuso.html |
| 17 | https://challenge-tensyoku.github.io/challenge-tensyoku/hitorigurase-seikatsuhi.html |
| 18 | https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-shippai.html |
| 19 | https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-eigyo.html |
| 20 | https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-kaisuu.html |
| 21 | https://challenge-tensyoku.github.io/challenge-tensyoku/seishain-zeikin.html |
| 22 | https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-baito.html |
| 23 | https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-shibo-doki.html |
| 24 | https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-riyuu-kotaekata.html |
| 25 | https://challenge-tensyoku.github.io/challenge-tensyoku/about.html |

※ URLの1〜24はsitemap.xmlに記載済み。25（about.html）はsitemap.xml未掲載のため個別申請のみ。

---

## STEP 1：Search Consoleにログイン・プロパティ確認

1. ブラウザで https://search.google.com/search-console/ を開く
2. challenge-tensyokuで使用しているGoogleアカウントでログインする
3. 左上のプロパティセレクタ（ドロップダウン）を確認する
4. 「https://challenge-tensyoku.github.io/challenge-tensyoku/」のプロパティが存在するか確認する
   - 存在する場合 → そのプロパティを選択してSTEP 2へ
   - 存在しない場合 → 「プロパティを追加」からURLプレフィックス型で追加し、STEP 2へ

---

## STEP 2：サイト所有権の確認（メタタグ検証）

index.htmlには既に以下のメタタグが記述されています。

```html
<meta name="google-site-verification" content="HUHKqryzjBKE0063mRAArV8Uj2S74yrHbLanFUyZfNk" />
```

### 所有権確認の手順

1. Search Consoleの左メニューから「設定」をクリックする
2. 「所有権の確認」セクションを開く
3. 「HTMLタグ」タブを選択する
4. 表示されるverification codeが `HUHKqryzjBKE0063mRAArV8Uj2S74yrHbLanFUyZfNk` と一致していることを確認する
5. 「確認」ボタンをクリックする
6. 「所有権が確認されました」と表示されれば完了

※ メタタグがすでにindex.htmlに入っているため、GitHubにpush済みであれば即座に確認が通るはずです。

---

## STEP 3：サイトマップの送信

### 手順

1. Search Consoleの左メニューから「サイトマップ」をクリックする
2. 「新しいサイトマップの追加」の入力欄に以下を入力する
   ```
   sitemap.xml
   ```
   （ベースURL「https://challenge-tensyoku.github.io/challenge-tensyoku/」は自動補完されます）
3. 「送信」ボタンをクリックする
4. ステータスが「成功しました」になることを確認する
   - 送信したサイトマップのURL：https://challenge-tensyoku.github.io/challenge-tensyoku/sitemap.xml
   - 検出されたURL数が「24」になっていることを確認する（about.htmlは未掲載のため）

---

## STEP 4：URLインデックス申請（URL検査ツール）

### URL検査ツールの基本操作

1. Search Consoleの上部検索バーにURLを貼り付けてEnterを押す
   （または左メニューの「URL検査」をクリックしてからURLを入力する）
2. 「URLはGoogleに登録されていません」または「URLはGoogleに登録されています」と表示される
3. 「インデックス登録をリクエスト」ボタンをクリックする
4. 「インデックス登録をリクエストできます」と表示されたら「リクエストを送信」をクリックする
5. 「リクエストを受け付けました」と表示されれば申請完了

### 全25ページの申請手順

以下のURLを上記の手順で**1件ずつ順番に申請**してください。
1件あたり約30秒〜1分かかります。25件で合計約20〜25分が目安です。

**申請URL一覧（コピー用）**

```
https://challenge-tensyoku.github.io/challenge-tensyoku/
https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-seishain.html
https://challenge-tensyoku.github.io/challenge-tensyoku/kotsotsu-shoshain.html
https://challenge-tensyoku.github.io/challenge-tensyoku/neet-shushoku.html
https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-nenshu-sa.html
https://challenge-tensyoku.github.io/challenge-tensyoku/agent-vs-site.html
https://challenge-tensyoku.github.io/challenge-tensyoku/20dai-freeter-roadmap.html
https://challenge-tensyoku.github.io/challenge-tensyoku/haken-seishain.html
https://challenge-tensyoku.github.io/challenge-tensyoku/mikeiken-shigoto.html
https://challenge-tensyoku.github.io/challenge-tensyoku/mensetsu-taisaku.html
https://challenge-tensyoku.github.io/challenge-tensyoku/20dai-tensyoku-kostu.html
https://challenge-tensyoku.github.io/challenge-tensyoku/rirekisho-kakikata.html
https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-chokin.html
https://challenge-tensyoku.github.io/challenge-tensyoku/shikaku-osusume.html
https://challenge-tensyoku.github.io/challenge-tensyoku/seishain-saishoni.html
https://challenge-tensyoku.github.io/challenge-tensyoku/mensetsu-fukuso.html
https://challenge-tensyoku.github.io/challenge-tensyoku/hitorigurase-seikatsuhi.html
https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-shippai.html
https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-eigyo.html
https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-kaisuu.html
https://challenge-tensyoku.github.io/challenge-tensyoku/seishain-zeikin.html
https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-baito.html
https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-shibo-doki.html
https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-riyuu-kotaekata.html
https://challenge-tensyoku.github.io/challenge-tensyoku/about.html
```

---

## STEP 5：申請後の確認・注意事項

### インデックス反映の目安

- 申請後、通常1〜7日でGoogleのインデックスに反映されます
- 早い場合は数時間で反映されることもあります
- 反映されたかどうかは、Search ConsoleのURL検査でそのURLを再確認すると確認できます

### 申請後の確認方法

1. Search Consoleの左メニューから「URL検査」を開く
2. 確認したいURLを入力してEnterを押す
3. 「URLはGoogleに登録されています」と表示されれば成功です
4. 「カバレッジ」セクションに「インデックス済み」と表示されていれば完了

### よくあるエラーと対処

| エラー | 原因 | 対処 |
|---|---|---|
| 「リクエストの上限に達しました」 | 1日あたりのリクエスト数制限（通常10〜100件）に達した | 翌日以降に残りを申請する |
| 「URLにアクセスできません」 | GitHubページが正しく公開されていない | GitHub Pagesの設定を確認する |
| 「canonicalがこのページを指していない」 | canonical設定の問題 | 各ページのcanonicalタグを確認する |
| 所有権確認が失敗する | メタタグが正しく反映されていない | GitHubへのpushが完了しているか確認する |

### Googleへの検索ランキング反映の目安

- インデックス登録から検索結果への表示まで：数日〜数週間
- 安定した順位がつくまで：1〜3ヶ月
- インデックス登録はあくまで「Googleに認識させること」であり、順位は別途コンテンツの品質によって決まります

---

## 申請進捗管理（チェックリスト）

各URLを申請したらチェックしてください。

- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-seishain.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/kotsotsu-shoshain.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/neet-shushoku.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-nenshu-sa.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/agent-vs-site.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/20dai-freeter-roadmap.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/haken-seishain.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/mikeiken-shigoto.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/mensetsu-taisaku.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/20dai-tensyoku-kostu.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/rirekisho-kakikata.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-chokin.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/shikaku-osusume.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/seishain-saishoni.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/mensetsu-fukuso.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/hitorigurase-seikatsuhi.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-shippai.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-eigyo.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-kaisuu.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/seishain-zeikin.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-baito.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/freeter-shibo-doki.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/tensyoku-riyuu-kotaekata.html
- [ ] https://challenge-tensyoku.github.io/challenge-tensyoku/about.html

---

*以上*
