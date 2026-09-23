print("=== AI SECURITY SYSTEM PROFILE ===")
system_name = "Finance AI Assistant"
owner = "CFO's Office"
classification = "Secret"

risk_score = 9
monthly_cost = 63.50

internet_access = False
contains_pii = True
mfa_enabled = True

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