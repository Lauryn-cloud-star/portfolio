from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Configuration
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

# Personal information - customize these
PERSONAL_INFO = {
    'name': 'Lauryn',
    'title': 'Full Stack Developer & Creative Problem Solver',
    'description': 'I craft beautiful, functional web experiences. Passionate about clean code, user experience, and building products that make a difference.',
    'email': 'lauryn@example.com',
    'phone': '+256 (xxx) xxx-xxx',
    'location': 'Uganda',
    'github': 'https://github.com/Lauryn-cloud-star',
    'linkedin': 'https://linkedin.com/in/lauryn',
    'twitter': 'https://twitter.com/lauryn'
}

# About section content
ABOUT_CONTENT = {
    'paragraph1': "I'm a passionate developer with a love for creating elegant solutions to complex problems. With years of experience in web development, I specialize in building responsive, user-friendly applications that deliver exceptional experiences.",
    'paragraph2': "When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community. I believe in continuous learning and staying up-to-date with the latest industry trends."
}

# Projects data
PROJECTS = [
    {
        'title': 'Karibu Groceries',
        'description': 'Inventory management and sales system for a grocery store dealing in rice, beans, maize, and cowpeas. Streamlined operations and improved sales tracking.',
        'technologies': ['Python', 'Tailwind CSS', 'Django', 'SQLite', 'HTML/CSS'],
        'live_url': '#',
        'code_url': 'https://github.com/Lauryn-cloud-star/final_project',
        'icon': 'shopping-cart'
    },
    {
        'title': 'ICPAU Audit Tool',
        'description': 'Comprehensive audit management system for auditors and ICPAU regulators in Uganda. Streamlined compliance processes and regulatory reporting.',
        'technologies': ['Python', 'Django REST Framework', 'PostgreSQL', 'TypeScript', 'React'],
        'live_url': '#',
        'code_url': '#',
        'icon': 'chart-bar'
    },
    {
        'title': 'FOSA Sacco System',
        'description': 'Complete management system for FOSA Sacco. Handles member registration, loan management, savings tracking, and financial reporting.',
        'technologies': ['JavaScript', 'Tailwind CSS', 'MySQL', 'Bootstrap', 'HTML'],
        'live_url': '#',
        'code_url': 'https://github.com/Lauryn-cloud-star/grow-sacco-hub',
        'icon': 'university'
    }
]

# Skills data
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

@app.route('/')
def index():
    return render_template('index.html', 
                         personal_info=PERSONAL_INFO,
                         about_content=ABOUT_CONTENT,
                         projects=PROJECTS,
                         skills=SKILLS)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Email validation
        import re
        if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Send email (if configured)
        if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
            try:
                send_email(name, email, message)
                flash('Thank you for your message! I\'ll get back to you soon.', 'success')
            except Exception as e:
                flash('There was an error sending your message. Please try again.', 'error')
                print(f"Email error: {e}")
        else:
            # Log the message (for development)
            print(f"Contact form submission: {name} ({email}): {message}")
            flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        
        return redirect(url_for('index') + '#contact')

def send_email(name, email, message):
    """Send email notification for contact form submission"""
    msg = MIMEMultipart()
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = PERSONAL_INFO['email']
    msg['Subject'] = f"Portfolio Contact Form - {name}"
    
    body = f"""
    New contact form submission:
    
    Name: {name}
    Email: {email}
    Message: {message}
    
    Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
    server.starttls()
    server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    text = msg.as_string()
    server.sendmail(app.config['MAIL_USERNAME'], PERSONAL_INFO['email'], text)
    server.quit()

@app.route('/api/projects')
def api_projects():
    """API endpoint for projects (if needed for future enhancements)"""
    return jsonify(PROJECTS)

@app.route('/api/skills')
def api_skills():
    """API endpoint for skills (if needed for future enhancements)"""
    return jsonify(SKILLS)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
