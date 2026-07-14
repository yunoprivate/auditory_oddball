import psychtoolbox.audio as audio
devices = [
    {
        'name': dev['DeviceName'],
        'fs': dev['DefaultSampleRate'],
        'latency': dev['LowOutputLatency'],
    }
    for dev in audio.get_devices()
    if dev['NrOutputChannels'] > 0 and dev['HostAudioAPIName'] == 'Windows WASAPI'
]

print('=== Available Devices ===')
print(
    f'{"Index":<6} '
    f'{"Device Name":<45} '
    f'{"FS [Hz]":<8} '
    f'{"Latency [ms]":<12}'
)
print('-' * 74)
for i, dev in enumerate(devices):
    print(
        f'{i:<6} '
        f'{dev["name"]:<45} '
        f'{dev["fs"]:<8} '
        f'{dev["latency"]*1000:<12.3f}'
    )

while True:
    try:
        idx = int(input('Select Speaker: '))
        if 0 <= idx < len(devices):
            break
        print('Invalid number.')
    except ValueError:
        print('Please enter an integer.')
from psychopy import prefs
prefs.hardware['audioDevice'] = devices[idx]["name"]

from psychopy.hardware.speaker import SpeakerDevice
temp = SpeakerDevice()
print(temp.getAvailableDevices())
temp.testDevice()
print(prefs.hardware)