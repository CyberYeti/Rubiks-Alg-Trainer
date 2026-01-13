import time

class Algorithm:
    def __init__(self, name):
        self.name = name
        self.status = "New" # New, Learning, Graduated
        self.step_index = 0 # Current position on the ladder
        self.next_due_at = 0
        self.ease_factor = 2.5 # For graduated algs
        self.interval = 0

class CubeSRS:
    def __init__(self):
        # CONFIGURATION
        self.MAX_ACTIVE_SLOTS = 5
        self.LEARNING_LADDER = [1, 3, 6, 12, 20, 35] # The 6 steps
        self.MAINTENANCE_CAP = 50 # Max interval for graduated cards
        
        # STATE
        self.total_solves = 0
        self.active_slots = [] # Holds Algorithm objects
        self.graduated_pile = [] # Holds Algorithm objects
        
        # MOCK DATABASE OF ALGS TO LEARN
        self.new_queue = [
            Algorithm("T-Perm"), Algorithm("Jb-Perm"), Algorithm("Y-Perm"),
            Algorithm("H-Perm"), Algorithm("Ua-Perm"), Algorithm("Ub-Perm"),
            Algorithm("F-Perm"), Algorithm("V-Perm"), Algorithm("Na-Perm"),
            Algorithm("Nb-Perm"), Algorithm("Ga-Perm"), Algorithm("Gb-Perm")
        ]

    def fill_slots(self):
        """Auto-pulls new algs if slots are open."""
        while len(self.active_slots) < self.MAX_ACTIVE_SLOTS and self.new_queue:
            new_alg = self.new_queue.pop(0)
            new_alg.status = "Learning"
            new_alg.step_index = 0
            new_alg.next_due_at = self.total_solves + self.LEARNING_LADDER[0]
            self.active_slots.append(new_alg)
            print(f"🆕 NEW ALG ADDED: {new_alg.name}")

    def get_next_card(self):
        """Decides which card to show based on Priority Logic."""
        all_active = self.active_slots + self.graduated_pile
        
        if not all_active:
            return None, "Empty"

        # 1. PRIORITY: Strictly Due (Overdue)
        # Sort by who is most overdue (smallest next_due_at)
        due_cards = [c for c in all_active if c.next_due_at <= self.total_solves]
        if due_cards:
            # Return the one most overdue
            due_cards.sort(key=lambda x: x.next_due_at)
            return due_cards[0], "Due"

        # 2. GAP FILLER: Grind Mode
        # If nothing is due, pick the Active Learning card with the closest due date
        # We prefer Learning cards for grind over Graduated cards
        learning_only = [c for c in self.active_slots]
        if learning_only:
            learning_only.sort(key=lambda x: x.next_due_at)
            return learning_only[0], "Grind"
        
        # 3. Last Resort: Practice a graduated card early
        all_active.sort(key=lambda x: x.next_due_at)
        return all_active[0], "Grind"

    def process_rating(self, card, rating, mode):
        """Updates algorithm stats based on user rating."""
        
        # LOGIC FOR LEARNING PHASE
        if card.status == "Learning":
            delta = 0
            
            if rating == "a": # Again/Fail
                print(f"❌ Resetting {card.name} steps.")
                card.step_index = max(0, card.step_index - 1) # Step back
                delta = self.LEARNING_LADDER[card.step_index]
            
            elif rating == "g": # Good
                # If in Grind Mode (practicing early), we don't necessarily advance the step
                # unless they are very close to the due date, but for simplicity
                # let's say a Good grind rep counts as a step forward.
                card.step_index += 1
                
                # CHECK GRADUATION
                if card.step_index >= len(self.LEARNING_LADDER):
                    print(f"🎓 GRADUATED: {card.name} moved to Maintenance!")
                    card.status = "Graduated"
                    self.active_slots.remove(card)
                    self.graduated_pile.append(card)
                    card.interval = self.LEARNING_LADDER[-1] * card.ease_factor
                    card.next_due_at = self.total_solves + int(card.interval)
                    return # Exit early
                
                delta = self.LEARNING_LADDER[card.step_index]
            
            card.next_due_at = self.total_solves + delta

        # LOGIC FOR GRADUATED PHASE
        elif card.status == "Graduated":
            if rating == "a": # Fail on a graduated card
                print(f"⚠️ LAPSE: {card.name} sent back to Learning!")
                card.status = "Learning"
                card.step_index = 2 # Start back at Step 3 (not 0)
                self.graduated_pile.remove(card)
                self.active_slots.append(card) # Takes up a slot!
                # Note: If slots are full, this temporarily overflows (6/5), which is fine.
                card.next_due_at = self.total_solves + self.LEARNING_LADDER[2]
            
            elif rating == "g": # Good
                card.interval = min(card.interval * card.ease_factor, self.MAINTENANCE_CAP)
                card.next_due_at = self.total_solves + int(card.interval)

    def run_session(self):
        print("--- 🧊 CUBE SRS PROTOTYPE ---")
        print(f"Rules: Active Limit {self.MAX_ACTIVE_SLOTS} | Cap {self.MAINTENANCE_CAP} solves")
        
        while True:
            self.fill_slots()
            current_card, mode = self.get_next_card()
            
            if not current_card:
                print("All algorithms learned! Add more to queue.")
                break

            # UI Display
            print("\n" + "="*30)
            print(f"SOLVE #{self.total_solves + 1} | Mode: {mode.upper()}")
            print(f"Algorithm: {current_card.name}")
            print(f"Current Status: {current_card.status} (Step {current_card.step_index})")
            print(f"Ideally Due At: Solve #{current_card.next_due_at}")
            
            if mode == "Grind":
                print("💡 (Practicing early to fill gap)")

            # Simulation
            input(f"Press [Enter] to simulate solve...")
            
            # Rating
            rating = ""
            while rating not in ['a', 'g']:
                rating = input("Rating? [a]gain / [g]ood: ").lower()
            
            self.total_solves += 1
            self.process_rating(current_card, rating, mode)

if __name__ == "__main__":
    app = CubeSRS()
    app.run_session()