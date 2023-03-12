from csvfun import *

l_banks = ["chase", "bankofamerica", "capitalone"]
min_headers = ["fecha", "descripcion", "", "salida", "entrada"]

if __name__ == "__main__":
  mth = datetime.datetime.now().strftime("%b")
  #opts = (list_addr("casas"))
  if not os.path.exists("accts"):
    permission = input("No encontre un sobre de cuentas, lo puedo comencar? Escribi 'si' o 'no'.\n")
    if permission.lower() == "si":
      os.mkdir("accts")
      
    else:
      print("Esta bien, hasta luego")
      exit()

  if len(os.listdir("accts")) == 0:
    divfold = input("Sugerio devidir este sobre como un archivo y dividir lo mas, por ejemplo me gustaria comencar dos sobres adentro con los nombres, '9027' y '8901', puedo?\n")
    if divfold.lower() == "si":
      os.mkdir("accts/9027")
      os.mkdir("accts/8901")

  opts = os.listdir("accts")
  address = "accts/" + input(f"Sobre cual casa te gustaria trabajar {*opts,}?\n")


  while not os.path.exists(address):
    suffix = address.split("/")[-1]
    print(f"Escribiste {suffix} y esa direccion no existe.\n")
    address = "accts/" + input(f"Por favor escoje una de las opciones {*opts,}?\n")
    try:
      os.listdir(address)
      break
    except:
      print("Este es el ultimo attempto, si no sirve habla con Juanca.\n")
      address = "accts/" + input(f"Por favor escoje una de las opciones {*opts,}?\n") 
      break

  suffix = address.split("/")[-1]

  if os.path.exists(address):
    #search for redundant step files
    try:
      rf = createthis(f"{address}/{suffix}repeatable.text")
    except:
      pass

    rf = open(f"{address}/{suffix}repeatable.text", "r")
    bank = rf.readline()
    rf.close()
    if len(bank) < 1:
      bank = find_csv(l_banks)
    #   bank = input("No hay un banco associado con esta direccion, si te gustaria associar uno entre el nombre ahora, por favor.\n")
    #   verify = input(f"Entraste '{bank}', esta correcto?\n")
    #   while verify.lower() == "no":
    #     bank = input("No hay un banco associado con esta direccion, si te gustaria associar uno entre el nombre ahora, por favor.\n")
    #     verify = input(f"Entraste '{bank}', esta correcto?\n")
    #     if verify.lower() == "no":
    #       bank = input("No hay un banco associado con esta direccion, si te gustaria associar uno entre el nombre ahora, por favor.\n")
    #       break
    #     else:
    #       break

      # with open(f"{address}/{suffix}repeatable.text") as rf:
      #       rf.append(bank)












  else:
    print("Hubo un error habla con Juanca.") 

 
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
    
    

    
 
  # if firstmonth(address):
  #   if(firstmonth(address, mth)):
  #     if one_timer:
  #       aptList = input("Esta es la primera vez que inicias sesión necesito los numeros de los apartamentos, entra los separados por comas.\n Ejemple '1f, 2r'\n")

  #       if not aptList:
  #         aptList = input("Estas segura que no quieres entran los apartamentos?\n")

  #       else:
  #         for i in range(len(aptList)):
  #           print(i + 1, aptList[i])
            
  #     st_month = input("Esta es la primera vez que inicias sesión con esta casa este mes. Te gustaria empezar la cuenta mensual?\nEscribi 'si' o 'no'\n")

  #     if st_month.lower() == 'si':
  #       with open(f"{address}/{mth}.csv", "w", newline="") as file:
  #         writer = csv.writer(file)
  #         writer.writerow(min_headers)

