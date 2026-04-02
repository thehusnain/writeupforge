#!/bin/bash

# WriteupForge Global Installer for Linux
# Author: WriteSec

echo "[!] WriteupForge: Starting Installation..."

# 1. Setup local environment
chmod +x setup_env.sh
./setup_env.sh

# 2. Create the wrapper script
INSTALL_PATH="/usr/local/bin/fgwrite"
APP_DIR=$(pwd)

cat <<EOF > fgwrite
#!/bin/bash
cd $APP_DIR
source venv/bin/activate
python run.py "\$@"
EOF

chmod +x fgwrite

# 3. Move to /usr/local/bin (requires sudo)
echo "[/] Requesting sudo to install globally as 'fgwrite'..."
sudo mv fgwrite $INSTALL_PATH

if [ $? -eq 0 ]; then
    echo "[+] Success! WriteupForge is now installed."
    echo "🚀 You can now run it from anywhere by typing: fgwrite"
else
    echo "❌ Error: Failed to move to $INSTALL_PATH. Ensure you have sudo permissions."
fi
