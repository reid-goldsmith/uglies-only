import sqlite3

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(ide,upload):
    try:
        sqliteConnection = sqlite3.connect('/Users/reidgoldsmith/Desktop/Computa/uglies-only/uglies-only/pics.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO oldpictures
                                  (id, unedited) VALUES (?, ?)"""
        
        photo = upload #convertToBinaryData(upload)
        # Convert data into tuple format
        data_tuple = (ide, photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")


###OUTPUT###
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(ide):
    try:
        sqliteConnection = sqlite3.connect('/Users/reidgoldsmith/Desktop/Computa/uglies-only/uglies-only/pics.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from oldpictures where id = ?"""
        cursor.execute(sql_fetch_blob_query, (ide,))
        record = cursor.fetchall()
        for row in record:
            photo  = row[1]

            #print("Storing employee image and resume on disk \n")
            #photoPath = "E:\pynative\Python\photos\db_data\\" + name + ".jpg"
            #resumePath = "E:\pynative\Python\photos\db_data\\" + name + "_resume.txt"
            #writeTofile(photo, photoPath)
            #writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")
    return photo

