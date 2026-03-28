"""Test import."""
import importlib


def loading() -> None:
    """Load import."""
    print("\nLOADING STATUS: Loading programs...\n")

    print("\nChecking dependencies:")
    try:
        pandas = importlib.import_module("pandas")
        print(f"[OK] {pandas.__name__} ({pandas.__version__})"
              " - Data manipulation ready")
    except Exception as e:
        print(e)
    try:
        numpy = importlib.import_module("numpy")
        print(f"[OK] {numpy.__name__} ({numpy.__version__})"
              " - Data Calculating ready")
    except Exception as e:
        print(e)
    try:
        requests = importlib.import_module("requests")
        print(f"[OK] {requests.__name__} ({requests.__version__})"
              " - Network access ready")
    except Exception as e:
        print(e)
    try:
        mtp = importlib.import_module("matplotlib.pyplot")
        print(
            f"[OK] {mtp.__name__} ({mtp.matplotlib.__version__})"
            " - Visualization ready")
    except Exception as e:
        print(e)

    try:
        print("\nAnalyzing Matrix data...")
        respenons = requests.get("https://jsonplaceholder.typicode.com/postss")
        if respenons.status_code == 200 or respenons.status_code == 201:
            json_data = respenons.json()
        else:
            raise Exception("RequestsError: Api is not valaibale")
        data: dict = {
            "x": numpy.arange(len(json_data)),
            "y": [post["id"] for post in json_data]}
        print("Processing 1000 data points...")
        print(pandas.DataFrame(data))
        print("Generating visualization...")
        mtp.bar(data["x"], data["y"])
        mtp.savefig("./matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    loading()
