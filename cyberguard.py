import re

print("=" * 40)
print("       CYBERGUARD AI")
print("    PHISHING DETECTOR")
print("=" * 40)

text = input("\nEnter Message or URL: ")

score = 0
reasons = []

suspicious_words = [
    "win",
    "winner",
    "prize",
    "urgent",
    "verify",
    "claim",
    "free",
    "password"
]

for word in suspicious_words:
    if word in text.lower():
        score += 1
        reasons.append("Suspicious word detected: " + word)

if re.search(r"https?://", text):
    score += 1
    reasons.append("Link detected")

if score >= 3:
    result = "HIGH RISK"
elif score >= 1:
    result = "MEDIUM RISK"
else:
    result = "LOW RISK"

print("\nResult:", result)

print("\nReasons:")

if reasons:
    for reason in reasons:
        print("-", reason)
else:
    print("- No obvious suspicious pattern found")

print("\nSafety Advice:")
print("Do not open unknown or suspicious links.")

print("\n" + "=" * 40)
print("Educational Cyber Security Project")
print("=" * 40)
