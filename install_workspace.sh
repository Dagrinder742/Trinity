#!/bin/bash

echo "===================================================="
echo "STARTING TERMUX WORKSPACE ARCHITECTURE INSTALLATION"
echo "===================================================="

# 1. Update and upgrade system packages
echo "Updating package repositories..."
pkg update -y && pkg upgrade -y

# 2. Install Development Utilities
echo "Installing core terminal utilities..."
pkg install -y git curl wget nano openssh build-essential tar

# 3. Install Programming Languages
echo "Installing Python environment..."
pkg install -y python python-pip

echo "Installing Node.js environment..."
pkg install -y nodejs

echo "Installing OpenJDK (Java) environment..."
pkg install -y openjdk-17

# 4. Install Cryptographic & Blockchain Utilities
echo "Installing cryptographic dependencies..."
pkg install -y openssl libgmp libsodium

# 5. Install Python Data and Crypto Libraries via pip
echo "Configuring Python packages..."
pip install --upgrade pip
pip install pycryptodome requests solders solana

# 6. Verify System Paths
echo "===================================================="
echo "INSTALLATION COMPLETE. VERIFYING COMPILER PATHS:"
echo "===================================================="
echo "Bash version:   $(bash --version | head -n 1)"
echo "Git version:    $(git --version)"
echo "Python version: $(python3 --version)"
echo "Node version:   $(node --version)"
echo "Java version:   $(javac --version | head -n 1)"
echo "===================================================="
