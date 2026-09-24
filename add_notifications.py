import glob
import re

html_files = glob.glob("*.html")

notification_html = '''
<button aria-label="Notifications" class="relative p-space-xs rounded-full text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors" type="button" onclick="toggleNotifications()">
<span class="material-symbols-outlined text-[24px]">notifications</span>
<span id="notifCount" class="absolute top-0 right-0 flex items-center justify-center min-w-[16px] h-4 px-1 rounded-full bg-error text-on-error font-badge-counter text-badge-counter leading-none">3</span>
</button>
<div id="notificationDropdown" class="hidden absolute right-0 top-full mt-2 w-80 bg-surface-container-lowest rounded-2xl shadow-xl border border-surface-container-highest overflow-hidden z-50">
  <div class="p-space-md border-b border-surface-container-highest flex items-center justify-between">
    <span class="font-headline-sm font-bold">Notifications</span>
    <button class="text-primary font-label-md hover:underline" onclick="markAllRead()">Mark all as read</button>
  </div>
  <div class="flex flex-col max-h-80 overflow-y-auto">
    <div class="p-space-md border-b border-surface-container-highest hover:bg-surface-container-low transition-colors cursor-pointer bg-surface-container-lowest">
      <div class="flex items-center justify-between mb-1">
        <p class="font-label-lg font-bold flex items-center gap-1"><span class="material-symbols-outlined text-primary text-[18px]">self_improvement</span> Time for a break!</p>
        <span class="w-2 h-2 rounded-full bg-primary"></span>
      </div>
      <p class="font-body-sm text-on-surface-variant">You've been studying for 50 minutes. Stretch your legs.</p>
    </div>
    <div class="p-space-md border-b border-surface-container-highest hover:bg-surface-container-low transition-colors cursor-pointer bg-surface-container-lowest">
      <div class="flex items-center justify-between mb-1">
        <p class="font-label-lg font-bold flex items-center gap-1"><span class="material-symbols-outlined text-secondary text-[18px]">water_drop</span> Hydration Reminder</p>
        <span class="w-2 h-2 rounded-full bg-primary"></span>
      </div>
      <p class="font-body-sm text-on-surface-variant">Don't forget to log your water intake today.</p>
    </div>
    <div class="p-space-md hover:bg-surface-container-low transition-colors cursor-pointer bg-surface-container-lowest">
      <div class="flex items-center justify-between mb-1">
        <p class="font-label-lg font-bold flex items-center gap-1"><span class="material-symbols-outlined text-tertiary text-[18px]">emoji_events</span> New Badge Unlocked</p>
        <span class="w-2 h-2 rounded-full bg-primary"></span>
      </div>
      <p class="font-body-sm text-on-surface-variant">You earned the "7-Day Streak" badge!</p>
    </div>
  </div>
</div>
'''

script_html = '''
<script>
function toggleNotifications() {
  const dropdown = document.getElementById('notificationDropdown');
  if (dropdown.classList.contains('hidden')) {
    dropdown.classList.remove('hidden');
  } else {
    dropdown.classList.add('hidden');
  }
}

function markAllRead() {
  document.getElementById('notifCount').style.display = 'none';
  const dots = document.querySelectorAll('#notificationDropdown .w-2.h-2.bg-primary');
  dots.forEach(dot => dot.style.display = 'none');
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
  const dropdown = document.getElementById('notificationDropdown');
  const btn = document.querySelector('button[aria-label="Notifications"]');
  if (dropdown && !dropdown.classList.contains('hidden') && !dropdown.contains(event.target) && !btn.contains(event.target)) {
    dropdown.classList.add('hidden');
  }
});
</script>
</body>
'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace the existing notification button
    old_btn_pattern = re.compile(r'<button aria-label="Notifications"[^>]*>[\s\S]*?</button>')
    content = old_btn_pattern.sub(notification_html, content, count=1)
    
    # 2. Add the script before </body> if not already there
    if 'function toggleNotifications' not in content:
        content = content.replace('</body>', script_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Notifications added to all files.")
