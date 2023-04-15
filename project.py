from pathlib import Path
import sympy as sp
from sympy import *
from pprint import pprint
import numpy as np
import pandas as pd


#add the symbols '&' and '\\' to any dataframe to make it printable in latex tabular
def tex_df (df):
    
    #---number of columns and rows
    rows = df.shape[0]
    col = df.shape[1]+1
    
    #---add '&' to the columns and the rest
    df = df.add_prefix('&')
    df = " & "+df

    #--- add '\\' and '___' to the end of columns and rest, first defining a column and then adding the column
    final = [ '\\\\ \\cline{1-'+str(col)+'}']*rows
    df['\\\\ \\cline{1-'+str(col)+'}']= final
    return df

#read exel as a panda dataframe 
#df = pd.read_excel('Platos.xlsx', index_col=0)
df = pd.read_csv("Platos.csv",skiprows=1,skipfooter=1)
print(df)

#---number of columns and rows (again)
rows = df.shape[0]
col = df.shape[1]+1

#get the path of this python file 
Path = str(Path.cwd())

#create .tex file
f = open(Path+"\Table.tex", "w")

#--- begin writing latex document
print( "\\documentclass[a4paper]{amsart}", file=f)
print("\\begin{document}",file=f )

#print an element of the dataframe
#print("Desayuno:"+df.iloc[0, 1]+"\\\\", file=f)

#-- dataframe good for latex
tdf=tex_df(df)
#begin tabular and print the data frame
print("\\begin{tabular}{"+"c|"*col + "}", file =f)
print(tdf, file=f)

#fancy last line
print("\\multicolumn{"+str(col)+"}{|c|}{fin} \\\\ \\cline{1-"+str(col)+"}", file=f)

# end tabular
print("\\end{tabular}", file=f )

#end document
print("\\end{document}",file=f)

#close file
f.close()  