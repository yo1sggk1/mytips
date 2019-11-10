import psycopg2
#コネクション作成
conn = psycopg2.connect("dbname=test host=localhost user=postgres")
#カーソル作成
cur = conn.cursor()
# SQLコマンド実行 (今回はテーブル作成)
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# SQLコマンド実行 (プレースホルダー使用。エスケープも勝手にされる)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
# SQL結果を受け取る
cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")
# コミット
conn.commit()
# クローズ
cur.close()
conn.close()
