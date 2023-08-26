import os
import re
from bs4 import BeautifulSoup

# フォルダのパスを指定
folder_path = "./log"

# オブジェクト格納用の配列
players = {}

# 名前を追加する関数
def add_name(name):
    if name in players:
        # 既存の名前ならそのまま
        pass
    else:
        # 新しい名前なら技名配列を追加しておく
        skills = {}
        players[name] = skills

# 技名を追加する関数
def add_skill(name, skill):
    if skill in players[name]:
        # 既存の技名ならそのまま
        pass
    else:
        # 新しい技名なら結果配列を追加しておく
        results = {}
        players[name][skill] = results

# 結果を追加する関数
def add_result(name, skill, result):
    if result in players[name][skill]:
        # 既存の結果ならカウントを+1
        players[name][skill][result] += 1
    else:
        # 新しい結果ならカウントを1で初期化
        players[name][skill][result] = 1

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

    # mode=0:テキスト内容がメインログかチェック mode=1:プレイヤー名取得 mode=2:技、成功失敗取得
    mode = 0
    player_name = ""
    play_skill = ""
    play_result = ""
    for content in span_contents:
        if content == " [メイン]":
            mode = 1 # メインの次の内容を取得するためflagを立てる
        elif mode == 1:
            player_name = content.strip() # strip()を使って余分な空白を取り除きます
            add_name(player_name )
            mode = 2
        elif mode == 2:
            # 【】の中の文字を抽出　技名　
            match_brackets = re.search(r'【(.*?)】', content)
            if match_brackets:
                play_skill = match_brackets.group(1)
                add_skill(player_name, play_skill )
                # 一番最後の＞の後の文字を抽出　結果
                match_last_gt = re.search(r'＞([^＞]*)$', content)
                if match_last_gt:
                    play_result = match_last_gt.group(1).strip().replace('\n', '')
                    add_result(player_name, play_skill, play_result)

            mode = 0

for name in players:
    print(f"{name}: {players[name]}")
