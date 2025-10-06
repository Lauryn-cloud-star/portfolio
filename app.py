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

# About section content
ABOUT_CONTENT = {
    'paragraph1': "I'm a passionate developer with a love for creating elegant solutions to complex problems. With years of experience in web development, I specialize in building responsive, user-friendly applications that deliver exceptional experiences.",
    'paragraph2': "When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or sharing knowledge with the developer community. I believe in continuous learning and staying up-to-date with the latest industry trends."
}

# Projects data
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

# Skills data
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
