
## pip install seaborn
import seaborn as sb
def diamonds():
    df = sb.load_dataset('diamonds')
    print(df.shape)
    print(df.head())

    df.to_csv('data/diamonds.csv')
# diamonds()
