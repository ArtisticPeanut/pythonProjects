from pushbullet import Pushbullet

# Replace 'YOUR_API_KEY' with your actual Pushbullet API key
pb = Pushbullet('o.hfSU0YeVUEBdpjT7uimYg7xwuhBF3HvZ')

# Get a list of your devices
devices = pb.devices
print(devices)

# Choose the device where you want to receive notifications (e.g., your computer)
target_device = None
for device in devices:
    if device.nickname == 'Your Computer Name':  # Replace with your computer's name
        target_device = device

if target_device:
    # Send a test notification
    push = target_device.push_note("Notification from Phone", "This is a test notification.")
    print("Notification sent successfully.")
else:
    print("Target device not found.")
