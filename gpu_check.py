import torch

print('Torch version: ',torch.__version__)
mps_device = str(torch.device('mps'))
device_check = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
if mps_device == 'mps':
    print('Metal GPU available')
else:
    print('Device available: {}'.format(device_check))