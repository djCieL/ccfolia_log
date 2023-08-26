import os
import re
from bs4 import BeautifulSoup

# 入力ログファイルのあるフォルダのパスを指定
folder_path = "./log"

# 結果出力先のフォルダのパスを指定
output_directory = "output"
# 出力ディレクトリが存在しない場合は作成しておく
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# オブジェクト格納用の配列
players = {}

# 名前を追加する関数
def add_name(name):
    # 新しい名前なら技名配列を追加しておく
    if not name in players:
        skills = {}
        players[name] = skills

# 技名を追加する関数
def add_skill(name, skill):
    # 新しい技名なら結果配列を追加しておく
    if not skill in players[name]:
        results = {}
        players[name][skill] = results

# 結果を追加する関数
def add_result(name, skill, result):
    if result in players[name][skill]:
        # 既存の結果ならカウントを+1
        players[name][skill][result] += 1
    else:
        # 新しい結果なら新たにkey-valueを作ってカウントを1で初期化
        players[name][skill][result] = 1

try:
    # フォルダ内のファイル一覧を取得
    file_names = os.listdir(folder_path)
except FileNotFoundError:
    print(f"{folder_path} が見つかりませんでした。")
except Exception as e:
    print(f"エラーが発生しました: {str(e)}")

for file_name in file_names:
    file_path = folder_path + "/" +  file_name
    try:
        # HTMLファイルを読み込みモード(r)で記載
        with open(file_path, "r", encoding="utf-8") as html_file:
            # ファイルの内容を読み込みます
            html_content = html_file.read()
    except FileNotFoundError:
        print(f"{html_file_path} が見つかりませんでした。")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, 'html.parser')

    # <span>タグの内容だけを取得し、リストに格納
    span_contents = [span.get_text() for span in soup.find_all('span')]

    # mode=0:テキスト内容がメインログかチェック
    # mode=1:プレイヤー名取得
    # mode=2:技、成功失敗取得
    mode = 0 # 初期値は0
    # プレイヤー名一時保存
    player_name = ""
    # スキル名一時保存
    play_skill = ""
    # 結果一時保存
    play_result = ""

    for content in span_contents:
        if content == " [メイン]":
            mode = 1 # メインの次の内容を取得するためmodeを変更
        elif mode == 1:
            player_name = content.strip() # strip()を使って余分な空白を取り除きます
            add_name(player_name )
            mode = 2 # スキル名、結果取得フェーズへ
        elif mode == 2:
            # 【】の中の文字を抽出　技名　
            match_brackets = re.search(r'【(.*?)】', content)
            # 【】が存在する場合のみ取得処理。それ以外は無視。
            if match_brackets:
                play_skill = match_brackets.group(1)
                add_skill(player_name, play_skill )
                # 一番最後の＞の後の文字を抽出　(一番最後の＞の後に結果がくるため)
                match_last_gt = re.search(r'＞([^＞]*)$', content)
                if match_last_gt:
                    play_result = match_last_gt.group(1).strip().replace('\n', '')
                    add_result(player_name, play_skill, play_result)
            mode = 0

for name in players:
    # ファイルに書き出す
    output_file_path = os.path.join(output_directory, "log.txt")
    # 追記モード(a)でファイルを開き、書き込み。
    with open(output_file_path, "a") as file:
        # fileオプションで、openしているファイルを指定すれば、printで書き込みできる
        print(f"{name}: {players[name]}" , file = file)