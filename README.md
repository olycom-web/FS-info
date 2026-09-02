# FS.com (www.fs.com) 全站数据归档仓库

> 目标站点: https://www.fs.com/ (美国英文站)
> 归档方式: 分批爬取 → 每批立即提交,可持续多轮“继续”扩大覆盖
> 首轮快照日期: 2026-09-02

## 重要说明(请先读)

1. **网络与工具限制**:本工作区代码环境只能访问 GitHub/PyPI(直连 fs.com 被网络策略阻断,已实测;GitHub Actions 亦因令牌权限无法创建)。因此抓取使用平台的网页读取通道,一次一页,分批进行。
2. **保真度边界**:抓取通道返回的是页面可见文本/图片URL/链接的结构化转写(Markdown 级),**不是**浏览器原始 HTML 字节;且价格、销量、库存为抓取时点快照。可见文字、型号、规格表、图片地址与链接均逐项保留。
3. **规模**:FS 官方口径 12 万+ SKU;仅商品详情 sitemap 即数万页。全部内容需多轮持续抓取(回复“继续”即可接力,进度保存在本仓库)。
4. robots.txt 允许通用爬虫抓取商品/分类/博客页(仅账户、购物车、结算与带查询参数页被禁),本归档严格遵守,仅爬取公开商品/内容页。

## 仓库结构

```
data/
  excel/FS.com_catalog_US.xlsx      ← 商品目录总表(Excel,每个SKU一行)
  excel/FS.com_catalog_US.csv       ← 同上 CSV(UTF-8 BOM,Excel可直接打开)
  products/catalog_001.jsonl        ← 原始抓取记录(JSON Lines,每行一个商品)
  products/catalog_002.jsonl        ← 后续批次按序递增 catalog_NNN.jsonl
  categories/CATEGORY_MAP.md        ← 全站分类树 + 进度状态
mirrors/                            ← 整页镜像(后续阶段;按板块分区)
tools/build_excel.py                ← 合并所有 jsonl → 去重 → 生成 xlsx/csv
```

## Excel 字段(表头)

SKU | 型号P/N | 一级分类 | 分类路径 | 商品标题 | 单价USD | 销量原文 | 销量(数值) | 评论数 | 标签(热门/新品) | 库存状态 | 可选配置 | 特性标签 | 主图URL | 商品页URL | 抓取日期 | 来源分类页

- “销量(数值)”:把 `2.8K Sold` 之类换算为整数(如 2800);K 为约数,精确值以“销量原文”为准。
- 同一 SKU 出现在多个分类页时按 SKU 去重,只保留一行(原始跨分类出现记录保留在 jsonl)。

## 当前进度(2026-09-02 第1轮)

- ✅ 全站分类入口盘点完成;Switches 分支全部分类 URL 已录入分类地图
- ✅ 交换机-数据中心分支:26 SKU 全部翻页完成
- ✅ 交换机-SME 分支:45 SKU 全部翻页完成(5页)
- ✅ 交换机-工业分支:48 SKU 全部翻页完成(5页;站点计数51含跨分类重复配件)
- 🔄 交换机其余分支第 1 页已抓:Enterprise(105,已录12)、PicOS DC(43,已录12)
- 📊 当前 Excel 共 **143 个 SKU**(去重后)
- ⬜ 待续(回复“继续”):Enterprise 2-11 页、PicOS DC 2-5 页 → PicOS Enterprise/PoE+/PoE 等其余交换机分支 → 其他一级分类(光模块/线缆/铜缆/机柜/网通等) → 商品详情页镜像 → 博客/方案/词条等文字板块

## 站点结构备忘(供后续轮次使用)

- 分类页: `https://www.fs.com/c/<slug>-<id>[?page=N]`,父分类聚合子类商品,约10-12个/页
- 商品页: `https://www.fs.com/products/<sku>.html`(含规格/详情/图片/文档;镜像阶段逐页归档)
- 图片域: `resource.fs.com`(URL 已随记录保存,镜像阶段按需批量取图)
- sitemap: `https://www.fs.com/sitemap.xml` → 各类型 sitemap .xml.gz(商品/博客/词条/方案/案例…)
- 商品页典型字段: P/N 型号、SKU、价格、X Sold(销量)、Reviews(评论数)、Questions、规格表、特性标签、图片集
