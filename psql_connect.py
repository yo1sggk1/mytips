#psycopg2をインポート
import psycopg2 as psy2
# コネクション作成
conn = psy2.connect(dbname="", user="", password="", host="", port="")
# カーソル作成
cur = conn.cursor()
# テスト
test1 = "select * from logs;"
# SQL結果を受け取る
cur.execute(test1)
#結果の最初の行だけ取ってくる
result1 = cur.fetchone()
# 結果の表示
result1
#全ての結果を取得する
result2 = cur.fetchall()
# 結果の表示
result2
# クローズ
cur.close()
conn.close()