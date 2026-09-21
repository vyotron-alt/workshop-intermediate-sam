# Shared basics CI — what each job verifies

**Audience:** Partner / CTO  
**Rule:** Job **names** stay `skill-1…skill-7` (portal map unchanged). **No LLM grading** — deterministic scripts only. Assessed unlock rules live in StudentTraining `intermediate-portal`, not here.

| Job name | Floor node | What it actually checks |
|---|---|---|
| `skill-1-git-pr` | 1 | README + `.gitignore` present; README mentions workshop/portal |
| `skill-2-cli` | 2 | `python skills/cli/greet_cli.py Alex` prints `Hello, Alex` |
| `skill-3-read-code` | 3 | `hello.greet` importable; source contains greeting; `greet("Sam")` |
| `skill-4-pytest` | 4 | Deeper pytest suite (`tests/`) including skill-check smoke |
| `skill-5-http-api` | 5 | Stdlib HTTP `/health` returns JSON `ok=true`, `skill=5` |
| `skill-6-db-lite` | 6 | SQLite create/insert/select round-trip |
| `skill-7-deploy` | 7 | `scripts/deploy_dry_run.sh` exits 0 and prints `DRY_RUN_OK` |
| `skill-8-hardware` | 8 (never gates) | Practice-mode banner only |

Portal Sync greens nodes from successful check-run **names** containing these fragments (`skill-1` … `skill-7`).

## Partner: workflow paste (if eng token lacks `workflow` scope)

1. Open this repo → **Actions** or edit `.github/workflows/shared-basics.yml`
2. Replace the placeholder workflow with the file from StudentTraining:  
   `intermediate-portal/docs/workshop-ci/shared-basics.yml`
3. Commit on `main` (or merge the open PR that already has the skill scripts)
