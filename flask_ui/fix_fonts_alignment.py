import re

filepath = r"c:\Users\Admin\OneDrive\Documents\code\HQTCSDL\HQTCSDL\flask_ui\templates\admin_feedback_detail.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove custom fonts
content = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=DM\+Sans[^"]+" rel="stylesheet">', '', content)
content = content.replace("font-family: 'DM Sans', sans-serif;", "font-family: var(--font-body);")
content = content.replace("font-family: 'Playfair Display', serif;", "font-family: var(--font-heading);")

# 2. Fix Step header alignment and text styles
content = content.replace('.step-header {', '.step-header {\n    text-align: left;\n')

# 3. Add explicit text alignment for the header content just in case
content = content.replace('.step-header h3 {', '.step-header h3 {\n    font-family: var(--font-heading);\n    text-align: left;\n')
content = content.replace('.step-header p {', '.step-header p {\n    text-align: left;\n')

# 4. Remove center alignments from other places that might have broken
content = content.replace('text-align: center;', 'text-align: left; /* fixed center alignment */')
# Wait, some tables need center! Let's only target .step-header
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated fonts and fixed alignment.")
