# Censortron

Multi-layer text moderation framework

```
   ██████╗ ███████╗███╗   ██╗ ██████╗  ██████╗ ██████╗ 
  ██╔════╝ ██╔════╝████╗  ██║██╔════╝ ██╔═══██╗██╔══██╗
  ██║      █████╗  ██╔██╗ ██║ ╚█████╗ ██║   ██║██████╔╝
  ██║      ██╔══╝  ██║╚██╗██║     ╚██╗██║   ██║██╔══██╗
  ╚██████╗ ███████╗██║ ╚████║ ██████╔╝╚██████╔╝██║  ██║
   ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
████████╗██████╗  ██████╗ ███╗   ██╗
╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
   ██║   ██████╔╝██║   ██║██╔██╗ ██║
   ██║   ██╔══██╗██║   ██║██║╚██╗██║
   ██║   ██║  ██║╚██████╔╝██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

---

> [!CAUTION]
> <details><summary>Content Warning⚠️</summary>
>
> **Important Notice Regarding Repository Content**  
> This framework contains explicit language examples and moderation patterns that include:
>
> - **Offensive terminology**
> - **Sensitive lexical patterns**
> - **Profanity** (both explicit and masked variations)
>
> </details>

---

Features:

- simple and robust regex-based banword moderation
- multiple moderation layers
- enhanced overcensoring control
- Docker-ready FastAPI endpoint

Moderation layers:

- regex-based
- LLM classification: BERT, sensitive topics
- LLM classification: BERT, overall acceptablity

## ⚙️ Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

#### Run via main.py (recommended for local development)

Make sure you're in the root folder and the virtual environment is activated

Launch the app:

```
python main.py
```

The application will be available at:

```
http://localhost:8000/docs
```

#### Run in development mode

uvicorn src.api:app --host 0.0.0.0 --port 22230 --reload

## 🐳 Docker Deployment

To run the application using Docker, follow these steps:

1. Build the Docker image:

```
docker build -t Dockerfile.censortron .
```

2. Run the Docker container

```
docker run -p 22230:22230 censortron
```

The application will be accessible at <http://localhost:22230>.

### Customization

You can customize the moderation layers by modifying the following files:

Regex-based Moderation: Update the rules in src/regex_censure.py.

Language-specific Rules: Modify the files in src/censure/lang/ (e.g., ru.py, en.py) to adjust language-specific REGEX moderation logic.

LLM Classification: Adjust the models or parameters in src/filter_service.py.

### How to contribute

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Open pull request
