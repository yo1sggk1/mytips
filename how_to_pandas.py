import pandas as pd
#csvfileをpandasで読み込む
reserve_tb = pd.read_csv('reserve.csv', encoding='utf-8')
#配列に文字配列をしてすることで指定した列名の列を抽出
reserve_tb[['reserve_id', 'hotel_id']]
#drop関数によって不要な行を削除
#axisを１にすることによって、列の削除を指定
#inplaceをTrueにすることで、reserve_tbの書き換えを指定
reserve_tb.drop(['people_num', 'total_price'], axis=1, inplace=True)
#query関数で日付によって結果を制限
reserve_tb.query('"2016-10-13" <= checkout_date <= "2016-10-14"')
#reserve.tbから50%ランダムサンプリング
reserve_tb.sample(frac=0.5)
#件数を指定するときは、
reserve_tb.sample(n=100)
#重複を排除したcustomerIDを返す
reserve_tb['customer_id'].unique()
#sample関数によって顧客ＩＤをサンプリング
target = pd.Series(reserve_tb['customer_id'].unique()).sample(frac=0.5)
#isin関数によってcutomer_idがサンプリングした顧客ＩＤにのいずれかに一致した行を抽出
reserve_tb[reserve_tb['customer_id'].isin(target)]

#agg関数を利用して集約処理をまとめて指定
#reserve_idを対象にcount関数を適用
#customer_idを対象にnunique関数を適用
result = reserve_tb \
    .groupby('hotel_id') \
    .agg({'reserve_id':'count', 'customer_id':'nunique'})
#reset_index関数によって列番号を振り直す
result.reset_index(inplace=False)
result.columns = ['hotel_id', 'rsv_cnt', 'cus_cnt']

#集約単位をhotel_idとpeople_numの組み合わせを指定
#集約したデータからtotal_priceを取り出し、sum関数に適用することで売上合計金額を算出
result = reserve_tb \
    .groupby(['hotel_id', 'people_num'])['total_price'] \
    .sum().reset_index()
#total_priceからprice_sumに名前を変更
result.rename(columns={'total_price':'price_sum'}, inplace=False)
