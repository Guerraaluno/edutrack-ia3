## Why

The current subjects table lacks fields for teacher assignment, course hours, and direct user association. Adding these fields now enables better tracking of subject ownership and academic details in the EduTrack system.

## What Changes

- Update the subjects table schema to include teacher (text), hours (int), and user_id (foreign key to user table).
- Ensure the schema aligns with Xano authentication requirements.

## Capabilities

### New Capabilities

### Modified Capabilities
- `subjects`: Update the subjects table schema to include teacher, hours, and user_id fields.
