import json, os, subprocess, sys, time  # kullanım: python3 plan/push.py <kaç issue açılsın>

D = os.path.dirname(os.path.abspath(__file__))
REPO = "ulaskorpe/devops-sprint"
PROG = f"{D}/progress.json"
data = json.load(open(f"{D}/issues.json"))
prog = json.load(open(PROG)) if os.path.exists(PROG) else {"labels": [], "milestones": {}, "issues": {}}


def save():
    json.dump(prog, open(PROG, "w"), ensure_ascii=False, indent=1)


def gh(method, path, payload=None):
    cmd = ["gh", "api", "-X", method, path]
    if payload is not None:
        cmd += ["--input", "-"]
    r = subprocess.run(cmd, input=json.dumps(payload) if payload is not None else None,
                       capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


# labels
for lb in data["labels"]:
    if lb["name"] in prog["labels"]:
        continue
    rc, out, err = gh("POST", f"repos/{REPO}/labels", {"name": lb["name"], "color": lb["color"]})
    if rc != 0 and "already_exists" not in (out + err):
        print("LABEL FAIL", lb["name"], out[:300], err[:300]); sys.exit(1)
    prog["labels"].append(lb["name"]); save()
print("labels ok", len(prog["labels"]))

# milestones
for m in data["milestones"]:
    k = str(m["no"])
    if k in prog["milestones"]:
        continue
    rc, out, err = gh("POST", f"repos/{REPO}/milestones", {"title": m["title"], "description": m["description"]})
    if rc != 0:
        print("MILESTONE FAIL", m["title"], out[:300], err[:300]); sys.exit(1)
    prog["milestones"][k] = json.loads(out)["number"]; save()
print("milestones ok", len(prog["milestones"]))

# issues
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9
made = 0
for it in data["issues"]:
    key = f"{it['sprint']}-{it['n']}"
    if key in prog["issues"]:
        continue
    if made >= limit:
        break
    rc, out, err = gh("POST", f"repos/{REPO}/issues", {
        "title": it["title"], "body": it["body"], "labels": it["labels"],
        "milestone": prog["milestones"][str(it["sprint"])]})
    if rc != 0:
        print("ISSUE FAIL", key, out[:300], err[:300]); sys.exit(1)
    prog["issues"][key] = json.loads(out)["number"]; save()
    made += 1
    time.sleep(1.5)
print("issues done", len(prog["issues"]), "of", len(data["issues"]))
