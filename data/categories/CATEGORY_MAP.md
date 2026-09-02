# FS.com (www.fs.com, 美国英文站) — 分类地图 / Category Map

> 抓取日期: 2026-09-02 · 抓取工具: 平台网页转写(可见文本/图片URL/链接) · 数据快照有时间属性,价格/销量为当日值
> 状态标记: ✅已完成  🔄已开始(部分页码)  ⬜未开始

## 一级导航(首页 mega-menu,2026-09-02 快照)

主页横幅/促销/方案、分类入口、New Products / Recommended 等区块已归档于 `mirrors/00_homepage/`(见下),以下为商品分类树。

| 顶级分类 | 分类页 | 状态 |
|---|---|---|
| Switches 交换机 | /c/switches-4222 | 🔄 分支级进行中 |
| Networking(含路由器/防火墙/服务器等,子分类待细分) | /c/networking-... (待补) | ⬜ |
| Optical Transceivers 光模块 | (待补) | ⬜ |
| Fiber Optic Cables 光纤跳线/布线 | (待补) | ⬜ |
| Panels, Enclosures & Racks 配线/机柜 | (待补) | ⬜ |
| Optical Networking (波分/OLT等) | (待补) | ⬜ |
| Copper Systems 铜缆系统 | (待补) | ⬜ |
| Testers & Tools 测试仪/工具 | (待补) | ⬜ |
| 非商品板块: Solutions / Specials / Blogs / Case Study / Glossary / Resources / Support / Video / Services | sitemap 索引已获取 | ⬜ 镜像阶段 |

## Switches 分支详情(当前进度)

| 分类 | 分类URL | 商品数 | 状态 | 说明 |
|---|---|---|---|---|
| Switches (总) | https://www.fs.com/c/switches-4222 | - | ⬜ | 全交换机汇总列表 |
| ├ Data Center Switches | /c/data-center-switches-3404 | 26 | ✅ | 3页已全抓(含其下子类商品) |
| │ ├ 10/25G Data Center | /c/10-25g-data-center-switches-3500 | 4 | ✅ | 与主干重复,已确认可跳过 |
| │ ├ 100G Data Center | /c/100g-data-center-switches-3503 | 7 | ✅ | 与主干重复 |
| │ ├ Modular DC / NPB / NVIDIA / UFM / Accessories | /c/modular-data-center-switches-4225 等 | - | ⬜ | 产品已含在主干26个内,镜像阶段再抓子页 |
| ├ Enterprise Switches | /c/enterprise-switches-3079 | 105 | 🔄 | 第1/11页已抓,剩2-11页 |
| ├ PicOS® Data Center Switches | /c/picos-data-center-switches-5125 | 43 | 🔄 | 第1/5页已抓,剩2-5页 |
| ├ Industrial Ethernet Switches | /c/industrial-ethernet-switches-4073 | 51* | ✅ | 全部5页已抓;*官方计数含跨类重复配件,实际去重48个 |
| ├ SME Switches | /c/sme-switches-4235 | 45 | ✅ | 全部5页已抓(第5页为空),45个全部入表 |
| ├ PicOS® Enterprise Switches | /c/picos-enterprise-switches-4223 | ? | ⬜ | |
| ├ PicOS® PoE+ Switches | /c/picos-poe-switches-5585 | ? | ⬜ | |
| ├ PoE+ Switches | /c/poe-switches-3150 | ? | ⬜ | |
| └ (PicOS 软件/授权等专题) | ampcon / license | - | ⬜ | |

> 经验规则: 父分类页默认聚合所有子类商品并按销量排序,每页约10-12个;抓父分支根的分页即可覆盖整支。
> 翻页URL格式: `https://www.fs.com/c/<slug>-<id>?page=N`(已验证 page=2/3 有效)。

## 分片原始数据文件

- `data/products/catalog_001.jsonl` — Data Center Switches 全支(26) + PicOS® Data Center 第1页(12)
- `data/products/catalog_002.jsonl` — Enterprise(12) + Industrial(12) + SME(12),各第1页
- 汇总: `data/excel/FS.com_catalog_US.xlsx` + `.csv`(全量去重合并,每次运行 tools/build_excel.py 重新生成)
