from PIL import Image

# 1. Open your large PNG image
# Replace 'logo.png' with your actual image file name
img = Image.open("log.png")

# 2. Define the sizes a professional Windows icon needs
# (Windows uses different sizes for Taskbar, Desktop, File Explorer, etc.)
icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# 3. Save as .ico with all sizes included
img.save("log.ico", format='ICO', sizes=icon_sizes)

print("Success! Created log.ico with multiple sizes.")