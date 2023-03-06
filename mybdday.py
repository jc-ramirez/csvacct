from csvfun import *

min_headers = ["cta or apt", "", "salida", "entrada"]
  
if __name__ == "__main__":
  mth = datetime.datetime.now().strftime("%b")
  opts = (list_addr("casas"))

  address = "casas/" + input(f"Sobre cual casa te gustaria trabajar {*opts,}?\n")
  # opts = find_csv()
  
  # if len(opts) > 1:
  #   path = input(f"Con que mes te gustaria trabajar {*opts,}?\n")

  # elif len(opts) == 1:
  #   opciones =input(f"Si te gustaria habrir {opts[0]}, escribi, '{opts[0]}'' o si te gustraria comencar otra mes, escribi 'otra'.\n")
  #   if opciones == opts[0]:
  #     path = opts[0]
  #   else:
  #     path = input("Por favor entra el nombre para iniciar (ejemplo '9027'.)") + ".xlsx"

  # else:
  #   path = input("No existen informacion de cuenta bancaria, con que te puedo ayudar.\n")
    
    

    
 
  if firstmonth(address, mth):
    st_month = input("Esta es la primera vez que inicias sesión con esta cuenta este mes. Te gustaria empezar la cuenta mensual?\nEscribi 'si' o 'no'\n")

    if st_month.lower() == 'si':
      with open(f"{address}/{mth}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(min_headers)

#       print(f"Worksheet names: {wb.sheetnames}")
#       #wr_values(d, f"{mth}", "A2:B5")

#   else:
#     st_month = input("Con que te puedeo ayudar?\n")







