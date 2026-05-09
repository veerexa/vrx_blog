import os
import re

directory = '/home/kapil-dev-pal/Desktop/school_blog/space'

with open(os.path.join(directory, 'isro-space-missions-india.html'), 'r', encoding='utf-8') as f:
    template = f.read()

head_additions_match = re.search(r'(<!-- Google Fonts.*?)</head>', template, re.IGNORECASE | re.DOTALL)
head_additions = head_additions_match.group(1).strip() if head_additions_match else ""

top_elements_match = re.search(r'(<!-- Ambient Background Layer -->.*?</header>)', template, re.IGNORECASE | re.DOTALL)
top_elements = top_elements_match.group(1).strip() if top_elements_match else ""

bottom_nav_match = re.search(r'(<!-- BottomNavBar -->.*?)</nav>', template, re.IGNORECASE | re.DOTALL)
bottom_nav = bottom_nav_match.group(1).strip() + "\n" if bottom_nav_match else ""

for filename in os.listdir(directory):
    if not filename.endswith('.html') or filename == 'isro-space-missions-india.html':
        continue
        
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove old tailwind and style.css
    content = re.sub(r'<link href="\.\./assets/css/style\.css".*?>\n?', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>\n?', '', content, flags=re.IGNORECASE)
    
    if '<!-- Google Fonts -->' not in content:
        content = content.replace('</head>', '\n' + head_additions + '\n</head>')
        
    content = re.sub(r'<body[^>]*>', '<body class="font-body-md text-[#334155] bg-[#f8fafc] pb-32">', content)
    
    content = re.sub(r'<header class="sticky top-0.*?</header>', top_elements, content, flags=re.IGNORECASE | re.DOTALL)
    
    content = re.sub(r'<footer.*?</footer>', '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<!-- Mobile Bottom Nav -->\s*<nav class="mobile-bottom-nav">.*?</nav>', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    if '<!-- BottomNavBar -->' not in content:
        content = content.replace('</body>', bottom_nav + '</body>')
        
    # Adjust main container
    content = re.sub(r'<main class="bg-slate-50">', '<main class="relative z-10 w-full max-w-7xl mx-auto flex flex-col mt-8">', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated figma structure for all space pages!")
