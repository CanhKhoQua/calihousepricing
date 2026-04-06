### California House Pricing Prediction

### Software And Tools Requirements

1. [Github Account](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

### Getting Started

1. Clone the repository
```
git clone https://github.com/CanhKhoQua/calihousepricing.git
cd calihousepricing
```

2. Create and activate a conda environment
```
conda create -n calihousepricing python=3.10
conda activate calihousepricing
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the app
```
python app.py
```

Then open your browser at `http://127.0.0.1:5000`

---

### Deployment (Render)

This app is hosted for free on [Render](https://render.com).

To deploy your own:
1. Push the repo to GitHub
2. Go to [render.com](https://render.com) and sign up with GitHub
3. Click **New → Web Service** and connect your repo
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
5. Click **Deploy** — Render will provide a public URL