# BDCOM 英文主站 分类地图 / Category Map(2026-09-11 探测)

> 站点: https://bdcomnetworks.com/ · 通道:平台网页转写 · 状态:✅完成 ⏳进行中 ⬜未开始

## 导航结构(顶级)

- Products: Switch · Industrial Switch · PON · Wireless · Router · Firewall(共 6 类)
- Solutions: Service Provider · Education · Hospitality · Healthcare · Finance · Government
- Support: Download Search(页面入口未定位,枚举走站内搜索)
- Company: About · News · Cases · Career · Warranty Policy · Become Our Partner · Contact Us
- 语言站:EN(本站)/ 中文 bdcom.com.cn / FR /fr/ / ES /es/ / RU /ru/(本轮仅 EN)

## 产品分类(✅ 已定位,数字 ID 空间 81–86)

| 分类 | URL | 收录方式 | 状态 |
|---|---|---|---|
| Switch | /c/81 | 页内 10 代表系列;全量走搜索枚举 | ✅ 已探测 |
| Industrial Switch | /c/82 | 同上 | ✅ 已探测 |
| PON | /c/83 | 同上 | ✅ 已探测 |
| Wireless | /c/84 | 同上 | ✅ 已探测 |
| Router | /c/85 | 同上(5 项) | ✅ 已探测 |
| Firewall | /c/86 | 同上(1 项:F5100-40MH) | ✅ 已探测 |

> 注:分类页分页参数(page/p/pageno/pageNo)实测无效,均返回同一页(JS "Load more")。
> 完整产品枚举 = 站内搜索字母扫描(sweeps),去重后按 /products/<id>.html 归档。

## URL 模式(实测)

| 板块 | 模式 | 分片 | 备注 |
|---|---|---|---|
| 首页 | / | 1 chunk | hero 卡 Learn more 均指回根(未转录目标) |
| 产品页 | /products/<id>.html | 1 chunk | 系列级:型号+规格表+Features+Ordering+Download |
| 分类页 | /c/<id> | 1 chunk | 仅 81–86 有效;每页 ≤10 项 |
| 搜索 | /search?keyword=<kw>&page=N | 1 chunk | 服务端分页;全站混排;空 keyword 无结果 |
| 新闻列表/详情 | /news.html · /news/<id>.html | — | 列表 Load more 为 JS |
| 案例列表/详情 | /case.html · /case/<id>.html | — | 列表服务端分页 1..10 |
| 方案详情 | /solution-detail/<id>.html | 1 chunk | /solution/<slug> 直接访问 500 |
| 静态页 | /about-us.html 等 | 1–2 chunks | sitemap.xml 列 9 页 |
| 站图 | /sitemap.xml | — | 仅顶级页,不覆盖商品 |
| robots.txt | — | — | `Disallow: /`(用户确认继续,见 README) |

## 页面清单与进度

> 全站 URL 台账见 `data/bdcom/urls/inventory.md`(随字母扫描追加)。
> 已确认可抓页面(截至 2026-09-11 首轮探测):
> - 静态: / 、about-us、news.html、case.html、warranty-policy、career、weekly1(待补 become-our-partner、contact-us)
> - 分类: /c/81…/c/86
> - 产品页样例: 575(S9600)、502、501、512、545、509、553、530、510、511、508、507、506、505、504、503、586、580、579、573、570、577、535、571、523、572、536、496、557、524、565、567、566、568、569、563、526、531、527、525、532、574、533、529、528、564、555、556、562、578、587、588、486、489、488、487、484、483、482、500、548
