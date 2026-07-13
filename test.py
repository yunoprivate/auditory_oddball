import psychtoolbox.audio as audio
devices = audio.get_devices()

print('=== Audio Output Devices ===')

for dev in devices:
    if dev['NrOutputChannels'] > 0:
        print(
            int(dev['DeviceIndex']),
            dev['HostAudioAPIName'],
            dev['DeviceName'],
            int(dev['DefaultSampleRate']),
            dev['LowOutputLatency'],
        )

while True:
    try:
        idx = int(input('Select audioDevice: '))
        if 0 <= idx < len(devices):
            break
        print('Invalid number.')
    except ValueError:
        print('Please enter an integer.')
print(devices[idx])