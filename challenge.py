import os
from datetime import datetime

# Example: Generate a new challenge file
def generate_challenge():
    date = datetime.now().strftime('%Y-%m-%d')
    challenge_path = f"challenges/{date}-challenge.txt"
    
    os.makedirs("challenges", exist_ok=True)  # Ensure the directory exists
    
    with open(challenge_path, 'w') as file:
        file.write(f"Today's Challenge ({date}):\n")
        file.write("Reverse a string without using built-in functions.\n")
    
    print(f"Challenge for {date} saved to {challenge_path}")

if __name__ == "__main__":
    generate_challenge()
