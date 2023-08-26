# 使用方法
logフォルダにココフォリアのログ(html形式)を配置。
main.pyを実行すると、outputフォルダ内にログの集計結果が.txtで出力される。


## やりたいこと
- .pyを.exe化して、python環境のない人にも使えるようにビルドする。
  - 以下を実行して、pyinstallerでのビルドを行う
  - pip install pyinstaller
  - pyinstaller --onefile main.py
  