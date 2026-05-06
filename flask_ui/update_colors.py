import os
import re

templates_dir = r"c:\Users\Admin\OneDrive\Documents\code\HQTCSDL\HQTCSDL\flask_ui\templates"

for filename in os.listdir(templates_dir):
    if not filename.endswith('.html'): continue
    filepath = os.path.join(templates_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove hardcoded inline hero backgrounds
    content = re.sub(r'<section class="hero"\s+style="background:\s*linear-gradient[^"]+;">', r'<section class="hero">', content)
    content = re.sub(r'<section class="hero"\s+style="background:\s*linear-gradient[^"]+;\s*display:[^"]+;">', r'<section class="hero" style="display: flex; align-items: center; justify-content: center; text-align: center; flex-direction: column;">', content)
    
    # Change colors
    content = content.replace('#1e293b', '#002D3C')
    content = content.replace('#0F172A', '#002D3C')
    content = content.replace('#1E1B4B', '#002D3C')
    content = content.replace('#312E81', '#005F6E')
    content = content.replace('#1D4ED8', '#005F6E')
    content = content.replace('#10B981', '#D4B068') # Green to Gold
    content = content.replace('#064E3B', '#002D3C')
    content = content.replace('#059669', '#B89650') # Dark Green to Dark Gold
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Template colors updated.")
