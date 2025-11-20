#!/usr/bin/env python3
"""
Generate static site from Flask template with current changes
"""

import os
import shutil

def generate_static():
    """Generate static HTML from Flask template"""
    
    # Create static directory
    os.makedirs('static_deploy', exist_ok=True)
    
    # Your portfolio data
    personal_info = {
        'name': 'Lauryn',
        'title': 'Full Stack Developer & Creative Problem Solver',
        'description': 'I craft beautiful, functional web experiences. Passionate about clean code, user experience, and building products that make a difference.',
        'email': 'laurynhope29@gmail.com',
        'phone': '+256 (77) 368-0805',
        'location': 'Uganda',
        'github': 'https://github.com/Lauryn-cloud-star',
        'linkedin': 'https://www.linkedin.com/in/lauryn-hope-tuhaise-6a7236289/',
        'twitter': 'https://twitter.com/lauryn'
    }
    
    # Read Flask template
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Replace Flask variables with static content
    replacements = {
        "{{ personal_info.name }}": personal_info['name'],
        "{{ personal_info.title }}": personal_info['title'],
        "{{ personal_info.description }}": personal_info['description'],
        "{{ personal_info.email }}": personal_info['email'],
        "{{ personal_info.phone }}": personal_info['phone'],
        "{{ personal_info.location }}": personal_info['location'],
        "{{ personal_info.github }}": personal_info['github'],
        "{{ personal_info.linkedin }}": personal_info['linkedin'],
        "{{ personal_info.twitter }}": personal_info['twitter'],
        "{{ url_for('static', filename='images/lauryn_pic.jpg') }}": "images/lauryn_pic.jpg",
        "{{ url_for('static', filename='images/' + project.image) }}": lambda project: f"images/{project['image']}",
        "{{ url_for('static', filename='js/main.js') }}": "js/main.js"
    }
    
    # Apply simple replacements
    for key, value in replacements.items():
        if callable(value):
            # Handle dynamic image replacements
            for project in [
                {'image': 'image.png'},
                {'image': 'icpau_site.png'},
                {'image': 'fosa.png'}
            ]:
                old_pattern = f"{{{{ url_for('static', filename='images/' + project.image) }}}}"
                new_pattern = f"images/{project['image']}"
                template_content = template_content.replace(old_pattern, new_pattern)
        else:
            template_content = template_content.replace(key, str(value))
    
    # Remove Jinja2 template syntax
    import re
    
    # Remove Jinja2 for loops
    template_content = re.sub(r'{% for .*? %}', '', template_content)
    template_content = re.sub(r'{% endfor %}', '', template_content)
    template_content = re.sub(r'{% if .*? %}', '', template_content)
    template_content = re.sub(r'{% endif %}', '', template_content)
    template_content = re.sub(r'{% with .*? %}', '', template_content)
    template_content = re.sub(r'{% endwith %}', '', template_content)
    
    # Handle projects data
    projects_html = """
                <div class="project-card shadow-sm hover:shadow-lg">
                    <div class="project-image-container">
                        <img src="images/image.png" 
                             alt="Karibu Groceries" 
                             class="w-full">
                    </div>
                    <div class="space-y-4">
                        <h3 class="text-xl font-semibold text-brown-900 mb-3">Karibu Groceries</h3>
                        <p class="text-brown-600 mb-4 leading-relaxed">Inventory management and sales system for a grocery store dealing in rice, beans, maize, and cowpeas. Streamlined operations and improved sales tracking.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">Python</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">Tailwind CSS</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">Django</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">SQLite</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">HTML/CSS</span>
                        </div>
                    </div>
                </div>
                <div class="project-card shadow-sm hover:shadow-lg">
                    <div class="project-image-container">
                        <img src="images/icpau_site.png" 
                             alt="ICPAU Audit Tool" 
                             class="w-full">
                    </div>
                    <div class="space-y-4">
                        <h3 class="text-xl font-semibold text-brown-900 mb-3">ICPAU Audit Tool</h3>
                        <p class="text-brown-600 mb-4 leading-relaxed">Comprehensive audit management system for auditors and ICPAU regulators in Uganda. Streamlined compliance processes and regulatory reporting.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">Python</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">Django REST Framework</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">PostgreSQL</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">TypeScript</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">React</span>
                        </div>
                    </div>
                </div>
                <div class="project-card shadow-sm hover:shadow-lg">
                    <div class="project-image-container">
                        <img src="images/fosa.png" 
                             alt="FOSA Sacco System" 
                             class="w-full">
                    </div>
                    <div class="space-y-4">
                        <h3 class="text-xl font-semibold text-brown-900 mb-3">FOSA Sacco System</h3>
                        <p class="text-brown-600 mb-4 leading-relaxed">Complete management system for FOSA Sacco. Handles member registration, loan management, savings tracking, and financial reporting.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">JavaScript</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">Tailwind CSS</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">MySQL</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">Bootstrap</span>
                            <span class="bg-brown-100 text-brown-700 px-3 py-1 rounded-full text-sm font-medium">HTML</span>
                        </div>
                    </div>
                </div>
    """
    
    # Replace the dynamic projects loop with static HTML
    template_content = re.sub(r'{% for project in projects %}.*?{% endfor %}', projects_html, template_content, flags=re.DOTALL)
    
    # Handle about content
    about_content = "I'm a passionate developer with a love for creating elegant solutions to complex problems. I'm also a Climate in action fellowship member. With years of experience in web development, I specialize in building responsive, user-friendly applications that deliver exceptional experiences."
    about_content2 = "When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community. I believe in continuous learning and staying up-to-date with the latest industry trends."
    
    template_content = template_content.replace('{{ about_content.paragraph1 }}', about_content)
    template_content = template_content.replace('{{ about_content.paragraph2 }}', about_content2)
    
    # Write static HTML
    with open('static_deploy/index.html', 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    # Copy static assets
    if os.path.exists('static'):
        if os.path.exists('static_deploy/images'):
            shutil.rmtree('static_deploy/images')
        shutil.copytree('static/images', 'static_deploy/images')
        
        if os.path.exists('static_deploy/js'):
            shutil.rmtree('static_deploy/js')
        shutil.copytree('static/js', 'static_deploy/js')
    
    print("Static site generated successfully!")
    print("Upload 'static_deploy' folder to Netlify")

if __name__ == "__main__":
    generate_static()