# 📋 Git Commands Cheatsheet

Quick reference for common Git commands.

## 🚀 Initial Setup

```bash
# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize repository
git init

# Add remote repository
git remote add origin https://github.com/username/repo.git

# Verify remote
git remote -v
```

## 📝 Basic Workflow

```bash
# Check status
git status

# Add all files
git add .

# Add specific file
git add filename.py

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main
```

## 🌿 Branching

```bash
# Create new branch
git branch feature-name

# Switch to branch
git checkout feature-name

# Create and switch in one command
git checkout -b feature-name

# List all branches
git branch -a

# Delete branch
git branch -d feature-name

# Merge branch into main
git checkout main
git merge feature-name
```

## 🔍 Viewing History

```bash
# View commit history
git log

# View compact history
git log --oneline

# View last 5 commits
git log -5

# View changes in a file
git log -p filename.py

# View who changed what
git blame filename.py
```

## ↩️ Undoing Changes

```bash
# Discard changes in working directory
git checkout -- filename.py

# Unstage file (keep changes)
git reset HEAD filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert a commit (creates new commit)
git revert commit-hash
```

## 🔄 Syncing

```bash
# Fetch changes (don't merge)
git fetch origin

# Pull and rebase
git pull --rebase origin main

# Push force (use carefully!)
git push --force origin main

# Push new branch
git push -u origin branch-name
```

## 🏷️ Tags

```bash
# Create tag
git tag v1.0.0

# Create annotated tag
git tag -a v1.0.0 -m "Version 1.0.0"

# Push tags
git push --tags

# List tags
git tag -l

# Delete tag
git tag -d v1.0.0
```

## 🔧 Configuration

```bash
# View all config
git config --list

# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code --wait"

# Enable color output
git config --global color.ui auto
```

## 🗑️ Removing Files

```bash
# Remove file from Git and filesystem
git rm filename.py

# Remove file from Git only (keep local)
git rm --cached filename.py

# Remove folder
git rm -r folder-name/

# Commit the removal
git commit -m "Removed file"
```

## 🔍 Searching

```bash
# Search in files
git grep "search term"

# Search in commit messages
git log --grep="search term"

# Search in diffs
git log -S "search term"
```

## 🆘 Emergency Commands

```bash
# Stash changes temporarily
git stash

# Apply stashed changes
git stash pop

# List stashes
git stash list

# Discard all local changes
git reset --hard HEAD

# Clean untracked files
git clean -fd

# Abort merge
git merge --abort

# Abort rebase
git rebase --abort
```

## 📊 Useful Aliases

Add these to your `.gitconfig`:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --oneline --graph --decorate --all'
```

Now you can use:
```bash
git st          # instead of git status
git co main     # instead of git checkout main
git br          # instead of git branch
git ci -m "msg" # instead of git commit -m "msg"
git visual      # pretty log view
```

## 🔐 SSH Setup (Recommended)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key (add to GitHub)
cat ~/.ssh/id_ed25519.pub

# Test connection
ssh -T git@github.com
```

## 📦 Submodules

```bash
# Add submodule
git submodule add https://github.com/user/repo.git path/to/submodule

# Initialize submodules
git submodule init

# Update submodules
git submodule update

# Clone with submodules
git clone --recursive https://github.com/user/repo.git
```

## 🎯 Best Practices

1. **Commit often**: Small, focused commits
2. **Write good messages**: Clear, descriptive commit messages
3. **Pull before push**: Always pull latest changes first
4. **Use branches**: Don't work directly on main
5. **Review before commit**: Check `git status` and `git diff`
6. **Don't commit secrets**: Use `.gitignore` for sensitive files
7. **Test before push**: Make sure code works

## 📝 Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Example:
```
feat: Add document download by file ID

- Added new /download/<file_id> endpoint
- Improved error handling for missing files
- Updated documentation

Closes #123
```

## 🔗 Useful Links

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [Git Cheat Sheet PDF](https://education.github.com/git-cheat-sheet-education.pdf)
- [Interactive Git Tutorial](https://learngitbranching.js.org)

---

**Pro Tip**: Keep this file handy for quick reference! 📌
