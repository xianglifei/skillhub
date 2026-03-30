The following is a semantic Markdown representation of a webpage.

Source: https://docs.openclaw.ai/tools/creating-skills

---

```markdown 
# <a href="https://docs.openclaw.ai/tools/creating-skills#creating-skills"></a> Creating Skills

Skills teach the agent how and when to use tools. Each skill is a directory
containing a `SKILL.md` file with YAML frontmatter and markdown instructions. For how skills are loaded and prioritized, see [Skills](ref0).
## <a href="https://docs.openclaw.ai/tools/creating-skills#create-your-first-skill"></a> Create your first skill

1 <a href="ref1"></a> Create the skill directory

Skills live in your workspace. Create a new folder:
```
mkdir -p ~/.openclaw/workspace/skills/hello-world
```
2 <a href="ref1"></a> Write SKILL.md

Create `SKILL.md` inside that directory. The frontmatter defines metadata,
and the markdown body contains instructions for the agent.
```
---
name: hello_world
description: A simple skill that says hello.
---

# Hello World Skill

When the user asks for a greeting, use the `echo` tool to say
"Hello from your custom skill!".
```
3 <a href="ref1"></a> Add tools (optional)

You can define custom tool schemas in the frontmatter or instruct the agent
to use existing system tools (like `exec` or `browser`). Skills can also
ship inside plugins alongside the tools they document. 4 <a href="ref1"></a> Load the skill

Start a new session so OpenClaw picks up the skill:
```
# From chat
/new

# Or restart the gateway
openclaw gateway restart
```
Verify the skill loaded:
```
openclaw skills list
```
5 <a href="ref1"></a> Test it

Send a message that should trigger the skill:
```
openclaw agent --message "give me a greeting"
```
Or just chat with the agent and ask for a greeting.
## <a href="https://docs.openclaw.ai/tools/creating-skills#skill-metadata-reference"></a> Skill metadata reference

The YAML frontmatter supports these fields:
| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Unique identifier (snake_case) |
| `description` | Yes | One-line description shown to the agent |
| `metadata.openclaw.os` | No | OS filter (`["darwin"]`, `["linux"]`, etc.) |
| `metadata.openclaw.requires.bins` | No | Required binaries on PATH |
| `metadata.openclaw.requires.config` | No | Required config keys |

## <a href="https://docs.openclaw.ai/tools/creating-skills#best-practices"></a> Best practices

- **Be concise** — instruct the model on *what* to do, not how to be an AI
- **Safety first** — if your skill uses `exec`, ensure prompts don’t allow arbitrary command injection from untrusted input
- **Test locally** — use `openclaw agent --message "..."` to test before sharing
- **Use ClawHub** — browse and contribute skills at [ClawHub](https://clawhub.com/)

## <a href="https://docs.openclaw.ai/tools/creating-skills#where-skills-live"></a> Where skills live

| Location | Precedence | Scope |
| --- | --- | --- |
| `\<workspace\>/skills/` | Highest | Per-agent |
| `~/.openclaw/skills/` | Medium | Shared (all agents) |
| Bundled (shipped with OpenClaw) | Lowest | Global |
| `skills.load.extraDirs` | Lowest | Custom shared folders |

## <a href="https://docs.openclaw.ai/tools/creating-skills#related"></a> Related

- [Skills reference](ref0) — loading, precedence, and gating rules
- [Skills config](ref2) — `skills.*` config schema
- [ClawHub](ref3) — public skill registry
- [Building Plugins](ref4) — plugins can ship skills
```
