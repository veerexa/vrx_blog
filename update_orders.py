import os

directory = '/home/kapil-dev-pal/Desktop/school_blog'

for root, dirs, files in os.walk(directory):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Replace order classes
            new_content = content.replace('order-2 lg:order-1', 'order-1')
            new_content = new_content.replace('order-1 lg:order-2', 'order-2')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
