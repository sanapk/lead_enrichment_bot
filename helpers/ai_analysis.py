from config import GEMINI_API_KEY, USE_GEMINI
import google.generativeai as genai

model = None
if USE_GEMINI and GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("models/gemini-1.5-flash")  
    print("Gemini not configured properly")

def analyze_with_llm(homepage_text):
    if not homepage_text.strip() or not model:
        return {"summary": "no content or model available", "pitch": "No content or model not available"}
    trimmed = homepage_text[:500] 

    prompt = f"""
    Based on this homepage content:
    ---
    {trimmed}
    ---
    1. What does this company do?
    2. Who is their target customer?
    3. Suggest a custom AI automation QF Innovate could pitch.
    """

    print("Sending prompt to Gemini...")
    try:
        response = model.generate_content(prompt)
        print("Response received")
        return {
            "summary": response.text.split('\n')[0],
            "pitch": response.text.split('\n')[-1]
        }
    except Exception as e:
        import traceback
        traceback.print_exc()  # Show full error trace
        print(f"Error in LLM: {e}")
        return {"summary": "", "pitch": f"Error: {e}"}
