import pandas as pd
from pandas.io.json import build_table_schema
from data import jobs

jobs_DF = pd.DataFrame(data=jobs, columns=jobs[0],)

print(jobs_DF.info)
# schema = build_table_schema(data=jobs_DF, index=True)
# print(schema)
