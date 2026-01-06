---
name: review-epics
description: Review epic health - check for missing descriptions, milestones, and stale updates
allowed-tools:
  - Bash
  - Read
argument-hint: "[team_member_name]"
---

# Review Epics Command

Review the health of active YouTrack epics and identify issues that need attention.

## Arguments

- `[team_member_name]`: Optional - filter to epics where this person is Bearbeiter

## Workflow

### 1. Run Health Check

```bash
python ${CLAUDE_PLUGIN_ROOT}/helper_tools/youtrack/yt.py health-check [team_member_name]
```

### 2. Generate Report

Format the results into a structured health report.

## Output Format

```markdown
# Epic Health Check

**Stand:** [Datum]
**Filter:** [Team member or "Alle"]

## Zusammenfassung

| Kategorie | Anzahl |
|-----------|--------|
| Gesamt Epics | XX |
| ✅ Gesund | XX |
| ⚠️ Mit Problemen | XX |

---

## ❌ Fehlende Beschreibung/Projektziel

Diese Epics haben keine oder nur minimale Beschreibung:

| Epic | Projekt | Bearbeiter |
|------|---------|------------|
| AI-XXX | [Name] | [Name] |

**Aktion:** Beschreibung mit Projektziel und Meilensteinen ergänzen

---

## ❌ Fehlende Meilensteine

Diese Epics haben keine Meilenstein-Tabelle:

| Epic | Projekt | Bearbeiter |
|------|---------|------------|
| AI-XXX | [Name] | [Name] |

**Aktion:** Meilensteine mit Ziel-KW definieren

---

## ⚠️ Kein Bearbeiter zugewiesen

| Epic | Projekt |
|------|---------|
| AI-XXX | [Name] |

**Aktion:** Bearbeiter zuweisen

---

## 🟡 Veraltete Updates (>2 Wochen)

Diese Epics haben seit mehr als 2 Wochen kein KW-Update:

| Epic | Projekt | Bearbeiter | Letztes Update |
|------|---------|------------|----------------|
| AI-XXX | [Name] | [Name] | X Wochen |

**Aktion:** KW-Update posten oder Epic archivieren falls inaktiv

---

## ✅ Gesunde Epics

| Epic | Projekt | Bearbeiter |
|------|---------|------------|
| AI-XXX | [Name] | [Name] |

---

## Empfohlene nächste Schritte

1. [ ] Epics ohne Beschreibung aktualisieren
2. [ ] Meilensteine für alle aktiven Projekte definieren
3. [ ] Veraltete Epics: Update posten oder archivieren
4. [ ] Bearbeiter für verwaiste Epics zuweisen
```

## Health Criteria

| Check | Healthy | Issue |
|-------|---------|-------|
| **Beschreibung** | Has Projektziel or >50 chars | Missing or too short |
| **Meilensteine** | Contains "Meilenstein" or "KW" | No milestone table |
| **Bearbeiter** | Field is set | No assignee |
| **KW Update** | Within last 2 weeks | Older than 2 weeks |

## Example

### Review all epics

```bash
/review-epics
```

### Review specific team member's epics

```bash
/review-epics "Maximilian"
```

Output:
```markdown
# Epic Health Check

**Stand:** 06.01.2026
**Filter:** Maximilian

## Zusammenfassung

| Kategorie | Anzahl |
|-----------|--------|
| Gesamt Epics | 12 |
| ✅ Gesund | 0 |
| ⚠️ Mit Problemen | 12 |

---

## ❌ Fehlende Beschreibung/Projektziel

| Epic | Projekt | Bearbeiter |
|------|---------|------------|
| AI-319 | MCP Testing und Apps | Maximilian Bruhn |

---

## 🟡 Veraltete Updates (>2 Wochen)

| Epic | Projekt | Bearbeiter | Letztes Update |
|------|---------|------------|----------------|
| AI-301 | Customer Support Chatbot | Maximilian Bruhn | 3 Wochen |
| AI-338 | Checkout Chatbot | Maximilian Bruhn | 2 Wochen |
| AI-62 | Web Research Agents | Maximilian Bruhn | 3 Wochen |
| AI-73 | Assistent/Agent Use Cases | Maximilian Bruhn | 9 Wochen |

---

## Empfohlene nächste Schritte

1. [ ] AI-319: Beschreibung mit Projektziel ergänzen
2. [ ] KW-Updates für aktive Projekte posten
3. [ ] AI-73, AI-61, AI-68: Archivieren falls inaktiv?
```

## Use Cases

- **Weekly Review**: Check health before Friday updates
- **Cleanup**: Identify epics to archive or update
- **Onboarding**: See which projects need attention
- **Management**: Overview of team's project health

## Follow-up Commands

After reviewing, use these commands to fix issues:

| Issue | Command |
|-------|---------|
| Missing KW update | `/add-kw-update "<project>" update "..."` |
| Need full overview | `/prepare-update "<project>"` |
| Prepare for JF | `/prepare-jf-team "<name>"` |

## Reference

See `skills/youtrack-dashboard/references/youtrack-documentation-guide.md` for:
- Epic description template
- KW comment format
- Milestone structure
