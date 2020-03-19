from __future__ import print_function
import torch

# 创建一个 5x3 矩阵, 但是未初始化
x = torch.empty(5, 3)

# 创建一个随机初始化的矩阵
x = torch.rand(5, 3)

# 创建一个0填充的矩阵，数据类型为long
x = torch.zeros(5, 3, dtype=torch.long)

# 创建tensor并使用现有数据初始化
x = torch.tensor([5, 5, 3])

# 根据现有的张量创建张量。 这些方法将重用输入张量的属性，
# 例如, dtype 除非设置新的值进行覆盖
x = x.new_ones(5, 3, dtype=torch.double)  # new_* 方法来创建对象
x = torch.randn_like(x, dtype=torch.float)  # 覆盖 dtype!

# 获取 size,torch.Size返回值是 tuple类型, 所以它支持tuple类型的所有操作.
print(x.size())
print(x)

# 加法1:
y = torch.rand(5, 3)
print(x + y)
# 加法2:
print(torch.add(x, y))
# 提供输出tensor作为参数
result = torch.empty(5, 3)
torch.add(x, y, out=result)

print(result)
