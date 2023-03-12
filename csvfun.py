import csv
#import openpyxl
import datetime
import string
import os 
import sys

# from openpyxl import Workbook
# from openpyxl import load_workbook

#path = "9027.xlsx"

#def open_workbook(path):
  #wb = load_workbook(path)
  #print(f"Worksheet names: {wb.sheetnames}")
  #sheet = wb.active
  #print(sheet)

l_ofmths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def find_csv(str):
  arr = []
  for file in os.listdir(str):
    if file.endswith(".csv"):
      arr.append(file.split(".")[0].strip())

def findthis(str):
  arr = []
  for file in os.listdir():
    if file.find(str):
      arr.append(file)

  return arr

def createthis(name):
  pass

def list_addr(str):
  arr = []
  for file in os.listdir(str):
    if "." not in file:
      arr.append(file.split(".")[0].strip())

  return arr
  
def firstmonth(dir, mth = l_ofmths):
  for m in l_ofmths:
    if mth in find_csv(dir):
      return False
    else:
      return True
  




def coord_conv(str):
  if ":" not in str:
    print("Please recheck coordinates.")
    return 0
  else:
    #A2:B5
    x = str.split(":")
    d = {"min_row" : int(x[0][1]), "min_col" : string.ascii_lowercase.index(x[0][0].lower()) + 1, "max_row" : int(x[1][1]) + 1, 
    "max_col" : string.ascii_lowercase.index(x[1][0].lower()) + 1}
    return d

def init_headers():
  hders = input("Vamos a iniciar las cabeceras.\nCta o Apt, ingresa y salida ya fueron iniciados.\nPor favor escriba un lista con sus opciones separada por ','.\n").split(",")
  for i in range(len(hders)):
    hders[i] = hders[i].strip()

  return hders

def create_col(sh, iter, val):
  sh.cell(1, iter).value = val
   

def cp_values(sheet_name, cell_range):
  try:
    sh = wb[sheet_name]
    cdinates = coord_conv(cell_range)
    d = {}

    for i in range(cdinates['min_row'], cdinates['max_row']):
      cell_value_aptno = sh.cell(i,cdinates['min_col']).value
      cell_value_rent = sh.cell(i, cdinates['max_col']).value
      d[cell_value_aptno] = cell_value_rent

    for e in d:
      print(f"{e} = {d[e]}")
  
  except:
    print(f"'{sheet_name}' not found. Quitting.")
    return

  return d


def wr_values(dict, sheet_name, cell_range):
  try:
    sh = wb[sheet_name]
    cdinates = coord_conv(cell_range)
    ind = 0

    for i in range(cdinates['min_row'], cdinates['max_row']):
        sh.cell(i,cdinates['min_col']).value = list(dict.keys())[ind]
        sh.cell(i, cdinates['max_col']).value = list(dict.values())[ind]
        ind += 1

    for e in dict:
      print(f"{e} = {dict[e]}")
  
  except:
    print(f"'Couldn't write.")
    return

  return