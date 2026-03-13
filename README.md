# Multilingual Translation Service

A lightweight multilingual translation service built in Python.
The project implements a reusable translation engine capable of translating text into multiple languages, exposed through a REST API.

The goal of the project is both educational and practical: to learn modern backend architecture while building a service that can evolve into a micro-SaaS or an API product.

# Tech Stack

- Python — core language
- FastAPI — REST API
- CTranslate2 — offline translation engine (MarianMT Models)
- Docker — containerized deployment

# Project Goals

This project has three main goals:

1. Learn modern backend architeture in Python
2. Build a practical service that can be used daily
3. Experiment with micro-SaaS infrastructure and API monetization

This system is being developed incrementally starting with a simple translation engine and gradually evolving into a scalable service.

# Planned Features

Core features:

- Text translation between multiple languages
- Translation into multiple target languages in a single request
- Offline translation using local models
- REST API for programmatic access

Future features:

- Automatic language detection
- Translation of documents (PDF / DOCX)
- Rate limiting and API keys
- API marketplace integration

# System Overview

The project is structured around a reusable translation engine.

Architecture concept:


User / Client

   ↓

API or Bot Interface

  ↓

Translation Service

  ↓

Translation Engine


The translation engine can be reused by different interfaces such as:

- REST API
- Telegram bot
- AI agents via MCP
- External applications

# License

This project is released under the **Creative Commons Attribution-NonCommercial (CC BY-NC 4.0)** license.
