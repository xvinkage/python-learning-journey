# Day 70 – Version Control with Git

## 1. Initialize a Repository

```bash
git init
```
- Initializes a local Git repository in the current directory.

## 2. Check Repository Status

```bash
git status
```
- Shows modified, untracked, and staged files.

## 3. Stage Changes

```bash
git add filename
```
- Adds a specific file to the staging area.

```bash
git add .
```
- Stages all changes in the current directory and its subdirectories.

## 4. Commit Changes

```bash
git commit -m "Describe your changes"
```
- Saves staged changes as a commit.
- A commit is a snapshot of your project at a particular point in time.

## 5. View Commit History

```bash
git log
```
- Displays previous commits and their details.

## 6. Compare Changes

```bash
git diff filename
```
- Shows unstaged changes compared with the last committed version.

## 7. Undo Changes

```bash
git restore filename
```
- Discards unstaged changes in a file, reverting it to its last committed version.

**Note:** `git checkout filename` is an older command that can do the same thing.

## 8. Connect to a Remote Repository

```bash
git push -u origin main
```
- Pushes your local commits to the remote repository named `origin`, on the `main` branch.
- `-u` sets the upstream branch for future pushes.

```bash
git clone <URL>
```
- Downloads a remote repository to your local machine.

## 9. Git Ignore

Create a file named `.gitignore` in your project directory.

Example:
```gitignore
*.txt
.env
__pycache__/
venv/
```

- Tells Git which untracked files and directories to ignore.
- `*` is a wildcard that matches multiple characters.
- Useful for excluding virtual environments, temporary files, and sensitive configuration files.

## 10. Branching

```bash
git branch
```
- Lists existing branches.

```bash
git branch feature-name
```
- Creates a new branch.

```bash
git switch feature-name
```
- Switches to another branch.

```bash
git switch -c feature-name
```
- Creates and switches to a new branch.

## 11. Merging Branches

First, switch to the branch you want to merge changes into:

```bash
git switch main
```

Then merge the other branch:

```bash
git merge feature-name
```

- Combines the changes from `feature-name` into your current branch.
- Git may automatically merge changes or ask you to resolve conflicts.

---

## Typical Git Workflow

```bash
git status
git add .
git commit -m "Describe changes"
git push
```

**Remember:**
- Repository = Your project tracked by Git.
- Staging = Changes selected for the next commit.
- Commit = Saved snapshot of your changes.
- Branch = Separate line of development.
- Merge = Combines changes from different branches.
- Remote = A copy of your repository hosted elsewhere, such as GitHub.
