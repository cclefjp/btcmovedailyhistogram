# getpatho
UTHのpathology system自動取得スクリプト

patho systemは2021年時点のEXPatho  
GitHubのプライベートリポジトリに取得するが、具体的なURL等はGitHubには持ち出さない。

---

## Version 0.3へのロードマップ

* HTMLの取得を関数化する
* configで取得するレポートをリストで複数指定できるようにし、インターバルを置いて取得する

---

## Version 0.2へのロードマップ

* "sid"をconstantsに入れる
* constants.jsonとconfig.jsonのテンプレートをgithubへ
* pathocodeが存在しないときの処理を追加
* 結果のHTMLを出力フォルダに保存

---

## Version 0.1へのロードマップ

* constants.jsonでURL等の定数を記述
* config.jsonで取得するpathoレポートを指定
* requestsライブラリを使ってHTTP通信
* 結果は標準出力へ表示



