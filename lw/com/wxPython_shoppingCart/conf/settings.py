# 登录的用户名和密码
ACCOUNTS = {
        'admin': {'pwd': 'admin'},
        'root': {'pwd': '123456'},
        'user': {'pwd': 'user123'},
    }

# 商品列名
COLUMN_NAMES = ["商品编号", "商品类别", "商品中文名", "商品英文名"]

# 商品类别
CATEGORY = ["食品", "酒类", "男装", "女装", "童装"]

# 商品信息，商品信息有点少，最好多搞几十条
PRODUCTS = [
    {'id': "001", 'category': "食品", 'name_cn': "薯片", 'name_en': "ShuPian"},
    {'id': "002", 'category': "酒类", 'name_cn': "葡萄酒", 'name_en': "PuTaoJiu"},
    {'id': "003", 'category': "男装", 'name_cn': "西装", 'name_en': "XiZhuang"},
    {'id': "004", 'category': "女装", 'name_cn': "短裙", 'name_en': "DuanQun"},
    {'id': "005", 'category': "童装", 'name_cn': "连衣裙", 'name_en': "LianYiQun"},
]