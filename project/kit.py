import matplotlib.pyplot as plt
import seaborn as sns
import palmerpenguins
pg = palmerpenguins.load_penguins().dropna()

sns.set_style(style='whitegrid')
sns.set_context(context='notebook')
plt.rcParams['figure.figsize'] = (11, 9.4)
penguin_color = {
    'Adelie': '#ff6602ff',
    'Gentoo': '#0f7175ff',
    'Chinstrap': '#c65dc9ff'
}

"""
    DATOS A IMPORTAR
import kit
from kit import penguin_color
import matplotlib.pyplot as plt
import seaborn as sns
import palmerpenguins
pg = palmerpenguins.load_penguins().dropna()

"""