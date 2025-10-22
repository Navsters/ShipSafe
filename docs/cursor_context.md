🧭 Cursor Context — ShipSafe (Automated Release Governance System)

👤 Personal Context

- Location: California, USA
- Background: 5 years of experience as a Project / Program Manager in IT and biotech, leading system implementations, compliance initiatives, and software rollouts.
- Certifications: PMP (Project Management Professional), CCNA (Cisco Certified Network Associate).
- Technical level: Intermediate — solid in Python, basic understanding of web frameworks and frontend concepts, familiar with VS Code, now using Cursor for AI-assisted coding.
- Goal: Transition into a Technical Program Manager / Compliance-Release Manager role at a top-tier tech company (Google-level) with a target base salary of $160 – $180 K.
- Learning goal: Build real software systems that demonstrate technical fluency, risk and compliance automation, and systems thinking — not just project coordination.

🚀 Project Overview — ShipSafe

- Tagline: Automating trust in software delivery.

Concept:
ShipSafe simulates a software release governance platform that enforces company compliance and security policies automatically before code is deployed. Developers submit release requests; ShipSafe runs rule-based checks, determines risk level, and routes the release through approval workflows. All actions are recorded for audit visibility.

🎯 Why This Project Matters

- Demonstrates understanding of CI/CD workflows, compliance, and automation.
- Bridges your management and technical backgrounds — you’re both the architect and implementer.
- Portfolio-ready example showing leadership in technical process automation.
- Fits directly with TPM/ITPM skill sets sought at Google, Meta, Amazon, and large SaaS companies.

🧱 Architecture Overview

- Backend: Python + FastAPI
- Frontend: React (Vite or CRA)
- Database: SQLite for simplicity
- Hosting: Railway or Render (free tier)
- Auth: mock roles (Developer / Approver)
- Policy Engine: Python logic simulating security and compliance checks
- Audit Trail: SQLite table logging all user actions

Data Flow

Developer → Submit Release
        ↓
Policy Engine → runs simulated checks
        ↓
Workflow → auto-approve or send to Approver
        ↓
Approver approves/rejects → Audit Log entry

⚙️ MVP Scope (1–2 weeks)

Core Features

- Submit new release request.
- Run mock “security” and “compliance” rules.
- Auto-approve low-risk; require manual approval for high-risk.
- Approver can approve/reject.
- Every action stored in AuditLog.
- Dashboard showing releases, policy results, and status.

Stretch Goals

- Role-based access (JWT or sessions).
- Simulated Slack/email notifications.
- Analytics: approvals per month, average lead time.

🧩 Example Entities

Table  | Key Fields
------ | --------------------------------------------
ReleaseRequest | id, name, version, risk_level, status, created_at
PolicyResult   | id, release_id, passed, message
Approval       | id, release_id, approver, decision, timestamp
AuditLog       | id, actor, action, release_id, timestamp

🧠 Mock Policy Logic

```python
if release.version.endswith(".0"):
    risk_level = "high"
else:
    risk_level = "low"

if "vuln" in release.name.lower():
    passed = False
else:
    passed = True
```

Display results:

- ✅ No critical vulnerabilities found — auto-approved.
- ⚠️ Policy failed — routed for manual review.

📁 Project Structure

```
shipsafe/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   │   ├── releases.py
│   │   ├── approvals.py
│   │   └── audit.py
│   └── policy_engine.py
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── api/
│   └── package.json
└── README.md
```

🪜 Development Plan

Phase | Deliverables | Est. Time
----- | ------------ | ---------
1 | FastAPI + SQLite setup, models & endpoints | 1–2 days
2 | Mock policy engine & routing logic | 1–2 days
3 | React UI (submit, view, approve) | 3–4 days
4 | Audit view & deployment | 1 day
5 | Docs + short demo video | 1–2 days

≈ 30–40 hours total for a polished MVP.

🧰 Suggested Cursor Prompts

1. Backend scaffold
   - Generate FastAPI app using SQLite with models for ReleaseRequest, Approval, and AuditLog.
2. Policy checker
   - Write a FastAPI function that evaluates 2–3 fake compliance rules and returns pass/fail.
3. Audit log
   - Every approval or rejection writes actor, action, release_id, timestamp to AuditLog.
4. Frontend
   - React page with form to submit new release and table showing all releases + status.
5. Deploy
   - Create Dockerfile + Railway config to deploy backend/frontend together.

💼 Portfolio Presentation

Project Title: ShipSafe – Automated Release Governance System

Summary:
Built a simulated release governance platform that automates policy checks, risk scoring, and approvals to ensure compliant software delivery. Demonstrates knowledge of CI/CD pipelines, security governance, and process automation.

Show:

- Screenshots or 90-second video walkthrough.
- Architecture diagram.
- README explanation of “Phase 2: Real integrations (Snyk, Trivy, GitHub).”

🧭 Phase 2 Vision

When ready to expand:

- Integrate a real vulnerability-scan API (Snyk or Trivy).
- Add Open Policy Agent (OPA) for dynamic rules.
- Connect to GitHub Actions or Jenkins webhooks.
- Implement OAuth2 login for multi-user teams.

In Cursor you can re-initialize context anytime by saying:

“@cursor load context from /docs/cursor_context.md and continue from where we left off on ShipSafe.”

---

Collaboration Contract

- You drive; I advise. I will not auto-generate large code edits unless explicitly asked. I focus on options, tradeoffs, rationale, and interview-ready explanations.
- Depth and clarity: I will expand acronyms, define terms, and explain logic, syntax, purpose, broader architecture, and alternatives at each step.
- Learning-first cadence: UI-first instructions where possible (e.g., “create a new file”), minimal shell commands, and gentle troubleshooting.
- Decision capture: I’ll append key decisions and rationales here so you can reload context.

Working Rules

- Keep `docs/cursor_context.md` tracked for now; we can scrub history later using `git filter-repo` or BFG.
- Prefer simple, testable increments (health endpoint → DB setup → first entity → policy engine → approvals → audit logging → UI).
- Use SQLite for development (zero setup). Consider PostgreSQL in Phase 2 with migrations (Alembic).
- Choose an ORM per phase goals; explain tradeoffs clearly (SQLModel vs SQLAlchemy ORM/Core).

Decisions So Far

- Runtime: Python 3.11, FastAPI (ASGI web framework), Uvicorn (ASGI server).
- Folder layout adopted: `backend/main.py` with future `routes/`, `models.py`, `schemas.py`, `policy_engine.py`.
- Health endpoint verified: `GET /health -> {"status":"ok"}`.
- Editor setup pitfalls documented (Windows Store Python vs `.venv`), plus remedies (explicit interpreter path, `python -m` execution).

Acronym and Term Glossary

- API (Application Programming Interface): The set of HTTP endpoints your frontend or tools call.
- ASGI (Asynchronous Server Gateway Interface): Modern Python web server interface; FastAPI runs on ASGI servers like Uvicorn.
- ORM (Object-Relational Mapper): Maps Python classes/objects to SQL tables/rows (e.g., SQLAlchemy ORM, SQLModel uses it under the hood).
- SQL (Structured Query Language): Language used to interact with relational databases.
- SQLite: File-backed relational database; great for local development and MVPs.
- OpenAPI: Machine-readable specification for REST APIs used to auto-generate docs (`/docs`).
- MVP (Minimum Viable Product): smallest useful version to validate value and demonstrate concepts.
- Alembic: Database migration tool commonly used with SQLAlchemy.

Time/Complexity Guidance (MVP-scale)

- Database: SQLite vs PostgreSQL — SQLite is zero-ops; PostgreSQL adds ~1–2 hours setup and config.
- ORM choice: SQLModel vs SQLAlchemy ORM — SQLModel often saves ~1.5–2.5 hours for a 3–4 table MVP by reducing boilerplate; SQLAlchemy ORM is more explicit and standard at scale.

---

## 📍 CURRENT PROJECT STATUS (Last Updated: Desktop Setup Session)

### ✅ COMPLETED
- **Environment Setup**: Python 3.11, virtual environment (.venv) created
- **Dependencies Installed**: FastAPI 0.119.1, SQLAlchemy 2.0.44, Uvicorn 0.38.0, Pydantic 2.12.3
- **Basic FastAPI App**: Health endpoint working (`GET /health` returns `{"status":"ok"}`)
- **Database Models**: SQLAlchemy models defined in `backend/models.py` (ReleaseRequests table)
- **Database Config**: SQLite setup in `backend/db.py`
- **Project Structure**: Backend folder with main.py, models.py, db.py
- **Git Setup**: .gitignore configured, requirements.txt generated, committed to GitHub
- **Code Issues Fixed**: Fixed typos in models.py (DateTime, default) and db.py (autoflush=False)

### 🔧 CURRENT STATE
- **Phase**: Phase 1 - FastAPI + SQLite setup (IN PROGRESS)
- **Working Directory**: `C:\Users\Navneet\Documents\ShipSafe Dev Application\ShipSafe`
- **Virtual Environment**: Created but activation has PowerShell execution policy issues
- **API Status**: Basic FastAPI app running on http://127.0.0.1:8000
- **Database**: SQLite configured but tables not yet created
- **Next Logical Step**: Create database tables and add CRUD endpoints for release requests

### 🎯 IMMEDIATE NEXT STEPS
1. **Database Initialization**: Create database tables from models
2. **CRUD Endpoints**: Add POST/GET endpoints for release requests
3. **Policy Engine**: Implement mock compliance rules
4. **Test Endpoints**: Verify API functionality

### 🚧 KNOWN ISSUES
- Virtual environment activation blocked by PowerShell execution policy
- Using `python -m uvicorn` instead of direct `uvicorn` command due to PATH issues
- Database tables not yet created (need to run Base.metadata.create_all())

### 🔧 POWERSHELL EXECUTION POLICY FIX (for both devices)
**Problem**: `.\.venv\Scripts\Activate.ps1` fails with "running scripts is disabled"
**Solution**: Run this command once per machine:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
**Alternative**: Use batch file instead: `.\.venv\Scripts\activate.bat`
**Verify**: After activation, prompt shows `(.venv)` and `python -c "import sys; print(sys.executable)"` shows `.venv\Scripts\python.exe`

### 📋 DEVELOPMENT NOTES
- Using SQLAlchemy ORM (not SQLModel) as planned
- SQLite database file will be `./shipsafe.db`
- All dependencies properly captured in requirements.txt
- Ready for laptop sync via git pull + pip install -r requirements.txt

### 📚 RECENT LEARNING SESSION
**Terminology Clarified:**
- **CRUD**: Create, Read, Update, Delete operations
- **HTTP Methods**: GET (read), POST (create), PUT/PATCH (update), DELETE (remove)
- **Endpoints**: URLs that API responds to (e.g., GET /releases, POST /releases)
- **ORM**: Object-Relational Mapper - lets you work with databases using Python objects instead of raw SQL
- **Declarative Base**: Special class that gives models database superpowers, handles Python-to-SQL mapping
- **Class Differences**: Regular classes use `__init__` constructor; SQLAlchemy models use `__tablename__` attribute and `Column()` definitions

**Next Session Focus**: Database table creation and CRUD endpoint implementation

