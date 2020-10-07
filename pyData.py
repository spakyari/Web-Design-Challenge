import pandas as pd

table_df = pd.read_csv("Resources/cities.csv")


myTable = table_df.to_html(index=False)

myTable = myTable.replace('<table border="1" class="dataframe">\n','')

with open("data-temp.html", 'r') as text:
    
    template = text.read()


data_html = template.replace('<!-- insert table -->', myTable)

with open("data.html", 'w') as text:
    
    text.write(data_html)
    
print('New html is generated')
