import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update HTML onclicks
    content = content.replace('onclick="toggleProfile()"', 'onclick="toggleProfile(event)"')
    content = content.replace('onclick="toggleNotifications()"', 'onclick="toggleNotifications(event)"')

    # Update JS functions
    content = content.replace('function toggleProfile() {', 'function toggleProfile(event) {\n  if(event) event.stopPropagation();')
    content = content.replace('function toggleNotifications() {', 'function toggleNotifications(event) {\n  if(event) event.stopPropagation();')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Fixed dropdowns in all files.')
