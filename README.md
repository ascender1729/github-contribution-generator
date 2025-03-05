# GitHub Contribution Generator

A powerful tool to generate custom contribution patterns on your GitHub profile by creating backdated commits for any date range you choose.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Installation](#installation)
- [Usage](#usage)
- [Command Reference](#command-reference)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [FAQ](#faq)

## 🔍 Overview

This tool allows you to customize your GitHub contribution graph by generating commits with specified dates. Whether you need to:
- Fill in gaps in your contribution history
- Create artistic patterns
- Backdate commits for projects you worked on offline
- Generate a rich contribution history

## ✨ Features

- **Custom Date Ranges**: Generate commits for any time period
- **Adjustable Commit Frequency**: Set minimum and maximum commits per day
- **Parallel Processing**: Fast generation using multithreading
- **Chronological Ordering**: Commits are ordered by timestamp for each day
- **Simple Setup**: Easy-to-follow instructions for all skill levels
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.6 or higher
- Git installed and configured
- GitHub account
- Personal Access Token with repository permissions

## 🔧 Setup Instructions

### 1. Create a New GitHub Repository

1. Go to GitHub and log in
2. Click the "+" icon in the top right corner, then select "New repository"
3. Name the repository whatever you want (e.g., "my-contribution-history")
4. Add a brief description
5. Choose Public or Private based on your preference
6. DO NOT initialize with README, .gitignore, or license
7. Click "Create repository"

### 2. Create a Personal Access Token (PAT)

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Note: "Contribution Generator"
4. Select scopes: check "repo" (Full control of private repositories)
5. Click "Generate token"
6. IMPORTANT: Copy your token immediately! You won't be able to see it again.

### 3. Set Up Local Repository

```bash
# Create a new directory for your activity repository
mkdir my-activity-repo
cd my-activity-repo

# Initialize git
git init

# Configure git with your details
git config user.name "YourUsername"
git config user.email "your.email@example.com"

# Create a README file
echo "# My Contribution History" > README.md

# Set up the remote repository
git remote add origin https://github.com/YourUsername/my-contribution-history.git

# Create the contribution script (copy the provided script to local_contribute.py)
# Use a text editor to paste the script contents

# Add your files
git add README.md local_contribute.py
git commit -m "Initial setup"

# Configure your PAT
git remote set-url origin https://YOUR_PAT_TOKEN@github.com/YourUsername/my-contribution-history.git
```

## 🚀 Installation

1. **Clone this repository**

```bash
# Clone this repository
git clone https://github.com/ascender1729/github-contribution-generator.git

# Copy the script file to your project
cp github-contribution-generator/local_contribute.py .
```

2. **Set up your target repository**

```bash
# Create a new directory for your activity
mkdir my-activity-repo
cd my-activity-repo

# Initialize git
git init

# Configure git with your details
git config user.name "YourUsername"
git config user.email "your.email@example.com"

# Copy the script from the cloned repository
cp ../github-contribution-generator/local_contribute.py .

# Create a README file
echo "# My Contribution History" > README.md

# Add your remote repository
git remote add origin https://github.com/YourUsername/my-contribution-history.git

# Add your files
git add README.md local_contribute.py
git commit -m "Initial setup"

# Add your PAT to the remote URL (replace with your actual token)
git remote set-url origin https://YOUR_PAT_TOKEN@github.com/YourUsername/my-contribution-history.git
```

## 🚀 Usage

1. **Run the script**

```bash
python local_contribute.py
```

2. **Enter requested information**
   - Start date (YYYY-MM-DD format)
   - End date (YYYY-MM-DD format)
   - Minimum commits per day (8-100)
   - Maximum commits per day (must be ≥ minimum)

3. **Wait for completion**
   - The script will show progress updates
   - Generation may take from minutes to hours depending on date range

4. **Push to GitHub**

```bash
git push -f origin main
```

5. **View your GitHub profile**
   - Visit your profile to see the updated contribution graph
   - Changes usually appear within a few minutes

## 💻 Command Reference

| Command | Description |
|---------|-------------|
| `git init` | Initialize a new Git repository |
| `git config user.name "YourUsername"` | Set your Git username |
| `git config user.email "your.email@example.com"` | Set your Git email |
| `git remote add origin URL` | Connect to remote repository |
| `git remote set-url origin URL` | Update remote repository URL (for PAT) |
| `git add .` | Stage all files for commit |
| `git commit -m "Message"` | Commit staged files |
| `python local_contribute.py` | Run the contribution script |
| `git push -f origin main` | Force push changes to GitHub |

## 🔧 Troubleshooting

### Common Issues:

1. **"Error: remote origin already exists"**
   ```bash
   git remote remove origin
   git remote add origin https://github.com/YourUsername/repo-name.git
   ```

2. **"Permission denied" when pushing**
   - Check that you've correctly added your PAT to the remote URL
   ```bash
   git remote set-url origin https://YOUR_PAT_TOKEN@github.com/YourUsername/repo-name.git
   ```

3. **Encoding errors with emoji**
   - Use the script with `encoding='utf-8'` as provided
   - If errors persist, modify script to remove emoji characters

4. **Script runs too slowly**
   - Adjust the `chunk_size` and `max_workers` variables in the script
   - Try a smaller date range or fewer commits per day

## 🤝 Contributing

To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

Pavan Kumar - pavankumard.pg19.ma@nitp.ac.in  
LinkedIn: [linkedin.com/in/im-pavankumar](https://linkedin.com/in/im-pavankumar)  
Project Link: [GitHub Contribution Generator](https://github.com/ascender1729/github-contribution-generator)

## ❓ FAQ

**Q: Is this against GitHub's terms of service?**  
A: GitHub does not explicitly prohibit backdated commits. However, use this tool responsibly and ethically.

**Q: Will this affect my GitHub streaks?**  
A: Yes, GitHub counts all commits regardless of date.

**Q: Can I use this with private repositories?**  
A: Yes, the tool works with both public and private repositories.

**Q: How can I create specific patterns?**  
A: Create multiple repositories with different date ranges to build specific patterns.

**Q: Will my commits appear immediately?**  
A: GitHub typically updates contribution graphs within minutes, but it can sometimes take longer.

---

**Disclaimer**: This tool is meant for educational purposes. Use responsibly and ethically.