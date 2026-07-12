print("=" * 40)
print("🚀 Welcome to Freedom AI v0.1")
print("=" * 40)

def business_idea():
    print("\n💡 Business Idea")
    print("Look for repetitive tasks businesses do every day.")

def daily_motivation():
    print("\n🔥 Daily Motivation")
    print("Small improvements every day become massive improvements over time.")

def automation_idea():
    print("\n🤖 Automation Idea")
    print("Think of one task at work that someone repeats every single day.")

print("1. Business Ideas")
print("2. Daily Motivation")
print("3. Automation Ideas")
print("4. Exit")

choice = input("\nChoose an option (1-4): ")
if choice == "1":
    business_idea()

elif choice == "2":
    daily_motivation()

elif choice == "3":
    automation_idea()

elif choice == "4":
    print("\n👋 Thanks for using Freedom AI!")

else:
    print("\n❌ Invalid option. Please choose 1-4.")
    