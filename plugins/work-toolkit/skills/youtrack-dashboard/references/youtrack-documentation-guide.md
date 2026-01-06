# YouTrack Documentation Guide

This reference documents how we use YouTrack for project tracking, team coordination, and weekly status reporting at fazit.youtrack.cloud.

## Overview

YouTrack serves as our **single source of truth** for project status and team coordination.

| Content | Location | Updated |
|---------|----------|---------|
| Project goals & milestones | Epic description | When plans change |
| Weekly progress | KW comments | Every Friday |
| Concrete work items | Aufgaben (child tickets) | Continuously |
| Responsibility | Bearbeiter & Support fields | At project start |

---

## Epic Structure

### Anatomy of an Epic

```
EPIC (Type: Story, State: Projektticket)
│
├── Fields
│   ├── Summary: Project name
│   ├── Bearbeiter: Main responsible person
│   ├── Support: Supporting team members
│   └── State: Projektticket (active)
│
├── Description
│   ├── Projektziel
│   ├── Meilensteine (with target KW)
│   └── Kontext/Hintergrund
│
├── KW Comments
│   └── Weekly status updates
│
└── Aufgaben (child tickets)
    ├── AI-XXX: Task 1
    ├── AI-XXX: Task 2
    └── ...
```

### Epic Lifecycle States

```
Backlog → Projektticket → in Abnahme → Geschlossen
   │           │              │            │
   │           │              │            └── Project completed
   │           │              └── Final review/acceptance
   │           └── Active development (receives KW updates)
   └── Planned but not started
```

---

## Epic Description Template

Every epic description should follow this structure:

```markdown
## Projektziel

[Was ist das Ziel? Was bedeutet Erfolg? Mit klarem Zeithorizont]

**Ziel Q[X]:** [Konkretes Quartalsziel mit messbarem Outcome]

## Stakeholder

- **Auftraggeber:** [Wer hat das Projekt beauftragt]
- **Alpha-Tester:** [Namen oder Gruppe, z.B. "5 Redakteure"]
- **Fachbereich:** [Betroffene Abteilung/Team]

## Links

- **Langfuse:** [Tracing URL]
- **Hosting:** [Langdock / Replit / Azure URL]

## Meilensteine

- ⏳ **KW XX** - [Meilenstein-Beschreibung]
- 🔄 **KW XX** - [Meilenstein-Beschreibung]
- ✅ **KW XX** - [Meilenstein-Beschreibung]

Status: ✅ Erledigt | 🔄 In Arbeit | ⏳ Geplant | ❌ Blockiert

## Kontext

[Optional: Hintergrund, technische Abhängigkeiten]
```

### Example Epic Description

```markdown
## Projektziel

Redakteure können strukturierte Briefings beauftragen, die automatisch aus Web-Quellen generiert und regelmäßig (z.B. täglich) per E-Mail zugestellt werden.

**Ziel Q1:** Abgeschlossene Alpha-Phase mit Iterationen, Präsentation im Lenkungsausschuss KI, und Freigabe für Beta-Launch.

## Stakeholder

- **Auftraggeber:** Redaktion Digital
- **Alpha-Tester:** 5 Redakteure (Check-ins alle 1-2 Wochen)
- **Fachbereich:** Redaktion

## Links

- **Langfuse:** https://cloud.langfuse.com/project/web-research
- **Hosting:** https://web-research-agents.replit.app

## Meilensteine

- ✅ **KW 50** - Initiales Setup und Erkenntnisse
- ✅ **KW 01** - Eigenes Setup mit FastAPI entwickelt
- 🔄 **KW 02** - Alpha-Rollout an 5 Redakteure
- ⏳ **KW 04** - Feedback-Iteration
- ⏳ **KW 08** - Präsentation Lenkungsausschuss KI
- ⏳ **KW 10** - Beta-Launch Freigabe

## Kontext

Ersetzt manuelle tägliche Recherche durch automatisierte Briefings.
Technische Abhängigkeiten: Exa API, Perplexity Sonar API, OpenAI.
```

---

## Responsibility Fields

### Bearbeiter (Assignee)

The **main responsible person** for the project:
- Owns the project outcome
- Updates KW comments
- Drives progress on Aufgaben

### Support

**Supporting team members** who contribute:
- Work on specific Aufgaben
- Provide expertise
- May attend JF meetings

### Query by Responsibility

```
# Find projects where Max is responsible
project: AI Type: Story Bearbeiter: Max

# Find projects where someone is assigned
project: AI Type: Story State: Projektticket has: Bearbeiter
```

---

## Aufgaben (Child Tickets)

Aufgaben are concrete work items under an Epic.

### Creating Aufgaben

- **Type:** Task (or Bug, Feature)
- **Parent:** Link to Epic via "Übergeordnetes Ticket" field
- **Summary:** Clear, actionable title
- **Bearbeiter:** Person doing the work

### Aufgaben States

```
Open → In Arbeit → Done
```

### Query Aufgaben for an Epic

```
# All Aufgaben under AI-301
parent: AI-301

# Open Aufgaben under AI-301
parent: AI-301 State: Open
```

### Aufgaben in KW Comments

Reference completed and in-progress Aufgaben in KW updates:

```markdown
## KW42

**Updates:**
- AI-305 (Prompt Refinement) erledigt
- AI-306 (User Testing) in Arbeit
- Feedback von Customer Care eingearbeitet

**Blocker:** Keine

**Next Steps:**
- AI-307 (Production Deployment) starten
```

**Format:** `AI-XXX (Kurztitel) Status`

---

## KW Comment Format

KW (Kalenderwoche) comments are weekly status updates posted to epic tickets.

### Standard Format

```markdown
## KW{number}

**Updates:**
- [Completed Aufgaben with AI-XXX reference]
- [Other accomplishments]

**Blocker:** [Issues blocking progress, or "Keine"]

**Next Steps:**
- [Planned Aufgaben for next week]
- [Key activities ahead]
```

### Complete Example

```markdown
## KW50

**Updates:**
- AI-310 (Tester-Feedback Integration) erledigt
- AI-311 (Preisübersichten) erledigt
- System Prompt v2 deployed
- 60+ Testfragen, 16 Szenarien verarbeitet

**Blocker:** Keine

**Next Steps:**
- AI-312 (Knowledge Base Refresh) starten
- Weiteres Testing durch Customer Support
```

### Format Rules

1. **Header:** Use `## KW{number}` (h2 markdown heading)
2. **Updates:** Reference Aufgaben with `AI-XXX (Titel)` format
3. **Blocker:** Always include, use "Keine" if none
4. **Next Steps:** Include planned Aufgaben
5. **Language:** German, English technical terms acceptable

### Multi-Week Updates

When catching up on missed weeks:

```markdown
## KW36-37

**Updates:**
- Keine Updates aufgrund von Urlaub

## KW38

**Updates:**
- AI-305 (Testing Setup) erledigt
- Warten auf Feedback von Customer Care

**Blocker:** Warten auf Feedback

**Next Steps:**
- Einbauen von Feedbackwünschen
```

---

## JF (Jour Fixe) Preparation

Regular project sync meetings use YouTrack as the preparation source.

### What to Review Before JF

For each Epic:

| Source | Information |
|--------|-------------|
| Description | Milestones & target dates |
| Latest KW Comment | Current status, blockers |
| Aufgaben | Open tasks, who's working on what |
| Bearbeiter/Support | Who should attend |

### JF Agenda Structure

```markdown
# JF: [Projektname] - [Datum]

## Status (aus KW-Update)
[Summary of latest KW comment]

## Meilenstein-Check
| Meilenstein | Ziel | Aktuell |
|-------------|------|---------|
| [Next milestone] | KW XX | On track? |

## Offene Aufgaben
- AI-XXX: [Task] - [Bearbeiter]
- AI-XXX: [Task] - [Bearbeiter]

## Blocker & Entscheidungen
- [From KW comment or discussion]

## Nächste Schritte
- [Agreed actions]
```

### After JF

Update YouTrack based on JF outcomes:
1. Add new Aufgaben for agreed tasks
2. Update Blocker status in next KW comment
3. Adjust milestone dates in Epic description if needed

---

## When to Update What

| Event | Action |
|-------|--------|
| **Friday** | Post KW comment with week's progress |
| **Task completed** | Mark Aufgabe as Done |
| **New task identified** | Create Aufgabe under Epic |
| **Plan changes** | Update Epic description milestones |
| **After JF** | Create Aufgaben for action items |
| **Blocker resolved** | Note in next KW comment |
| **Project complete** | Final KW update → State: in Abnahme |

---

## Query Patterns

### Active Projects

```
project: AI Type: Story State: Projektticket
```

### Projects with Team Assigned

```
project: AI Type: Story State: Projektticket has: Bearbeiter
```

### Projects by Person

```
project: AI Type: Story Bearbeiter: "Maximilian Bruhn"
project: AI Type: Story Support: "Maximilian Bruhn"
```

### Epic with Open Aufgaben

```
parent: AI-301 State: -Done
```

### Recently Updated Epics

```
project: AI Type: Story updated: {Last week}
```

---

## Best Practices

### Do

- Keep KW comments concise (3-5 bullet points)
- Reference Aufgaben by ID in KW comments
- Update milestone status in description when completed
- Include metrics when available
- Post KW updates consistently on Fridays
- Use "Keine" explicitly for no blockers
- Include Quartalsziel in Projektziel section
- List Alpha-Tester in Stakeholder section

### Avoid

- Overly detailed technical descriptions
- KW comments without Aufgaben references (when applicable)
- Stale milestone dates in descriptions
- Skipping weeks without explanation
- Mixing multiple project updates in one comment
- **Referencing Linear or Linear issue IDs** (Linear is a personal planning system, not for YouTrack documentation)
- Using tables instead of bullet point lists in descriptions

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/add-kw-update <project> <section> <content>` | Add entry to current KW comment |
| `/update-youtrack-epic <project>` | Generate full KW update |
| `/weekly-email` | Compile all KW updates for Lenkungsausschuss |
| `/prepare-jf <project>` | Prepare JF agenda from YouTrack |

---

## API Reference

For programmatic access, see `api-reference.md` in this directory.

```bash
# Find epic by name
python helper_tools/youtrack/yt.py find-epic "Customer Support Chatbot"

# Get epic with Aufgaben count
python helper_tools/youtrack/yt.py search "parent: AI-301"

# Post KW comment
python helper_tools/youtrack/yt.py comment AI-301 "## KW51..."

# Get full comments
python helper_tools/youtrack/yt.py comments AI-301 --full
```
