import matplotlib.pyplot as plt
import pandas as pd

nucs = ['Pu239', 'U235', 'U233']

fig = plt.figure()
for nuc in nucs:
    df = pd.read_csv('{}.txt'.format(nuc), skiprows=1, header=None, 
                     sep=" ", names=['energy', 'xs'])
    plt.loglog(df['energy'], df['xs'], label=nuc, figure=fig)
plt.legend(loc=0)
plt.xlabel('Energy (eV)')
plt.ylabel('$\sigma(E)$ (barns)')
plt.title('Fission Cross Section')
plt.savefig('xs.pdf')
