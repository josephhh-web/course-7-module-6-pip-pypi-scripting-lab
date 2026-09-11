from datetime import datetime


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    import json
    from urllib.request import urlopen

    try:
        with urlopen("https://jsonplaceholder.typicode.com/posts/1") as response:
            title = json.load(response).get("title", "No title found")
    except Exception:
        title = "No title found"

    generate_log(
        [
            "User logged in",
            f"Fetched Title: {title}",
            "Report generated successfully",
        ]
    )