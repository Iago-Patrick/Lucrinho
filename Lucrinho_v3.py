from tkinter import *


def calculo():	
	#print(" Lucrinho v2.1")
	
	valor=float(valor1.get())
	taxa_de_compra=float(valor2.get())
	taxa_de_venda=float(valor3.get())
	valor_de_compra_moeda=float(valor4.get())
	valor_de_venda_moeda=float(valor5.get())
	
	taxa_valor_c = (valor * taxa_de_compra)/100
	valor_com_taxa_c=valor-taxa_valor_c

	vartaxa1["text"] =valor_com_taxa_c
	taxac["text"]=taxa_valor_c
	#
	compra = valor_com_taxa_c/valor_de_compra_moeda

	taxa_valor_v = (compra*taxa_de_venda)/100

	valor_com_taxa_v = compra-taxa_valor_v
	venda = valor_com_taxa_v*valor_de_venda_moeda
	lucro = venda-valor

	vartaxa3["text"]=valor_com_taxa_v
	taxav["text"]=taxa_valor_v
	resut["text"]=venda
	resu["text"]=lucro
	
	'''print('')
	print("COMPRA")'''

	'''print("valor menos a taxa:'")
	print(valor_com_taxa)
	print('taxa:')
	print(taxa)'''

	'''print('')
	print('VENDA')
	
	print('valor menos a taxa:')
	print(valor_com_taxa1)

	print('taxa:')
	print(taxa21)
	print('vendido:')
	print(venda)
	
	print('')
	print('LUCRO')
	lucro=venda-valor
	print(lucro)'''
	

'''
def main():	
	calculo()
	print('se quiser continuar digite "s" se nao "n":')
	conf=input()
	if conf=='s':
		main()
	else:
		exit(0)
main()
'''

janela=Tk()

janela.title("Lucrinho v3.0")
janela.geometry("600x300")

texo1=Label(janela, text="Digite o valor da transação:")
texo1.grid(column=1,row=1)
valor1=Entry(janela)
valor1.grid(column=1,row=2)

texo2=Label(janela, text="Digite a taxa de compra:")
texo2.grid(column=1,row=3)
valor2=Entry(janela)
valor2.grid(column=1,row=4)

texo3=Label(janela, text="Digite a taxa de venda:")
texo3.grid(column=1,row=5)
valor3=Entry(janela)
valor3.grid(column=1,row=6)

texo4=Label(janela, text="Digite o valor de compra da moeda:")
texo4.grid(column=1,row=7)
valor4=Entry(janela)
valor4.grid(column=1,row=8)

texo5=Label(janela, text="Digite o valor de venda da moeda:")
texo5.grid(column=1,row=9)
valor5=Entry(janela)
valor5.grid(column=1,row=10)


play=Button(janela,text="Calcular",command=calculo)
play.grid(column=2,row=5)

vartaxa=Label(janela, text="Valor menos a taxa:")
vartaxa.grid(column=4,row=1)
vartaxa1=Label(janela, text="")
vartaxa1.grid(column=5,row=1)

taxa1=Label(janela, text="Taxa:")
taxa1.grid(column=4,row=2)
taxac=Label(janela, text="")
taxac.grid(column=5,row=2)

vartaxa2=Label(janela, text="Quantidade menos taxa:")
vartaxa2.grid(column=4,row=3)
vartaxa3=Label(janela, text="")
vartaxa3.grid(column=5,row=3)

taxa2=Label(janela, text="Taxa:")
taxa2.grid(column=4,row=4)
taxav=Label(janela, text="")
taxav.grid(column=5,row=4)

vendido=Label(janela, text="Vendido:")
vendido.grid(column=4,row=5)
resut=Label(janela, text="")
resut.grid(column=5,row=5)

lucro1=Label(janela, text="Lucro:")
lucro1.grid(column=4,row=6)
resu=Label(janela, text="")
resu.grid(column=5,row=6)

janela.mainloop()
