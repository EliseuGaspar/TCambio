import json as j
import sqlite3 as db

class Gerenciador():

    def Versao(self):
        with open('admin/database/app_info.json',encoding='utf-8') as file:
            self.version_app = j.load(file)
            print(self.version_app)
        return self.version_app
    
    def Cadastrar(self,email):
        correspondencia = False
        self.conection = db.connect('admin/database/database.db')
        self.cursor = self.conection.cursor()

        emails_lista = self.cursor.execute(
            "SELECT * FROM 'email_table' "
        ).fetchall()

        lista_de_emails = emails_lista

        for mail in lista_de_emails:
            if email in mail[0]:
                correspondencia = True
        
        if (correspondencia):
            self.conection.close()
            return {'estado':'Já existe um e-mail igual a esse!'}
        else:
            self.cursor.execute(
                f"INSERT INTO 'email_table' VALUES('{email}')"
            )
            self.conection.commit()
            self.conection.close()
            return {'estado':'Cadastramento efectuado com sucesso!'}

        

        
