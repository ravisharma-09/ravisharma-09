import json, subprocess
res = subprocess.check_output(['gh', 'api', 'users/ravisharma-09/repos?per_page=100'])
repos = json.loads(res.decode('utf-8'))
filtered = [r for r in repos if not r['fork'] and r['name'] != 'ravisharma-09']
sorted_repos = sorted(filtered, key=lambda x: (x['stargazers_count'], x['pushed_at']), reverse=True)
top4 = sorted_repos[:4]

for r in top4:
    desc = r.get('description') or ''
    lang = r.get('language') or 'Unknown'
    print(f"## 🔹 {r['name']}")
    print(f"{desc}")
    print(f"{lang}")
    print("")
