
from main import CSV_FILE
import csv 


def write_all_items(items):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item"])

        for item in items:
            writer.writerow([item])


def load_data(item_id: int | None = None):
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader, None)

            items = [row[0] for row in reader if row]

            if item_id is None:
                return items

            if 0 <= item_id < len(items):
                return items[item_id]

            raise HTTPException(
                status_code=404,
                detail=f"There is no item {item_id}"
            )

    except FileNotFoundError:
        return []