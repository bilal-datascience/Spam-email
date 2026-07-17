# Simple Spam Identifier

A basic Python script that checks email text against common spam keywords 
and tells you whether an email is likely spam or safe.

# How It Works
The script checks the user's email text against a predefined list of spam 
keywords (like "free", "winner", "prize", "cash", "lottery", "click here", 
"urgent"). If any keyword matches, it shows a warning along with the matched words.

# Example
**Input:** "You are the winner of a free cash prize!"  
**Output:** ⚠️ Alert: This might be Spam! (matched: winner, free, cash, prize)
