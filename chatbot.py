# College Enquiry Chatbot

print("====================================")
print("   Welcome to College Enquiry Bot")
print(" Type 'exit' to end the chat")
print("====================================")

responses = {
    "admission": "Admissions start in June. Apply through the college website or admission office.",
    "course": "Our college offers BCA, BSc, BCom, MCA, and MBA programs.",
    "fees": "Course fees range from ₹40,000 to ₹80,000 per year depending on the program.",
    "placement": "Our college provides placement support with many companies visiting every year.",
    "hostel": "Yes, hostel facilities are available for both boys and girls.",
    "library": "The library is open from 9 AM to 6 PM with books and digital resources.",
    "contact": "Contact: 9876543210 or email info@college.com"
}

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print("Bot: Thank you for using the College Enquiry Chatbot!")
        break

    found = False

    for keyword in responses:
        if keyword in user_input:
            print("Bot:", responses[keyword])
            found = True

    if not found:
        print("Bot: Sorry, I couldn't understand. Please ask about admission, courses, fees, hostel, placement, or contact.")
