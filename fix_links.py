import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update navigation links
    content = re.sub(r'data-path="([^"]+)"\s+href="#"', r'data-path="\1" href="\1.html"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Create index.html to redirect to dashboard.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write('<meta http-equiv="refresh" content="0; url=dashboard.html" />')

print("Links updated and index.html created.")
