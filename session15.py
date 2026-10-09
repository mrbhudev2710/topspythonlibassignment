# task1
import pandas as pd
# pyrefly: ignore [missing-import]
from ydata_profiling import ProfileReport

# Load Spotify dataset
df = pd.read_csv("spotify_top_100_songs.csv")

# Generate profile report
profile = ProfileReport(
    df,
    title="Spotify Top 100 Songs Report",
    explorative=True
)

# Save report as HTML
profile.to_file("spotify_report.html")
print("Report generated successfully!")


# task2
import pandas as pd
# pyrefly: ignore [missing-import]
import sweetviz as sv

# Load both datasets
mumbai = pd.read_csv("zomato_mumbai.csv")
delhi = pd.read_csv("zomato_delhi.csv")

# Compare the datasets
report = sv.compare(
    [mumbai, "Mumbai"],
    [delhi, "Delhi"]
)

# Generate and open the HTML report
report.show_html("zomato_comparison.html")
print("Comparison report generated!")


# task3
import pandas as pd
# pyrefly: ignore [missing-import]
import dtale

# Load Myntra dataset
df = pd.read_csv("myntra_products.csv")

# Open dataset in D-Tale
d = dtale.show(df)
d.open_browser()


# task4
import pandas as pd
# pyrefly: ignore [missing-import]
from ydata_profiling import ProfileReport

# Load Flipkart reviews dataset
df = pd.read_csv("flipkart_reviews.csv")

# Generate profile report
profile = ProfileReport(
    df,
    title="Flipkart Product Reviews Report",
    explorative=True
)

profile.to_file("flipkart_report.html")
print("Report generated successfully!")


# task5
import pandas as pd
# pyrefly: ignore [missing-import]
from ydata_profiling import ProfileReport

# Load Swiggy food order dataset
df = pd.read_csv("swiggy_orders.csv")

# Display basic dataset information
print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

# Generate Auto-EDA report
profile = ProfileReport(
    df,
    title="Swiggy Food Orders Analysis",
    explorative=True
)

# Save report as an HTML file
profile.to_file("swiggy_eda_report.html")
print("\nReport saved as swiggy_eda_report.html")