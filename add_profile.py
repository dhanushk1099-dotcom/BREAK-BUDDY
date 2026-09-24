import glob
import re

html_files = glob.glob("*.html")

profile_html = '''
<div class="relative flex items-center">
<button id="profileBtn" class="flex items-center gap-space-xs p-space-xs rounded-full hover:bg-surface-container transition-colors" type="button" onclick="toggleProfile()">
<img alt="Profile" class="w-8 h-8 rounded-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAqzpEcdJtRhcou9haPrkOEA_36oyjM0Xzl2P-TxjNaYSCFUFCXH_e1Zp73mEnJy4_MuTAZ6D1NijOkuNGk5KevsP-sRVtI_xzFUJ5bRWvVKNoEdi8sLtzCxu4W-ioe0MaCP4979uCSyDjhHCNZWID9pIxyW0b6axa3NKdRDmy9HEcy0vuLlGXvkT54gzfq1ITGFIMQNl_AMDf-3B4xz1KZIPvHqT59F7BdBGCXRI8B4NuvkiHcoT0Orw"/>
<span class="material-symbols-outlined text-on-surface-variant text-[18px]">expand_more</span>
</button>
<div id="profileDropdown" class="hidden absolute right-0 top-full mt-2 w-56 bg-surface-container-lowest rounded-2xl shadow-xl border border-surface-container-highest overflow-hidden z-50">
  <div class="p-space-md border-b border-surface-container-highest">
    <p class="font-headline-sm font-bold truncate">Dhanush</p>
    <p class="font-body-sm text-on-surface-variant truncate">Level 7 Wellness Student</p>
  </div>
  <div class="flex flex-col py-2">
    <a href="settings.html" class="flex items-center gap-3 px-space-md py-2 hover:bg-surface-container-low transition-colors text-on-surface font-label-lg">
      <span class="material-symbols-outlined text-[20px]">manage_accounts</span>
      My Profile
    </a>
    <a href="settings.html" class="flex items-center gap-3 px-space-md py-2 hover:bg-surface-container-low transition-colors text-on-surface font-label-lg">
      <span class="material-symbols-outlined text-[20px]">tune</span>
      Preferences
    </a>
    <div class="h-px bg-surface-container-highest my-2"></div>
    <a href="#" class="flex items-center gap-3 px-space-md py-2 hover:bg-surface-container-low transition-colors text-error font-label-lg">
      <span class="material-symbols-outlined text-[20px]">logout</span>
      Log Out
    </a>
  </div>
</div>
</div>
'''

script_addition = '''
function toggleProfile() {
  const dropdown = document.getElementById('profileDropdown');
  if (dropdown.classList.contains('hidden')) {
    dropdown.classList.remove('hidden');
  } else {
    dropdown.classList.add('hidden');
  }
}

document.addEventListener('click', function(event) {
  const profileDropdown = document.getElementById('profileDropdown');
  const profileBtn = document.getElementById('profileBtn');
  if (profileDropdown && !profileDropdown.classList.contains('hidden') && !profileDropdown.contains(event.target) && !profileBtn.contains(event.target)) {
    profileDropdown.classList.add('hidden');
  }
});
</script>
'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace the existing profile button wrapper
    old_btn_pattern = re.compile(r'<div class="flex items-center gap-space-sm">\s*<button class="flex items-center gap-space-xs p-space-xs rounded-full hover:bg-surface-container transition-colors" type="button">\s*<img alt="Profile"[^>]+>\s*<span class="material-symbols-outlined[^>]+>expand_more</span>\s*</button>\s*</div>')
    
    if old_btn_pattern.search(content):
        content = old_btn_pattern.sub(profile_html, content, count=1)
        
        # 2. Add the script addition right before the closing script tag of the notification script
        if 'function toggleProfile' not in content:
            content = content.replace('</script>\n</body>', script_addition + '\n</body>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added profile dropdown to {file}")
    else:
        print(f"Could not find profile button in {file}")

print("Profile dropdowns processed.")
