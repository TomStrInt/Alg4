import heapq
import time

class Notification:
    def __init__(self, content, notif_type, priority):
        self.timestamp = time.time()
        self.content = content
        self.notif_type = notif_type
        self.priority = priority  

    def __lt__(self, other):
        
        return self.priority > other.priority or (self.priority == other.priority and self.timestamp < other.timestamp)

class NotificationSystem:
    def __init__(self, low_priority_limit=10):
        self.queue = []  
        self.low_priority_limit = low_priority_limit
        self.low_priority_count = 0

    def add_notification(self, content, notif_type, priority): 
        if priority == 1:  
            if self.low_priority_count >= self.low_priority_limit:
                self._remove_oldest_low_priority()
            self.low_priority_count += 1
        heapq.heappush(self.queue, Notification(content, notif_type, priority))

    def _remove_oldest_low_priority(self):
        for i in range(len(self.queue)):
            if self.queue[i].priority == 1:
                self.low_priority_count -= 1
                del self.queue[i]
                heapq.heapify(self.queue)
                break

    def get_next_notification(self):
        if self.queue:
            notification = heapq.heappop(self.queue)
            if notification.priority == 1:
                self.low_priority_count -= 1
            return notification
        return None

    def count_pending_notifications(self):
        return len(self.queue)

notif_system = NotificationSystem(low_priority_limit=5)

notif_system.add_notification("Masz nowe zadanie!", "info", 2)
notif_system.add_notification("Instalacja dobiegla konca", "warning", 3)
notif_system.add_notification("Błąd krytyczny: Kernel panic", "error", 4)
notif_system.add_notification("Przypomnienie: Masz rozmowe na teamsie", "info", 1)  # niski priorytet

while notif_system.count_pending_notifications() > 0:
    next_notif = notif_system.get_next_notification()
    if next_notif:
        print(f"[{next_notif.notif_type.upper()}] {next_notif.content} (czas: {time.ctime(next_notif.timestamp)})")
