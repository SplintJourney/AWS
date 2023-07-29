# AWS
**システム概要**

AWSを用いたChat-GPTとの音声対話システム

**背景**

・日本人の約７５%がモバイルからの検索を行う[1]

・世界では2020年までには約50%の検索が音声検索になると予想[2]

・そのため、今後日本でも同様に音声検索が主流になるのではないか

[1] https://webtan.impress.co.jp/e/2021/03/19/39461

[2]https://www.campaignlive.co.uk/article/just-say-it-future-search-voice-personal-digital-assistants/1392459

**構成図**

 <img width="942" alt="image" src="https://github.com/SplintJourney/AWS/assets/139861013/366fb3a7-c263-4b31-bc58-b785dfcb5d41">


**使ったサービス、言語**

<バックエンド AWS>

  EC2
  
  labmda(ランタイム:Python3.8)
  
  Amazon DynamoDB
  
  API Gateway

  Load Barancer

  chat-gptのapi

  Route53

  ACM(SSL証明書発行)

<フロントエンド>

  node.js
  
  javascript
  
  HTML
  
  CSS

**開発期間**

３ヶ月

**開発時期と人数**

大学4年時に同じ研究室の友人３人で計4人で行なった

**担当箇所**

バックエンド(AWS全般)

**工夫点**

ブラウザでマイクを活用するために、Httpsにしたこと

今後の拡張性を考慮し、Lambdaにてchat-gptのapiを操作、DBの管理を行なったこと

**課題**

Https通信にするためにロードバランサを用いる必要がなかった

効率的に検索するためのDynamoDBを活用することができなかった



