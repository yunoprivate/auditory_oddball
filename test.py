import psychtoolbox.audio as audio
devices = audio.get_devices()

print('=== Audio Output Devices ===')

for device in devices:
    if device['NrOutputChannels'] > 0:
        print(f"{device['DeviceName']} ({device['DeviceID']})")