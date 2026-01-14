# rpg-platform

API-first Role Playing Game Platform built with Flask and modular decision logic.

This project is a professional refactor of a legacy RPG web application into a clean, scalable, API-driven backend, designed as a foundation for decision engines, simulations, and future SaaS platforms.

---

## Project Purpose

The goal of rpg-platform is not to build a simple game.

It is designed as:

- a backend platform for RPG-style decision systems
- a technical laboratory for clean architecture and refactoring
- a portfolio-grade project showing senior-level backend design
- a base for future commercial and pro versions (private engine core)

The RPG domain is used as a metaphor for decision-based workflows.

---

## Key Concepts

- API-first architecture
- Clear separation of concerns
- Domain-driven design principles
- Stateless backend
- Frontend-agnostic (React, mobile, CLI, etc.)
- Ready for cloud deployment (Render, Docker, Gunicorn)

---

## Architecture Overview

```

Client (React / Web / Mobile)
↓
REST JSON API
↓
rpg-platform (Flask)
↓
Domain / Services / Repositories

```

The frontend never accesses game logic directly.  
All interactions go through HTTP APIs.

---

## Project Structure

```

rpg-platform/
│
├── server.py              # Application entrypoint
├── config.py              # Global configuration
├── requirements.txt
│
├── core_app/
│   ├── __init__.py        # Flask application factory
│   │
│   ├── api/               # HTTP API layer (Blueprints)
│   │   └── ping_api.py
│   │
│   ├── domain/            # Domain models (pure logic)
│   │
│   ├── services/          # Use cases / business workflows
│   │
│   └── repositories/      # Data access layer
│
└── data/                  # Runtime data (JSON, DB, etc.)

```

---

## Public vs Private Code

This repository contains only the public API platform.

Core game logic (rules, combat algorithms, scoring, AI, simulations) is intended to live in a separate private repository:

```

rpg-engine-core (private)

````

The platform communicates with the engine through adapters or imports, keeping proprietary logic hidden.

---

## Getting Started (Local Development)

### 1. Create virtual environment

```bash
python -m venv venv
````

Activate it:

Windows

```powershell
.\venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the API server

```bash
flask --app server run
```

The server will start on:

```
http://127.0.0.1:5000
```

---

### 4. Test API

Example endpoint:

```
GET /api/ping
```

Response:

```json
{
  "status": "ok",
  "message": "RPG Platform API is running"
}
```

---

## Testing Strategy

* APIs can be tested locally using:

  * Postman
  * curl
  * VS Code REST Client
* No frontend is required to validate backend behavior.

---

## Deployment

The project is designed to be deployed as a stateless API service.

Typical production command:

```bash
gunicorn server:flask_app
```

Compatible with:

* Render
* Docker
* Kubernetes
* Any WSGI-based platform

---

## Roadmap

* Character API
* Inventory API
* Battle and simulation API
* Mission and decision flows
* Token-based authentication
* React frontend client
* Pro version with private engine core

---

## License

This repository contains platform code only.
Game logic and advanced decision engines are proprietary and not included.

---

## Author

Built as part of a professional backend engineering and refactoring portfolio.


