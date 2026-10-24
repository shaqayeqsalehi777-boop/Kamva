# Adds microphone permission + speech-service visibility to the generated Android manifest
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
if "android.permission.RECORD_AUDIO" not in s:
    s = s.replace("</manifest>", '    <uses-permission android:name="android.permission.RECORD_AUDIO" />\n</manifest>')
if "android.speech.RecognitionService" not in s:
    s = s.replace("</manifest>", '    <queries>\n        <intent>\n            <action android:name="android.speech.RecognitionService" />\n        </intent>\n    </queries>\n</manifest>')
open(p, "w", encoding="utf-8").write(s)
print(s)
