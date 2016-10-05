# github.com/mateuszpiela
# Import Bibliotek
import serial
import mysql.connector
import datetime
import time
# COM Ustawienia
COM = "COM3"
BAUDRATE = 9600
# Baza Danych Ustawienia
USER = "root"
PASSWORD = "-------"
HOST = "localhost"
DATABASE = "arduino"
# Dla czasu w tabeli SQL
timestamp = datetime.datetime.now()

# Pobieranie wartosci z serial portu
arduino = serial.Serial(COM, BAUDRATE)
time.sleep(10);
arduino.write(b"HELLO");
data = arduino.readline().decode("utf-8").strip();
# MySQL logowanie
mysql = mysql.connector.connect(user=USER, password=PASSWORD,host=HOST,database=DATABASE)
mysql.autocommit = True
#  [Uwaga twoja tabela musi mieć auto_increment]
# Tabela potrzebuje 3 kolumny [ID,temp,time]
# Możesz zmienić nazwę temp na inną 
cur = mysql.cursor() #buffered=true
idno = cur.lastrowid
add_data = ("""INSERT INTO temp VALUES (%s,%s,%s)""")
add_value = (idno,data,timestamp)
cur.execute(add_data, add_value);
mysql.commit();
cur.close();
arduino.close();
