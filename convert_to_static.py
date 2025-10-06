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
    'name': 'Your Name',
    'title': 'Full Stack Developer & Creative Problem Solver',
    'description': 'I craft beautiful, functional web experiences. Passionate about clean code, user experience, and building products that make a difference.',
    'email': 'your.email@example.com',
    'phone': '+1 (234) 567-890',
    'location': 'San Francisco, CA',
    'github': 'https://github.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourusername',
    'twitter': 'https://twitter.com/yourusername'
}

ABOUT_CONTENT = {
    'paragraph1': "I'm a passionate developer with a love for creating elegant solutions to complex problems. With years of experience in web development, I specialize in building responsive, user-friendly applications that deliver exceptional experiences.",
    'paragraph2': "When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community. I believe in continuous learning and staying up-to-date with the latest industry trends."
}

PROJECTS = [
    {
        'title': 'E-Commerce Platform',
        'description': 'A full-stack e-commerce solution with payment integration, inventory management, and real-time analytics.',
        'technologies': ['React', 'Node.js', 'PostgreSQL', 'Stripe'],
        'live_url': '#',
        'code_url': '#',
        'icon': 'shopping-cart'
    },
    {
        'title': 'Task Management App',
        'description': 'Collaborative task management tool with real-time updates, team collaboration features, and advanced filtering.',
        'technologies': ['TypeScript', 'React', 'Firebase', 'Tailwind'],
        'live_url': '#',
        'code_url': '#',
        'icon': 'tasks'
    },
    {
        'title': 'Analytics Dashboard',
        'description': 'Data visualization dashboard with interactive charts, custom reports, and export functionality.',
        'technologies': ['React', 'D3.js', 'Express', 'MongoDB'],
        'live_url': '#',
        'code_url': '#',
        'icon': 'chart-bar'
    }
]

SKILLS = {
    'Frontend Development': {
        'icon': 'code',
        'skills': ['React', 'TypeScript', 'Next.js', 'Tailwind CSS', 'HTML5/CSS3']
    },
    'Backend Development': {
        'icon': 'server',
        'skills': ['Node.js', 'Express', 'Python', 'REST APIs', 'GraphQL']
    },
    'Database & Storage': {
        'icon': 'database',
        'skills': ['PostgreSQL', 'MongoDB', 'Redis', 'Firebase', 'Supabase']
    },
    'Tools & Practices': {
        'icon': 'tools',
        'skills': ['Git', 'Docker', 'CI/CD', 'Testing', 'Agile']
    },
    'Mobile Development': {
        'icon': 'mobile-alt',
        'skills': ['React Native', 'Flutter', 'PWA', 'Responsive Design']
    },
    'Other Skills': {
        'icon': 'bolt',
        'skills': ['UI/UX Design', 'Cloud Computing', 'DevOps', 'Project Management']
    }
}

def create_static_site():
    """Create static HTML files from Flask template"""
    
    # Read the Flask template
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Create Jinja2 template
    template = Template(template_content)
    
    # Render with data (remove Flask-specific functions)
    html_content = template.render(
        personal_info=PERSONAL_INFO,
        about_content=ABOUT_CONTENT,
        projects=PROJECTS,
        skills=SKILLS,
        get_flashed_messages=lambda: [],
        url_for=lambda x: x
    )
    
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
    contact_js = """
    // Simple contact form handler for static site
    document.addEventListener('DOMContentLoaded', function() {
        const form = document.querySelector('form[method="POST"]');
        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const name = this.querySelector('input[name="name"]').value;
                const email = this.querySelector('input[name="email"]').value;
                const message = this.querySelector('textarea[name="message"]').value;
                
                if (!name || !email || !message) {
                    alert('Please fill in all fields.');
                    return;
                }
                
                // Create mailto link
                const subject = `Portfolio Contact from ${name}`;
                const body = `Name: ${name}\\nEmail: ${email}\\n\\nMessage:\\n${message}`;
                const mailtoLink = `mailto:your.email@example.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
                
                // Open email client
                window.location.href = mailtoLink;
                
                // Show success message
                alert('Thank you! Your email client should open with a pre-filled message.');
            });
        }
    });
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
