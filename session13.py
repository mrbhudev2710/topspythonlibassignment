# task1
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# Create pairplot
sns.pairplot(tips)

# Display plot
plt.show()


# task2
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights = sns.load_dataset('flights')

# Reshape data using pivot
flights_pivot = flights.pivot(
    index='month',
    columns='year',
    values='passengers'
)

# Create heatmap
sns.heatmap(flights_pivot, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Monthly Flight Passengers by Year')
plt.xlabel('Year')
plt.ylabel('Month')
plt.show()


# task3
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
fmri = sns.load_dataset('fmri')

# Create relational plot
sns.relplot(
    data=fmri,
    x='timepoint',
    y='signal',
    hue='event',
    kind='line'
)
plt.title('Signal Changes Over Time')
plt.show()


# task4
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
titanic = sns.load_dataset('titanic')

# Create categorical plot
sns.catplot(
    data=titanic,
    x='class',
    y='survived',
    kind='bar',
    errorbar=('ci', 95)
)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()


# task5
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset('penguins')

# Remove missing values
penguins = penguins.dropna(
    subset=['bill_length_mm', 'flipper_length_mm']
)

# Create jointplot with regression line
sns.jointplot(
    data=penguins,
    x='bill_length_mm',
    y='flipper_length_mm',
    kind='reg'
)
plt.show()