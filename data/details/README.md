# data/details/ 镜像归档约定(2026-09-02)

`<sku>.md` = 交换机整机/线卡商品详情页的整页镜像,由 `tools/assemble_detail.py` 将
`data/details/.parts/<sku>.c<N>.md` 逐段拼接而成(每段为平台抓取通道返回原文)。

## 保真原则与压缩规则(为在可行轮次内完成 200+ 页而设)

页面原文(platform 转写)含大量**页内重复块**(同一图集出现 2-3 次、软件亮点每个条目
以 `[X](a) [X](b)` 成对重复、认证段落逐页重复、页脚表单区逐页重复)。镜像时:

1. **图集去重**: 同一图片 URL 全尺寸/180x180/主图 各保留一份(URL 全量不丢),重复块以
   `<!-- 图集重复块已去重 -->` 注明。
2. **成对链接归一**: `X [X](u1) [X](u2)` 保留为 `[X](u2)`(u2 为商品页/外链),`[X](https://www.fs.com/)` 站内占位重复删除。
3. **"Products:" 同系列清单**保留一份(含跳转链接与 alt 型号);重复清单删除并注明。
4. **认证合规标准段**(REACH / CE / FCC / KC / UL / VCCI / CB / RCM / UKCA 等大段解释文本)
   正文只在本文件收录一次;各商品页保留**本页实际出现的认证图标 URL + 名称清单**,
   并注明"标准合规全文见本文件 §Certifications"。
5. **页底交互区**(Sign in 提问/评价、Suggestion 表单、Add to Cart 底栏、Recently Viewed 等)
   逐页相同且无商品信息,统一以一行注明,不再逐页复录。
6. 视频时长行(如 `01:17`)、评分/图标字形等平台装饰符号尽量保留,无法编码处忽略。

> 规格表、描述、亮点、软件功能清单、链接、下载、资源、Q&A 计数等**商品特有正文一律逐字保留**。

## Certifications(标准合规全文,出现在多数产品页)

- 引导句: Fully certified to meet strict international safety and quality standards for
  the industry. Go to the [Compliance Center](https://www.fs.com/compliance-center-h0007.html)
  for specific certifications.

- REACH: REACH is a European Union regulation concerning the Registration, Evaluation,
  Authorization and Restriction of Chemicals. It came into force on 1st June 2007 and replaced
  a number of European Directives and Regulations with a single system. The regulation aims to
  protect human health and environmental safety, maintain and improve the competitiveness of the
  EU chemical industry, and develop innovative capabilities for non-toxic and harmless compounds
  to prevent market fragmentation, increase the transparency of the use of chemicals, promote
  non-animal experiments, and pursue sustainable social development. Please contact us to learn
  more. (contact: https://www.fs.com/company/quality_control.html)

- CE-ROHS/CE-EMF/CE-LVD: This product meets the applicable requirements of Directive (EU)
  2015/863 of RoHS. It restricts the use of 10 hazardous materials in the manufacture of various
  types of electronic and electrical equipment: lead, mercury, cadmium, hexavalent chromium,
  polybrominated biphenyls, polybrominated diphenyl ethers, and four different phthalates.
  Please [contact us](https://www.fs.com/contact_us.html) to learn more.

- FCC: This product fully accords with the FCC, which aims to manage the radio wave and magnetic
  fields more reasonably. Please [contact us](https://www.fs.com/contact_us.html) to learn more.

- KC: KC certification, or Korea Certification, is a product certification which ensures the
  conformity of products to Korean safety standards - called K Standards. The KC Certification
  (KC Mark Korea Certification) focuses on prevention and reduction of risks regarding safety,
  health or impact on the environment. Please [contact us](https://www.fs.com/contact_us.html)
  to learn more.

- UL Listed: This product was produced under the requirements of UL, which is a global safety
  consulting and certification. Please [contact us](https://www.fs.com/contact_us.html) to learn
  more.

- VCCI: The VCCI (Voluntary Control Council for Interference) mark is a mandatory certification
  for multimedia equipment (MME) in Japan, and it is specifically for IT equipment,
  electromagnetic launch control, which is product EMC certification. This product fully accords
  with the Japan VCCI certification. Please [contact us](https://www.fs.com/contact_us.html) to
  learn more.

- CB: CB is an international system operated by IECEE. This product is based on IEC standards for
  testing the safety performance of electrical products. Please
  [contact us](https://www.fs.com/contact_us.html) to learn more.

- ETL: This product fully accords with the ETL to indicate conformity with relevant industry
  standards for any electrical or mechanical product. Please
  [contact us](https://www.fs.com/contact_us.html) to learn more.

- RCM: This product is RCM compliant, which indicates compliance with electrical safety, EMC,
  EME and telecommunications legislative requirements. Please
  [contact us](https://www.fs.com/contact_us.html) to learn more.

- UKCA: This product fully accords with UKCA (UK Conformity Assessed) certificate, which
  signifies that it meets all relevant quality standards as well as health and safety
  requirements. Please [contact us](https://www.fs.com/contact_us.html) to learn more.

## 页底交互区(逐页相同,不再复录)

- 标签行: Specifications / Connectivity Solutions / Features / Videos / Q&A / Reviews /
  Resources / Case Study;Questions & Answers: "Ask a question" 与 Reviews "Write a review"
  均需 Sign in(redirect=%2Fproducts%2F<sku>.html);Resources 链接
  `https://www.fs.com/products_support/search.html?keyword=<sku>`。
- Suggestion 反馈表单: "Thanks for browsing this product... put your suggestion..." 含
  Main Picture / Item Spotlights / Description / Network Connectivity / Product Highlights /
  Videos / Questions & Answers / Customer Reviews / Resources / Recently Viewed 复选框、
  Email Address + Submit、"You have submitted successfully!" 提示文案。
