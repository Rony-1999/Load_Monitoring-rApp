import time, json, requests
from config import POLICY_MANAGER_URL, THROUGHPUT_THRESHOLD, PRB_THRESHOLD

created_policies = []
policytype_counter = 0

def trigger_policy_creation(ric_id, field, value):
    global policytype_counter
    policy_id = f"policy_{ric_id}_{int(time.time())}"
    policytype_counter += 1

    service_id = "THROUGHPUT_MANAGEMENT" if field == "DRB.UEThpDl" else "PRB_MANAGEMENT"
    action = "Adjust Bandwidth allocation" if field == "DRB.UEThpDl" else "Optimize PRB allocation"

    policy = {
        "ric_id": ric_id,
        "policy_id": policy_id,
        "service_id": service_id,
        "policy_data": {
            "field": field,
            "value": value,
            "threshold": THROUGHPUT_THRESHOLD if field == "DRB.UEThpDl" else PRB_THRESHOLD,
            "action": action
        },
        "policytype_id": policytype_counter
    }

    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(POLICY_MANAGER_URL, json=policy, headers=headers, timeout=15)
        print(f"[RESPONSE] {response.status_code} - {response.text}")
        if response.status_code == 200:
            created_policies.append(policy)
            return True
        else:
            return False
    except Exception as e:
        print(f"[ERROR] Failed to create policy: {e}")
        return False

