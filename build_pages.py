import re

# Read template
with open('dashboard.html', 'r', encoding='utf-8') as f:
    template = f.read()

pages = {
    'challenges': '''
<div class="flex flex-col gap-space-xs px-space-lg pt-space-xl">
  <div class="inline-flex items-center gap-space-xs px-space-sm py-0.5 rounded-full bg-tertiary-fixed text-on-tertiary-fixed w-fit font-label-md text-label-md">
    <span class="material-symbols-outlined text-[16px]">flag</span>
    <span>Weekly Quests</span>
  </div>
  <h1 class="font-display-hero text-display-hero text-on-surface tracking-tight">Challenges</h1>
  <p class="font-body-lg text-body-lg text-on-surface-variant">Complete tasks to earn XP and level up your wellness journey.</p>
</div>

<div class="px-space-lg py-space-lg grid grid-cols-1 lg:grid-cols-3 gap-space-lg">
  <div class="lg:col-span-2 relative overflow-hidden bg-gradient-to-br from-primary to-tertiary text-on-primary rounded-3xl p-space-lg shadow-xl group">
    <div class="absolute -right-16 -top-16 w-64 h-64 bg-white/10 rounded-full blur-3xl pointer-events-none group-hover:bg-white/20 transition-all duration-700"></div>
    <div class="flex flex-col gap-space-sm relative z-10">
      <span class="font-badge-counter text-badge-counter uppercase tracking-wider text-primary-fixed-dim flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">star</span> Major Quest</span>
      <h2 class="font-headline-lg text-headline-lg font-bold">The Perfect Posture Week</h2>
      <p class="font-body-md text-body-md text-primary-fixed max-w-md">Complete at least one stretch session every day for 7 consecutive days to earn the Golden Spine badge.</p>
      
      <div class="mt-space-md flex flex-col gap-space-xs">
        <div class="flex items-center justify-between font-label-md text-label-md">
          <span>4 / 7 Days Completed</span>
          <span class="font-bold text-secondary-fixed bg-black/20 px-2 py-1 rounded-full flex items-center gap-1"><span class="material-symbols-outlined text-[16px]">bolt</span> +500 XP Reward</span>
        </div>
        <div class="w-full h-3 bg-black/20 rounded-full overflow-hidden">
          <div class="h-full bg-secondary-fixed rounded-full w-[57%]"></div>
        </div>
      </div>
    </div>
  </div>

  <div class="flex flex-col gap-space-md">
    <h3 class="font-headline-sm text-headline-sm text-on-surface font-bold flex items-center gap-2"><span class="material-symbols-outlined text-primary text-[20px]">today</span> Daily Tasks</h3>
    
    <div class="bg-surface-container-lowest rounded-2xl p-space-md flex items-center justify-between shadow-sm hover:shadow-md transition-shadow cursor-pointer border-l-4 border-primary">
      <div class="flex items-center gap-space-sm">
        <div class="w-12 h-12 rounded-full bg-primary-fixed text-primary flex items-center justify-center">
          <span class="material-symbols-outlined">water_drop</span>
        </div>
        <div class="flex flex-col">
          <span class="font-label-lg text-label-lg font-bold">Hydration Hero</span>
          <span class="font-body-sm text-body-sm text-on-surface-variant">Log 3 waters before noon</span>
        </div>
      </div>
      <button class="px-space-sm py-1 rounded-full bg-secondary text-on-secondary font-label-md font-bold shadow-sm hover:bg-secondary-container transition-colors">+50 XP</button>
    </div>
    
    <div class="bg-surface-container-lowest rounded-2xl p-space-md flex items-center justify-between shadow-sm border-l-4 border-transparent opacity-60">
      <div class="flex items-center gap-space-sm">
        <div class="w-12 h-12 rounded-full bg-surface-container-high text-on-surface flex items-center justify-center">
          <span class="material-symbols-outlined">check_circle</span>
        </div>
        <div class="flex flex-col">
          <span class="font-label-lg text-label-lg font-bold line-through">Morning Stretch</span>
          <span class="font-body-sm text-body-sm text-on-surface-variant">Done!</span>
        </div>
      </div>
      <span class="font-label-md text-tertiary font-bold px-space-sm py-1 rounded-full bg-tertiary-fixed text-on-tertiary-fixed">Claimed</span>
    </div>
  </div>
</div>
    ''',
    
    'achievements': '''
<div class="flex flex-col gap-space-xs px-space-lg pt-space-xl">
  <div class="inline-flex items-center gap-space-xs px-space-sm py-0.5 rounded-full bg-secondary-fixed text-on-secondary-fixed w-fit font-label-md text-label-md">
    <span class="material-symbols-outlined text-[16px]">emoji_events</span>
    <span>Trophy Case</span>
  </div>
  <h1 class="font-display-hero text-display-hero text-on-surface tracking-tight">Achievements</h1>
  <p class="font-body-lg text-body-lg text-on-surface-variant">Showcase your milestones and wellness badges.</p>
</div>

<div class="px-space-lg py-space-lg flex flex-col gap-space-xl">
  <div class="bg-gradient-to-r from-surface-container-lowest to-surface-container-low rounded-3xl p-space-lg shadow-sm flex items-center justify-between border border-surface-container-highest">
    <div class="flex items-center gap-space-md">
      <div class="w-20 h-20 rounded-full bg-tertiary text-on-tertiary flex items-center justify-center text-4xl shadow-md border-4 border-surface-container-lowest">
        7
      </div>
      <div class="flex flex-col">
        <span class="font-headline-md text-headline-md font-bold text-on-surface flex items-center gap-2">Level 7: Wellness Scholar <span class="material-symbols-outlined text-tertiary">verified</span></span>
        <span class="font-body-md text-body-md text-on-surface-variant">1,240 / 1,500 XP to Level 8</span>
      </div>
    </div>
  </div>

  <div>
    <h3 class="font-headline-sm text-headline-sm text-on-surface font-bold mb-space-md flex items-center gap-2"><span class="material-symbols-outlined text-secondary">workspace_premium</span> Unlocked Badges</h3>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-space-md">
      <div class="bg-surface-container-lowest rounded-2xl p-space-lg flex flex-col items-center text-center shadow-sm hover:shadow-md transition-all duration-300 cursor-pointer group">
        <div class="w-24 h-24 rounded-full bg-gradient-to-br from-secondary to-primary flex items-center justify-center text-on-primary shadow-lg mb-space-sm transform group-hover:scale-110 transition-transform duration-300">
          <span class="material-symbols-outlined text-[48px]">local_fire_department</span>
        </div>
        <span class="font-label-lg text-label-lg font-bold text-on-surface">7-Day Streak</span>
        <span class="font-badge-counter text-badge-counter text-secondary uppercase mt-1 bg-secondary-fixed/50 px-2 py-0.5 rounded-full">Rare</span>
      </div>
      
      <div class="bg-surface-container-lowest rounded-2xl p-space-lg flex flex-col items-center text-center shadow-sm hover:shadow-md transition-all duration-300 cursor-pointer group">
        <div class="w-24 h-24 rounded-full bg-gradient-to-br from-tertiary to-primary-container flex items-center justify-center text-on-primary shadow-lg mb-space-sm transform group-hover:scale-110 transition-transform duration-300">
          <span class="material-symbols-outlined text-[48px]">water_drop</span>
        </div>
        <span class="font-label-lg text-label-lg font-bold text-on-surface">Hydration Pro</span>
        <span class="font-badge-counter text-badge-counter text-tertiary uppercase mt-1 bg-tertiary-fixed/50 px-2 py-0.5 rounded-full">Epic</span>
      </div>
      
      <div class="bg-surface-container rounded-2xl p-space-lg flex flex-col items-center text-center opacity-60 grayscale cursor-not-allowed">
        <div class="w-24 h-24 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface-variant shadow-inner mb-space-sm">
          <span class="material-symbols-outlined text-[48px]">lock</span>
        </div>
        <span class="font-label-lg text-label-lg font-bold">Zen Master</span>
        <span class="font-badge-counter text-badge-counter text-on-surface-variant uppercase mt-1">Locked</span>
      </div>
      
      <div class="bg-surface-container rounded-2xl p-space-lg flex flex-col items-center text-center opacity-60 grayscale cursor-not-allowed">
        <div class="w-24 h-24 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface-variant shadow-inner mb-space-sm">
          <span class="material-symbols-outlined text-[48px]">lock</span>
        </div>
        <span class="font-label-lg text-label-lg font-bold">Marathon Reader</span>
        <span class="font-badge-counter text-badge-counter text-on-surface-variant uppercase mt-1">Locked</span>
      </div>
    </div>
  </div>
</div>
    ''',
    
    'progress': '''
<div class="flex flex-col gap-space-xs px-space-lg pt-space-xl">
  <div class="inline-flex items-center gap-space-xs px-space-sm py-0.5 rounded-full bg-primary-fixed text-primary w-fit font-label-md text-label-md">
    <span class="material-symbols-outlined text-[16px]">bar_chart</span>
    <span>Analytics</span>
  </div>
  <h1 class="font-display-hero text-display-hero text-on-surface tracking-tight">Progress</h1>
  <p class="font-body-lg text-body-lg text-on-surface-variant">Visualize your wellness habits over time.</p>
</div>

<div class="px-space-lg py-space-lg grid grid-cols-1 lg:grid-cols-3 gap-space-lg">
  <div class="flex flex-col gap-space-md">
    <div class="bg-surface-container-lowest rounded-2xl p-space-lg flex items-center gap-space-md shadow-sm border-l-4 border-primary hover:shadow-md transition-shadow">
      <div class="w-14 h-14 rounded-2xl bg-primary-fixed text-primary flex items-center justify-center">
        <span class="material-symbols-outlined text-[28px]">trending_up</span>
      </div>
      <div class="flex flex-col">
        <span class="font-headline-md text-headline-md font-bold text-on-surface">42h</span>
        <span class="font-body-sm text-body-sm text-on-surface-variant">Total Focused Study Time</span>
      </div>
    </div>
    
    <div class="bg-surface-container-lowest rounded-2xl p-space-lg flex items-center gap-space-md shadow-sm border-l-4 border-secondary hover:shadow-md transition-shadow">
      <div class="w-14 h-14 rounded-2xl bg-secondary-fixed text-secondary flex items-center justify-center">
        <span class="material-symbols-outlined text-[28px]">water_drop</span>
      </div>
      <div class="flex flex-col">
        <span class="font-headline-md text-headline-md font-bold text-on-surface">1.8 L</span>
        <span class="font-body-sm text-body-sm text-on-surface-variant">Daily Avg. Hydration</span>
      </div>
    </div>
    
    <div class="bg-surface-container-lowest rounded-2xl p-space-lg flex items-center gap-space-md shadow-sm border-l-4 border-tertiary hover:shadow-md transition-shadow">
      <div class="w-14 h-14 rounded-2xl bg-tertiary-fixed text-tertiary flex items-center justify-center">
        <span class="material-symbols-outlined text-[28px]">accessibility_new</span>
      </div>
      <div class="flex flex-col">
        <span class="font-headline-md text-headline-md font-bold text-on-surface">32</span>
        <span class="font-body-sm text-body-sm text-on-surface-variant">Total Stretch Sessions</span>
      </div>
    </div>
  </div>

  <div class="lg:col-span-2 bg-surface-container-lowest rounded-3xl p-space-lg shadow-sm flex flex-col gap-space-md">
    <div class="flex items-center justify-between">
      <h3 class="font-headline-sm text-headline-sm font-bold text-on-surface flex items-center gap-2"><span class="material-symbols-outlined text-primary">insights</span> Weekly Activity Score</h3>
      <select class="bg-surface-container text-on-surface font-label-md rounded-lg px-2 py-1 border-none focus:ring-0">
        <option>This Week</option>
        <option>Last Week</option>
      </select>
    </div>
    
    <div class="flex items-end gap-3 h-64 w-full border-b border-surface-container-high pb-2 mt-space-md pt-space-lg">
      <div class="flex-1 flex flex-col items-center gap-2 group cursor-pointer">
        <div class="w-full max-w-[48px] bg-primary rounded-t-xl h-[40%] group-hover:opacity-80 transition-opacity relative"><span class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-inverse-surface text-inverse-on-surface font-badge-counter px-2 py-1 rounded">40%</span></div>
        <span class="font-label-md text-on-surface-variant">Mon</span>
      </div>
      <div class="flex-1 flex flex-col items-center gap-2 group cursor-pointer">
        <div class="w-full max-w-[48px] bg-primary rounded-t-xl h-[60%] group-hover:opacity-80 transition-opacity relative"><span class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-inverse-surface text-inverse-on-surface font-badge-counter px-2 py-1 rounded">60%</span></div>
        <span class="font-label-md text-on-surface-variant">Tue</span>
      </div>
      <div class="flex-1 flex flex-col items-center gap-2 group cursor-pointer">
        <div class="w-full max-w-[48px] bg-primary rounded-t-xl h-[80%] group-hover:opacity-80 transition-opacity relative"><span class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-inverse-surface text-inverse-on-surface font-badge-counter px-2 py-1 rounded">80%</span></div>
        <span class="font-label-md text-on-surface-variant">Wed</span>
      </div>
      <div class="flex-1 flex flex-col items-center gap-2 group cursor-pointer">
        <div class="w-full max-w-[48px] bg-gradient-to-t from-tertiary to-primary rounded-t-xl h-[100%] shadow-[0_0_15px_rgba(107,56,212,0.4)] relative"><span class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-inverse-surface text-inverse-on-surface font-badge-counter px-2 py-1 rounded">100%</span></div>
        <span class="font-label-md text-tertiary font-bold">Thu</span>
      </div>
      <div class="flex-1 flex flex-col items-center gap-2 group cursor-pointer">
        <div class="w-full max-w-[48px] bg-primary rounded-t-xl h-[50%] group-hover:opacity-80 transition-opacity relative"><span class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-inverse-surface text-inverse-on-surface font-badge-counter px-2 py-1 rounded">50%</span></div>
        <span class="font-label-md text-on-surface-variant">Fri</span>
      </div>
      <div class="flex-1 flex flex-col items-center gap-2 group cursor-pointer">
        <div class="w-full max-w-[48px] bg-surface-container-highest rounded-t-xl h-[20%] group-hover:bg-outline-variant transition-colors relative"><span class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-inverse-surface text-inverse-on-surface font-badge-counter px-2 py-1 rounded">20%</span></div>
        <span class="font-label-md text-on-surface-variant">Sat</span>
      </div>
      <div class="flex-1 flex flex-col items-center gap-2 group cursor-pointer">
        <div class="w-full max-w-[48px] bg-surface-container-highest rounded-t-xl h-[30%] group-hover:bg-outline-variant transition-colors relative"><span class="absolute -top-8 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity bg-inverse-surface text-inverse-on-surface font-badge-counter px-2 py-1 rounded">30%</span></div>
        <span class="font-label-md text-on-surface-variant">Sun</span>
      </div>
    </div>
  </div>
</div>
    ''',
    
    'settings': '''
<div class="flex flex-col gap-space-xs px-space-lg pt-space-xl">
  <div class="inline-flex items-center gap-space-xs px-space-sm py-0.5 rounded-full bg-surface-container-high text-on-surface font-label-md text-label-md w-fit">
    <span class="material-symbols-outlined text-[16px]">tune</span>
    <span>Preferences</span>
  </div>
  <h1 class="font-display-hero text-display-hero text-on-surface tracking-tight">Settings</h1>
  <p class="font-body-lg text-body-lg text-on-surface-variant">Manage your account and customize your experience.</p>
</div>

<div class="px-space-lg py-space-lg grid grid-cols-1 lg:grid-cols-12 gap-space-lg">
  <div class="lg:col-span-4 bg-surface-container-lowest rounded-3xl p-space-lg shadow-sm flex flex-col items-center text-center h-fit border border-surface-container-highest">
    <div class="relative mb-space-md group cursor-pointer">
      <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuAqzpEcdJtRhcou9haPrkOEA_36oyjM0Xzl2P-TxjNaYSCFUFCXH_e1Zp73mEnJy4_MuTAZ6D1NijOkuNGk5KevsP-sRVtI_xzFUJ5bRWvVKNoEdi8sLtzCxu4W-ioe0MaCP4979uCSyDjhHCNZWID9pIxyW0b6axa3NKdRDmy9HEcy0vuLlGXvkT54gzfq1ITGFIMQNl_AMDf-3B4xz1KZIPvHqT59F7BdBGCXRI8B4NuvkiHcoT0Orw" class="w-32 h-32 rounded-full object-cover shadow-md group-hover:opacity-50 transition-opacity" alt="Profile Picture"/>
      <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
        <span class="material-symbols-outlined text-white text-[32px] drop-shadow-md">edit</span>
      </div>
    </div>
    <h3 class="font-headline-md text-headline-md font-bold text-on-surface">Dhanush</h3>
    <span class="font-body-sm text-body-sm text-on-surface-variant mb-space-lg bg-surface-container-low px-3 py-1 rounded-full mt-2">Level 7 Wellness Student</span>
    
    <button class="w-full py-2 px-4 rounded-full border border-outline-variant text-on-surface font-label-md font-bold hover:bg-surface-container transition-colors flex items-center justify-center gap-2">
      <span class="material-symbols-outlined text-[18px]">manage_accounts</span>
      Manage Account
    </button>
  </div>

  <div class="lg:col-span-8 flex flex-col gap-space-md">
    <div class="bg-surface-container-lowest rounded-3xl p-space-lg shadow-sm flex flex-col gap-space-md">
      <h3 class="font-headline-sm text-headline-sm font-bold text-on-surface border-b border-surface-container-high pb-3 flex items-center gap-2"><span class="material-symbols-outlined text-primary">notifications</span> Notifications</h3>
      
      <div class="flex items-center justify-between py-2">
        <div class="flex flex-col">
          <span class="font-label-lg font-bold text-on-surface">Smart Nudges</span>
          <span class="font-body-sm text-on-surface-variant">Receive gentle reminders based on your study habits.</span>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" checked class="sr-only peer">
          <div class="w-11 h-6 bg-surface-container-highest peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-surface-container-lowest after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-surface-container-lowest after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
        </label>
      </div>

      <div class="flex items-center justify-between py-2">
        <div class="flex flex-col">
          <span class="font-label-lg font-bold text-on-surface">Audio Chimes</span>
          <span class="font-body-sm text-on-surface-variant">Play a subtle sound when a timer ends.</span>
        </div>
        <label class="relative inline-flex items-center cursor-pointer">
          <input type="checkbox" checked class="sr-only peer">
          <div class="w-11 h-6 bg-surface-container-highest peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-surface-container-lowest after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-surface-container-lowest after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
        </label>
      </div>
    </div>

    <div class="bg-surface-container-lowest rounded-3xl p-space-lg shadow-sm flex flex-col gap-space-md">
      <h3 class="font-headline-sm text-headline-sm font-bold text-on-surface border-b border-surface-container-high pb-3 flex items-center gap-2"><span class="material-symbols-outlined text-secondary">room_preferences</span> Preferences</h3>
      
      <div class="flex items-center justify-between py-2">
        <div class="flex flex-col">
          <span class="font-label-lg font-bold text-on-surface">Daily Hydration Goal</span>
          <span class="font-body-sm text-on-surface-variant">Target amount of water per day.</span>
        </div>
        <select class="bg-surface-container border-none text-on-surface font-label-md rounded-lg py-2 pl-3 pr-8 focus:ring-2 focus:ring-primary outline-none">
          <option>1.5 Liters (6 glasses)</option>
          <option selected>2.0 Liters (8 glasses)</option>
          <option>2.5 Liters (10 glasses)</option>
        </select>
      </div>
      
      <div class="flex items-center justify-between py-2">
        <div class="flex flex-col">
          <span class="font-label-lg font-bold text-on-surface">Default Focus Interval</span>
          <span class="font-body-sm text-on-surface-variant">Time before reminding to rest eyes.</span>
        </div>
        <select class="bg-surface-container border-none text-on-surface font-label-md rounded-lg py-2 pl-3 pr-8 focus:ring-2 focus:ring-primary outline-none">
          <option>15 Minutes</option>
          <option selected>20 Minutes</option>
          <option>30 Minutes</option>
          <option>60 Minutes</option>
        </select>
      </div>
    </div>
  </div>
</div>
    '''
}

for path, content in pages.items():
    main_start_match = re.search(r'<main[^>]*>', template)
    if not main_start_match:
        continue
    
    main_start_idx = main_start_match.end()
    main_end_idx = template.rfind('</main>')
    
    nav_content = template
    nav_content = nav_content.replace('aria-current="page" class="flex items-center gap-space-sm px-space-md py-space-sm transition-colors bg-primary text-on-primary font-label-lg rounded-xl shadow-[0_2px_6px_-1px_rgba(0,88,190,0.3)]" data-path="dashboard"', 
                                      'class="flex items-center gap-space-sm px-space-md py-space-sm rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" data-path="dashboard"')
    
    target_link = f'class="flex items-center gap-space-sm px-space-md py-space-sm rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" data-path="{path}"'
    active_link = f'aria-current="page" class="flex items-center gap-space-sm px-space-md py-space-sm transition-colors bg-primary text-on-primary font-label-lg rounded-xl shadow-[0_2px_6px_-1px_rgba(0,88,190,0.3)]" data-path="{path}"'
    nav_content = nav_content.replace(target_link, active_link)
    
    final_html = nav_content[:main_start_idx] + content + nav_content[main_end_idx:]
    
    with open(f'{path}.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

print("Pages fully implemented.")
