import pandas as pd
import numpy as np
from faker import Faker
import random
import datetime

# Initialize Faker
fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# Parameters
num_rows = 1500
regions = ["Nairobi", "Central", "Western", "Nyanza", "Rift Valley", "Coast", "Eastern", "North Eastern"]
policy_types = ["Comprehensive", "Third Party", "Life", "Health", "Property"]
incident_types = ["Accident", "Theft", "Fire", "Medical", "Natural Disaster", "Other"]
statuses = ["Approved", "Pending", "Cancelled", "Rejected"]
genders = ["Male", "Female"]

# Helper to introduce dirty data
def introduce_noise(value, noise_type="missing"):
    if noise_type == "missing":
        return np.nan
    elif noise_type == "wrong_type":
        return "???"
    elif noise_type == "typo":
        return str(value)[:3] + "xx"
    return value

# Set dates
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)

# Data generation
data = []
for i in range(num_rows):
    claim_id = f"CLM{1000 + i}"
    customer_id = f"CUST{random.randint(10000, 99999)}"
    # Generate National ID as a 8-digit number without hyphens
    national_id = fake.random_number(digits=8, fix_len=True) if random.random() > 0.05 else introduce_noise("", "missing")
    policy_type = random.choice(policy_types)
    region = random.choice(regions)
    claim_date = fake.date_between(start_date=start_date, end_date=end_date)
    claim_amount = round(random.uniform(1000, 500000), 2)
    status = random.choice(statuses)
    policy_start = fake.date_between(start_date=datetime.date(2022, 1, 1), end_date=claim_date)
    premium_amount = round(random.uniform(2000, 100000), 2)
    customer_age = random.randint(18, 75)
    incident_type = random.choice(incident_types)
    gender = random.choice(genders)

    # Introduce dirty data in 20% of rows
    if random.random() < 0.2:
        field_to_dirty = random.choice(["claim_amount", "premium_amount", "customer_age", "region", "gender", "claim_date", "national_id"])
        if field_to_dirty == "claim_amount":
            claim_amount = introduce_noise(claim_amount, "wrong_type")
        elif field_to_dirty == "premium_amount":
            premium_amount = introduce_noise(premium_amount, "missing")
        elif field_to_dirty == "customer_age":
            customer_age = introduce_noise(customer_age, "wrong_type")
        elif field_to_dirty == "region":
            region = introduce_noise(region, "typo")
        elif field_to_dirty == "gender":
            gender = introduce_noise(gender, "missing")
        elif field_to_dirty == "claim_date":
            claim_date = introduce_noise(claim_date, "wrong_type")
        elif field_to_dirty == "national_id":
            national_id = introduce_noise(national_id, "wrong_type")

    data.append([
        claim_id, customer_id, policy_type, region, claim_date, claim_amount, status,
        policy_start, premium_amount, customer_age, incident_type, gender, national_id
    ])

# Create DataFrame
columns = [
    "Claim ID", "Customer ID", "Policy Type", "Region", "Claim Date", "Claim Amount",
    "Status", "Policy Start Date", "Premium Amount", "Customer Age", "Incident Type",
    "Gender", "National ID"
]
df_dirty = pd.DataFrame(data, columns=columns)

# Save to CSV
df_dirty.to_csv("insurance1_data.csv", index=False)
print("✅ Data saved as 'kenya_insurance_dirty_data.csv'")
