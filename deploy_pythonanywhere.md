# Deploy to PythonAnywhere - Free Forever

## Step 1: Create PythonAnywhere Account
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Click "Create a Beginner account" (free)
3. Verify your email

## Step 2: Upload Your Files
1. Go to "Files" tab in PythonAnywhere dashboard
2. Navigate to `/home/yourusername/`
3. Create a new folder called `portfolio`
4. Upload all your files:
   - `app.py`
   - `requirements.txt`
   - `templates/` folder
   - `static/` folder

## Step 3: Install Dependencies
1. Go to "Consoles" tab
2. Start a new Bash console
3. Run these commands:
```bash
cd portfolio
pip3.10 install --user -r requirements.txt
```

## Step 4: Configure Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Click "Next"

## Step 5: Set Up WSGI File
1. In the Web tab, click on the WSGI configuration file link
2. Replace the content with:
```python
import sys
path = '/home/yourusername/portfolio'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

## Step 6: Configure Static Files
1. In the Web tab, scroll down to "Static files"
2. Add these mappings:
   - URL: `/static/`
   - Directory: `/home/yourusername/portfolio/static/`

## Step 7: Reload Your Web App
1. Click the green "Reload" button
2. Your site will be live at `yourusername.pythonanywhere.com`

## Step 8: Custom Domain (Optional)
1. In Web tab, go to "Domains"
2. Add your custom domain
3. Update DNS settings with your domain provider

## Troubleshooting
- If you get import errors, check the WSGI file path
- If static files don't load, verify static file mappings
- Check the "Error log" tab for any issues
