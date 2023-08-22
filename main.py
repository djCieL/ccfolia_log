import os
from bs4 import BeautifulSoup

# フォルダのパスを指定します
folder_path = "./log"

try:
    # フォルダ内のファイル一覧を取得します
    file_names = os.listdir(folder_path)
    
    # フォルダ内の各ファイル名を表示します
    # for file_name in file_names:
        # print(file_name)
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

    # リスト内の内容を表示
    for content in span_contents:
        print(content.strip())  # strip()を使って余分な空白を取り除きます
