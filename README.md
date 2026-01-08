# FinTech

FinTech is a privacy first payments web app that hides users' real names when they send money, showing only a username to vendors and receivers.

---

## Problem

Many people avoid cashless transactions because their legal name or identifying information is exposed to vendors and recipients. This creates privacy risks, unwanted profiling, and potential safety concerns for users who need to keep their identity protected during everyday transactions.

---

## Proposed Solution

Fin hide allows users to transact without exposing their full legal name. Users register with verified identity data (phone, NIN, BVN, biometrics, email) while the platform displays only a chosen username to vendors or receivers. The system maintains regulatory compliance and transaction traceability internally while protecting user facing identity.

---

## Key Features (MVP)

- **Account Creation & Verification**
    - Register with **phone number**, username, and email.
    - Collect and verify **NIN** and **BVN** for KYC/AML compliance.
    - Optional identity proofing biometrics: **face scan** and **fingerprint** for secure login.
    - Email notifications for welcome and token delivery.
    
- **Privacy-first Display**
    - Hide the user's full legal name; display only the user chosen **username** to vendors and receivers.

- **Payments**
    - Send money to other users or vendors using username or phone number.
    - Receive payments without exposing full name.
    - Buy airtime and data bundles.
    - Pay utility bills (electricity/prepaid meter top-ups).

- **Security & Fraud Controls**
    - Two-factor authentication (phone OTP + biometrics when enabled).
    - Transaction limits, velocity checks, and device fingerprinting.
    - Secure storage of sensitive PII with encryption at rest and in transit.

---

## Privacy & Compliance

- Encrypt all personally identifiable information (PII) including full name, NIN, BVN, email, and biometrics.
- Strict access control and audit trails for PII access.
- Build KYC/AML flows that meet local regulatory requirements (Nigeria - BVN, NIN linkage) and keep logs for compliance.
- Provide clear privacy policy and user consent screens explaining data collection, purpose, and usage.

---

## High-level Architecture

1. **Frontend**: JavaScript (React),  Css (Tailwind); optionally a PWA for mobile like experience.
2. **Backend**: Python (Flask) — handles authentication, KYC workflows, payments orchestration, and business logic.
3. **Database**: PostgreSQL for transactional data. Encrypted store or column level encryption for PII.
4. **Identity & Biometrics**: Vetted third-party provider for face/fingerprint scanning or government APIs.
5. **Payments**: Paystack, Flutterwave, or bank APIs for transfers, airtime, and utilities.
6. **Hosting & Infra**: Dockerized services on AWS/GCP/Azure with KMS for encryption keys.

---

## Data Flow (Simplified)

1. User registers with phone, email, username, NIN, BVN, and consents to biometrics.
2. Backend verifies BVN/NIN via APIs and stores verified status.
3. User funds wallet (via card/bank transfer) or links bank account.
4. When sending money, recipient sees only the sender's **username**; backend records real identity encrypted for compliance.

---

## Security Considerations

- TLS 1.2+ for transport; AES-256 (or equivalent) for data at rest.
- Key management: use a managed KMS; rotate keys regularly.
- Store only biometric templates (not raw images) and encrypt them.
- Rate limiting and behavioral anomaly detection to reduce fraud.
- Penetration testing and regular security audits.

---

## Legal & Ethical Notes

- Hiding a user's legal name increases privacy but does not remove obligations for law enforcement or AML/KYC compliance.  
- Biometric and national ID handling is sensitive — consult legal/compliance experts before collecting.

---

## MVP Roadmap (12 Weeks)

- **Weeks 1–2**: Requirements, architecture, regulatory research, choose identity & payment partners.  
- **Weeks 3–5**: Backend auth, user registration, KYC integration, encrypted PII storage.  
- **Weeks 6–7**: Frontend flows (register/login/send/receive), wallet integration, username masking logic.  
- **Weeks 8–9**: Integrate payments, airtime/data, and utility APIs.  
- **Weeks 10–11**: Biometrics login (optional), security hardening.  
- **Week 12**: QA, penetration testing, legal sign-off, beta launch.

---

## Suggested Tech Stack

- Frontend: React + Bootstrap (PWA optional)  
- Backend: Python + FastAPI/Flask  
- Database: PostgreSQL  
- Payments: Paystack / Flutterwave  
- Identity Verification: Local NIN API or third-party provider  
- Hosting: AWS / GCP + Docker  

---

## Installation (Developer Quickstart)

1. Clone the repo.  
2. Create `.env` with DB credentials, KMS keys, and API keys for payment/identity providers.  
3. Run database migrations (`alembic` or equivalent).  
4. Start backend: `docker-compose up --build`.  
5. Start frontend: `npm install && npm run dev`.

---

## Known Risks & Mitigations

- **Regulatory Exposure**: Mitigation — onboard legal/compliance early and log KYC/transaction activity.  
- **Biometric Theft**: Mitigation — store templates, encrypt, provide fallback login methods.  
- **Vendor Resistance**: Mitigation — optional business accounts with verified receipts showing legal name when required.

---

## Next Steps

1. Finalize regulatory requirements and choose identity/payment partners.  
2. Build a narrow MVP focusing on send/receive + username masking.  
3. Run closed beta with clear opt-in consent and manual KYC checks.

---

## Contact

Project owner: Queen Adebisi product team  
Email: (mailto:adebisiqueen231@gmail.com) 

---

*This README is a product blueprint — pragmatic, compliance aware, and prioritizes user privacy while acknowledging legal realities.*
