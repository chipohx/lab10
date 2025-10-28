import datetime

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO] Простой Python-проект запущен через Jenkins. Текущее время: {now}")

if __name__ == "__main__":
    main()
