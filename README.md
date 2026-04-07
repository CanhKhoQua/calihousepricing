# California House Pricing Prediction

A Flask web app that predicts California house prices using a pre-trained Random Forest model (scikit-learn). Users input 8 housing features and receive an estimated price.

---

## Requirements

- Python 3.10+
- Docker (for containerized setup)
- `rfrmodel.pkl` — pre-trained model file must be present in the project root

---

## Option 1: Local Setup (Conda)

1. Clone the repository
```bash
git clone https://github.com/CanhKhoQua/calihousepricing.git
cd calihousepricing
```

2. Create and activate a conda environment
```bash
conda create -n calihousepricing python=3.10
conda activate calihousepricing
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the app
```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000`

---

## Option 2: Docker Setup

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed and running

### Build the image
```bash
docker build -t calihousepricing .
```

### Run the container
```bash
docker run -p 5000:5000 calihousepricing
```

Open your browser at `http://localhost:5000`

### Useful Docker commands
```bash
# Run in background (detached mode)
docker run -d -p 5000:5000 calihousepricing

# List running containers
docker ps

# View logs
docker logs <container_id>

# Stop the container
docker stop <container_id>

# Remove the image
docker rmi calihousepricing
```

---

## Running Tests

```bash
pytest tests/ --verbose
```

Tests cover model loading, prediction output, and Flask routes (`/` and `/predict`).

---

## CI/CD

GitHub Actions runs automatically on every push or pull request to `main`:
- Sets up Python 3.10
- Installs dependencies
- Runs the full test suite

See `.github/workflows/main.yaml` for details.

---

## Deployment (Render)

This app can be hosted for free on [Render](https://render.com).

1. Push the repo to GitHub
2. Go to [render.com](https://render.com) and sign up with GitHub
3. Click **New → Web Service** and connect your repo
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
5. Click **Deploy** — Render will provide a public URL

---

## Tech Stack

- **Backend:** Flask
- **ML Model:** scikit-learn (Random Forest)
- **Data:** pandas, numpy
- **Testing:** pytest
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Deployment:** Render