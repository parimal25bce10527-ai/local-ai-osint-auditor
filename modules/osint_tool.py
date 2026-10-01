# modules/osint_tool.py

def get_mock_osint_data(username):
    """
    Mock OSINT data. 
    In a real production environment, this would connect to Hiker API or instagrapi.
    For this open-source demo, we return realistic simulated data.
    """
    print(f"[*] Simulating OSINT data collection for @{username}...")
    
    # We create a realistic text block that the AI can analyze for privacy leaks
    mock_data = f"""
    --- OSINT DATA FOR @{username} ---
    Full Name: John Doe
    Biography: "Software Engineer @ TechCorp | Austin, TX 📍 | Coffee addict ☕ | Dog dad to Max 🐶"
    Followers: 1,245
    Following: 890
    Posts: 142
    External URL: https://johndoe.dev
    
    --- RECENT POSTS ---
    [1] Caption: "Early morning run around Lady Bird Lake before my 9 AM standup! 🏃‍♂️"
    [2] Caption: "Huge win for the team today! Celebrating at the TechCorp office downtown 🍻"
    [3] Caption: "Weekend trip to Dallas to visit the parents. Max loves the car ride! 🚗"
    [4] Caption: "Late night debugging session. Thanks for the pizza, @SarahJane! 🍕"
    
    --- SAMPLE FOLLOWERS ---
    @sarahjane
    @techcorp_hr
    @max_the_dog
    @austinrunners
    """
    return mock_data