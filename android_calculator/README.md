# Android Calculator

This project uses Python and Kivy.

## Run on Linux desktop

```bash
cd /home/kazuma/Code-OSS/android_calculator
/home/kazuma/Code-OSS/.venv/bin/python main.py
```

## Build an APK on Linux

```bash
pip install buildozer
buildozer init
buildozer -v android debug
```

Building Android apps requires Android SDK/NDK dependencies and can take a long time. The APK is created in `bin/`.
