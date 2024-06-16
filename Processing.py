import ast
import pandas as pd
lines = []
path = './details.txt'
with open(path , 'r') as f:
    lines = f.read()
lines = lines.split('}{')
lines = [line.strip() for line in lines]
lines = [line.replace('\n' , '') for line in lines]

lines = [line.replace('    ', '') for line in lines]

lines = [line.replace(': ', ':') for line in lines]

details = [line.split(',') for line in lines]
details.pop()
data = []
error_indices = []
for ind ,detail in enumerate(details):
    print(ind)
    try:
        s = '{'
        for info in detail:
            info.replace('NULL' ,'NA')
            s += info + ','
        s = s[ : len(s)-1]
        s += '}'
        data.append(ast.literal_eval(s))
    except (ValueError , SyntaxError) as e:
        print(f'Error occured at index {ind}: {e}')
        error_indices.append(ind)
df = pd.DataFrame(data)
df.to_csv('Final_Output.csv',index= False)