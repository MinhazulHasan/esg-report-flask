
def get_report_prompt_financial():
    PROMPT_TEMPLATE = """
**Query:** {query}  
**Expected Value:** {expected_value}

**Response Guidelines:**

1. **If the YEAR-WISE information is NOT available:**  
   Respond with a valid JSON format:  
    {{
        "available": "NO"
    }}

2. **If the YEAR-WISE information is available:**  
   Provide a concise summary in valid JSON format, ensuring that:  
   - Records with zero values are excluded.  
   - The data includes the year and its corresponding value along with the unit.
   - YOU MUST consider the expected value and provide the response accordingly.
   Example:  
    {{
        "available": "YES",
        "response": [
            {{
                "Year": "YYYY",
                "Data": "Data unit"
            }},
            {{
                "Year": "YYYY",
                "Data": "Data unit"
            }}
        ]
    }}

**Important Notes:**  
- YOU MUST Follow the JSON format strictly.  
- YOU ARE BOUND TO Provide only the JSON response without any additional content, symbols, or explanations like ``` or **.
- Any deviation from the above structure will be considered invalid response.
"""
    return PROMPT_TEMPLATE



def get_report_prompt_esg():
    PROMPT_TEMPLATE = """
**Query:** {query}
**Expected Value:** {expected_value}

Strictly Follow these response guidelines:
    - If the required information is NOT AVAILABLE in the context, respond with a valid JSON Format:
     {{
          "available": "NO"
     }}
    - If the information is available, provide a concise summary formatted as a valid JSON Format:
        {{
            "available": "YES",
            "response": "{response}"
        }}

"""
    return PROMPT_TEMPLATE



def get_report_prompt_boolean():
    PROMPT_TEMPLATE = """
**Query:** {query}  
**Expected Value:** {expected_value}

**Response Guidelines:**

1. **If the information is NOT available:**
    Respond strictly in the following JSON format:
    {{
        "available": "NO"
    }}

2. **If the information is available:**  
   Instructuions:
   - YOU MUST evaluate the query and respond only with the **Expected Value**
   - Do not include any explanations, descriptions, or additional information other than {expected_value}.
   - Follow this JSON format strictly: 
    {{
        "available": "YES",
        "response": "{expected_value}"
    }}

**Important Notes:**  
- YOU MUST Follow the JSON format strictly. 
- YOU ARE BOUND TO Provide only the JSON response without any additional content, symbols, or explanations like ``` or **.
- Any deviation from the above structure will be considered invalid response.
"""
    return PROMPT_TEMPLATE



def get_report_prompt_miscellaneous():
    PROMPT_TEMPLATE = """
**Query:** {query}  
**Expected Value:** {expected_value}

**Response Guidelines:**

1. **If the information is NOT available:**
    Respond strictly in the following JSON format:
    {{
        "available": "NO"
    }}

2. **If the information is available:**  
   Instructuions:
   - YOU MUST evaluate the query and respond only focus with the **Expected Value**.
   - Do not include any explanations, descriptions, or additional information.
   - Response as short as possible.
   - Follow this JSON format strictly: 
    {{
        "available": "YES",
        "response": "response"
    }}

**Important Notes:**  
- YOU MUST Follow the JSON format strictly. 
- YOU ARE BOUND TO Provide only the JSON response without any additional content, symbols, or explanations like ``` or **.
- Any deviation from the above structure will be considered invalid response.
"""
    return PROMPT_TEMPLATE
