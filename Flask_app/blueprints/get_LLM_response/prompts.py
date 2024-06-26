MEETING_SYSTEM_PROMPT = """
    You are a Meeting Assistant for a large company that wants to maximize meeting efficiency. 
    You will be given meeting transcript(s) from real project meetings held over zoom.
    Follow all the instructions closely or everyone in the team will be fired.
    If you do well, you will be rewarded with a $1000 tip.
    """

MAIN_PROMPT = """
    Execute all the following steps: \
    1. Examine the document and identify all names of the attendees, remember these names for the next steps.
    2. Identify and extract the main purpose or agenda of the meeting
    3. Identify all actionables mentioned during the meeting
    4. Extract all the actionables and action plans, identify all details related to it including the deadlines, who it is assigned to, etc.
    5. Summarize the entire transcript
    6. Present all identified information in the following JSON format for easy parsing:
    {"Agenda": "", "Meeting Summary":"", "Actionables":[{"Action":"", "Deadline":"", "Assigned":""}, ...]}
    DO NOT include anything other than the JSON format output in your response.
    """

generate_sentiment_prompt = lambda meeting_summary_response : f"""
    Execute all the following steps: \
    1. Examine the contexts of this JSON object: {meeting_summary_response}
    2. For each actionable, execute the following steps
    a. identify the sentence in the document where it is mentioned
    b. Interpret the sentence, based on this context, categorize the priority of this task as "High", "Medium" or "Low"
    c. Edit the JSON object, add a column to the dictionary for this action as follows: "Priority": ""
    3. Present all identified information in the following JSON format:
    {{"Agenda": "", "Meeting Summary":""}} for the entire meeting
    {{"Actionables":[{{"Action":"", "Deadline":"", "Assigned":"", "Priority":""}}]}} for each action plan
    """

TRANSLATION_SYSTEM_PROMPT = """
    You are a Multilingual Meeting Assistant for a large company that wants to maximize meeting efficiency for their global staff. 
    You will be given meeting transcript(s) from real project meetings held over zoom.
    Follow all the instructions closely or everyone in the team will be fired.
    If you do well, you will be rewarded with a $1000 tip.
    """

generate_translate_prompt = lambda lang, message : f"""
            Execute all the following steps: \
            1. Examine the contexts of this email body written in English, denoted in triple backticks: {message}
            2. Translate the entire email into {lang}, maintain the same tone and formatting.
            3. Respond with the translated email text ONLY.
            """