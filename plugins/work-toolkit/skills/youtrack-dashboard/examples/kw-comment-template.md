# KW Comment Template

Standard format for weekly status updates on YouTrack epic tickets.

## Template

```markdown
## KW{number}

**Updates:**
- [What was accomplished this week]
- [Another completed item]

**Blocker:** [Issues or "Keine"]

**Next Steps:**
- [What's planned for next week]
```

## Example: Active Development

```markdown
## KW51

**Updates:**
- System prompt v1 created with full checkout flow guidance
- Defined command structure (`checkout idle` trigger for 60s inactivity)
- Documented approach, limitations, and step-specific FAQ content

**Blocker:** Keine

**Next Steps:**
- Deploy to staging environment
- Gather initial user feedback
```

## Example: Waiting on External

```markdown
## KW40

**Updates:**
- Warten auf Feedback von Customer Care nach erstem Testing

**Blocker:** Warten auf Feedback

**Next Steps:**
- Einbauen von Feedbackwünschen nach Rückmeldung
```

## Example: Multi-Week Catch-Up

```markdown
## KW36-37

**Updates:**
- Keine Updates aufgrund von Urlaub

## KW38

**Updates:**
- Testing phase completed
- Documentation updated

**Blocker:** Keine

**Next Steps:**
- Production deployment geplant für KW39
```

## Quick Reference

| Section | Required | Notes |
|---------|----------|-------|
| `## KW{n}` | Yes | h2 heading with week number |
| `**Updates:**` | Yes | 3-5 bullet points ideal |
| `**Blocker:**` | Yes | Use "Keine" if none |
| `**Next Steps:**` | Yes | What's planned next |

## Tips

- Keep bullets concise (1 line each)
- Include metrics when available
- German preferred, English tech terms OK
- Post consistently on Fridays
- See `youtrack-documentation-guide.md` for full guidelines
