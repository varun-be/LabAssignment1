import sqlite3
conn = sqlite3.connect('worldwar.db')
c = conn.cursor()




#This function prints the table, send table name as the argument
def printfun(t_name):
	c.execute("select * from "+ t_name)
	conn.commit()
	for row in c.fetchall():
		print(row)
	
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
	battle_name = input("Enter battle_name\n")
	battle_date  = input("Enter battle_date\n")
	query = """INSERT INTO battle(name , date) VALUES (?,?)"""
	c.execute(query, (battle_name, battle_date))
	print("Updated table is\n ")
	printfun("battle")
	
	
def insert2(table_no):
	table_n = str(this_dict[table_no])
	print("Schema of the table: " +table_n+"\n")
	class_t = input("Enter class\n")
	ty  = input("Enter type\n")
	countr = input("Enter country\n")
	no_guns = input("Enter number of guns\n")
	bore = input("Enter bore\n")
	disp = input("Enter displacement\n")
	query = """INSERT INTO classes(CLASS,TYPE,COUNTRY,NUM_GUNS,BORE,DISPLACEMENT) VALUES (?,?,?,?,?,?)"""
	c.execute(query, (class_t,ty,countr,no_guns,bore,disp))
	print("Updated table is\n ")
	printfun("classes")
	
	
def insert3(table_no):
	table_n = str(this_dict[table_no])
	print("Schema of the table: " +table_n+"\n")
	sn = input("Enter ship name\n")
	ba  = input("Enter battle\n")
	res = input("Enter result\n")
	query = """INSERT INTO outcomes(ship,battle,result) VALUES (?,?,?)"""
	c.execute(query, (sn,ba,res))
	print("Updated table is\n ")
	printfun("outcomes")
	
def insert4(table_no):
	str(this_dict[table_no])
	this_dict[table_no]
	print("Schema of the table: " +table_n+"\n")
	sn = input("Enter ship name\n")
	ba  = input("Enter class\n")
	res = input("Enter launched\n")
	query = """INSERT INTO ships(ship_name,class,launched) VALUES (?,?,?)"""
	c.execute(query, (sn,ba,res))
	print("Updated table is\n ")
	printfun("ships")


def delete1(table_no):
	table_n = str(this_dict[table_no])
	print("Before delete")
	printfun("battle")
	sn = input("Enter ship name to be deleted\n")
	query = """delete from battle where name = (?)"""
	c.execute(query,(sn,))
	conn.commit()
	print("After delete")
	printfun("battle")
	
def delete2(table_no):
	table_n = str(this_dict[table_no])
	print("Before delete")
	printfun("classes")
	sn = input("Enter class type  to be deleted\n")
	query = """delete from classes where class = (?)"""
	c.execute(query,(sn,))
	conn.commit()
	print("After delete")
	printfun("classes")
	
def delete3(table_no):
	table_n = str(this_dict[table_no])
	print("Before delete")
	printfun("outcomes")
	sn = input("Enter ship name to be deleted\n")
	query = """delete from outcomes where ship  = (?)"""
	c.execute(query,(sn,))
	conn.commit()
	print("After delete")
	printfun("outcomes")

def delete4(table_no):
	table_n = str(this_dict[table_no])
	print("Before delete")
	printfun("ships")
	sn = input("Enter ship name to be deleted\n")
	query = """delete from ships where ship_name  = (?)"""
	c.execute(query,(sn,))
	conn.commit()
	print("After delete")
	printfun("ships")




'''````````````````````````````````````````````````````````````````````````````````````````````````````````````'''
def update(table_choice):
	#print(table_choice)
	'''battle table'''
	if table_choice=='1':
		key=(input("Enter the Battle name:"))
		#print(key)
		attribute=int(input("What do you want to update:\n" + str(this_dict[table_choice])+"\n"))
		ans=input("Enter the updated value:  ")
		#sql_command="""UPDATE battle SET %s=%s WHERE name=%s"""
		
		if attribute==1:			
			c.execute("""UPDATE battle SET name=(?) WHERE name=(?)""" ,(ans, key,))
			c.execute("""SELECT * FROM battle WHERE name=(?)""",(ans,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)
		elif attribute==2:
			c.execute("""UPDATE battle SET 'date'=(?) WHERE name=(?)""" ,(ans, key,))
			c.execute("""SELECT * FROM battle WHERE name=(?)""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)
	

	elif table_choice=='2':		
		'''classes table'''
		key=(input("Enter the Class of the ship: "))
		attribute=int(input("What do you want to update(enter the number):\n" +str(this_dict[table_choice])+"\n"))
		ans=input("Enter the updated value:  ")
		#sql_command="""UPDATE classes SET (?)=(?) WHERE class=(?)"""
		
		if attribute==1:			
			c.execute("""UPDATE classes SET class=(?) WHERE class=(?)""",(ans, key,))
			c.execute("""SELECT * FROM classes WHERE class=?""",(ans,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)
		elif attribute==2:
			c.execute ("""UPDATE classes SET type=(?) WHERE class=(?)""",(ans, key,))
			c.execute("""SELECT * FROM classes WHERE class=?""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)
		elif attribute==3:
			c.execute ("""UPDATE classes SET country=(?) WHERE class=(?)""",(ans, key,))
			c.execute("""SELECT * FROM classes WHERE class=?""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)
		elif attribute==4:
			c.execute ("""UPDATE classes SET num_guns=(?) WHERE class=(?)""",(ans, key,))
			c.execute("""SELECT * FROM classes WHERE class=?""",(key))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)
		elif attribute==5:
			c.execute ("""UPDATE classes SET bore=(?) WHERE class=(?)""",(ans, key,))
			c.execute("""SELECT * FROM classes WHERE class=?""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)
		elif attribute==6:
			c.execute ("""UPDATE classes SET displacement=(?) WHERE class=(?)""",(ans, key,)) 
			c.execute("""SELECT * FROM classes WHERE class=?""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row)  


	elif table_choice=='3':
		''' outcomes table'''	
		key1=(input("Enter the ship  name:  "))
		key2=(input("Enter the battle name:  "))
		attribute=int(input("What do you want to update: \n"+str(this_dict[table_choice]) +"\n"))
		ans=input("Enter the updated value:  ")
		#sql_command="""UPDATE outcomes SET ?=? WHERE ship_name=?"""
		if attribute==1:			
			c.execute ("""UPDATE outcomes SET ship=(?) WHERE ship=(?) AND battle=(?)""",(ans,key1,key2,))
			c.execute("""SELECT * FROM outcomes WHERE ship=(?) AND battle=(?)""",(ans,key2))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row) 
		elif attribute==2:
			c.execute ("""UPDATE outcomes SET battle=(?) WHERE ship=(?) AND battle=(?)""",(ans, key1,key2,))
			c.execute("""SELECT * FROM outcomes WHERE ship=(?) AND battle=(?)""",(key1,ans,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row) 
		elif attribute==3:
			c.execute ("""UPDATE outcomes SET result=(?) WHERE ship=(?) AND battle=(?)""",(ans, key1,key2,)) 
			c.execute("""SELECT * FROM outcomes WHERE ship=(?) AND battle=(?)""",(key1,key2,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row) 


	
	elif  table_choice=='4':	
		'''ships table'''	
		key=(input("Enter the ship name:  "))
		attribute=int(input("What do you want to update:\n"+str(this_dict[table_choice])+"\n"))
		ans=input("Enter the updated value:  ")
		#sql_command="""UPDATE ships SET ?=? WHERE ship=? AND battle=?"""
		if attribute==1:			
			c.execute("""UPDATE ships SET ship_name=(?) WHERE ship_name=(?)""",(ans, key,))
			c.execute("""SELECT * FROM ships WHERE ship_name=(?)""",(ans,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row) 
		elif attribute==2:
			c.execute ("""UPDATE ships SET class=(?) WHERE ship_name=(?)""",(ans, key,))
			c.execute("""SELECT * FROM ships WHERE ship_name=(?)""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row) 
		elif attribute==3:
			c.execute ("""UPDATE ships SET launched=(?) WHERE ship_name=(?)""",(ans, key,)) 
			c.execute("""SELECT * FROM ships WHERE ship_name=(?)""",(key,))
			rows = c.fetchall()
			print("\nThe updated tuple is:\n")
			for row in rows:
				print(row) 



n=input("Select choice\n 1:insert\n 2:update\n 3:delete\n")

table_name=input("Select table\n 1.battle\n 2. classes\n 3. outcome\n 4. ships\n")
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



