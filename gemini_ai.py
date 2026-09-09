import os
from google import genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

mykey = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=mykey)

def get_sustainability_advice(summary):
    prompt=f"""
    You are a Sustainable AI consultant. 
    Analyze the following AI usage information. 
    
    AI REQUESTS: {summary["total_requests"]} 
    
    TOTAL ENERGY: {summary["total_energy"]:.2f} kWh 
    
    ESTIMATED CO2: {summary["total_co2"]:.2f} kg 
    
    SUSTAINABILITY SCORE: {summary["score"]}/100 
    
    HIGHEST ENERGY AI MODEL: {summary["highest_model"]} 

    HIGHEST ENERGY DEPARTMENT: {summary["highest_department"]} 
    
    Provide a concise sustainability report. 
    Include: 
    1. Overall assessment 
    2. Main sustainability problem 
    3. Three practical recommendations 
    4. How smaller AI models could help 
    5. How unnecessary AI requests can be reduced 
    6. A short Responsible AI recommendation 
    
    Important rules: 
    - Use ONLY the supplied data. 
    - Do not invent measurements. 
    - Clearly say that the energy and CO2 values are estimates based on assumptions. 
    - Do not claim that the values represent actual datacenter measurements. 
    - Keep the explanation suitable for students. 
    """

    response = client.models.generate_content(model="gemini-3.7-flash",contents=prompt)
    return response.text