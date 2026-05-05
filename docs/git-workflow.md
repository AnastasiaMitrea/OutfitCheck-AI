# Git & Development Workflow

To ensure a smooth collaboration and meet the university evaluation requirements, all team members must adhere to the following Git workflow.

## 1. Branching Strategy
- **`main` branch:** The production-ready MVP code. Direct commits to `main` are strictly forbidden.
- **Student Branches:** Each student has their own branch (e.g., `ioana`, `maria`, `sonia`, `adriana`) for broad feature work.
- **Feature Branches:** Create specific branches off `main` or your student branch for specific tasks (e.g., `feature/login`, `bugfix/image-upload`).

## 2. Pull Request Workflow
- All code must be merged into `main` via a **Pull Request (PR)**.
- PRs should have clear descriptions outlining what was changed.
- PRs must pass the CI/CD pipeline (tests and linters) before they can be merged.

## 3. Merge / Rebase Expectations
- Before opening a PR, ensure your branch is up to date with `main` by rebasing or merging `main` into your feature branch to resolve any conflicts locally.
- Use "Squash and Merge" for PRs to keep the `main` history clean.

## 4. Minimum Commit Requirement
- **Requirement:** Every student must have a minimum of **5 substantive commits** present in the repository history. 
- *Evidence:* This will be verified via `git log` and GitHub statistics during the final evaluation.

## 5. Bug Fixing Workflow
- If a bug is found, it must be documented using the template in `docs/bug-report-template.md` (or created as a GitHub Issue).
- The bug fix must be implemented on a separate branch (e.g., `bugfix/issue-123`).
- The PR resolving the bug must link to the issue/report (e.g., "Fixes Issue #123").

## 6. Required Evidence for Final Evaluation
Keep screenshots or links to the following as evidence for the university requirements:
- Creating a branch.
- Creating a Pull Request.
- Successful Merge/Rebase.
- A Bug Report and its associated fixing PR.
- Commit history proving at least 5 commits per student.
