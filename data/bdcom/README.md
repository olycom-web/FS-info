# data/bdcom/ 归档说明(2026-09-11 建立)

BDCOM(上海博达数据通信,1994 年成立)已并入 FS.com 体系。本目录归档
**bdcomnetworks.com 英文主站**全站公开内容(用户指令:与 FS.com 归档同规格,"甚至更多更深")。

## 范围与口径

- 范围:英文主站全部板块 —— 产品(6 大类)、方案、客户案例、新闻、公司/招聘/保修/联系等静态页、下载资源。
- 其他语言站(中文 www.bdcom.com.cn、法 /fr/、西 /es/、俄 /ru/)本轮**不抓**(用户确认,后续按需)。
- 抓取通道:仅平台网页转写通道(一次一页,分片返回;与 FS.com 相同)。价格/内容为抓取时点快照(ts 记入记录)。

## ⚠️ robots.txt 合规记录(用户已确认)

- 站点声明:`robots.txt` = `User-Agent: * / Disallow: /`(禁止所有爬虫)。
- 用户明确确认(**2026-09-11**):继续抓取,用户指令优先。
- 执行方式:一次一页、低频、仅公开页面内容,归档用途;本记录永久保留供追溯。

## 目录结构

```
data/bdcom/
  README.md                  ← 本文件
  CATEGORY_MAP.md            ← 站点导航/分类图 + 页面清单与进度
  urls/
    inventory.md             ← 全站 URL 台账(去重,按类型计数,附来源 sweep)
    sweep_<keyword>.txt      ← 搜索枚举原始记录(keyword → 结果链接)
  products/
    catalog_NNN.jsonl        ← 产品页记录(系列级: id/pn/标题/分类/型号/URL/ts)
  excel/                     ← 汇总表(枚举完成后生成)
  details/<id>.md            ← 产品系列页整页镜像
  news/<id>.md               ← 新闻页镜像
  cases/<id>.md              ← 客户案例页镜像
  solutions/<id>.md          ← 解决方案页镜像
  site/<name>.md             ← 静态页镜像(about/career/warranty/contact 等)
  downloads/<id>.md          ← 产品下载区链接清单(+可解析的 PDF 文本)
```

## 镜像约定(沿袭 data/details/README.md 的压缩原则,按 BDCOM 页面形态适配)

1. 图 URL 重复块去重(同图 180x180/全尺寸各留一份,注明去重)。
2. 成对 `[X](a) [X](b)` 重复链接归一为后者;`[X](站点根)` 占位链接删除。
3. 产品页标签区(Overview / Typical Application / Technical Parameter / Features / Ordering Information / Download)
   全部正文逐字保留;规格表逐字保留。
4. 页尾重复块(语言切换链接、版权/导航尾)压缩为一行注明。
5. 认证/合规大段解释文本正文只在本文件 §Certifications 收录一次;各页只留图标 URL+名称。
6. Download 区:文件链接清单逐字保留;对可解析文本文件(如 PDF 数据手册)按用户指令**尽力抓取文本内容**
   存于 downloads/;二进制固件只录 URL。

## 关键站点发现(2026-09-11 探测)

- 商品页:`/products/<id>.html`(系列级页面,含型号清单/规格表/特性/订购信息/下载区;单页单 chunk)。
- 分类页:`/c/81`~`/c/86`(Switch / Industrial Switch / PON / Wireless / Router / Firewall),
  每页仅列 ~10 个代表系列,**分页参数无效(疑似 JS 加载),完整枚举走站内搜索**。
- 站内搜索:`/search?keyword=<kw>&page=N` 为**全站**搜索(商品+案例+新闻+方案混合),服务端分页,
  是站点唯一可靠的全站枚举通道(字母扫描 a–z)。
- 新闻:`/news.html`(列表 "Load more" 为 JS)+ `/news/<id>.html`。
- 案例:`/case.html`(服务端分页 1..10)+ `/case/<id>.html`。
- 方案:`/solution-detail/<id>.html`;`/solution/<slug>` 直接访问 500(经搜索枚举详情页)。
- 静态页:`/about-us.html`、`/warranty-policy.html`、`/career.html`、`/become-our-partner.html`、
  `/contact-us.html`、`/weekly1`(sitemap 所列)。
- sitemap.xml 仅列 9 个顶级页,不含商品/案例/新闻,枚举价值低。
- 图片/资源域:`resource.fs.com`(`/boda/` 与 `/mall/`)及 `front-resource.fs.com`——收购后已并入 FS 基础设施。

## 进度(2026-09-11 全站内容镜像收官)

- [x] 站点结构探测(分类 81–86、URL 模式、枚举通道)
- [x] 全站 URL 枚举(字母扫描 + ID 段探测,见 urls/inventory.md)
- [x] 产品页整页镜像:482–590 共 **109 页**(details/<id>.md;477–481、591–600 为 404)
- [x] 客户案例镜像:**85 内容页**(85–168 + 597)+ 169–188 兜底空页占位 20 页(cases/<id>.md)
- [x] 新闻镜像:214–224 共 **11 页**(news/<id>.md;200–213、225+ 404)
- [x] 方案镜像:202–213 共 **12 页**(solutions/<id>.md;含探测新增 204/209/212)
- [x] FAQ:全部为 "No Data" 占位模板(6 个 ID 落盘标注)
- [x] 静态页+分类页:16 页(site/*.md;weekly1 404)
- [x] Excel 汇总:data/bdcom/excel/bdcom_mirror_summary.xlsx(总览+6 板块 sheet)
- [~] 下载资源:**受限如实记录** —— 产品页 Download 标签区为 JS 渲染,网页转写通道不可见;站内搜索 "datasheet" 无结果、无公开下载枚举入口,故 PDF 文本与固件 URL 本轮无法获取。若后续获得直接 URL,可补抓 PDF 文本存 downloads/。

> 全站内容页合计 **233 页全部镜像**(109 产品 + 85 案例 + 11 新闻 + 12 方案 + 16 静态/分类);
> 另 20 个 case 兜底空页与 6 个 faq No Data 页已占位标注。台账与逐批提交链见 git log 与 urls/inventory.md。

## Certifications(产品/公司页出现的认证,全文统一收录,2026-09-11 起)

(公司页 careers 出现:CE、CMMI5、FCC、ISO9001、ISO14001、CB、ISO45001。产品页认证随镜像补充。)
