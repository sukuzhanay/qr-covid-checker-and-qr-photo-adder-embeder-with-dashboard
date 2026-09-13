# QR Covid Platform
## Distributed Health Credential Verification & Analytics System

### QR Certificate Processing, Photo Embedding & Vaccination Dashboard

**Academic Engineering Project · Technical & Academic Direction · Distributed Systems / Cloud / Data**

![Academic project](https://img.shields.io/badge/Project-Academic-08111f?style=flat-square)
![Python](https://img.shields.io/badge/Python-Streamlit-08111f?style=flat-square&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Cloud-Firebase-f59e0b?style=flat-square&logo=firebase&logoColor=white)
![Dashboard](https://img.shields.io/badge/Data-Dashboard-08111f?style=flat-square&logo=plotly&logoColor=white)

A collaborative final project for **Programación Concurrente y Distribuida (Concurrent and Distributed Programming)** at **Universidad Europea**. Student teams connected QR processing, photo embedding, cloud persistence and analytical views in a Python application under the academic and technical direction of **Christian Vladimir Sucuzhanay Arévalo**.

[Overview](#overview) · [Architecture](#system-architecture--data-flow) · [Stack](#technology-stack) · [Team](#academic-collaboration--team-structure) · [Getting Started](#getting-started)

---

## Overview

QrCovid explores a university vaccination-dashboard use case through three connected workflows:

- Read a QR payload from an image or camera and decode HC1 vaccination data.
- Generate a QR image with a photograph overlaid at its centre.
- Store records and generated images in Firebase, then display vaccination summaries in Streamlit.

The repository preserves an academic prototype and its development experiments. **HC1 prefix checks and payload decoding do not establish certificate authenticity.** The inspected Python flow does not verify cryptographic signatures or certificate trust, and photo embedding does not establish a person's identity.

## System Architecture / Data Flow

```text
                    Streamlit UI · prueba.py
                         │           │
                  Firebase Auth      │
                                     ▼
Image / camera ──► QR reading · crearQr.py
                         │
                    HC1 payload
                         │
              ┌──────────┴─────────────┐
              ▼                        ▼
    Photo overlay + QR image    Base45 → zlib → CBOR
         crearQr.py                hc1_decode.py
              │                        │
              ▼                  ┌─────┴──────────┐
       Firebase Storage          ▼                ▼
       Generated QR images   JSON in Storage   Realtime Database
                                              Usuarios records
                                                   │
                                                   ▼
                                            main.py dashboard
                                            Plotly + Altair
```

This flow follows the calls in [`prueba.py`](prueba.py), [`crearQr.py`](crearQr.py), [`hc1_decode.py`](hc1_decode.py) and [`main.py`](main.py). The camera branch has integration gaps described below.

<details>
<summary>Original academic workflow illustration</summary>

![Original QrCovid workflow mockup: certificate, login and photo-embedded QR](https://raw.githubusercontent.com/sukuzhanay/qr-covid-checker-and-qr-photo-adder-embeder-with-dashboard/18ec9cf4f9add5ba235ba351863099bfdaba8798/qrcovid.drawio.png)

The original `qrcovid.drawio.png` is preserved here through its historical commit because it is absent from the current tree. It is a design mockup; its validation symbols and mobile screens are not evidence of verified certificate authenticity or a native mobile application.

</details>

## Core Capabilities

| Capability | Repository evidence |
|---|---|
| QR reading | `crearQr.py` uses OpenCV and pyzbar for saved-image and camera input. |
| Photo embedding | `crearQr.py` generates a QR with high error correction and overlays a photo using Pillow. Readability after embedding is not validated by this documentation update. |
| HC1 decoding | `hc1_decode.py` removes the HC1 prefix, decodes Base45, decompresses with zlib and extracts CBOR vaccination fields. |
| Account access | `prueba.py` contains Firebase email/password registration and sign-in through Pyrebase. |
| Cloud persistence | Generated QR images and decoded JSON are uploaded to Storage; vaccination records are written to Realtime Database. |
| Existing-record checks | `hc1_decode.py` searches stored vaccination identifiers and updates a matching record or inserts one under the user ID. |
| Dashboard | `main.py` contains vaccine-type, dose-completion, elapsed-time and vaccination-month summaries using Plotly, Altair and pandas. |

## Technology Stack

| Layer | Technologies and scope |
|---|---|
| Application | Python · Streamlit |
| Image input and processing | OpenCV · pyzbar · qrcode · Pillow · Tkinter |
| Certificate payload decoding | Base45 · zlib · cbor2 |
| Cloud integration | Pyrebase · Firebase Authentication · Realtime Database · Storage |
| Data and visualization | pandas · Plotly · Altair |
| Exploration | Jupyter notebooks · IPython |
| Historical integration assignment | JavaScript / Node.js / Pathcheck, credited in the original README; no standalone JavaScript implementation or Node.js manifest is present in the current tree. |

## Engineering Scope

The project brings together **application integration, data transformation, cloud services and visualization** within a team-based university assignment. Its distributed-systems context is reflected in the interaction between the local Python application and remote Firebase services.

The repository supports discussion of module boundaries, shared data structures and integration across team responsibilities. It does not establish a dedicated concurrency implementation, measured scalability, production operation or formal security validation. The database sanitization and HC1 endpoint responsibilities below preserve the original team assignments; they are not claims of comprehensive sanitization or a deployed endpoint.

## Academic Collaboration / Team Structure

Credits and group responsibilities are preserved from the original README.

| Contributor | Role | Original responsibility |
|---|---|---|
| **Christian Vladimir Sucuzhanay Arévalo** | Professor · Academic & Technical Director | Course supervision and academic/technical direction |
| **Carlos Moreno** | Group 1 lead | Dashboard data |
| **Camilo Quiroz** | Group 2 lead | Pathcheck / Node.js |
| **Jolie Alain** | Group 3 lead | QR photo embedding / UI / authentication |
| **Maria Rodriguez** | Group 4 lead | Database design / storage / sanitization / existing-user checks |
| **Santiago Barreiro** | Group 5 lead | HC1-to-endpoint integration |

**Student implementation is credited to the collaborating teams.** Christian's role is academic and technical direction, not exclusive authorship of their work.

## Project Structure

```text
.
├── prueba.py                 # Original documented Streamlit entry point
├── main.py                   # Firebase-backed dashboard functions
├── crearQr.py                # QR reading, generation and photo overlay
├── camara2.py                # Streamlit camera experiment used by the entry point
├── hc1_decode.py             # HC1 decoding and Firebase persistence
├── Hc1_DB.py                 # Earlier database/decoder variant
├── CodigoQRlogo.py           # Standalone QR image-overlay implementation
├── login.py                  # Login development script
├── camara.py                 # Camera development script
├── explorer.py               # File-dialog experiment
├── estado_vacunacion.py      # Vaccination-status development script
├── periodo_vacunacion.py     # Vaccination-period development script
├── vacunas_dosis.py          # Vaccine/dose development script
├── busquedaFoto_QR.ipynb      # QR/photo exploration notebook
├── pedirQrPorCamara.ipynb     # Camera/QR exploration notebook
├── tiempo_medio.png          # Historical dashboard image
├── periodo_vacunacion.png    # Historical dashboard image
├── resultado2.PNG            # Historical result image
└── README.md
```

## Getting Started

**Historical reproduction requires environment and integration work.** No dependency manifest or lockfile is included, and execution was not revalidated for this documentation update.

1. Clone the repository and create an isolated Python environment:

   ```bash
   git clone https://github.com/sukuzhanay/qr-covid-checker-and-qr-photo-adder-embeder-with-dashboard.git
   cd qr-covid-checker-and-qr-photo-adder-embeder-with-dashboard
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Review the imports in the five files identified by the original README: `prueba.py`, `main.py`, `crearQr.py`, `camara2.py` and `hc1_decode.py`. Keep these files together. In addition to the stack above, their imports include NumPy, Pygments and Requests. Resolve compatible package versions; the code uses legacy APIs such as `Image.ANTIALIAS`. Camera and file-dialog paths require a local graphical environment, Tkinter, a camera and the native library required by pyzbar.

3. Before execution, prepare an isolated Firebase project with Authentication, Realtime Database and Storage, and review the hard-coded configuration in the source. `main.py` attempts sign-in at import time using embedded historical credentials. Do not reuse those credentials or the original backend. The decoder expects `archivos/vacunas.json`, `archivos/Fabricante.json` and `archivos/profilaxis.json` in Storage; these lookup files are not included in the repository. Use synthetic records for reproduction.

4. After resolving configuration, dependencies and the integration gaps below, the original launch command is:

   ```bash
   streamlit run prueba.py
   ```

The UI contains **Entrar/Registrar** (sign-in/registration), **Home** (dashboard) and **Ajustes** (QR workflows).

**Known integration gaps:** `prueba.py` calls `camara2.hacerFotoCara()`, which is not defined in `camara2.py`. Its camera branch also calls `BBDD().decode(hc1)` without the required `localId` argument and expects `fotoCara.png`, while `camara2.py` writes `fotoPersona.png`. These functional issues remain unchanged. The original README identifies the other scripts as development material rather than additional application entry points.

## Legacy / Context Note

QrCovid is a historical educational project about COVID-era QR data and vaccination dashboards. It makes no claim about current certificate acceptance, operational availability, clinical suitability or production readiness. Dashboard calculations describe the prototype's stored records and rules; they are not validated public-health metrics.

The original README referenced [Pathcheck](https://github.pathcheck.org/verify.html#processed) for verification. That historical reference and the group assignment are retained as context; current service availability and integration are not established here.

## Related Work & Professional Identity

This collaborative teaching project illustrates the **Former University Lecturer** dimension of Christian's professional background: guiding student teams across application, cloud and data components.

Explore [eBurnout](https://github.com/sukuzhanay/eburnout) for related historical engineering work and the [technical portfolio](https://sukuzhanay.github.io/) for broader project context. The professional headline below describes Christian's current identity; it does not attribute AWS, generative AI or machine learning capabilities to QrCovid.

---

## Academic & Technical Direction

**Christian Vladimir Sucuzhanay Arévalo**

Data & AI Solutions Architect | AWS Data Architecture | Generative AI & Amazon Bedrock | Big Data | Former University Lecturer

[![Website](https://img.shields.io/badge/Website-Entity_Home-08111f?style=flat-square)](https://christiansucuzhanay.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-08111f?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyBmaWxsPSJ3aGl0ZSIgcm9sZT0iaW1nIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI%2BPHRpdGxlPkxpbmtlZEluPC90aXRsZT48cGF0aCBkPSJNMjAuNDQ3IDIwLjQ1MmgtMy41NTR2LTUuNTY5YzAtMS4zMjgtLjAyNy0zLjAzNy0xLjg1Mi0zLjAzNy0xLjg1MyAwLTIuMTM2IDEuNDQ1LTIuMTM2IDIuOTM5djUuNjY3SDkuMzUxVjloMy40MTR2MS41NjFoLjA0NmMuNDc3LS45IDEuNjM3LTEuODUgMy4zNy0xLjg1IDMuNjAxIDAgNC4yNjcgMi4zNyA0LjI2NyA1LjQ1NXY2LjI4NnpNNS4zMzcgNy40MzNjLTEuMTQ0IDAtMi4wNjMtLjkyNi0yLjA2My0yLjA2NSAwLTEuMTM4LjkyLTIuMDYzIDIuMDYzLTIuMDYzIDEuMTQgMCAyLjA2NC45MjUgMi4wNjQgMi4wNjMgMCAxLjEzOS0uOTI1IDIuMDY1LTIuMDY0IDIuMDY1em0xLjc4MiAxMy4wMTlIMy41NTVWOWgzLjU2NHYxMS40NTJ6TTIyLjIyNSAwSDEuNzcxQy43OTIgMCAwIC43NzQgMCAxLjcyOXYyMC41NDJDMCAyMy4yMjcuNzkyIDI0IDEuNzcxIDI0aDIwLjQ1MUMyMy4yIDI0IDI0IDIzLjIyNyAyNCAyMi4yNzFWMS43MjlDMjQgLjc3NCAyMy4yIDAgMjIuMjIyIDBoLjAwM3oiLz48L3N2Zz4%3D)](https://www.linkedin.com/in/sucuzhanay)
[![AWS Builder](https://img.shields.io/badge/AWS-Builder-f59e0b?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyBmaWxsPSJ3aGl0ZSIgcm9sZT0iaW1nIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI%2BPHRpdGxlPkFtYXpvbiBBV1M8L3RpdGxlPjxwYXRoIGQ9Ik02Ljc2MyAxMC4wMzZjMCAuMjk2LjAzMi41MzUuMDg4LjcxLjA2NC4xNzYuMTQ0LjM2OC4yNTYuNTc2LjA0LjA2My4wNTYuMTI3LjA1Ni4xODMgMCAuMDgtLjA0OC4xNi0uMTUyLjI0bC0uNTAzLjMzNWEuMzgzLjM4MyAwIDAgMS0uMjA4LjA3MmMtLjA4IDAtLjE2LS4wNC0uMjM5LS4xMTJhMi40NyAyLjQ3IDAgMCAxLS4yODctLjM3NSA2LjE4IDYuMTggMCAwIDEtLjI0OC0uNDcxYy0uNjIyLjczNC0xLjQwNSAxLjEwMS0yLjM0NyAxLjEwMS0uNjcgMC0xLjIwNS0uMTkxLTEuNTk2LS41NzQtLjM5MS0uMzg0LS41OS0uODk0LS41OS0xLjUzMyAwLS42NzguMjM5LTEuMjMuNzI2LTEuNjQ0LjQ4Ny0uNDE1IDEuMTMzLS42MjMgMS45NTUtLjYyMy4yNzIgMCAuNTUxLjAyNC44NDYuMDY0LjI5Ni4wNC42LjEwNC45MTguMTc2di0uNTgzYzAtLjYwNy0uMTI3LTEuMDMtLjM3NS0xLjI3Ny0uMjU1LS4yNDgtLjY4Ni0uMzY3LTEuMy0uMzY3LS4yOCAwLS41NjguMDMxLS44NjMuMTAzLS4yOTUuMDcyLS41ODMuMTYtLjg2Mi4yNzJhMi4yODcgMi4yODcgMCAwIDEtLjI4LjEwNC40ODguNDg4IDAgMCAxLS4xMjcuMDIzYy0uMTEyIDAtLjE2OC0uMDgtLjE2OC0uMjQ3di0uMzkxYzAtLjEyOC4wMTYtLjIyNC4wNTYtLjI4YS41OTcuNTk3IDAgMCAxIC4yMjQtLjE2N2MuMjc5LS4xNDQuNjE0LS4yNjQgMS4wMDUtLjM2YTQuODQgNC44NCAwIDAgMSAxLjI0Ni0uMTUxYy45NSAwIDEuNjQ0LjIxNiAyLjA5MS42NDcuNDM5LjQzLjY2MiAxLjA4NS42NjIgMS45NjN2Mi41ODZ6bS0zLjI0IDEuMjE0Yy4yNjMgMCAuNTM0LS4wNDguODIyLS4xNDQuMjg3LS4wOTYuNTQzLS4yNzEuNzU4LS41MS4xMjgtLjE1Mi4yMjQtLjMyLjI3Mi0uNTEyLjA0Ny0uMTkxLjA4LS40MjMuMDgtLjY5NHYtLjMzNWE2LjY2IDYuNjYgMCAwIDAtLjczNS0uMTM2IDYuMDIgNi4wMiAwIDAgMC0uNzUtLjA0OGMtLjUzNSAwLS45MjYuMTA0LTEuMTkuMzItLjI2My4yMTUtLjM5LjUxOC0uMzkuOTE3IDAgLjM3NS4wOTUuNjU1LjI5NS44NDYuMTkxLjIuNDcuMjk2LjgzOC4yOTZ6bTYuNDEuODYyYy0uMTQ0IDAtLjI0LS4wMjQtLjMwNC0uMDgtLjA2NC0uMDQ4LS4xMi0uMTYtLjE2OC0uMzExTDcuNTg2IDUuNTVhMS4zOTggMS4zOTggMCAwIDEtLjA3Mi0uMzJjMC0uMTI4LjA2NC0uMi4xOTEtLjJoLjc4M2MuMTUxIDAgLjI1NS4wMjUuMzEuMDguMDY1LjA0OC4xMTMuMTYuMTYuMzEybDEuMzQyIDUuMjg0IDEuMjQ1LTUuMjg0Yy4wNC0uMTYuMDg4LS4yNjQuMTUxLS4zMTJhLjU0OS41NDkgMCAwIDEgLjMyLS4wOGguNjM4Yy4xNTIgMCAuMjU2LjAyNS4zMi4wOC4wNjMuMDQ4LjEyLjE2LjE1MS4zMTJsMS4yNjEgNS4zNDggMS4zODEtNS4zNDhjLjA0OC0uMTYuMTA0LS4yNjQuMTYtLjMxMmEuNTIuNTIgMCAwIDEgLjMxMS0uMDhoLjc0M2MuMTI3IDAgLjIuMDY1LjIuMiAwIC4wNC0uMDA5LjA4LS4wMTcuMTI4YTEuMTM3IDEuMTM3IDAgMCAxLS4wNTYuMmwtMS45MjMgNi4xN2MtLjA0OC4xNi0uMTA0LjI2My0uMTY4LjMxMWEuNTEuNTEgMCAwIDEtLjMwMy4wOGgtLjY4N2MtLjE1MSAwLS4yNTUtLjAyNC0uMzItLjA4LS4wNjMtLjA1Ni0uMTE5LS4xNi0uMTUtLjMybC0xLjIzOC01LjE0OC0xLjIzIDUuMTRjLS4wNC4xNi0uMDg3LjI2NC0uMTUuMzItLjA2NS4wNTYtLjE3Ny4wOC0uMzIuMDh6bTEwLjI1Ni4yMTVjLS40MTUgMC0uODMtLjA0OC0xLjIyOS0uMTQzLS4zOTktLjA5Ni0uNzEtLjItLjkxOC0uMzItLjEyOC0uMDcxLS4yMTUtLjE1MS0uMjQ3LS4yMjNhLjU2My41NjMgMCAwIDEtLjA0OC0uMjI0di0uNDA3YzAtLjE2Ny4wNjQtLjI0Ny4xODMtLjI0Ny4wNDggMCAuMDk2LjAwOC4xNDQuMDI0LjA0OC4wMTYuMTIuMDQ4LjIuMDguMjcxLjEyLjU2Ni4yMTUuODc4LjI3OS4zMTkuMDY0LjYzLjA5Ni45NS4wOTYuNTAyIDAgLjg5NC0uMDg4IDEuMTY1LS4yNjRhLjg2Ljg2IDAgMCAwIC40MTUtLjc1OC43NzcuNzc3IDAgMCAwLS4yMTUtLjU1OWMtLjE0NC0uMTUxLS40MTYtLjI4Ny0uODA3LS40MTVsLTEuMTU3LS4zNmMtLjU4My0uMTgzLTEuMDE0LS40NTQtMS4yNzctLjgxM2ExLjkwMiAxLjkwMiAwIDAgMS0uNC0xLjE1OGMwLS4zMzUuMDczLS42My4yMTYtLjg4Ni4xNDQtLjI1NS4zMzUtLjQ3OS41NzUtLjY1NC4yNC0uMTg0LjUxLS4zMi44My0uNDE1LjMyLS4wOTYuNjU1LS4xMzYgMS4wMDYtLjEzNi4xNzUgMCAuMzU5LjAwOC41MzUuMDMyLjE4My4wMjQuMzUuMDU2LjUxOC4wODguMTYuMDQuMzEyLjA4LjQ1NS4xMjcuMTQ0LjA0OC4yNTYuMDk2LjMzNi4xNDRhLjY5LjY5IDAgMCAxIC4yNC4yLjQzLjQzIDAgMCAxIC4wNzEuMjYzdi4zNzVjMCAuMTY4LS4wNjQuMjU2LS4xODQuMjU2YS44My44MyAwIDAgMS0uMzAzLS4wOTYgMy42NTIgMy42NTIgMCAwIDAtMS41MzItLjMxMWMtLjQ1NSAwLS44MTUuMDcxLTEuMDYyLjIyMy0uMjQ4LjE1Mi0uMzc1LjM4My0uMzc1LjcxIDAgLjIyNC4wOC40MTYuMjQuNTY3LjE1OS4xNTIuNDU0LjMwNC44NzcuNDRsMS4xMzQuMzU4Yy41NzQuMTg0Ljk5LjQ0IDEuMjM3Ljc2Ny4yNDcuMzI3LjM2Ny43MDIuMzY3IDEuMTE3IDAgLjM0My0uMDcyLjY1NS0uMjA3LjkyNi0uMTQ0LjI3Mi0uMzM2LjUxMS0uNTgzLjcwMy0uMjQ4LjItLjU0My4zNDMtLjg4Ni40NDctLjM2LjExMS0uNzM0LjE2Ny0xLjE0Mi4xNjd6TTIxLjY5OCAxNi4yMDdjLTIuNjI2IDEuOTQtNi40NDIgMi45NjktOS43MjIgMi45NjktNC41OTggMC04Ljc0LTEuNy0xMS44Ny00LjUyNi0uMjQ3LS4yMjMtLjAyNC0uNTI3LjI3Mi0uMzUxIDMuMzg0IDEuOTYzIDcuNTU5IDMuMTUzIDExLjg3NyAzLjE1MyAyLjkxNCAwIDYuMTE0LS42MDcgOS4wNi0xLjg1Mi40MzktLjIuODE0LjI4Ny4zODMuNjA3ek0yMi43OTIgMTQuOTYxYy0uMzM2LS40My0yLjIyLS4yMDctMy4wNzQtLjEwMy0uMjU1LjAzMi0uMjk1LS4xOTItLjA2My0uMzYgMS41LTEuMDUzIDMuOTY3LS43NSA0LjI1NC0uMzk5LjI4Ny4zNi0uMDggMi44MjYtMS40ODUgNC4wMDctLjIxNS4xODQtLjQyMy4wODgtLjMyNy0uMTUxLjMyLS43OSAxLjAzLTIuNTcuNjk1LTIuOTk0eiIvPjwvc3ZnPg%3D%3D)](https://builder.aws.com/community/@sukuzhanay)
[![GitHub](https://img.shields.io/badge/GitHub-08111f?style=flat-square&logo=github&logoColor=white)](https://github.com/sukuzhanay)

[Technical Portfolio](https://sukuzhanay.github.io/)

**Build. Explain. Teach. Share.**
