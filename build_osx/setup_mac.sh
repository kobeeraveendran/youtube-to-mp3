# install homebrew
echo "Installing dependencies..."

echo "Installing Homebrew..."
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
printf "----\ndone\n----"

# using homebrew, install ffmpeg
echo "Installing FFmpeg..."
brew install ffmpeg
printf "----\ndone\n----"

echo "Setup complete"