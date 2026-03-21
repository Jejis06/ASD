import random
import string
import time
import sys

# Importujemy Twoje rozwiązanie z pliku sol.py
try:
    from sol import solution
except ImportError:
    print("❌ Błąd: Nie znaleziono pliku 'sol.py' lub funkcji 'solution' w tym pliku.")
    sys.exit(1)

# ==========================================
# 1. ROZWIĄZANIE BRUTE-FORCE (Wzorzec)
# ==========================================
def brute_force_solution(T: list[str]) -> int:
    """Naiwne rozwiązanie O(n^2), na 100% poprawne. Służy do weryfikacji."""
    n = len(T)
    max_dominance = 0
    for i in range(n):
        current_dominance = 0
        for j in range(i):
            if T[j] < T[i]:
                current_dominance += 1
        max_dominance = max(max_dominance, current_dominance)
    return max_dominance

# ==========================================
# 2. GENERATOR SŁÓW
# ==========================================
def generate_random_words(n, min_len, max_len):
    """Generuje listę n losowych słów o długości od min_len do max_len."""
    words = []
    for _ in range(n):
        length = random.randint(min_len, max_len)
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        words.append(word)
    return words

# ==========================================
# 3. GŁÓWNY TESTER
# ==========================================
def run_stress_test(tests_per_group=3):
    # Parametry grup dokładnie takie, jak w kodzie nauczyciela:
    # (ilość słów, min długość słowa, max długość słowa)
    test_groups = [
        {"name": "Grupa 1 (N=10, len: 5-10)", "n": 10, "m_low": 5, "m_high": 10},
        {"name": "Grupa 2 (N=100, len: 5-10)", "n": 100, "m_low": 5, "m_high": 10},
        {"name": "Grupa 3 (N=100, len: 20-100)", "n": 100, "m_low": 20, "m_high": 100},
        {"name": "Grupa 4 (N=10000, len: 10-30)", "n": 10000, "m_low": 10, "m_high": 30}
    ]
    
    total_tests = len(test_groups) * tests_per_group
    print(f"🚀 Rozpoczynam testy: {tests_per_group} testów dla każdej z {len(test_groups)} grup (łącznie {total_tests}).\n")
    
    total_passed = 0

    for group in test_groups:
        print(f"--- {group['name']} ---")
        group_passed = 0
        
        for test_idx in range(1, tests_per_group + 1):
            words = generate_random_words(group['n'], group['m_low'], group['m_high'])
            
            # 1. Odpalamy Twoje rozwiązanie i mierzymy czas
            start_opt = time.perf_counter()
            ans_opt = solution(words.copy())
            time_opt = (time.perf_counter() - start_opt) * 1000 # w ms
            
            # Uwaga: Dla N=10000 brute-force w Pythonie zajmuje kilka sekund.
            if group['n'] >= 10000:
                print(f"    [Test {test_idx}] Generowanie odp. referencyjnej (brute-force dla N=10000 trochę potrwa)...", end="\r")
                
            # 2. Odpalamy Brute-Force jako punkt odniesienia
            start_brute = time.perf_counter()
            ans_brute = brute_force_solution(words.copy())
            time_brute = (time.perf_counter() - start_brute) * 1000 # w ms
            
            # 3. Porównujemy wyniki
            if ans_opt == ans_brute:
                # Wypisujemy ładny log z czasami (nadpisuje "Generowanie odp..." dzięki spacji na końcu)
                print(f"    ✅ Test {test_idx:<2}: OK  |  Twój czas: {time_opt:>7.2f} ms  |  Brute-force: {time_brute:>8.2f} ms   ")
                group_passed += 1
                total_passed += 1
            else:
                print(f"\n    ❌ BŁĄD w teście {test_idx}!")
                # Wypisujemy zawartość tablicy tylko jeśli nie jest gigantyczna
                if group['n'] <= 100: 
                    print(f"    Wejście: {words}")
                print(f"    Oczekiwano (Brute-Force): {ans_brute}")
                print(f"    Zwrócono (Twoje)        : {ans_opt}\n")
                return # Przerywamy działanie po napotkaniu pierwszego błędu
                
        print(f"Podsumowanie grupy: {group_passed}/{tests_per_group} zaliczone.\n")
        
    print("="*75)
    print(f"🎉 ZALICZONO WSZYSTKIE TESTY: {total_passed}/{total_tests}")
    print("="*75)

if __name__ == "__main__":
    # Domyślna liczba testów na grupę to 3, ale możesz to zmienić z poziomu terminala
    # np. odpalając: python tester.py 5
    n_tests = 3
    if len(sys.argv) > 1:
        try:
            n_tests = int(sys.argv[1])
            if n_tests < 1: raise ValueError
        except ValueError:
            print("Podaj poprawną, dodatnią liczbę całkowitą testów na grupę.")
            sys.exit(1)
            
    run_stress_test(tests_per_group=n_tests)
