from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miguel La Cruz — Data Scientist & MLOps</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0f172a;
            color: #e2e8f0;
            line-height: 1.7;
        }

        nav {
            position: sticky;
            top: 0;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #1e293b;
            padding: 16px 0;
        }
        nav ul {
            list-style: none;
            max-width: 900px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: center;
            gap: 32px;
        }
        nav a {
            color: #94a3b8;
            text-decoration: none;
            font-size: 0.9rem;
            text-transform: uppercase;
            transition: color 0.2s;
        }
        nav a:hover { color: #7dd3fc; }

        .hero {
            text-align: center;
            padding: 100px 24px 80px;
            max-width: 780px;
            margin: 0 auto;
        }
        .badge {
            display: inline-block;
            background: #1e293b;
            border: 1px solid #334155;
            color: #7dd3fc;
            font-size: 0.82rem;
            padding: 6px 14px;
            border-radius: 20px;
            margin-bottom: 24px;
        }
        h1 {
            font-size: 3rem;
            color: #f1f5f9;
            margin-bottom: 10px;
        }
        h1 span { color: #7dd3fc; }
        .subtitle {
            color: #94a3b8;
            margin-bottom: 6px;
        }
        .location {
            color: #64748b;
            margin-bottom: 30px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            margin: 6px;
        }
        .btn-primary { background: #7dd3fc; color: #0f172a; }
        .btn-outline { border: 1px solid #334155; color: #cbd5e1; }

        section { padding: 70px 24px; max-width: 900px; margin: 0 auto; }
        h2 { color: #f1f5f9; margin-bottom: 10px; }
        .divider {
            width: 44px;
            height: 3px;
            background: #7dd3fc;
            margin-bottom: 12px;
        }
        p { color: #cbd5e1; margin-bottom: 14px; }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 18px;
        }
        .card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
        }
        .card h4 { color: #7dd3fc; margin-bottom: 8px; }
        .card small { color: #64748b; }

        footer {
            text-align: center;
            padding: 40px;
            border-top: 1px solid #1e293b;
            color: #475569;
            font-size: 0.85rem;
        }
    </style>
</head>
<body>

<nav>
    <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#skills">Skills</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#connect">Contact</a></li>
    </ul>
</nav>

<header class="hero">
    <div class="badge">Data Scientist → MLOps</div>
    <h1>Miguel <span>La Cruz</span></h1>
    <p class="subtitle">Data Scientist | Machine Learning | Cloud & Kubernetes</p>
    <p class="location">Madrid, Spain</p>
    <a href="https://github.com/Mlcruz9" class="btn btn-primary" target="_blank">GitHub</a>
    <a href="https://www.linkedin.com/in/miguellacruz/" class="btn btn-outline" target="_blank">LinkedIn</a>
    <a href="mailto:miguellacruz.data@gmail.com" class="btn btn-outline">Email</a>
</header>

<section id="about">
    <div class="divider"></div>
    <h2>About Me</h2>
    <p>
        I build data products from experimentation to production.
        My focus is on deploying machine learning systems with reproducible pipelines,
        cloud-native architectures, and observability best practices.
    </p>
    <p>
        Experience across Data Science, Kubernetes optimization, and production ML systems.
        Currently transitioning deeper into MLOps engineering.
    </p>
</section>

<section id="skills">
    <div class="divider"></div>
    <h2>Skills</h2>
    <div class="card-grid">
        <div class="card">
            <h4>Cloud</h4>
            <small>AWS, Azure, Linux</small>
        </div>
        <div class="card">
            <h4>Containers</h4>
            <small>Docker, Kubernetes</small>
        </div>
        <div class="card">
            <h4>Data & ML</h4>
            <small>Python, Pandas, Scikit-learn, Spark</small>
        </div>
        <div class="card">
            <h4>APIs & Production</h4>
            <small>FastAPI, CI/CD, Monitoring</small>
        </div>
    </div>
</section>

<section id="projects">
    <div class="divider"></div>
    <h2>Projects</h2>
    <div class="card-grid">
        <div class="card">
            <h4>Client Segmentation + GenAI</h4>
            <small>Clustering + LLM explanation layer</small>
        </div>
        <div class="card">
            <h4>Travel Agent LLM App</h4>
            <small>Interactive AI-based travel assistant</small>
        </div>
        <div class="card">
            <h4>Well Log Reconstruction</h4>
            <small>ML pipeline for missing data recovery</small>
        </div>
        <div class="card">
            <h4>Battleship Monte Carlo AI</h4>
            <small>Probabilistic strategy simulation</small>
        </div>
    </div>
</section>

<section id="connect">
    <div class="divider"></div>
    <h2>Contact</h2>
    <p>Email: miguellacruz.data@gmail.com</p>
    <p>GitHub: github.com/Mlcruz9</p>
    <p>LinkedIn: linkedin.com/in/miguellacruz</p>
</section>

<footer>
    © 2026 Miguel La Cruz · Built with Flask for testing on AWS
</footer>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
