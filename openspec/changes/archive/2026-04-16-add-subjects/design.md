## Context

The repository currently has a Streamlit UI shell with a placeholder "Disciplinas" page, but no subject data model, backend APIs, or real frontend integration. This change introduces subject management as the first academic entity in the app, establishing the foundation for future coursework and task tracking.

## Goals / Non-Goals

**Goals:**
- Introduce a `subjects` capability with persistent backend storage.
- Build a minimal CRUD API surface for subject management.
- Connect the existing Streamlit app to subject data and render the Disciplinas page with real content.

**Non-Goals:**
- Implementing subject-to-task assignment or advanced scheduling features.
- Adding search, filtering, or pagination for subject lists in this iteration.
- Reworking the overall app layout beyond the subject management flow.

## Decisions

- Use a new backend `subjects` resource with fields such as `id`, `name`, `description`, and `active`.
- Add backend endpoints for listing, creating, updating, and deleting subjects.
- Keep the frontend implementation inside `app.py` using Streamlit controls and simple API integration.
- Favor a lightweight, first-pass UI to validate subject management before introducing additional features.

## Risks / Trade-offs

- [Risk] Backend API setup may require Xano configuration or credentials.
  → Mitigation: document the API schema clearly and provide a local data fallback if needed.
- [Risk] Subject management added without task linking may feel narrow.
  → Mitigation: focus on a stable subject model and clean UI first.
- [Trade-off] A simple subject list UI avoids complexity but limits usability for large catalogs.
  → Mitigation: reserve search and pagination for later iterations.

## Open Questions

- Should the initial subject model include an optional `description` field, or should it remain name-only?
- What exact Xano table fields and endpoint paths should be used for the `subjects` resource?
