#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble full-page mirror for one product: data/details/<sku>.md
Reads chunk parts data/details/.parts/<sku>.c<N>.md (fetched via platform channel),
prepends a metadata header from the deduped catalog rows, and removes the parts.
Run:  python3 tools/assemble_detail.py <sku>
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROD_DIR = os.path.join(ROOT, "data", "products")
DETAILS = os.path.join(ROOT, "data", "details")
PARTS = os.path.join(DETAILS, ".parts")

def load_row(sku):
    seen = set()
    for fp in sorted(glob.glob(os.path.join(PROD_DIR, "catalog_*.jsonl"))):
        for line in open(fp, encoding="utf-8"):
            line = line.strip()
            if not line: continue
            r = json.loads(line)
            if r.get("sku") in seen: continue
            seen.add(r["sku"])
            if str(r.get("sku")) == str(sku):
                return r
    return None

def main():
    sku = sys.argv[1]
    r = load_row(sku)
    parts = sorted(glob.glob(os.path.join(PARTS, f"{sku}.c*.md")),
                   key=lambda p: int(re.search(r"\.c(\d+)\.md$", p).group(1)))
    if not parts:
        print("no parts for", sku); sys.exit(1)
    head = []
    head.append(f"# {r.get('title') or sku}")
    head.append("")
    head.append(f"- 商品页: https://www.fs.com/products/{sku}.html")
    head.append(f"- SKU: {sku}")
    head.append(f"- 型号P/N: {r.get('pn') or ''}")
    head.append(f"- 分类: {r.get('cat') or ''}  |  {r.get('cat_url') or ''}")
    head.append(f"- 单价USD: {r.get('price') or r.get('price_raw') or ''}")
    head.append(f"- 销量: {r.get('sold_raw') or ''}  评论: {r.get('reviews') or ''}")
    head.append(f"- 主图: {r.get('img') or ''}")
    head.append(f"- 目录抓取日期: {r.get('ts') or ''}")
    head.append(f"- 整页镜像日期: 2026-09-02")
    head.append("")
    body = []
    for i, p in enumerate(parts):
        body.append(f"<!-- ===== 页面抓取片段 {i+1}/{len(parts)} ===== -->")
        body.append(open(p, encoding="utf-8").read().rstrip())
        body.append("")
    os.makedirs(DETAILS, exist_ok=True)
    out = os.path.join(DETAILS, f"{sku}.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(head) + "\n\n" + "\n".join(body))
    for p in parts:
        os.remove(p)
    print(f"wrote {out}  ({os.path.getsize(out)} bytes, {len(parts)} chunks)")

if __name__ == "__main__":
    main()
