import os
import re

filepath = r"c:\Users\Admin\OneDrive\Documents\code\HQTCSDL\HQTCSDL\flask_ui\templates\admin_feedback_detail.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS Variables
content = content.replace('--bg-main: #0a0e1a;', '--bg-main: #FFFFFF;')
content = content.replace('--bg-card: #111827;', '--bg-card: #F8FAFC;')
content = content.replace('--border-soft: rgba(255, 255, 255, 0.08);', '--border-soft: #E2E8F0;')
content = content.replace('--text-main: #e5e7eb;', '--text-main: #1E293B;')
content = content.replace('--text-muted: #9ca3af;', '--text-muted: #64748b;')
content = content.replace('--accent-grad: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);', '--accent-grad: linear-gradient(135deg, #D4B068 0%, #E5C37A 100%);')

# Background and borders
content = content.replace('background: radial-gradient(circle at 12% -5%, rgba(99, 102, 241, 0.22), transparent 45%), radial-gradient(circle at 90% 0%, rgba(139, 92, 246, 0.2), transparent 40%), var(--bg-main);', 'background: var(--bg-main);')
content = content.replace('background: rgba(17, 24, 39, 0.94);', 'background: #FFFFFF;')
content = content.replace('color: white;', 'color: var(--text-main);')
content = content.replace('color: #dbeafe;', 'color: #005F6E;')
content = content.replace('color: #c7d2fe;', 'color: #002D3C;')
content = content.replace('color: #e5e7eb;', 'color: #1E293B;')

# Other dark colors to light
content = content.replace('#111827', '#FFFFFF')
content = content.replace('#1e2535', '#F1F5F9')
content = content.replace('#0f172a', '#F8FAFC')
content = content.replace('rgba(255, 255, 255, 0.02)', 'rgba(0, 0, 0, 0.02)')
content = content.replace('rgba(255, 255, 255, 0.08)', 'rgba(0, 0, 0, 0.05)')
content = content.replace('rgba(255, 255, 255, 0.03)', 'rgba(0, 0, 0, 0.03)')
content = content.replace('rgba(255, 255, 255, 0.12)', 'rgba(0, 0, 0, 0.12)')
content = content.replace('rgba(255, 255, 255, 0.1)', 'rgba(0, 0, 0, 0.1)')
content = content.replace('rgba(255,255,255,0.05)', 'rgba(0,0,0,0.05)')
content = content.replace('rgba(255,255,255,0.1)', 'rgba(0,0,0,0.1)')

# Specific border/accent colors from indigo/purple to teal/gold
content = content.replace('border-color: rgba(99, 102, 241, 0.45);', 'border-color: #D4B068;')
content = content.replace('background: rgba(99, 102, 241, 0.16);', 'background: rgba(212, 176, 104, 0.16);')
content = content.replace('#6366f1', '#005F6E')
content = content.replace('#8b5cf6', '#D4B068')
content = content.replace('rgba(99, 102, 241, 0.3)', 'rgba(0, 95, 110, 0.3)')
content = content.replace('rgba(99, 102, 241, 0.22)', 'rgba(0, 95, 110, 0.22)')
content = content.replace('rgba(99, 102, 241, 0.12)', 'rgba(0, 95, 110, 0.12)')
content = content.replace('rgba(99, 102, 241, 0.1)', 'rgba(0, 95, 110, 0.1)')

# Progress bars background
content = content.replace('background: rgba(255, 255, 255, 0.08);', 'background: #E2E8F0;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated admin_feedback_detail.html colors to light theme.")
