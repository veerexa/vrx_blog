import os

directory = '/home/kapil-dev-pal/Desktop/school_blog/space'

for filename in os.listdir(directory):
    if not filename.endswith('.html') or filename == 'isro-space-missions-india.html':
        continue
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "What is the main objective of ISRO Hub - Veerexa Space?" in content:
        idx = content.find("What is the main objective of ISRO Hub - Veerexa Space?")
        start_idx = content.rfind('<script type="application/ld+json">', 0, idx)
        end_idx = content.find('</script>', idx) + len('</script>')
        
        content = content[:start_idx] + content[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Cleanup complete!")
