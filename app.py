from flask import Flask, render_template_string, url_for

app = Flask(__name__)

NAV = '''
<nav style="background:#f8f9fa;padding:1em 2em;display:flex;gap:2em;">
  <a href="/">Home</a>
  <a href="/projects">Projects</a>
  <a href="/resume">Resume</a>
  <a href="/contact">Contact</a>
</nav>
'''

HOME = NAV + '''
<div style="max-width:700px;margin:2em auto;font-family:sans-serif;">
  <h1>Yuheng Zhao</h1>
  <h2>PhD Candidate / Software Engineer</h2>
  <p>Welcome to my portfolio! I am passionate about AI, web development, and research. Explore my projects and experience below.</p>
</div>
'''

PROJECTS = NAV + '''
<div style="max-width:700px;margin:2em auto;font-family:sans-serif;">
  <h1>Projects</h1>
  <ul>
    <li><b>StarRealm</b>: Web-based card game platform</li>
    <li><b>Neon City</b>: Interactive 3D city visualization</li>
    <li><b>S2GEM & Sign Weng</b>: Innovative collaboration project</li>
  </ul>
</div>
'''

RESUME = NAV + '''
<div style="max-width:700px;margin:2em auto;font-family:sans-serif;">
  <h1>Resume</h1>
  <p><b>Education:</b> MSc in Computer Science, XYZ University</p>
  <p><b>Experience:</b> Software Engineer at ABC Corp, Research Intern at DEF Lab</p>
  <p><b>Skills:</b> Python, Flask, React, Machine Learning, Data Science</p>
</div>
'''

CONTACT = NAV + '''
<div style="max-width:700px;margin:2em auto;font-family:sans-serif;">
  <h1>Contact</h1>
  <p>Email: <a href="mailto:yuheng.zhao@email.com">yuheng.zhao@email.com</a></p>
  <p>LinkedIn: <a href="https://linkedin.com/in/yuhengzhao">linkedin.com/in/yuhengzhao</a></p>
</div>
'''

@app.route('/')
def home():
    return render_template_string(HOME)

@app.route('/projects')
def projects():
    return render_template_string(PROJECTS)

@app.route('/resume')
def resume():
    return render_template_string(RESUME)

@app.route('/contact')
def contact():
    return render_template_string(CONTACT)

if __name__ == '__main__':
    app.run(debug=True) 