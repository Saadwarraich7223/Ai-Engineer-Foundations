# 🧠 Side Skills Roadmap — ML / Data Science / AI Engineering

> Complementary skills to learn alongside the 30-day Python track.
> These are what separate job-ready engineers from "bootcamp" learners.

---

## 📋 How to Use This Alongside the Main Roadmap

| Time Block | Focus |
|------------|-------|
| **Hour 1** | Main Python roadmap (daily topic) |
| **Hour 2** | SQL / Statistics (alternate days) |
| **Hour 3** | Build something + push to GitHub |

```
Mon/Wed/Fri → SQL
Tue/Thu/Sat → Statistics / Math
Sun         → Revision & project cleanup
```

---

## 1️⃣ Git & GitHub — Start Day 1

**Why**: Daily commits mean nothing if you only know `git add` + `git commit`. Real ML teams use branches, PRs, and rebasing.

### What to Learn

| Concept | Why It Matters |
|---------|----------------|
| `git init`, `clone`, `add`, `commit`, `push`, `pull` | Daily workflow |
| Branching (`checkout -b`, `merge`) | Feature isolation |
| Rebasing (`rebase`, `rebase -i`) | Clean commit history |
| Pull requests (GitHub UI + `gh` CLI) | Code review culture |
| `.gitignore` | Keep secrets & large files out |
| `git stash`, `git log --oneline --graph` | Quick context switching |
| `git diff`, `git blame` | Debugging & auditing |
| Tagging (`git tag v1.0`) | Versioning models / datasets |

### Practice Workflow (Use This Daily)

```bash
# Start each day
git checkout -b day-XX-topic

# End each day
git add -A
git commit -m "Day XX: Topic learned"
git checkout main
git merge day-XX-topic
git push origin main
```

### Resources

- [Pro Git Book (free)](https://git-scm.com/book/en/v2) — read Chapters 1–3, 6
- [Learn Git Branching](https://learngitbranching.js.org/) — interactive visualizer
- [GitHub Skills](https://skills.github.com/) — free interactive courses
- [Oh My Git!](https://ohmygit.org/) — game-based Git learning

### Milestone

> Push 30 daily commits with clean commit messages. By Day 30 your GitHub graph is solid green.

---

## 2️⃣ Linux & Command Line — Start Day 1

**Why**: Every ML model trains on Linux. Every cloud server runs Linux. Every deployment target is Linux. If `ssh` into a box scares you, fix that now.

### What to Learn

| Command | Purpose |
|---------|---------|
| `pwd`, `ls`, `cd`, `mkdir`, `touch`, `rm`, `cp`, `mv` | File navigation |
| `cat`, `less`, `head`, `tail`, `wc` | File inspection |
| `grep`, `find`, `locate` | Search |
| `chmod`, `chown` | Permissions |
| `ps`, `top`, `htop`, `kill` | Process management |
| `ssh`, `scp`, `rsync` | Remote access / file transfer |
| `cron`, `systemctl` | Scheduling & services |
| `nano` / `vim` | Terminal text editing |
| `env`, `export`, `source` | Environment variables |
| `pip`, `python3`, `venv` | Python environment management |

### Key Skills

- Create and activate a virtual environment: `python -m venv .venv && source .venv/bin/activate`
- Run a Python script with CLI arguments: `python train.py --epochs 50 --lr 0.001`
- Grep through logs to find errors: `grep -r "Traceback" logs/`
- Find large files: `find . -type f -size +100M`
- SSH into a remote machine and run a script

### Resources

- [The Missing Semester of CS (MIT)](https://missing.csail.mit.edu/) — best free resource
- [Linux Journey](https://linuxjourney.com/) — gamified learning
- [Learn the Terminal (Codecademy)](https://www.codecademy.com/learn/learn-the-command-line)
- OverTheWire: [Bandit Wargame](https://overthewire.org/wargames/bandit/) — Linux skills via CTF

### Milestone

> Run `python train.py --epochs 100` on a remote Linux machine via SSH without errors.

---

## 3️⃣ SQL — Start Day 7 (Week 2)

**Why**: In real jobs, data lives in databases, not CSV files. SQL is the #1 asked skill in data science interviews, and most "AI Engineers" skip it — giving you an edge.

### What to Learn

| Topic | Level |
|-------|-------|
| `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT` | Beginner |
| `GROUP BY`, `HAVING`, aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) | Beginner |
| `JOIN` (`INNER`, `LEFT`, `RIGHT`, `FULL`, `CROSS`) | Intermediate |
| Subqueries (correlated & uncorrelated) | Intermediate |
| Window functions (`ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM OVER`) | Advanced |
| CTEs (`WITH ... AS`) | Advanced |
| Indexing, query performance | Advanced |
| `CREATE TABLE`, `ALTER`, data types | Intermediate |
| Database design: normalization, keys, relationships | Intermediate |

### Practice Dataset

```sql
-- Start with this schema for all exercises
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    join_date DATE
);

CREATE TABLE sales (
    id INT PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    amount DECIMAL(10, 2),
    sale_date DATE
);
```

### Practice Exercises

1. Find the top 3 highest-paid employees per department
2. Calculate running total of sales per employee
3. Find employees who sold more than the average in their department
4. Month-over-month sales growth rate
5. Employees with no sales in the last 30 days

### Resources

- [SQL Bolt](https://sqlbolt.com/) — interactive, 15 min each
- [LeetCode SQL Problem Set](https://leetcode.com/problemset/database/) — interview practice
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/) — best free deep dive
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) — pick one DB and learn it well
- **Book**: *Learning SQL* by Alan Beaulieu

### Tooling

```bash
# Install SQLite (comes with Python)
import sqlite3

# Or use Docker for PostgreSQL
docker run --name pg -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres
```

### Milestone

> Solve 10 medium LeetCode SQL problems without looking at solutions.

---

## 4️⃣ Statistics — Start Day 14 (Week 3)

**Why**: The biggest gap most developers have when entering ML. You can learn scikit-learn in a week. Statistics takes months — start early.

### What to Learn

| Week | Topic | Key Concepts |
|------|-------|--------------|
| Week 3 | Descriptive Stats | Mean, median, mode, variance, standard deviation, IQR, box plots |
| Week 4 | Probability | Conditional probability, Bayes theorem, law of large numbers, central limit theorem |
| Week 5 | Distributions | Normal, binomial, Poisson, uniform, exponential |
| Week 6 | Inferential Stats | Hypothesis testing, p-values, confidence intervals, t-tests, chi-square |
| Week 7 | Correlation & Regression | Pearson/Spearman correlation, covariance, R², p-value for coefficients |
| Week 8 | Advanced | ANOVA, Bayesian thinking, A/B testing, MLE |

### Resources

- [StatQuest with Josh Starmer (YouTube)](https://www.youtube.com/@statquest) — **THE best** intuition builder. Watch every video.
- [Khan Academy — Statistics & Probability](https://www.khanacademy.org/math/statistics-probability) — free, thorough
- [Seeing Theory](https://seeing-theory.brown.edu/) — interactive visual explanations
- [Think Stats (free book)](https://greenteapress.com/wp/think-stats-2e/) — statistics through Python
- **Book**: *Naked Statistics* by Charles Wheelan — intuition without math

### Python Practice (Do This in Stats Notebooks)

```python
import numpy as np
from scipy import stats

# Descriptive
data = np.random.normal(50, 10, 1000)
np.mean(data), np.median(data), np.std(data)

# Hypothesis test
stats.ttest_ind(group_a, group_b)

# Distribution fit
stats.norm.fit(data)
```

### Milestone

> Explain p-value to a non-technical person in plain English. Understand why it's NOT the probability the null hypothesis is true.

---

## 5️⃣ Mathematics for ML — Start Day 21 (Week 4+)

**Why**: You don't need a math degree, but you need to understand what the code is doing. Start with intuition, add formulas later.

### What to Learn

| Branch | Key Concepts | When You'll Use It |
|--------|--------------|-------------------|
| **Linear Algebra** | Vectors, matrices, dot product, matrix multiplication, transpose, inverse, eigenvalues | Neural networks, PCA, word embeddings, dimensionality reduction |
| **Calculus** | Derivatives, partial derivatives, chain rule, gradient | Backpropagation, gradient descent, optimization |
| **Optimization** | Gradient descent, SGD, learning rates, loss functions | Training any ML model |

### Don't Learn (Yet)

- Fourier transforms
- Differential equations
- Complex analysis
- Abstract algebra

### Resources

- [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — watch this first
- [3Blue1Brown — Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — watch this second
- [Immersive Linear Algebra](http://immersivemath.com/ila/) — interactive
- [Khan Academy — Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [Khan Academy — Calculus](https://www.khanacademy.org/math/calculus-1)
- **Book**: *Mathematics for Machine Learning* by Deisenroth (free online) — the only ML math book you need

### Python Practice

```python
import numpy as np

# Vector dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot = np.dot(a, b)  # 32

# Matrix multiplication
A = np.random.randn(3, 4)
B = np.random.randn(4, 2)
C = A @ B  # shape (3, 2)

# Gradient descent from scratch
def gradient_descent(x, lr=0.01, epochs=100):
    for _ in range(epochs):
        grad = 2 * x  # derivative of f(x) = x²
        x -= lr * grad
    return x
```

### Milestone

> Implement linear regression from scratch using only NumPy and gradient descent. Must match sklearn's result within 1% error.

---

## 6️⃣ Jupyter Notebook — Start Day 15

**Why**: Every data scientist/ML engineer lives in notebooks. It's not optional.

### What to Learn

- Installing: `pip install notebook jupyterlab`
- Cells: code vs markdown vs raw
- Keyboard shortcuts: `Shift+Enter`, `Esc`, `A`, `B`, `DD`, `M`, `Y`
- Magic commands: `%matplotlib inline`, `%timeit`, `%%bash`, `%%writefile`
- Widgets: `ipywidgets` for interactive controls
- Display: `display()`, rich outputs (images, DataFrames, plots inline)
- Extensions: JupyterLab extensions, jupyter-black, jupyter-contrib-nbextensions
- Export: `.ipynb` → `.py` / `.html` / `.pdf`
- Sharing: nbviewer, GitHub renders `.ipynb` natively

### Resources

- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Jupyter for Beginners (DataCamp)](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook)
- Real Python: [Jupyter Notebook: An Introduction](https://realpython.com/jupyter-notebook-introduction/)

### Milestone

> Create a well-structured notebook with markdown sections, code cells, inline visualizations, and exported as both HTML and PDF.

---

## 7️⃣ Data Analysis Mindset — Start Day 17

**Why**: Knowing Pandas functions is useless if you can't ask the right questions from data.

### The Analysis Framework

```
1. Define the question
   ↓
2. Collect / load data
   ↓
3. Clean & validate
   ↓
4. Explore (EDA)
   ↓
5. Model / analyze
   ↓
6. Interpret results
   ↓
7. Communicate findings
```

### Practice Data Analysis Workflow

For every dataset you touch:

1. **Question**: What am I trying to find out?
2. **Inspect**: `.head()`, `.info()`, `.describe()`, `.shape`, `.dtypes`
3. **Clean**: Missing values, outliers, duplicates, wrong types
4. **Explore**: Distributions, correlations, group comparisons
5. **Hypothesis**: What pattern do I expect?
6. **Visualize**: 3+ plots to test the hypothesis
7. **Conclude**: 3–5 bullet points of what you learned

### Datasets to Practice On

| Dataset | Where to Find | Skills |
|---------|--------------|--------|
| Titanic | Seaborn (`sns.load_dataset('titanic')`) | Classification, missing data |
| Iris | Seaborn / sklearn | Classification, clustering |
| Tips | Seaborn (`sns.load_dataset('tips')`) | Regression, group analysis |
| Housing | Kaggle | Feature engineering, regression |
| COVID-19 | Our World in Data | Time series, data cleaning |
| IMDB Reviews | Kaggle | Text data, NLP basics |

### Resources

- [Kaggle Learn Courses](https://www.kaggle.com/learn) — free, practical
- [Storytelling with Data](https://www.storytellingwithdata.com/) — visualization best practices
- **Book**: *Python Data Science Handbook* by Jake VanderPlas

### Milestone

> Pick a raw dataset from Kaggle, clean it, explore it, and write a 1-page analysis with 5 visualizations that tells a clear story.

---

## 8️⃣ Docker — Month 2 (Alongside Days 15–20)

**Why**: Reproducibility is the #1 problem in ML. Docker solves it. Also required for deployment.

### What to Learn

```bash
# Core commands
docker pull python:3.12
docker build -t my-ml-app .
docker run -p 8888:8888 my-ml-app
docker ps
docker stop <container_id>

# ML-specific
docker compose up    # ML app + database + API
docker volume create # persist models / data
```

### Sample Dockerfile for ML

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "train.py"]
```

### Resources

- [Docker Quickstart](https://docs.docker.com/get-started/)
- [Docker for Data Science (Medium)](https://towardsdatascience.com/docker-for-data-science-9c0e2c52bd28)
- [Play with Docker](https://labs.play-with-docker.com/) — browser-based practice

### Milestone

> Containerize a simple ML training script. Run it, verify the trained model artifact exists inside the container.

---

## 9️⃣ Cloud Basics — Month 2–3

**Why**: Models don't run on your laptop in production. Pick one cloud and learn the core services.

### Recommended Learning Path (AWS)

| Service | Purpose | When |
|---------|---------|------|
| S3 | Store datasets & models | Month 2 |
| EC2 | Run training on GPU instances | Month 2 |
| ECR + ECS | Deploy containerized models | Month 3 |
| SageMaker | Managed ML training/deployment | Month 3+ |
| Lambda | Lightweight inference endpoints | Month 3+ |

### Equivalent on GCP

| GCP Service | AWS Equivalent |
|-------------|---------------|
| Cloud Storage | S3 |
| Compute Engine | EC2 |
| Cloud Run | ECS |
| Vertex AI | SageMaker |
| Cloud Functions | Lambda |

### Resources

- [AWS Free Tier](https://aws.amazon.com/free/) — get hands-on
- [AWS Skill Builder](https://explore.skillbuilder.aws/learn) — free digital training
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/) — free credits for labs
- [Qwiklabs](https://www.qwiklabs.com/) — hands-on cloud labs

### Milestone

> Launch an EC2 instance, SSH in, install Python, clone a repo, and run training. Store the output model back to S3.

---

## 🔟 AI Engineering Concepts — Month 3+

**Why**: The market is shifting from "train models" to "build AI applications." LLMs, RAG, and agents are where the jobs are going.

### What to Learn

| Concept | What It Is | Why It Matters |
|---------|------------|----------------|
| **LLMs** | Large Language Models (GPT, Claude, Llama) | Foundation of modern AI apps |
| **Embeddings** | Vector representations of text | Search, similarity, clustering |
| **Vector Databases** | Pinecone, Weaviate, Qdrant, Chroma | Store & query embeddings at scale |
| **RAG** | Retrieval-Augmented Generation | Ground LLMs in your data |
| **Agents** | Autonomous LLM-driven task execution | Automation, research, coding |
| **Prompt Engineering** | Crafting effective LLM instructions | Day-to-day AI work |
| **Model Serving** | vLLM, Ollama, TGI, BentoML | Deploy models as APIs |
| **Fine-tuning** | LoRA, QLoRa | Adapt models to your domain |

### Tools to Know

| Tool | Category |
|------|----------|
| Hugging Face Transformers | Models & inference |
| LangChain / LlamaIndex | RAG & agent frameworks |
| Chroma / Pinecone | Vector databases |
| Ollama | Local model running |
| vLLM | High-throughput serving |
| Weights & Biases | Experiment tracking |

### Resources

- [Hugging Face Learn](https://huggingface.co/learn) — free NLP/transformers course
- [LangChain Tutorial](https://python.langchain.com/docs/tutorials/)
- [LLM Bootcamp (Full Stack Deep Learning)](https://fullstackdeeplearning.com/llm-bootcamp/)
- [Andrej Karpathy's "Intro to Large Language Models" (YouTube)](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- [RAG from Scratch (YouTube Series)](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyE7j1DR2oQ4kI)

### Milestone

> Build a RAG app: ingest a PDF, chunk it, embed it, store in a vector DB, and answer questions about it via an LLM.

---

## 📅 Integrated 4-Month Master Plan

```
Month 1 (Days 1–30 of Python)
├── Python Fundamentals → Data Science Stack
├── Git & GitHub ───────────────────────── daily commits
├── Linux CLI       ───────────────────────── daily practice
└── SQL             ──────────── Mon/Wed/Fri (Week 2+)

Month 2
├── Pandas, NumPy, Visualization, EDA
├── Statistics ──── Tue/Thu/Sat (deep dive)
├── Scikit-Learn ── basic ML algorithms
└── Docker ──────── containerize data projects

Month 3
├── Deep Learning (PyTorch)
├── Math for ML ─── Linear Algebra + Calculus
├── Cloud (AWS/GCP) ── EC2 + S3 for training
└── Advanced ML ──── XGBoost, hyperparameter tuning

Month 4+
├── LLMs, RAG, Agents
├── Model deployment & serving
├── MLOps basics (CI/CD, monitoring)
├── Portfolio projects on GitHub
└── Interview prep (SQL + ML + system design)
```

## 🎯 Skill Stack for AI Engineer Roles

```
Python + SQL + Statistics + PyTorch + LLMs + Deployment
```

This combination is what companies actually hire for. Not just "I trained a model on Iris." But "I built a full-stack AI app, deployed it, and it's serving real users."

---

## 📚 Quick Reference: Where to Start Each Skill

| Skill | Start | First Thing to Do |
|-------|-------|-------------------|
| Git | Day 1 | `git init` and make your first commit |
| Linux | Day 1 | Open terminal, run `ls`, `pwd`, `cd` |
| SQL | Day 7 | Go to SQLBolt.com, do first 4 lessons |
| Statistics | Day 14 | Watch StatQuest "p-value" video |
| Math | Day 21 | Watch 3Blue1Brown "Vectors" video |
| Jupyter | Day 15 | `pip install jupyterlab` then `jupyter lab` |
| Docker | Month 2 | Write a Dockerfile that runs a Python script |
| Cloud | Month 2 | Sign up for AWS Free Tier |
| AI Eng | Month 3+ | Run `ollama run llama3` and chat with it |

---

## ⚡ Weekly Check-In

```
Week ___

Main Python: Day ___ completed □
Git:        Pushed ___ commits this week □
SQL:        Solved ___ problems □
Statistics: Watched ___ StatQuest videos □
Linux:      Used ___ new commands □
Project:    Worked on ___ □

One thing I'm stuck on: _________________

Goal for next week: _________________
```

---

*Master the fundamentals. Build daily. The compound effect is real.* 🚀
