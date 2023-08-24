import os
from bs4 import BeautifulSoup

# フォルダのパスを指定
folder_path = "./log"

# オブジェクト格納用の配列
players = {}

# 名前を受け取る関数
def process_name(name):
    if name in players:
        # 既存の名前ならカウントを+1
        players[name] += 1
    else:
        # 新しい名前ならカウントを1に初期化
        players[name] = 1

try:
    # フォルダ内のファイル一覧を取得します
    file_names = os.listdir(folder_path)
except FileNotFoundError:
    print(f"{folder_path} が見つかりませんでした。")
except Exception as e:
    print(f"エラーが発生しました: {str(e)}")

for file_name in file_names:
    file_path = folder_path + "/" +  file_name
    try:
        # HTMLファイルを読み込みモードで開きます
        with open(file_path, "r", encoding="utf-8") as html_file:
            # ファイルの内容を読み込みます
            html_content = html_file.read()
            
            # HTMLコンテンツを表示するか、必要な処理を行います
            # print(html_content)
    except FileNotFoundError:
        print(f"{html_file_path} が見つかりませんでした。")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, 'html.parser')

    # <span>タグの内容を取得し、リストに格納
    span_contents = [span.get_text() for span in soup.find_all('span')]

    # リスト内の内容を表示(flagが1の時だけ)
    flag = 0
    for content in span_contents:
        if content == " [メイン]":
            flag = 1 # メインの次の内容を取得するためflagを立てる
        elif flag == 1:
            process_name( content.strip() )# strip()を使って余分な空白を取り除きます
            flag = 0
    
# 名前ごとのカウントを表示
for name, count in players.items():
    print(f"{name}: {count}回")