MODEL = "Film(Id Integer Primary Key AUTOINCREMENT, code_avtor Integer, name Text, description Text, genre Text, FOREIGN KEY(code_avtor) REFERENCES User(id))"