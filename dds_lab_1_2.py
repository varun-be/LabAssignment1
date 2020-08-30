import sqlite3
from sqlite3 import Error
from beautifultable import BeautifulTable

conn = sqlite3.connect('worldwar.db')
c = conn.cursor()





#This function prints the table, send table name as the argument
def printfun(t_num):
	print("`````````````````````````````````````````````````````")
	table = BeautifulTable()
	if t_num=='1':
		t_name="battle"
		table.columns.header = ["NAME","DATE"]
		c.execute("select * from "+ t_name)
		conn.commit()
		for row in c.fetchall():
			table.rows.append(row)
			#print(row)

	elif t_num=='2':
		t_name="classes"
		table.columns.header = ["CLASS","TYPE"," COUNTRY","NO_GUNS", " BORE", " DISPLACEMENT"]
		c.execute("select * from "+ t_name)
		conn.commit()
		for row in c.fetchall():
			table.rows.append(row)
			#print(row)
	elif t_num=='3':
		t_name="outcomes"
		table.columns.header = ["SHIP"," BATTLE"," RESULT"]
		c.execute("select * from "+ t_name)
		conn.commit()
		for row in c.fetchall():
			table.rows.append(row)
			#print(row)
	elif t_num=='4':
		t_name="ships"
		table.columns.header = ["SHIP_NAME","CLASS","LAUNCHED DATE"]
		c.execute("select * from "+ t_name)
		conn.commit()
		for row in c.fetchall():
			table.rows.append(row)
			#print(row)
	print(table)
'''
	table.columns.header = ["name","battle"]
	c.execute("select * from "+ t_name)
	conn.commit()
	for row in c.fetchall():
		table.rows.append(row)
		#print(row)
	'''
	
	
'''
this_dict={
	'1':"NAME DATE",
	'2':"CLASS TYPE COUNTRY NO_GUNS BORE DISPLACEMENT",
	'3':"SHIP BATTLE RESULT",
	'4':"SHIP_NAME CLASS LAUNCHED"
}
'''

this_dict={
	'1':{1:"NAME", 2: "DATE"},
	'2':{1:"CLASS", 2: "TYPE", 3:" COUNTRY",4:"NO_GUNS", 5:" BORE", 6:" DISPLACEMENT"},
	'3':{1:"SHIP",2:" BATTLE",3:" RESULT"},
	'4':{1:"SHIP_NAME",2:"CLASS",3:" LAUNCHED"}
}



'''
battle_schema = "NAME DATE"
battle_example = "'North Cape','19431226 00:00:00.000'"

classes_schema = "CLASS TYPE COUNTRY NUM_GUNS BORE DISPLACEMENT" 
classes_example = "'Bismarck','bb','Germany',8,15,42000"

outcomes_schema = "SHIP BATTLE RESULT"
outcomes_example = "'Bismarck','North Atlantic','sunk'"

ships_schema = "SHIP_NAME CLASS LAUNCHED"
ships_example = "'Repulse','Renown',1916"
'''	


def insert1(table_no):
	table_n = str(this_dict[table_no])
	print("Schema of the table: " +table_n+"\n")
	battle_name = (input("Enter battle_name\n")).lower()
	battle_date  = (input("Enter battle_date\n")).lower()
	query = """INSERT INTO battle(name , date) VALUES (?,?)"""
	try:
		c.execute(query, (battle_name, battle_date))
		conn.commit()
		print("Updated table is\n ")
		#printfun("battle")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")

	
	
	
def insert2(table_no):
	table_n = str(this_dict[table_no])
	print("Schema of the table: " +table_n+"\n")
	class_t = input("Enter class\n").lower()
	ty  = input("Enter type\n").lower()
	countr = input("Enter country\n").lower()
	no_guns = input("Enter number of guns\n").lower()
	bore = input("Enter bore\n").lower()
	disp = input("Enter displacement\n").lower()
	query = """INSERT INTO classes(CLASS,TYPE,COUNTRY,NUM_GUNS,BORE,DISPLACEMENT) VALUES (?,?,?,?,?,?)"""
	try:
		c.execute(query, (class_t,ty,countr,no_guns,bore,disp))
		conn.commit()
		print("Updated table is\n ")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")

	
	
	
def insert3(table_no):
	table_n = str(this_dict[table_no])
	print("Schema of the table: " +table_n+"\n")
	sn = input("Enter ship name\n").lower()
	ba  = input("Enter battle\n").lower()
	res = input("Enter result\n").lower()
	query = """INSERT INTO outcomes(ship,battle,result) VALUES (?,?,?)"""
	try:
		c.execute(query, (sn,ba,res))
		conn.commit()
		print("Updated table is\n ")
		#printfun("outcomes")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")

	
	
def insert4(table_no):
	table_n = str(this_dict[table_no])
	print("Schema of the table: " +table_n+"\n")
	sn = input("Enter ship name\n").lower()
	ba  = input("Enter class\n").lower()
	res = input("Enter launched\n").lower()
	query = """INSERT INTO ships(ship_name,class,launched) VALUES (?,?,?)"""
	try:
		c.execute(query, (sn,ba,res))
		conn.commit()
		print("Updated table is\n ")
		#printfun("ships")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")

##``````````````````````````````````````````````````````````````````````````````
def delete1(table_no):
	table_n = str(this_dict[table_no])
	#print("Before delete")
	printfun(table_no)
	printfun("battle")
	sn = (input("Enter battle name to be deleted\n")).lower()
	query = """delete from battle where name = (?)"""
	try:
		c.execute(query,(sn,))
		conn.commit()
		print("After delete")
		#printfun("battle")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")
	
	
def delete2(table_no):
	table_n = str(this_dict[table_no])
	print("Before delete")
	printfun(table_no)
	#printfun("classes")
	sn = (input("Enter class type  to be deleted\n")).lower()
	query = """delete from classes where class = (?)"""
	try:
		c.execute(query,(sn,))
		conn.commit()
		print("After delete")
		#printfun("classes")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")
	
	
def delete3(table_no):
	table_n = str(this_dict[table_no])
	print("Before delete")
	printfun(table_no)
	#printfun("outcomes")
	sn = (input("Enter ship name to be deleted\n")).lower()
	sn2= (input("Enter the corresponding battle name to be deleted\n")).lower()
	query = """delete from outcomes where ship  = (?) AND battle= (?)"""
	try:
		c.execute(query,(sn,sn2,))
		conn.commit()
		print("After delete")
		#printfun("outcomes")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")	

def delete4(table_no):
	table_n = str(this_dict[table_no])
	print("Before delete")
	printfun(table_no)
	#printfun("ships")
	sn = (input("Enter ship name to be deleted\n")).lower()
	query = """delete from ships where ship_name  = (?)"""
	try:
		c.execute(query,(sn,))
		conn.commit()
		print("After delete")
		#printfun("outcomes")
		printfun(table_no)
	except Error as err:
		print("ERROR:  "+ str(err))
		print("Oops!!! Operation failed. Try again later :)")


'''````````````````````````````````````````````````````````````````````````````````````````````````````````````'''
def update(table_choice):
	#print(table_choice)
	'''battle table'''
	if table_choice=='1':
		key=(input("Enter the Battle name:")).lower()
		#print(key)
		attribute=int(input("What do you want to update:\n" + str(this_dict[table_choice])+"\n"))
		ans=(input("Enter the updated value:  ")).lower()
		#sql_command="""UPDATE battle SET %s=%s WHERE name=%s"""
		
		if attribute==1:
			try:
				c.execute("""UPDATE battle SET name=(?) WHERE name=(?)""" ,(ans, key,))
				conn.commit()
				c.execute("""SELECT * FROM battle WHERE name=(?)""",(ans,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
				#return True
			except Error as err:
					print("ERROR:  "+ str(err))
					print("Oops!!! Operation failed. Try again later :)")


				


			
		elif attribute==2:
			try:
				c.execute("""UPDATE battle SET 'date'=(?) WHERE name=(?)""" ,(ans, key,))
				conn.commit()
				c.execute("""SELECT * FROM battle WHERE name=(?)""",(key,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			
	

	elif table_choice=='2':		
		'''classes table'''
		key=(input("Enter the Class of the ship: ")).lower()
		attribute=int(input("What do you want to update(enter the number):\n" +str(this_dict[table_choice])+"\n"))
		ans=(input("Enter the updated value:  ")).lower()
		#sql_command="""UPDATE classes SET (?)=(?) WHERE class=(?)"""
		
		if attribute==1:			
			try:
				c.execute("""UPDATE classes SET class=(?) WHERE class=(?)""",(ans, key,))
				conn.commit()
				c.execute("""SELECT * FROM classes WHERE class=(?)""",(ans,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			
		elif attribute==2:
			try:
				c.execute ("""UPDATE classes SET type=(?) WHERE class=(?)""",(ans, key,))
				conn.commit()
				c.execute("""SELECT * FROM classes WHERE class=(?)""",(key,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			
		elif attribute==3:
			try:
				c.execute ("""UPDATE classes SET country=(?) WHERE class=(?)""",(ans, key,))
				conn.commit()
				c.execute("""SELECT * FROM classes WHERE class=(?)""",(key,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			
		elif attribute==4:
			try:
				c.execute ("""UPDATE classes SET num_guns=(?) WHERE class=(?)""",(ans, key,))
				conn.commit()
				c.execute("""SELECT * FROM classes WHERE class=(?)""",(key,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")


			
		elif attribute==5:
			try:
				c.execute ("""UPDATE classes SET bore=(?) WHERE class=(?)""",(ans, key,))
				conn.commit()
				c.execute("""SELECT * FROM classes WHERE class=(?)""",(key,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			
		elif attribute==6:
			try:
				c.execute ("""UPDATE classes SET displacement=(?) WHERE class=(?)""",(ans, key,)) 
				conn.commit()
				c.execute("""SELECT * FROM classes WHERE class=(?)""",(key,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row) 
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)") 

			


	elif table_choice=='3':
		''' outcomes table'''	
		key1=(input("Enter the ship  name:  ")).lower()
		key2=(input("Enter the battle name:  ")).lower()
		attribute=int(input("What do you want to update: \n"+str(this_dict[table_choice]) +"\n"))
		ans=(input("Enter the updated value:  ")).lower()
		#sql_command="""UPDATE outcomes SET ?=? WHERE ship_name=?"""
		if attribute==1:			
			try:
				c.execute ("""UPDATE outcomes SET ship=(?) WHERE ship=(?) AND battle=(?)""",(ans,key1,key2,))
				conn.commit()
				c.execute("""SELECT * FROM outcomes WHERE ship=(?) AND battle=(?)""",(ans,key2,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row) 
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			
		elif attribute==2:
			try:
				c.execute ("""UPDATE outcomes SET battle=(?) WHERE ship=(?) AND battle=(?)""",(ans, key1,key2,))
				conn.commit()
				c.execute("""SELECT * FROM outcomes WHERE ship=(?) AND battle=(?)""",(key1,ans,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row) 
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			
		elif attribute==3:
			try:
				c.execute ("""UPDATE outcomes SET result=(?) WHERE ship=(?) AND battle=(?)""",(ans, key1,key2,)) 
				conn.commit()
				c.execute("""SELECT * FROM outcomes WHERE ship=(?) AND battle=(?)""",(key1,key2,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row) 
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			


	
	elif  table_choice=='4':	
		'''ships table'''	
		key=(input("Enter the ship name:  ")).lower()
		attribute=int(input("What do you want to update:\n"+str(this_dict[table_choice])+"\n"))
		ans=(input("Enter the updated value:  ")).lower()
		#sql_command="""UPDATE ships SET ?=? WHERE ship=? AND battle=?"""
		if attribute==1:			
			try:
				c.execute("""UPDATE ships SET ship_name=(?) WHERE ship_name=(?)""",(ans, key,))
				#conn.commit()
				c.execute("""SELECT * FROM ships WHERE ship_name=(?)""",(ans,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)") 

			
		elif attribute==2:
			try:
				c.execute ("""UPDATE ships SET class=(?) WHERE ship_name=(?)""",(ans, key,))
				#conn.commit()
				c.execute("""SELECT * FROM ships WHERE ship_name=(?)""",(key,))
				rows = c.fetchall()
				print("\nThe updated tuple is:\n")
				for row in rows:
					print(row)
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")

			 
		elif attribute==3:
			try:
				c.execute ("""UPDATE ships SET launched=(?) WHERE ship_name=(?)""",(ans, key,)) 
			except Error as err:
					print("ERROR:  "+ str(err))
					print("Oops!!! Operation failed. Try again later :)")
			#conn.commit()
			c.execute("""SELECT * FROM ships WHERE ship_name=(?)""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row) 
			'''
			except Error as err:
				print("ERROR:  "+ str(err))
				print("Oops!!! Operation failed. Try again later :)")
			'''
			
		conn.commit()


def main():

	while 1:
		print("`````````````````````````````````````````````")
		table_name=input("SELECT TABLE\n 1.battle\n 2. classes\n 3. outcome\n 4. ships \n 5.Exit Application\n")
		if table_name=='5':
			print("Have a nice day!! \nClosing....")
			conn.close()
			break
		else:
			while 1:
				if table_name=='1':
					print("```````````````TABLE: battle``````````````````")
				elif table_name=='2':
					print("```````````````TABLE: classes``````````````````")
				elif table_name=='3':
					print("```````````````TABLE: outcome``````````````````")
				elif table_name=='4':
					print("```````````````TABLE: ship````````````````````")



				n=input("SELECT CHOICE\n 1:Insert\n 2:Update\n 3:Delete\n 4:View table\n 5:Go Back\n 6:Exit application\n")
				if n=='6':
					print("Closing....")
					conn.close()
					exit()
				if n=='5':
					break

				#table_name=input("Select table\n 1.battle\n 2. classes\n 3. outcome\n 4. ships\n")
				if n=='1':
					if table_name=='1':
						insert1(table_name)
					if table_name=='2':
						insert2(table_name)
					if table_name=='3':
						insert3(table_name)
					if table_name=='4':
						insert4(table_name)

				if n=='2':
					update(table_name)
						
				if n=='3':
					if table_name=='1':
						delete1(table_name)
					if table_name=='2':
						delete2(table_name)
					if table_name=='3':
						delete3(table_name)
					if table_name=='4':
						delete4(table_name)
				if n=='4':
					printfun(table_name)
				print("`````````````````````````````````````````````````")
		

if __name__=="__main__":
	main()
	







