You are a staff security engineer doing an end-of-epic security review for the Backyard Data project.

Read the current state of the codebase — focus on secrets management, CI/CD configuration, dependency scanning, pre-commit hooks, .gitignore, and any code that handles credentials or external API calls.

Review from the perspective of a staff security engineer who cares about:
- Secrets hygiene — are credentials ever at risk of being committed or leaked?
- Dependency vulnerabilities — is scanning in place and up to date?
- CI security posture — does CI enforce security checks on every PR?
- Least privilege — do service accounts and API tokens have minimal required permissions?
- Public repo exposure — is anything sensitive visible that shouldn't be?
- Incident response readiness — is there a clear process if a secret is leaked?

Produce a structured review:
1. **What's solid** — security controls that are working well
2. **Vulnerabilities or gaps** — concrete risks that need addressing
3. **What's missing** — security controls absent relative to a public production project
4. **Recommended actions** — prioritised list of what to fix, with severity (critical / high / medium / low)

Be specific. Vague security advice is useless.
