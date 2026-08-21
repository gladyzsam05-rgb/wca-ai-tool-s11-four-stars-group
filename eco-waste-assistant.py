import os
import json
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ECO WASTE ASSISTANT

print("ECO WASTE ASSISTANT")
print("1. Analyze My Waste")
print("2. Get a Waste Disposal Action Plan")
print("3. Exit")

choice = input("Choose an option: ")


# STAGE 1: WASTE ANALYSIS

if choice == "1":

    print("You selected: Analyze My Waste")

    waste = input(
        "What type of waste do you need help with? "
    )
    if not waste.strip():
        print("Please enter at least one waste item.")
        exit()

    # R-T-C-C-O PROMPT - STAGE 1

    prompt = f"""
ROLE:
You are an AI waste-management assistant.

TASK:
Analyze and classify each waste item provided by the user.

CONTENT:
For each waste item, identify:
- waste_item
- waste_category
- reuse_possibility
- recycling_possibility
- environmental_concern

CONSTRAINTS:
- Analyze each waste item separately.
- Do not combine different waste items.
- Give clear, simple and practical answers.
- Do not invent specific local recycling facilities.
- Return only valid JSON.
- Use exactly the fields specified in the output format.
- Classify waste using clear categories such as organic, recyclable,hazadous,electronic,or general on the characteristic of the waste item provided.
- Base the classification on the characteristics of the waste item provided.
- If an item could reasonably fit more than ony category, select the most appropriate primary category and explain the environmental concern.

OUTPUT:
Return a JSON object containing a "waste_items" list.

Each waste item must contain exactly these fields:
- waste_item
- waste_category
- reuse_possibility
- recycling_possibility
- environmental_concern

USER INPUT:
{waste}
"""

    # AI CALL 1
    
try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

except Exception as e:
    print("\n Sorry, the AI service could not analyze your waste.")
    print("Error:", e)
    exit()

# Convert Stage 1 JSON into Python data
try:
      
    analysis = json.loads(response.text)
except json.JSONDecodeError:
    print("\nSorry, the AI returned an invalid response.")
    print("Please try again.")
    exit()


print("\n--- STAGE 1: WASTE ANALYSIS ---")
try:
    waste_items = analysis["waste_items"]
except KeyError:
   print("\nSorry , the AI response is missing the expected 'waste_items' field.")
   print("please try again.")
   exit()

for item in analysis["waste_items"]:

        print("\n--- WASTE CLASSIFICATION ---")
        print("Waste item:", item["waste_item"])
        print("Category:", item["waste_category"])
        print(
            "Reuse possibility:",
            item["reuse_possibility"]
        )
        print(
            "Recycling possibility:",
            item["recycling_possibility"]
        )
        print(
            "Environmental concern:",
            item["environmental_concern"]
        )

# STAGE 2: ACTION PLAN

action_prompt = f"""
ROLE:
You are an AI waste-management action planner.

TASK:
Create a practical action plan based on the Stage 1 waste analysis.

CONTEXT:
Here is the result from Stage 1:

{json.dumps(analysis, indent=2)}

For each waste item, provide:
- separation
- reuse
- recycling
- handling
- waste_reduction

CONSTRAINTS:
- Use the Stage 1 analysis provided above.
- Analyze each waste item separately.
- Give clear, simple and practical recommendations.
- Do not invent specific local recycling facilities.
- Do not change the waste classifications from Stage 1.
- Return only valid JSON.

OUTPUT:
Return a JSON object containing an "action_plans" list.

Each action plan must contain exactly these fields:
- waste_item
- separation
- reuse
- recycling
- handling
- waste_reduction
"""

        # SECOND GEMINI API CALL

try:
        action_response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=action_prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

except Exception as e:
        print("\nSorry, the AI service could not create the action plan.")
        print("Please try again later.")
        print("Error:", e)
        exit()

    # Convert Gemini's JSON response into Python data
try:
    action_plan = json.loads(action_response.text)
except json.JSONDecodeError:
    print("\nSorry, the AI returned an invalid action plan.")
    print("Please try again.")
    exit()   

    # Display Stage 2

print("\n--- STAGE 2: ACTION PLAN ---")

for plan in action_plan["action_plans"]:
        print("\nWaste item:", plan["waste_item"])
        print("Separation:", plan["separation"])
        print("Reuse:", plan["reuse"])
        print("Recycling:", plan["recycling"])
        print("Handling:", plan["handling"])
        print("Waste reduction:", plan["waste_reduction"])

# SAVE FINAL RESULT

final_result = {
        "stage_1_waste_analysis": analysis,
        "stage_2_action_plan": action_plan
    }

with open("eco_waste_result.json", "w", encoding="utf-8") as file:
        json.dump(final_result, file, indent=4)

print("\nFinal result saved to eco_waste_result.json")
   
