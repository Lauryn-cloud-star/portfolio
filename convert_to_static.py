#!/usr/bin/env python3
"""
Convert Flask app to static HTML files for free hosting
This creates a static version that works on GitHub Pages, Netlify, Vercel, etc.
"""

import os
import json
from jinja2 import Template

# Your portfolio data (same as in app.py)
PERSONAL_INFO = {
    'name': 'Lauryn Hope Tuhaise`',
    'title': 'Full Stack Developer & Climate in action fellowship member',
    'description': 'I craft beautiful, functional web experiences. Passionate about clean code, user experience, and building products that make a difference.',
    'email': 'laurynhope29@gmail.com',
    'phone': '+256 (77) 368-0805',
    'location': 'Kampala, Uganda',
    'github': 'https://github.com/Lauryn-cloud-star',
    'linkedin': 'https://www.linkedin.com/in/lauryn-hope-tuhaise-6a7236289',
    'twitter': 'https://twitter.com/laurynhope'
}

ABOUT_CONTENT = {
    'paragraph1': "I'm a passionate developer with a love for creating elegant solutions to complex problems. I'm also a Climate in action fellowship member. With years of experience in web development, I specialize in building responsive, user-friendly applications that deliver exceptional experiences.",
    'paragraph2': "When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community. I believe in continuous learning and staying up-to-date with the latest industry trends."
}

PROJECTS = [
    {
        'title': 'Karibu Groceries',
        'description': 'Inventory management and sales system for a grocery store dealing in rice, beans, maize, and cowpeas. Streamlined operations and improved sales tracking.',
        'technologies': ['Python', 'Tailwind CSS', 'Django', 'SQLite', 'HTML/CSS', 'React'],
        'live_url': '#',
        'code_url': 'https://github.com/Lauryn-cloud-star/final_project',
        'icon': 'shopping-cart',
        'image': 'image.png'
    },
    {
        'title': 'ICPAU Audit Tool',
        'description': 'Comprehensive audit management system for auditors and ICPAU regulators in Uganda. Streamlined compliance processes and regulatory reporting.',
        'technologies': ['Python', 'Django-rest-framework', 'PostgreSQL', 'Typescript', 'React'],
        'live_url': '#',
        'code_url': '#',
        'icon': 'chart-bar',
        'image': 'icpau.png'
    },
    {
        'title': 'FOSA Sacco System',
        'description': 'Complete management system for FOSA Sacco. Handles member registration, loan management, savings tracking, and financial reporting.',
        'technologies': ['JavaScript', 'Tailwind CSS', 'MySQL', 'Bootstrap', 'HTML', 'React'],
        'live_url': '#',
        'code_url': 'https://github.com/Lauryn-cloud-star/grow-sacco-hub',
        'icon': 'university',
        'image': 'fosa.png'
    }
]

SKILLS = {
    'Frontend Development': {
        'icon': 'js-square',
        'skills': ['JavaScript (ES6+)', 'HTML5/CSS3', 'Tailwind CSS', 'React', 'Bootstrap', 'Responsive Design']
    },
    'Backend Development': {
        'icon': 'python',
        'skills': ['Python', 'Django Framework', 'Django REST Framework', 'Flask', 'API Development', 'MySQL', 'PostgreSQL']
    },
    'Database Management': {
        'icon': 'database',
        'skills': ['PostgreSQL', 'MySQL', 'SQL Queries', 'Database Design', 'Django ORM', 'Data Migration']
    },
    'Development Tools': {
        'icon': 'tools',
        'skills': ['Git Version Control', 'VS Code', 'Command Line', 'Debugging', 'Testing', 'Docker', 'Virtual Machines']
    },
    'System Development': {
        'icon': 'cogs',
        'skills': ['Inventory Management', 'Audit Systems', 'Financial Systems', 'User Management', 'Reporting Systems']
    },
    'Additional Skills': {
        'icon': 'bolt',
        'skills': ['Problem Solving', 'System Analysis', 'Requirements Gathering', 'Client Communication', 'Project Management']
    }
}

def create_static_site():
    """Create static HTML files from Flask template"""
    
    # Read the static site template (already processed)
    with open('static_site/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Replace template variables with actual data
    replacements = {
        'Your Name': PERSONAL_INFO['name'],
        'your.email@example.com': PERSONAL_INFO['email'],
        '+1 (234) 567-890': PERSONAL_INFO['phone'],
        'San Francisco, CA': PERSONAL_INFO['location'],
        'https://github.com/yourusername': PERSONAL_INFO['github'],
        'https://linkedin.com/in/yourusername': PERSONAL_INFO['linkedin'],
        'https://twitter.com/yourusername': PERSONAL_INFO['twitter'],
        'Lauryn - Portfolio Photo': f"{PERSONAL_INFO['name']} - Portfolio Photo"
    }
    
    html_content = template_content
    for placeholder, value in replacements.items():
        html_content = html_content.replace(placeholder, value)
    
    # Create static directory
    os.makedirs('static_site', exist_ok=True)
    
    # Write static HTML
    with open('static_site/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Copy static files
    import shutil
    if os.path.exists('static'):
        shutil.copytree('static', 'static_site/static', dirs_exist_ok=True)
    
    # Create a simple contact form handler (client-side)
    contact_js = f"""
    // Simple contact form handler for static site
    document.addEventListener('DOMContentLoaded', function() {{
        const form = document.querySelector('form[method="POST"]');
        if (form) {{
            form.addEventListener('submit', function(e) {{
                e.preventDefault();
                
                const name = this.querySelector('input[name="name"]').value;
                const email = this.querySelector('input[name="email"]').value;
                const message = this.querySelector('textarea[name="message"]').value;
                
                if (!name || !email || !message) {{
                    alert('Please fill in all fields.');
                    return;
                }}
                
                // Create mailto link
                const subject = `Portfolio Contact from ${{name}}`;
                const body = `Name: ${{name}}\\nEmail: ${{email}}\\n\\nMessage:\\n${{message}}`;
                const mailtoLink = `mailto:{PERSONAL_INFO['email']}?subject=${{encodeURIComponent(subject)}}&body=${{encodeURIComponent(body)}}`;
                
                // Open email client
                window.location.href = mailtoLink;
                
                // Show success message
                alert('Thank you! Your email client should open with a pre-filled message.');
            }});
        }}
    }});
    """
    
    # Add contact form handler to main.js
    with open('static/js/main.js', 'r', encoding='utf-8') as f:
        main_js = f.read()
    
    with open('static_site/static/js/main.js', 'w', encoding='utf-8') as f:
        f.write(main_js + contact_js)
    
    print("✅ Static site created in 'static_site' folder!")
    print("📁 Upload the contents of 'static_site' to any free hosting:")
    print("   - GitHub Pages (free)")
    print("   - Netlify (free)")
    print("   - Vercel (free)")
    print("   - Firebase Hosting (free)")
    print("   - Surge.sh (free)")

if __name__ == "__main__":
    create_static_site()
