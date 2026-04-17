## ADDED Requirements

### Requirement: Subject storage
The system SHALL store subjects with an identifier, a name, and an active/inactive state.

#### Scenario: Load subjects from backend
- **WHEN** the user opens the Disciplinas page
- **THEN** the app loads subjects from the backend API and displays each subject's name

### Requirement: Create new subject
The system SHALL allow users to create new subjects.

#### Scenario: Successful subject creation
- **WHEN** the user submits a new subject name
- **THEN** the backend persists the subject and the frontend updates the list

### Requirement: Edit subject details
The system SHALL allow users to update an existing subject's name and active state.

#### Scenario: Successful subject update
- **WHEN** the user updates an existing subject
- **THEN** the backend saves the changes and the frontend shows the updated subject

### Requirement: Active/inactive subject state
The system SHALL allow subjects to be marked as active or inactive.

#### Scenario: Subject active state set
- **WHEN** the user toggles the active state of a subject
- **THEN** the system stores the new state and the subject listing reflects it
