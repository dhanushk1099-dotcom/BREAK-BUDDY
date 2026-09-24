import glob

old_logo_url = "https://lh3.googleusercontent.com/aida/AEtjO1XwQqYX6QmHHEwSKr4M5KW_1Yo1JCwTSqyHIi9-xyi6-Z873HfqOyovcEX_gyzMGQX-DFD0RUDQofgqalcvRR9Nm8MkiE9BmhADqezkRD8ZCkk8QUZsrx7g7NHpZwEudRnkvFJ-_LjOGeZBAhg7_7HqwGpRLEVDkUb4Q5FG8zw5y3-XyLkxLoLuXazDkv3kgc09x__Gvqv1pJlxzQefnD3_RrVJf64WzMfWK0GzbVtTcAXlU6DwvmrRpiWP"
new_logo_url = "logo.svg"

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_logo_url in content:
        content = content.replace(old_logo_url, new_logo_url)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed logo in {file}")
