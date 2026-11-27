# Inbox — manual inputs while the CRM and CMS are staged

Drop exports here. The loops read them, then you may delete them.

| File | Purpose | Required columns |
|---|---|---|
| `leads-YYYY-MM-DD.csv` | CRM lead export | `lead_id, created_at, source, name, company, country, email, message, utm_campaign` |
| `cms-inventory.csv` | page inventory | `url, title, target_keyword, status, last_updated` |
| `analytics-YYYY-MM-DD.csv` | site analytics export | `page, sessions, conversions, date` |

**PII rule:** these files may contain personal data. They are gitignored. Never copy their contents
into `knowledge/`, `docs/`, or any outbound artefact. Delete after the run.
