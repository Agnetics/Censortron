# Censortron
Mighty and flexible content moderation framework

```

   ██████╗ ███████╗███████╗██╗    ██╗ █████╗ ██████╗ ███╗   ██╗
  ██╔════╝ ██╔════╝██╔════╝██║    ██║██╔══██╗██╔══██╗████╗  ██║
  ██║  ███╗█████╗  █████╗  ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║
  ██║   ██║██╔══╝  ██╔══╝  ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║
  ╚██████╔╝███████╗██║     ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║
   ╚═════╝ ╚══════╝╚═╝      ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
```
--

> [!NOTE]
> Status: code base +/- ready, but implemented into another ready pipeline.
>
> TODO: extract to this repo, clean the code; prepare for non-docker user. Make more customizeable.


## 🔥⚠️Content Warning
**Important Notice Regarding Repository Content**  
This framework contains explicit language examples and moderation patterns that include:

- **Profanity** (both explicit and masked variations)
- **Offensive terminology** 
- **Sensitive lexical patterns** 

---

Features:
- simple and robust regex-based banword moderation
- multiple moderation layers
- enhanced overcensoring control
- Docker-ready FastAPI endpoint

Moderation layers (customizeable):
- regex-based
- LLM classification: BERT, sensitive topics
- LLM classification: BERT, overall acceptablity
- Mistral moderation API support


## ⚙️ Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```


####  Run in development mode
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

The application will be accessible at http://localhost:22230.


###  Customization
You can customize the moderation layers by modifying the following files:

Regex-based Moderation : Update the rules in src/regex_censure.py.
Language-specific Rules : Modify the files in src/censure/lang/ (e.g., ru.py, en.py) to adjust language-specific moderation logic.
LLM Classification : Adjust the models or parameters in src/filter_service.py.




## ⚖️ License Notice
> [!NOTE]
> **Important Legal Information**  
This repository contains partial code and may include components from py-censure, which is licensed under the GNU General Public License, Version 3. Please refer to the GNU GPL v3 for details on usage and distribution.

**Dual-License Components**  
Some modules may operate under different licenses. Always check individual file headers and documentation.

**Disclaimer**:  
The maintainers are not liable for license compliance issues. Users assume full responsibility for understanding and adhering to all applicable licenses.

### How to contribute:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Open pull request
