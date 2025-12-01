# brew install hidapi
devices = MyHIDAPI.enumerate 0x0, 0x0
dev = devices.find { |dev| dev.product_string == "ErgoDox EZ" }

handle = dev.open

while !handle
  p "retry"
  handle = dev.open
end

p handle

buf = [0x0, 0x3, 35]
loop do
  break if handle.write buf.pack('C*')
end
puts "done writing"

buf = handle.read_timeout 1, 500
p buf