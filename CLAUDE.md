# Claude Code Guide — Backyard Data

## Python / package management

This project uses [uv](https://docs.astral.sh/uv/). Always use uv commands — never call `pip` or `python` directly.

| Instead of | Use |
|---|---|
| `pip install <pkg>` | `uv add <pkg>` |
| `pip install -r requirements.txt` | `uv sync` |
| `python script.py` | `uv run script.py` |
| `python -m pytest` | `uv run pytest` |

## Notion task board

This project is tracked in Notion. Use the Notion MCP integration to read and update tasks as you work.

**Finding tasks:**
- Search by name: `notion-search "task name"`
- Main project page ID: `5d5adfd5-544b-8219-8a0b-8136ac66b663`
- Tasks database ID: `cbeadfd5-544b-8335-a0be-016ec0983099`

**Task status values** (use exactly as written):
- `Not started`
- `In progress`
- `Done`

**Story/project status values:**
- `Planning`
- `In progress`
- `Done`

**Workflow:**
1. Fetch the relevant task from Notion before starting work
2. Set status to `In progress` when you begin
3. Set status to `Done` when the work is merged
