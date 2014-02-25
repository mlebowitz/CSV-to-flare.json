import pandas as pd

def cluster(df):
    result = []
    
    for k,g in df.groupby(df.columns[0]):
        group_rows = g.drop(df.columns[0],1) 
        if len(g.columns) == 2: 
            result.append({"name": g[g.columns[0]].values[0],"value": int(g[g.columns[1]].values[0]),"size": int(g[g.columns[1]].values[0])})
        else:
            result.append({"name": k,"children":cluster(group_rows)})
    
    return result