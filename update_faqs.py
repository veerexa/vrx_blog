import os
import re
import datetime

directory = '/home/kapil-dev-pal/Desktop/school_blog/space'

def generate_faqs(title):
    return [
        {
            "q": f"What is the main objective of {title}?",
            "a": f"The primary objective of {title} is to advance our understanding of space exploration and contribute to India's growing capabilities in aerospace technology."
        },
        {
            "q": f"How does {title} impact future space missions?",
            "a": f"{title} sets a critical foundation for upcoming space missions by validating new technologies and operational procedures for ISRO and its partners."
        },
        {
            "q": f"What are the key technological advancements in {title}?",
            "a": f"Key advancements include improved propulsion systems, autonomous navigation, and cost-effective engineering methodologies that define {title}."
        },
        {
            "q": f"Why is {title} important for India's space program?",
            "a": f"{title} showcases India's self-reliance in space technology and strengthens its position in the global space economy."
        }
    ]

# Process HTML files
files_updated = []
for filename in os.listdir(directory):
    if filename.endswith('.html') and filename != 'index.html':
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1).split('|')[0].strip() if title_match else filename.replace('-', ' ').replace('.html', '').title()
        
        faqs = generate_faqs(title)
        
        # Build JSON-LD
        json_ld = '  <script type="application/ld+json">\n'
        json_ld += '{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n  "mainEntity": [\n'
        
        faq_html = '        <section class="mt-20 pt-10 border-t border-slate-200">\n'
        faq_html += f'          <h3 class="text-2xl font-display font-black text-slate-900 mb-8">Frequently Asked Questions about {title}</h3>\n'
        faq_html += '          <div class="faq-accordion space-y-4">\n'
        
        for i, faq in enumerate(faqs):
            json_ld += '    {\n      "@type": "Question",\n'
            json_ld += f'      "name": "{faq["q"]}",\n'
            json_ld += '      "acceptedAnswer": {\n        "@type": "Answer",\n'
            json_ld += f'        "text": "{faq["a"]}"\n      }}\n'
            if i < len(faqs) - 1:
                json_ld += '    },\n'
            else:
                json_ld += '    }\n'
            
            faq_html += '            <div class="faq-item bg-white rounded-xl shadow-sm border border-slate-100 p-4">\n'
            faq_html += '              <details class="group">\n'
            faq_html += f'                <summary class="faq-question font-semibold text-slate-800 cursor-pointer list-none flex justify-between items-center">{faq["q"]} <span class="text-brand-violet group-open:rotate-45 transition-transform text-xl">+</span></summary>\n'
            faq_html += f'                <div class="faq-answer mt-4 text-slate-600 leading-relaxed">{faq["a"]}</div>\n'
            faq_html += '              </details>\n'
            faq_html += '            </div>\n'
            
        json_ld += '  ]\n}\n  </script>\n'
        faq_html += '          </div>\n        </section>\n'
        
        # Remove existing FAQ schema if any
        content = re.sub(r'<script type="application/ld\+json">.*?FAQPage.*?</script>', '', content, flags=re.DOTALL)
        
        # Remove existing FAQ section if any (heuristics)
        content = re.sub(r'<section[^>]*>.*?FAQ.*?</section>', '', content, flags=re.IGNORECASE|re.DOTALL)
        
        # Inject JSON-LD
        content = content.replace('</head>', json_ld + '</head>')
        
        # Inject FAQ HTML
        if '</article>' in content:
            content = content.replace('</article>', faq_html + '</article>')
        else:
            # For isro-space-missions-india.html it might be </main>
            content = content.replace('</main>', faq_html + '</main>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        files_updated.append(filename)

print("Updated HTML files:", files_updated)

# Update Sitemap
sitemap_path = '/home/kapil-dev-pal/Desktop/school_blog/sitemap.xml'
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

today = datetime.datetime.now().strftime('%Y-%m-%d')

for filename in files_updated:
    url = f"https://blog.veerexa.com/space/{filename}"
    if filename in sitemap:
        # Update lastmod
        pattern = f'<url>\\s*<loc>{url}</loc>\\s*<lastmod>.*?</lastmod>'
        replacement = f'<url><loc>{url}</loc><lastmod>{today}</lastmod>'
        sitemap = re.sub(pattern, replacement, sitemap)
    else:
        # Add new entry
        new_entry = f'  <url><loc>{url}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
        sitemap = sitemap.replace('<!-- Space Blogs -->\n', '<!-- Space Blogs -->\n' + new_entry)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)
    
print("Updated sitemap.xml")
