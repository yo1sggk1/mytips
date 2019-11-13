# 簡易ヘルプ
%quickref
# Escキーで画面下部の表示を消せます

# グラフのインライン描画指定
%matplotlib inline

# 変数一覧（Jupyterでは予めいくつか設定されていることもあります）
a = 10
%whos

# 1行を1回、時間計測
%time a = 10

%%time
# セルを1回、時間計測
a = 10
b = a + 1

# 1行を複数回、時間計測
%timeit -n10 -r3 c = 10
# 変数cは定義されていません
try:
    print(c)
except NameError as e:
    print(e)

%%timeit -n10 -r3
# セルを複数回、時間計測
a = 10
b = a + 1

# 変数aをJupyterのDBに保存
a = 20
%store a

# 保存されている変数の一覧
%store

del a  # 変数aを削除
try:
    print(a)  # 定義されていないのでエラー
except NameError as e:
    print(e)

# aを戻す
%store -r
print(a)

!ls ~/.ipython/profile_default/db/autorestore

# DBの変数を全て削除
%store -z
# 保存されている変数の一覧は空に
%store

!ls ~/.ipython/profile_default/db/autorestore

# pickle形式で保存
import pickle
a = 30
with open('a', 'wb') as fp:
    pickle.dump(a, fp)

!rm a

#エラー直後に実行でデバッグしてくれる
%debug