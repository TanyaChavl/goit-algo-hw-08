import heapq

def minimize_cable_joining_cost(lengths):
    # Ініціалізуємо мінімальну купу з довжин кабелів
    heapq.heapify(lengths)
    
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(lengths) > 1:
        # Видаляємо два кабелі з найменшою довжиною
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        
        # Об'єднуємо кабелі
        new_length = first + second
        total_cost += new_length
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(lengths, new_length)
    
    return total_cost

# Приклад використання
cable_lengths = [5, 2, 4, 8, 6, 7]
GREEN = "\033[92m"
RESET = "\033[0m"
print(f"{GREEN}Мінімізація загальних витрат на об'єднання кабелів складає: {minimize_cable_joining_cost(cable_lengths)}{RESET}")
