def calculate_average_spam_confidence(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            total_confidence = 0
            count = 0
            
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    try:
                        confidence_value = float(line.split(":")[1].strip())
                        total_confidence += confidence_value
                        count += 1
                    except ValueError:
                        print(f"Pogreška pri obradi linije: {line.strip()}")
                        
            if count == 0:
                print("Nema pronađenih vrijednosti X-DSPAM-Confidence u datoteci.")
                return
            
            average_confidence = total_confidence / count
            print(f"Average X-DSPAM-Confidence: {average_confidence}")
    
    except FileNotFoundError:
        print("Datoteka nije pronađena. Provjerite unos.")
    except Exception as e:
        print(f"Došlo je do greške: {e}")

if __name__ == "__main__":
    filename = input("Ime datoteke: ").strip()
    calculate_average_spam_confidence(filename)