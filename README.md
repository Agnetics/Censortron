# Censortron
Mighty and flexible content moderation framework

`\\add here a mighty transformer pic`

--

> [!NOTE]
> Status: code base ready, but implemented into another ready pipeline.
>
> TODO: extract to this repo, clean the code; prepare for non-docker user. Make more customizeable.

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
