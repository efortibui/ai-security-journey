print("=== AI SECURITY SYSTEM PROFILE ===")
system_name = "Finance AI Assistant"
owner = "CFO's Office"
classification = "Secret"

risk_score = 9
monthly_cost = 63.50

internet_access = True
contains_pii = True
mfa_enabled = False
encryption_enabled = False

print("System:", system_name)
print("Owner:", owner)
print("Classification:", classification)
print("Risk Score:", risk_score)
print("Monthly Cost:", monthly_cost)
print("Internet Access:", internet_access)
print("Contains PII:", contains_pii)
print("MFA Enabled:", mfa_enabled)
print(type(system_name))
print(type(risk_score))
print(type(monthly_cost))
print(type(mfa_enabled))
if risk_score >= 8:
    print("Security Alert: HIGH RISK AI SYSTEM")
if risk_score >= 9:
    print("Risk Classification: CRITICAL")

elif risk_score >= 7:
    print("Risk Classification: HIGH")

elif risk_score >= 4:
    print("Risk Classification: MODERATE")

else:
    print("Risk Classification: LOW")

if contains_pii == True:
    print("Security Notice: System contains PII")

if internet_access == True:
    print("Security Notice: System is exposed to the internet")

if mfa_enabled == False:
    print("Security Warning: MFA is not enabled")
if contains_pii and internet_access and not mfa_enabled:
    print("CRITICAL: PII system is internet-facing without MFA")
if contains_pii and not encryption_enabled:
    print("Security Warning: Sensitive data is not encrypted")
if internet_access or contains_pii:
    print("System requires enhanced security review")

security_findings = [
    "Missing MFA",
    "Unencrypted PII",
    "Internet Exposure",
    "Outdated Software"
]

print(security_findings)

print(security_findings[0])
print(security_findings[1])
print(security_findings[2])
print(security_findings[3])

security_findings.append("Excessive Privileges")
print(security_findings)
print("Number of Findings:", len(security_findings))

print("\n=== SECURITY FINDINGS ===")

for finding in security_findings:
    print("-", finding)

security_controls = [
    "MFA",
    "Encryption",
    "Logging",
    "Access Control"
]

print("\n=== SECURITY CONTROLS ===")

for control in security_controls:
    print("-", control)

ai_system = {
    "name": "Finance AI Assistant",
    "owner": "CFO's Office",
    "classification": "Secret",
    "risk_score": 9,
    "internet_access": True,
    "contains_pii": True,
    "mfa_enabled": False,
    "encryption_enabled": False,
    "DAR_enabled": False
}

print("\n=== AI SYSTEM DICTIONARY ===")
print(ai_system)

print("System Name:", ai_system["name"])
print("Owner:", ai_system["owner"])
print("Risk Score:", ai_system["risk_score"])

if ai_system["contains_pii"] and not ai_system["mfa_enabled"]:
    print("Security Alert: PII is present and MFA is disabled")

if ai_system["contains_pii"] and not ai_system["encryption_enabled"]:
    print("CRITICAL FINDING: PII is not encrypted")

def display_security_message():
    print("\n=== AI SECURITY ASSESSMENT ===")
    print("Beginning security analysis...")

display_security_message()

def assess_risk(score):
    if score >= 9:
        print("Risk Level: CRITICAL")
    elif score >= 7:
        print("Risk Level: HIGH")
    elif score >= 4:
        print("Risk Level: MODERATE")
    else:
        print("Risk Level: LOW")

assess_risk(9)

def assess_ai_system(system):
    print("\n=== AUTOMATED SECURITY ASSESSMENT ===")
    print("System:", system["name"])

    if system["contains_pii"]:
        print("- Finding: System processes PII")

    if system["internet_access"]:
        print("- Finding: System has internet access")

    if not system["mfa_enabled"]:
        print("- Finding: MFA is disabled")

    if not system["encryption_enabled"]:
        print("- Finding: Encryption is disabled")

    if not system["DAR_enabled"]:
        print("- Finding: DAR is disabled") 

    if system["contains_pii"] and not system["mfa_enabled"]:
         print("- CRITICAL: PII present without MFA")

assess_ai_system(ai_system)