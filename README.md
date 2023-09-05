# 使用方法
logフォルダにココフォリアのログ(html形式)を配置。
main.pyを実行すると、outputフォルダ内にログの集計結果が.txtで出力される。


## やりたいこと
- .pyを.exe化して、python環境のない人にも使えるようにビルドする。
  - 以下を実行して、pyinstallerでのビルドを行う
  - pip install pyinstaller
  - pyinstaller --onefile main.py

## build時の問題  
- pyinstallerで.exe化すると、パス取得がおかしくなってしまう。
  - os.path.dirname(sys.argv[0])
  - 上記であれば、絶対パスを取得できた。

  - os.path.dirname(os.path.abspath(__file__))
  - こちらは.pyの間は動作したが、.exe化したあとは、おかしなパスを返すようになってしまった。

- python環境のないPCで.exeファイルを実行したところ、エラーが出ることがある問題が発生した。
  - pyinstallerがビルド時に、依存関係をうまく解決しきれていないために、not found系のエラーが発生している可能性がある。
  - hidden importを.specに記載していくことで、もしかしたら解消できるかもしれないが...?  

### 参考サイト
- https://syachiku.net/python%E3%82%92exe%E3%81%97%E3%81%9F%E9%9A%9B%E3%81%AB%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E5%AE%9F%E8%A1%8C%E3%83%91%E3%82%B9%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/
- https://teratail.com/questions/230283