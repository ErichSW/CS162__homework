employee_data = ["25X15", "Joe E. Baker", "33 Nowhere St.", "111223333", "S25X"]
job_id = ["S25X", "Secretary", "T5", "Personnel"]



data = ["Bob", "Suzie", "Mary", "Trieste", "Bill",
        "James", "Dylan", "Michael", "Alice", "Deanna"]


# generate unique hash code for each item and print it with the item
def hash_code(data):
    for i in data:
        print(f"{i}: {hash(i)}")


hash_code(data)