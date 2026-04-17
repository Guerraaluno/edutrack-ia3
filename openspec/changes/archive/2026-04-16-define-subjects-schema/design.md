## Context

The subjects table was initially created with basic fields (id, name, description, active, account_id). To support more detailed academic tracking, we need to add teacher, hours, and user_id fields.

## Goals / Non-Goals

**Goals:**
- Add teacher, hours, and user_id fields to the subjects table.
- Maintain compatibility with existing data.

**Non-Goals:**
- Implement API changes or frontend updates for these fields.
- Add validation or business logic beyond schema definition.

## Decisions

- Use text for teacher name.
- Use int for hours (assuming total course hours).
- Use user_id as FK to the user table for direct user association.

## Risks / Trade-offs

- [Risk] Adding fields may require data migration if existing records exist.
  → Mitigation: Fields can be nullable initially.
