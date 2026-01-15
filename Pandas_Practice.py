import pandas as pd

### 595) Big Countries

# time O(n) Bolean filter complexity
# space O(n) Bolean Mask time complexity
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world.population >= 25000000) | (world.area >= 3000000)]

    df = df[['name', 'population', 'area']]

    return df

