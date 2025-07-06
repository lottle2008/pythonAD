import numpy as np
# 创建一个示例数组
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# 基本属性
print("数组形状 (shape)：", arr.shape)  # (3, 4) 表示3行4列
print("数组维度 (ndim)：", arr.ndim)   # 2 表示二维数组
print("数组元素总数 (size)：", arr.size)  # 12 个元素
print("数组数据类型 (dtype)：", arr.dtype)  # 数据类型
print("每个元素字节大小 (itemsize)：", arr.itemsize)  # 字节数

# 内存相关信息
print("数组总字节数 (nbytes)：", arr.nbytes)  # size * itemsize
print("数组内存信息：", arr.flags)  # 显示内存布局等信息