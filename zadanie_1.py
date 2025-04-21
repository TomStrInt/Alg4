class ActionManager:
    def __init__(self):
        self.undo_stos = []  # Stos dla operacji UNDO
        self.redo_stos = []  # Stos dla operacji REDO

    def add_action(self, action):
        #Dodaje akcję do stosu UNDO i czyści stos REDO
        self.undo_stos.append(action)
        self.redo_stos.clear()
        print(f"Dodano akcję: {action}")

    def undo(self):
        #Cofanie ostatniego polecenia (UNDO)
        if not self.undo_stos:
            print("Brak akcji do cofnięcia.")
            return
        action = self.undo_stos.pop()
        self.redo_stos.append(action)
        print(f"Cofnięto: {action}")

    def redo(self):
        #Ponowne wykonanie cofniętego polecenia --REDO
        if not self.redo_stos:
            print("Brak akcji do ponownego wykonania.")
            return
        action = self.redo_stos.pop()
        self.undo_stos.append(action)
        print(f"Ponownie wykonano: {action}")

    def delete(self, action_to_delete):
        #Usuwanie określonej akcji ze stosu UNDO
        if action_to_delete in self.undo_stos:
            self.undo_stos.remove(action_to_delete)
            print(f"Usunięto akcję: {action_to_delete}")
        else:
            print("Nie znaleziono akcji do usunięcia w stosie UNDO.")


manager = ActionManager()

manager.add_action("Rysowanie krzywej")
manager.add_action("Rysowanie okręgu")
manager.add_action("Wypelnianie kolorem")
manager.undo()  # Cofnięcie 
manager.redo()  # Ponowne wykonanie polecenia
manager.delete("Rysowanie krzywej")  
