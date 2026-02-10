from datetime import datetime


def get_days_from_today(date: str) -> int:
    """Розраховує кількість днів між заданою датою і поточною."""
    try:
        day = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - day).days
    except ValueError:
        return "Неправильний формат дати!"


if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))
