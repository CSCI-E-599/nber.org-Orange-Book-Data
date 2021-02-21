import pandas as pd
data = pd.io.stata.read_stata('FDA_drug_exclusivity.dta')
data.to_csv('FDA_drug_exclusivity.csv')

data = pd.io.stata.read_stata('FDA_drug_exclusivity_codes.dta')
data.to_csv('FDA_drug_exclusivity_codes.csv')

data = pd.io.stata.read_stata('FDA_drug_patents.dta')
data.to_csv('FDA_drug_patents.csv')

data = pd.io.stata.read_stata('FDA_patent_use_codes.dta')
data.to_csv('FDA_patent_use_codes.csv')

