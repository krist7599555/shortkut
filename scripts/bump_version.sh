#!/bin/bash
set -e

# Get the latest tag, default to v0.0.0 if none exists
latest=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
echo "Current version: $latest"

# Remove 'v' prefix
ver="${latest#v}"

# Split into array based on '.' delimiter
IFS='.' read -r -a parts <<< "$ver"

major="${parts[0]}"
minor="${parts[1]}"
patch="${parts[2]}"

# Check if we got valid numbers, otherwise default to 0
re='^[0-9]+$'
if ! [[ $major =~ $re ]] ; then major=0; fi
if ! [[ $minor =~ $re ]] ; then minor=0; fi

# Increment minor version
minor=$((minor + 1))
# Reset patch to 0
patch=0

new_tag="v$major.$minor.$patch"
echo "New version: $new_tag"

# Create tag
git tag -a "$new_tag" -m "Release version $new_tag"

# Push tag
git push origin "$new_tag"
