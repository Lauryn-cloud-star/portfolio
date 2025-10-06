#!/usr/bin/env python3
"""
Create a static version of the portfolio for free hosting
"""

import os
import shutil

def create_static_site():
    """Create static HTML files"""
    
    # Read the Flask template and remove Flask-specific parts
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Flask-specific template code
    content = content.replace('{{ url_for(\'contact\') }}', '#contact')
    content = content.replace('{{ url_for(\'static\', filename=\'js/main.js\') }}', 'static/js/main.js')
    
    # Remove flash messages section
    flash_section = '''                    <!-- Flash Messages -->
                    {% with messages = get_flashed_messages(with_categories=true) %}
                        {% if messages %}
                            {% for category, message in messages %}
                                <div class="mb-6 p-4 rounded-lg {% if category == 'error' %}bg-red-100 text-red-700{% else %}bg-green-100 text-green-700{% endif %}">
                                    {{ message }}
                                </div>
                            {% endfor %}
                        {% endif %}
                    {% endwith %}'''
    content = content.replace(flash_section, '')
    
    # Replace template variables with actual data
    replacements = {
        '{{ personal_info.name }}': 'Your Name',
        '{{ personal_info.title }}': 'Full Stack Developer & Creative Problem Solver',
        '{{ personal_info.description }}': 'I craft beautiful, functional web experiences. Passionate about clean code, user experience, and building products that make a difference.',
        '{{ personal_info.email }}': 'your.email@example.com',
        '{{ personal_info.phone }}': '+1 (234) 567-890',
        '{{ personal_info.location }}': 'San Francisco, CA',
        '{{ personal_info.github }}': 'https://github.com/yourusername',
        '{{ personal_info.linkedin }}': 'https://linkedin.com/in/yourusername',
        '{{ personal_info.twitter }}': 'https://twitter.com/yourusername',
        '{{ about_content.paragraph1 }}': "I'm a passionate developer with a love for creating elegant solutions to complex problems. With years of experience in web development, I specialize in building responsive, user-friendly applications that deliver exceptional experiences.",
        '{{ about_content.paragraph2 }}': "When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community. I believe in continuous learning and staying up-to-date with the latest industry trends."
    }
    
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    # Replace projects section
    projects_html = '''                <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                    <div class="h-48 bg-gray-100 flex items-center justify-center">
                        <i class="fas fa-shopping-cart text-5xl text-gray-400"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-semibold text-gray-900 mb-3">E-Commerce Platform</h3>
                        <p class="text-gray-600 mb-4 leading-relaxed">A full-stack e-commerce solution with payment integration, inventory management, and real-time analytics.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">React</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">Node.js</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">PostgreSQL</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">Stripe</span>
                        </div>
                        <div class="flex gap-3">
                            <a href="#" class="flex items-center gap-2 text-gray-900 border border-gray-300 px-4 py-2 rounded-lg hover:bg-gray-900 hover:text-white transition-colors duration-300">
                                <i class="fas fa-external-link-alt"></i>
                                Live
                            </a>
                            <a href="#" class="flex items-center gap-2 text-gray-900 border border-gray-300 px-4 py-2 rounded-lg hover:bg-gray-900 hover:text-white transition-colors duration-300">
                                <i class="fab fa-github"></i>
                                Code
                            </a>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                    <div class="h-48 bg-gray-100 flex items-center justify-center">
                        <i class="fas fa-tasks text-5xl text-gray-400"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-semibold text-gray-900 mb-3">Task Management App</h3>
                        <p class="text-gray-600 mb-4 leading-relaxed">Collaborative task management tool with real-time updates, team collaboration features, and advanced filtering.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">TypeScript</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">React</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">Firebase</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">Tailwind</span>
                        </div>
                        <div class="flex gap-3">
                            <a href="#" class="flex items-center gap-2 text-gray-900 border border-gray-300 px-4 py-2 rounded-lg hover:bg-gray-900 hover:text-white transition-colors duration-300">
                                <i class="fas fa-external-link-alt"></i>
                                Live
                            </a>
                            <a href="#" class="flex items-center gap-2 text-gray-900 border border-gray-300 px-4 py-2 rounded-lg hover:bg-gray-900 hover:text-white transition-colors duration-300">
                                <i class="fab fa-github"></i>
                                Code
                            </a>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                    <div class="h-48 bg-gray-100 flex items-center justify-center">
                        <i class="fas fa-chart-bar text-5xl text-gray-400"></i>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-semibold text-gray-900 mb-3">Analytics Dashboard</h3>
                        <p class="text-gray-600 mb-4 leading-relaxed">Data visualization dashboard with interactive charts, custom reports, and export functionality.</p>
                        <div class="flex flex-wrap gap-2 mb-6">
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">React</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">D3.js</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">Express</span>
                            <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">MongoDB</span>
                        </div>
                        <div class="flex gap-3">
                            <a href="#" class="flex items-center gap-2 text-gray-900 border border-gray-300 px-4 py-2 rounded-lg hover:bg-gray-900 hover:text-white transition-colors duration-300">
                                <i class="fas fa-external-link-alt"></i>
                                Live
                            </a>
                            <a href="#" class="flex items-center gap-2 text-gray-900 border border-gray-300 px-4 py-2 rounded-lg hover:bg-gray-900 hover:text-white transition-colors duration-300">
                                <i class="fab fa-github"></i>
                                Code
                            </a>
                        </div>
                    </div>
                </div>'''
    
    # Replace the projects loop with static HTML
    import re
    projects_pattern = r'{% for project in projects %}.*?{% endfor %}'
    content = re.sub(projects_pattern, projects_html, content, flags=re.DOTALL)
    
    # Replace skills section
    skills_html = '''                <div class="bg-slate-50 p-8 rounded-2xl text-center hover:-translate-y-2 transition-transform duration-300">
                    <div class="w-16 h-16 bg-gray-900 text-white rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                        <i class="fas fa-code"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Frontend Development</h3>
                    <ul class="text-left space-y-2">
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            React
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            TypeScript
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Next.js
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Tailwind CSS
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            HTML5/CSS3
                        </li>
                    </ul>
                </div>

                <div class="bg-slate-50 p-8 rounded-2xl text-center hover:-translate-y-2 transition-transform duration-300">
                    <div class="w-16 h-16 bg-gray-900 text-white rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                        <i class="fas fa-server"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Backend Development</h3>
                    <ul class="text-left space-y-2">
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Node.js
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Express
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Python
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            REST APIs
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            GraphQL
                        </li>
                    </ul>
                </div>

                <div class="bg-slate-50 p-8 rounded-2xl text-center hover:-translate-y-2 transition-transform duration-300">
                    <div class="w-16 h-16 bg-gray-900 text-white rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                        <i class="fas fa-database"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Database & Storage</h3>
                    <ul class="text-left space-y-2">
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            PostgreSQL
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            MongoDB
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Redis
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Firebase
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Supabase
                        </li>
                    </ul>
                </div>

                <div class="bg-slate-50 p-8 rounded-2xl text-center hover:-translate-y-2 transition-transform duration-300">
                    <div class="w-16 h-16 bg-gray-900 text-white rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                        <i class="fas fa-tools"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Tools & Practices</h3>
                    <ul class="text-left space-y-2">
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Git
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Docker
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            CI/CD
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Testing
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Agile
                        </li>
                    </ul>
                </div>

                <div class="bg-slate-50 p-8 rounded-2xl text-center hover:-translate-y-2 transition-transform duration-300">
                    <div class="w-16 h-16 bg-gray-900 text-white rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                        <i class="fas fa-mobile-alt"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Mobile Development</h3>
                    <ul class="text-left space-y-2">
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            React Native
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Flutter
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            PWA
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Responsive Design
                        </li>
                    </ul>
                </div>

                <div class="bg-slate-50 p-8 rounded-2xl text-center hover:-translate-y-2 transition-transform duration-300">
                    <div class="w-16 h-16 bg-gray-900 text-white rounded-full flex items-center justify-center text-2xl mx-auto mb-6">
                        <i class="fas fa-bolt"></i>
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Other Skills</h3>
                    <ul class="text-left space-y-2">
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            UI/UX Design
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Cloud Computing
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            DevOps
                        </li>
                        <li class="text-gray-600 flex items-center">
                            <span class="w-2 h-2 bg-gray-900 rounded-full mr-3"></span>
                            Project Management
                        </li>
                    </ul>
                </div>'''
    
    # Replace the skills loop with static HTML
    skills_pattern = r'{% for category, data in skills.items\(\) %}.*?{% endfor %}'
    content = re.sub(skills_pattern, skills_html, content, flags=re.DOTALL)
    
    # Update contact form to use mailto
    contact_form = '''                    <form onsubmit="handleContactForm(event)">
                        <div class="space-y-6">
                            <div>
                                <label for="name" class="block text-sm font-medium text-gray-900 mb-2">Name</label>
                                <input type="text" id="name" name="name" required
                                       class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-colors duration-300"
                                       placeholder="Your name">
                            </div>
                            <div>
                                <label for="email" class="block text-sm font-medium text-gray-900 mb-2">Email</label>
                                <input type="email" id="email" name="email" required
                                       class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-colors duration-300"
                                       placeholder="your.email@example.com">
                            </div>
                            <div>
                                <label for="message" class="block text-sm font-medium text-gray-900 mb-2">Message</label>
                                <textarea id="message" name="message" rows="5" required
                                          class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gray-900 focus:border-transparent transition-colors duration-300 resize-none"
                                          placeholder="Tell me about your project..."></textarea>
                            </div>
                            <button type="submit" class="w-full bg-gray-900 text-white py-3 px-6 rounded-lg hover:bg-gray-800 transition-colors duration-300 font-medium">
                                Send Message
                            </button>
                        </div>
                    </form>'''
    
    # Replace the form
    form_pattern = r'<form method="POST" action="{{ url_for\(\'contact\'\) }}">.*?</form>'
    content = re.sub(form_pattern, contact_form, content, flags=re.DOTALL)
    
    # Add contact form handler script
    contact_script = '''
    <script>
    function handleContactForm(event) {
        event.preventDefault();
        
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;
        
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
    }
    </script>'''
    
    # Add script before closing body tag
    content = content.replace('</body>', contact_script + '</body>')
    
    # Create static directory
    os.makedirs('static_site', exist_ok=True)
    
    # Write static HTML
    with open('static_site/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', 'static_site/static', dirs_exist_ok=True)
    
    print("✅ Static site created in 'static_site' folder!")
    print("📁 Upload the contents of 'static_site' to any free hosting:")
    print("   - GitHub Pages (free forever)")
    print("   - Netlify (free forever)")
    print("   - Vercel (free forever)")
    print("   - Firebase Hosting (free forever)")
    print("   - Surge.sh (free forever)")

if __name__ == "__main__":
    create_static_site()
