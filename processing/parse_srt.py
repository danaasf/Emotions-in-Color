import re, csv, sys
from pathlib import Path

def parse_srt(path):
    text = Path(path).read_text(encoding='utf-8', errors='ignore')
    blocks = re.split(r'\n\s*\n', text.strip())
    out = []
    for b in blocks:
        lines = [l.strip() for l in b.splitlines() if l.strip()]
        if len(lines) >= 3:
            times = lines[1]
            content = " ".join(lines[2:])
            out.append((times, content))
    return out

def main(srt_path, csv_out):
    rows = []
    for i, (t, c) in enumerate(parse_srt(srt_path)):
        id_ = f"{Path(srt_path).stem}_{i:04d}"
        rows.append({"id": id_, "source":"movie", "title":Path(srt_path).stem, "time":t, "text":c})
    with open(csv_out,'a',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id","source","title","time","text"])
        if Path(csv_out).stat().st_size == 0:
            writer.writeheader()
        for r in rows:
            writer.writerow(r)

if __name__=='__main__':
    srt = sys.argv[1]
    out = sys.argv[2]
    main(srt,out)
