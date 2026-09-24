import os
import re

# Read dashboard.html as template
with open('dashboard.html', 'r', encoding='utf-8') as f:
    dashboard_content = f.read()

# Pages to create
pages = {
    'challenges': ('Challenges', 'flag', 'Explore daily and weekly wellness challenges to earn extra XP and unlock special rewards.'),
    'achievements': ('Achievements', 'emoji_events', 'View your earned badges, trophies, and milestones across your wellness journey.'),
    'progress': ('Progress', 'bar_chart', 'Track your activity, hydration, and study breaks over time with detailed analytics.'),
    'settings': ('Settings', 'tune', 'Manage your notification preferences, daily goals, and account details.')
}

for path, (title, icon, desc) in pages.items():
    # We want to replace the main content.
    # The main content starts at <main class="..."> and ends before </body>
    
    # Let's find <main ...> and replace its inner HTML.
    main_start_match = re.search(r'<main[^>]*>', dashboard_content)
    if not main_start_match:
        continue
    
    main_start_idx = main_start_match.end()
    main_end_idx = dashboard_content.rfind('</main>')
    
    if main_end_idx == -1:
        continue
    
    # We also need to update the active state in the sidebar.
    # The sidebar has a nav element with links.
    # First, let's remove aria-current="page" and the active classes from dashboard
    nav_content = dashboard_content
    # Remove active state from dashboard
    nav_content = nav_content.replace('aria-current="page" class="flex items-center gap-space-sm px-space-md py-space-sm transition-colors bg-primary text-on-primary font-label-lg rounded-xl shadow-[0_2px_6px_-1px_rgba(0,88,190,0.3)]" data-path="dashboard"', 
                                      'class="flex items-center gap-space-sm px-space-md py-space-sm rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" data-path="dashboard"')
    
    # Add active state to the current page
    target_link = f'class="flex items-center gap-space-sm px-space-md py-space-sm rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-colors" data-path="{path}"'
    active_link = f'aria-current="page" class="flex items-center gap-space-sm px-space-md py-space-sm transition-colors bg-primary text-on-primary font-label-lg rounded-xl shadow-[0_2px_6px_-1px_rgba(0,88,190,0.3)]" data-path="{path}"'
    
    nav_content = nav_content.replace(target_link, active_link)
    
    new_main_content = f'''
    <div class="flex flex-col w-full h-full items-center justify-center min-h-[80vh] p-space-xl text-center">
        <div class="w-24 h-24 rounded-3xl bg-primary-fixed text-primary flex items-center justify-center mb-space-lg shadow-sm">
            <span class="material-symbols-outlined text-[48px]">{icon}</span>
        </div>
        <h1 class="font-display-hero text-display-hero text-on-surface tracking-tight mb-space-sm">{title}</h1>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-md">{desc}</p>
        <div class="mt-space-xl px-space-lg py-space-sm rounded-full bg-surface-container-high text-on-surface font-label-lg text-label-lg inline-flex items-center gap-2">
            <span class="material-symbols-outlined text-[20px]">construction</span>
            <span>Coming Soon</span>
        </div>
    </div>
    '''
    
    final_html = nav_content[:main_start_idx] + new_main_content + nav_content[main_end_idx:]
    
    with open(f'{path}.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

print("Created 4 new pages successfully.")
