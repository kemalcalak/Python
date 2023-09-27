import torch

# CUDA kullanılabilir mi?
print(torch.cuda.is_available())

# CUDA cihazlarını listele
print(torch.cuda.device_count())

# Aktif CUDA cihazının adını ve özelliklerini alın
print(torch.cuda.get_device_name(torch.cuda.current_device()))
