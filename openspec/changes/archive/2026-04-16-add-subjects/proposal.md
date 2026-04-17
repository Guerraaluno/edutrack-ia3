## Why

The current app shell includes a placeholder for "Disciplinas" but no actual subject management backend or frontend list. Adding subjects now creates the core academic data model needed for tracking disciplines, assignments, and student progress.

## What Changes

- Add a new subjects capability to manage academic disciplines.
- Create backend subject storage and APIs for listing, creating, editing, and deleting subjects.
- Connect the Streamlit frontend to subject data so the "Disciplinas" page shows real content.
- Provide a clean user experience for browsing and managing subjects.

## Capabilities

### New Capabilities
- `subjects`: Subject management capability with backend storage and UI integration for academic disciplines.

### Modified Capabilities
- 

## Impact

- Adds a new subject data model and corresponding Xano backend resources.
- Updates `app.py` to display actual subject data instead of placeholder text.
- Impacts the frontend subject listing and the data integration layer.
- May require new API endpoints, database table definitions, and connection configuration.
