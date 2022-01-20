# DiscordVerifiyBot
## 色々
Version:1.0.0<br>LICENSE:MITLICENSE

## 詳細
Discordの認証Bot(適当)<br>
初期Prefixは`v!`

## 導入方法と使い方
1.とりあえず`config.json`にTokenを入れる<br>2.Botの設定で`SERVER MEMBERS INTENT`の項目をONにしてRunすれば動く(写真参照))<br>

![](https://data.tel1horjp.repl.co/png/member_intents.png)

## コマンド一覧
|v!verfiy|認証を作成する|
|-|-|
`v!verfiy [Role]`の形式で送信するとEmbedでボードが作成され、そこで認証できる<br>
`v!verfiy [Role] [MessagID]`の形式で送信すると指定されたメッセージIDのメッセージで認証ができる<br>
保存されるデータは最後に入力したコマンドのものになる
直接`verfiy.json`を変えてもできるがあまりおすすめしない

## その他
バグ報告とかは[Discordサーバー](https://tel1hor.tel1horjp.repl.co/tel1horserver.html)まで
