# Censortron
Mighty and flexible content moderation framework

> [!NOTE]
> Status: code base ready, but implemented into another ready pipeline.
>
> TODO: extract to this repo, clean the code; prepare for non-docker user. Make more customizeable.

Features:
- enchanced word banlist: regex-based robust content moderation
- multiple moderation layers
- NO to overcensoring
- Docker-ready, FastAPI endpoint

Moderation layers (customizeable):
- regex-based
- LLM classification: BERT, sensitive topics
- LLM classification: BERT, overall acceptablity
- Mistral moderation API support
