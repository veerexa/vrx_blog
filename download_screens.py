import urllib.request

urls = {
    "Rocket_Explorer.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzE0MWY0M2E2N2E2NjQ4NWI4ZDRjY2E3YTMwYjAxMDdiEgsSBxCrv5rT6RgYAZIBIwoKcHJvamVjdF9pZBIVQhMyNzcwODU0NTg5MTM2NTMyMzY3&filename=&opi=89354086",
    "Space_Companies.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2QxMDc2ZDhhOTlhYjRlMmZiNjU2Njg1ODIxMWU1YjhmEgsSBxCrv5rT6RgYAZIBIwoKcHJvamVjdF9pZBIVQhMyNzcwODU0NTg5MTM2NTMyMzY3&filename=&opi=89354086",
    "Rocket_Explorer_with_Comparison_Table.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzhhZWRlYTg0NTUwMjRkMzg5NDE0MmI2MGI5NWYxNTBkEgsSBxCrv5rT6RgYAZIBIwoKcHJvamVjdF9pZBIVQhMyNzcwODU0NTg5MTM2NTMyMzY3&filename=&opi=89354086",
    "Missions_Library.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzk4ZGU2ZDRjYTY2MzQyNzBiZmJhYWI2ZGM2ZmY4YmM1EgsSBxCrv5rT6RgYAZIBIwoKcHJvamVjdF9pZBIVQhMyNzcwODU0NTg5MTM2NTMyMzY3&filename=&opi=89354086",
    "Launch_Details.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2U5M2I5YzkyZmMxODRkYTNiM2ZhZmMyMDVjYWUzMzNmEgsSBxCrv5rT6RgYAZIBIwoKcHJvamVjdF9pZBIVQhMyNzcwODU0NTg5MTM2NTMyMzY3&filename=&opi=89354086"
}

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for name, url in urls.items():
    print(f"Downloading {name}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as response:
        with open(f"/home/kapil-dev-pal/Desktop/school_blog/{name}", "wb") as f:
            f.write(response.read())
print("Done!")
