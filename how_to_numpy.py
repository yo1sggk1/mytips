himport numpy as np

# リストから1次元配列作成
data1 = np.array([1, 2, 3])
data1

# リストから2次元配列作成
data2 = np.array([[1, 2, 3], [4, 5, 6]])
data2

# リストから3次元配列作成
data3 = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [14, 15, 16]]])
data3

# リストの代わりにタプルでも作成できます
data4 = np.array((1, 2, 3))
data4

# 明示的に型を指定
data6 = np.array([1, 2, 3], dtype=float)
data6.dtype

# 次元数（次元の軸の数、ベクトル→1、行列→2）
data2.ndim

# 各次元のサイズのタプル（2次元なら、行数と列数）
data2.shape

# 要素数
data2.size

# shapeは、reshape で変更できます
# 要素数が同じでないといけません
# 2×3の2次元配列から1次元の新しい配列を作成（data2はそのまま）
data2_reshape_6 = data2.reshape(6)
data2_reshape_6

# 2×3から3×2の新しい配列を作成（data2はそのまま）
data2_reshape_32 = data2.reshape((3, 2))
data2_reshape_32

# 転置（行と列を入れ替えた多次元配列）
data2.T

# リストから3次元配列作成
data3 = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [14, 15, 16]]])
data3

# 1要素のサイズ（バイト）
data2.itemsize

# 配列全体のサイズ（バイト）
data2.nbytes

# data2.nbytes と data2.itemsize * data2.size は等しい
data2.itemsize * data2.size