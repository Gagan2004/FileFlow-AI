   confirm = input("✅ Run this command? (y/n): ").strip().lower()
        if confirm != "y":
            print("⏩ Skipped execution.")
            continue