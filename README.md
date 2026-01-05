# Personal Budget Dashboard

This repo hosts a single-page budget dashboard and a small Streamlit wrapper to put it online.

## Quick start (local)

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/personal-budget.html`.

## Streamlit (local)

1) Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

2) Run Streamlit:

```powershell
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1) Push this repo to GitHub.
2) Go to https://share.streamlit.io and click **New app**.
3) Select your repo and set the entry point to `app.py`.
4) Deploy.

Notes:
- The app uses `st.components.v1.html` to render `personal-budget.html` directly.
- If you update the HTML, redeploy or restart the Streamlit app to pick up changes.
