def identify_spam():
    print("--- Simple Spam Identifier ---")
    
    # Spam alfaz ki list
    spam_keywords = ["free", "winner", "prize", "cash", "lottery", "click here", "urgent"]
    
    # User se email text lena
    email_text = input("Email ka message enter karein: ").lower()
    
    # Check karna
    found_keywords = []
    for word in spam_keywords:
        if word in email_text:
            found_keywords.append(word)
    
    # Result dikhana
    if len(found_keywords) > 0:
        print("\n⚠️ Alert: Ye Spam ho sakta hai!")
        print(f"Wajah: Ismein ye alfaz mile hain: {found_keywords}")
    else:
        print("\n✅ Ye email safe lag rahi hai.")

identify_spam()
