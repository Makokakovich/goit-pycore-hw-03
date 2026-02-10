from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """Визначає, кого з колег потрібно привітати на цьому тижні."""
    today = datetime.today().date()
    result = []

    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        bday = bday.replace(year=today.year)

        if bday < today:
            bday = bday.replace(year=today.year + 1)

        if 0 <= (bday - today).days <= 7:
            if bday.weekday() == 5:
                bday += timedelta(days=2)
            elif bday.weekday() == 6:
                bday += timedelta(days=1)

            result.append({"name": user["name"], "congratulation_date": bday.strftime("%Y.%m.%d")})

    return result


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]
    print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
