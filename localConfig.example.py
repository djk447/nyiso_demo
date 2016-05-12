from psycopg2 import connect

def makeConnection():
  try:
    conn = connect("dbname='nyiso' user='admin' host='localhost' port=5433 password= YOUR PASSWORD")
  except:
    print ("Failed to Connect")
  return (conn)