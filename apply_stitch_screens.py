import os
import re

mapping = {
    "Launch_Details.html": "gaganyaan-mission-updates.html",
    "Missions_Library.html": "isro-satellites-list.html",
    "Space_Companies.html": "indian-private-space-companies.html",
    "Rocket_Explorer_with_Comparison_Table.html": "india-vs-nasa-space-missions.html",
    "Rocket_Explorer.html": "isro-launches-2026-schedule.html"
}

source_dir = "/home/kapil-dev-pal/Desktop/school_blog"
dest_dir = "/home/kapil-dev-pal/Desktop/school_blog/space"

light_config = """        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "error": "#ba1a1a",
                        "surface-container": "#f1f5f9",
                        "inverse-surface": "#313033",
                        "on-secondary-fixed-variant": "#004e60",
                        "primary": "#0ea5e9",
                        "surface-container-high": "#e2e8f0",
                        "on-tertiary": "#ffffff",
                        "surface-container-lowest": "#ffffff",
                        "on-primary-fixed": "#001f2a",
                        "outline": "#79747e",
                        "error-container": "#ffdad6",
                        "on-surface-variant": "#334155",
                        "on-secondary": "#ffffff",
                        "inverse-on-surface": "#f4eff4",
                        "on-primary": "#ffffff",
                        "outline-variant": "#cac4d0",
                        "surface-tint": "#0ea5e9",
                        "secondary": "#7c3aed",
                        "primary-container": "#cff4ff",
                        "tertiary-fixed": "#ffd8e4",
                        "on-error": "#ffffff",
                        "background": "#f8fafc",
                        "surface": "#ffffff",
                        "surface-variant": "#e2e8f0",
                        "primary-fixed": "#cff4ff",
                        "secondary-container": "#e8def8",
                        "surface-bright": "#f8fafc",
                        "on-secondary-fixed": "#1d192b",
                        "tertiary": "#7d5260",
                        "on-tertiary-fixed-variant": "#31111d",
                        "on-background": "#0f172a",
                        "on-primary-container": "#001f2a",
                        "primary-fixed-dim": "#82d3f9",
                        "surface-container-low": "#f8fafc",
                        "tertiary-container": "#ffd8e4",
                        "secondary-fixed-dim": "#cbc2db",
                        "on-primary-fixed-variant": "#004b68",
                        "inverse-primary": "#82d3f9",
                        "on-surface": "#1e293b",
                        "on-tertiary-container": "#31111d",
                        "on-secondary-container": "#1d192b",
                        "surface-container-highest": "#cbd5e1",
                        "surface-dim": "#dcd8dd",
                        "on-error-container": "#410002",
                        "secondary-fixed": "#e8def8",
                        "tertiary-fixed-dim": "#efb8c8",
                        "on-tertiary-fixed": "#31111d"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "unit": "8px",
                        "component-gap": "16px",
                        "gutter": "24px",
                        "container-padding-desktop": "40px",
                        "container-padding-mobile": "20px"
                    },
                    "fontFamily": {
                        "label-caps": ["Space Mono"],
                        "display-lg": ["Inter"],
                        "telemetry-md": ["Space Mono"],
                        "headline-lg-mobile": ["Inter"],
                        "headline-lg": ["Inter"],
                        "body-md": ["Inter"]
                    },
                    "fontSize": {
                        "label-caps": ["12px", { "lineHeight": "16px", "letterSpacing": "0.1em", "fontWeight": "700" }],
                        "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "telemetry-md": ["14px", { "lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "400" }],
                        "headline-lg-mobile": ["28px", { "lineHeight": "36px", "fontWeight": "600" }],
                        "headline-lg": ["32px", { "lineHeight": "40px", "fontWeight": "600" }],
                        "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }]
                    }
                }
            }
        }"""

bottom_nav_html = """    <!-- BottomNavBar -->
    <nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-safe h-20 bg-surface/80 backdrop-blur-2xl border-t border-white/5 shadow-[0_-4px_24px_rgba(0,0,0,0.8)] md:hidden">
        <a href="isro-space-missions-india.html" class="flex flex-col items-center justify-center text-secondary relative after:content-[''] after:absolute after:-bottom-1 after:w-1 after:h-1 after:bg-secondary after:rounded-full transform scale-110 duration-200">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">rocket_launch</span>
            <span class="font-label-caps text-[10px] uppercase tracking-widest mt-1">ISRO</span>
        </a>
        <a href="index.html" class="flex flex-col items-center justify-center text-on-surface-variant opacity-60 hover:opacity-100 transition-opacity">
            <span class="material-symbols-outlined">explore</span>
            <span class="font-label-caps text-[10px] uppercase tracking-widest mt-1">Space</span>
        </a>
        <a href="../defense/index.html" class="flex flex-col items-center justify-center text-on-surface-variant opacity-60 hover:opacity-100 transition-opacity">
            <span class="material-symbols-outlined">shield</span>
            <span class="font-label-caps text-[10px] uppercase tracking-widest mt-1">Defense</span>
        </a>
    </nav>"""

for src, target in mapping.items():
    src_path = os.path.join(source_dir, src)
    target_path = os.path.join(dest_dir, target)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract FAQ schema from existing target file
    faq_schema = ""
    faq_html = ""
    if os.path.exists(target_path):
        with open(target_path, 'r', encoding='utf-8') as f:
            target_content = f.read()
            schema_match = re.search(r'(<script type="application/ld\+json">.*?FAQPage.*?</script>)', target_content, re.IGNORECASE | re.DOTALL)
            if schema_match:
                faq_schema = schema_match.group(1)
            
            html_match = re.search(r'(<section class="mt-20 pt-10 border-t border-slate-200">.*?Frequently Asked Questions.*?</section>)', target_content, re.IGNORECASE | re.DOTALL)
            if html_match:
                faq_html = html_match.group(1)
                
    # Modify content for Light Theme
    # Remove dark class
    content = content.replace('<html class="dark"', '<html class="light"')
    
    # Replace tailwind config
    content = re.sub(r'tailwind\.config = \{.*?\n        \}', light_config, content, flags=re.DOTALL)
    
    # Remove hardcoded backgrounds
    content = re.sub(r'background-color:\s*#141313;', 'background-color: #f8fafc;', content)
    content = re.sub(r'background:\s*rgba\(20, 19, 19, 0\.6\);', 'background: rgba(255, 255, 255, 0.6);', content)
    content = re.sub(r'border:\s*1px solid rgba\(255, 255, 255, 0\.1\);', 'border: 1px solid rgba(0, 0, 0, 0.05);', content)
    
    # Add FAQ schema
    if faq_schema:
        content = content.replace('</head>', '\n' + faq_schema + '\n</head>')
        
    # Add FAQ HTML at the end of <main>
    if faq_html:
        # Some files might have </main>, some might not
        if '</main>' in content:
            content = content.replace('</main>', '\n' + faq_html + '\n</main>')
        else:
            # Try to place it before bottom nav or </body>
            content = content.replace('</body>', '\n<main class="max-w-7xl mx-auto px-4">\n' + faq_html + '\n</main>\n</body>')
            
    # Replace bottom nav
    content = re.sub(r'<nav[^>]*bottom-0[^>]*>.*?</nav>', bottom_nav_html, content, flags=re.IGNORECASE | re.DOTALL)
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied 5 Stitch screens to the space pages!")
