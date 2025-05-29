git add main.py
git commit -m "Add main.py"
git push -u origin master
git branch -M main
git push -u origin main
^X
nano setup.sh
#!/bin/bash

echo "📁 Starting Git auto-setup..."

# Initialize git if not already initialized
git init

# Rename branch to main
git branch -M main

# Add all files
git add .

# Commit changes
git commit -m "Auto commit by setup.sh"

# Add remote (only needed the first time)
git remote add origin https://github.com/bling12345/Termux-practice.git

# Push to GitHub
git push -u origin main

echo "✅ Done! Pushed to GitHub successfully."

