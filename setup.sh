#!/bin/bash

echo "📁 Starting Git auto-setup..."

git init
git branch -M main
git add .
git commit -m "Auto commit by setup.sh"
git remote add origin https://github.com/bling12345/Termux-practice.git
git push -u origin main

echo "✅ Done! Pushed to GitHub successfully."

