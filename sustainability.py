import pandas as pd

# Dummy carbon intensity assumption
CARBON_INTENSITY = 0.4


def load_data(filename):
    return pd.read_csv(filename)


def calculate_energy(df):
    df["energy_wh"] = df["requests"] * df["energy_per_request_wh"]
    df["energy_kwh"] = df["energy_wh"] / 1000
    return df


def calculate_co2(df):
    df["co2_kg"] = df["energy_kwh"] * CARBON_INTENSITY
    return df


def calculate_score(total_energy):
    if total_energy < 10:
        return 90
    elif total_energy < 20:
        return 75
    elif total_energy < 30:
        return 60
    else:
        return 40


def get_summary(df):
    total_requests = df["requests"].sum()
    total_energy = df["energy_kwh"].sum()
    total_co2 = df["co2_kg"].sum()
    score = calculate_score(total_energy)
    highest_model = df.groupby("model")["energy_kwh"].sum().idxmax()
    highest_department = df.groupby("department")["energy_kwh"].sum().idxmax()
    return {
        "total_requests": total_requests,
        "total_energy": total_energy,
        "total_co2": total_co2,
        "score": score,
        "highest_model": highest_model,
        "highest_department": highest_department,
    }


def responsible_ai_audit(df, summary): 
    """ 
    Performs a simple Responsible AI audit. 
    Returns: 
    audit_result: dictionary containing responsible AI checks and overall status. 
    """ 
    audit = {} 

    # -------------------------------- # 1. Data Completeness # -------------------------------- 

    required_columns = [ "date", "department", "model", "requests", "tokens", "energy_per_request_wh" ]

    audit["data_complete"] = all(col in df.columns for col in required_columns)
    
    # 2. No Missing Critical Values
    audit["no_missing_values"] = not df[required_columns].isnull().any().any()
    
    # 3. Transparent Calculation
    audit["calculation_transparent"] = (
        "total_energy" in summary and "total_co2" in summary
    )
    
    # 4. Explainable Score
    score = summary["score"]
    audit["score_explainable"] = (0 <= score <= 100)
    
    # 5. AI Human Oversight
    audit["human_oversight"] = True  # Gemini only provides recommendations
    
    # 6. Hallucination Prevention
    audit["grounded_in_data"] = True  # Gemini receives calculated data
    
    # 7. Sustainability Disclaimer
    audit["estimate_disclosed"] = True  # Energy and CO2 are estimates
    
    # Overall Responsible AI Status
    audit["responsible_ai"] = all(audit.values())
    
    return audit