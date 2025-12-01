#!/usr/bin/env ruby

# Get current version
current = `git describe --tags --abbrev=0 2>/dev/null`.strip
current = "v0.0.0" if current.empty?

# Parse and increment
major, minor, _ = current.scan(/\d+/).map(&:to_i)
next_ver = "v#{major}.#{minor + 1}.0"

puts "Bumping: #{current} -> #{next_ver}"

# Tag and push
if system("git tag -a #{next_ver} -m 'Release #{next_ver}'")
  system("git push origin #{next_ver}")
else
  abort "Failed to create tag"
end
