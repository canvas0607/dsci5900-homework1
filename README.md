# Inventory Project

这是一个使用 Python 3 编写的简单库存价值计算程序。程序将商品保存在
`inventory` 列表中，并通过 `calculate_total_value()` 函数计算所有商品的总价值。

## 环境要求

- Python 3
- 不需要安装第三方库

可以运行下面的命令检查 Python 版本：

```bash
python3 --version
```

## 项目文件

- `inventory.py`：库存数据和总价值计算函数。
- `test_inventory.py`：程序的单元测试。
- `promote.md`：程序要求、伪代码和测试用例伪代码。

## 运行程序

首先在终端中进入项目文件夹：

```bash
cd dsci5900-homework1
```

然后运行：

```bash
python3 inventory.py
```

预期输出：

```text
Total inventory value: $5399.65
```

## 运行测试用例

在项目文件夹中运行所有测试：

```bash
python3 -m unittest -v
```

也可以只运行库存测试文件：

```bash
python3 -m unittest -v test_inventory.py
```

如果所有测试都通过，终端会显示：

```text
Ran 7 tests

OK
```

测试内容包括：

1. 计算完整库存的总价值。
2. 计算空库存的总价值。
3. 计算单个商品的价值。
4. 拒绝缺少必要键的商品。
5. 拒绝数据类型错误的商品。
6. 拒绝数量或价格为负数的商品。
7. 拒绝不是字典的商品。
