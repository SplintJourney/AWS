# AWS
・システム概要

AWSを用いたChat-GPTとの音声対話システム

・構成図

 <img width="942" alt="image" src="https://github.com/SplintJourney/AWS/assets/139861013/366fb3a7-c263-4b31-bc58-b785dfcb5d41">


・使ったサービス、言語

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

・開発期間

３ヶ月

・開発時期と人数

大学4年時に同じ研究室の友人３人で計4人で行なった

・担当箇所

AWS全般

・工夫点

ブラウザでマイクを活用するために、Httpsにしたこと

今後の拡張性を考慮し、Lambdaにてchat-gptのapiを操作、DBの管理を行なったこと



