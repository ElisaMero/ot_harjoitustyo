
import sqlite3

def get_connection():
    """Vastaa yhteyden luonnista tietokantaan.
    """
    connection = sqlite3.connect("database1.db")
    return connection


class SaveData:
    """Luokka, joka vastaa tietokannan luonnista ja
    päivityksestä.
    Attribuutit:
        self.database = kutsuu yhteyden luontifunktiota
        self.highscore = varastoi pelin loputtua
        osumien arvon.
    """
    def __init__(self, highscore):
        """Kutsutaan myös ensimmäistä funktiota
        Args:
        self.database = kutsuu yhteyden luontifunktiota
        self.highscore = varastoi pelin loputtua
        osumien arvon.
        """
        self.database = get_connection()
        self.highscore = highscore
        self.create_table()

    def create_table(self):
        """Kokeillaan luoda tietokanta.
        Jos se on jo olemassa, 
        kutsutaan vain seuraavaa funktiota,
        jolle annetaan syötteenä pelin tulos.
        """
        try:
            self.database.execute(
                "CREATE TABLE Highscores (id SERIAL PRIMARY KEY, highscore INTEGER)")
        except sqlite3.OperationalError:
            pass
        self.store_scores(self.highscore)

    def store_scores(self, highscore):
        """Lisää tuloksen tietokantaan Highscore.
        """
        self.database.execute("INSERT INTO Highscores (highscore) VALUES (:highscore);", {
                              "highscore": highscore})
        self.database.commit()
        self.scores_in_order()

    def scores_in_order(self):
        """Järjestää tietokannan suuruusjärjestykseen, 
        suurimmasta pienempään ja valitaan 5
        kaikista suurinta tulosta.
        Lisäksi listan tupleista valitaan tuplen
        ensimmäinen indeksi (indeksi0) ja lisätään
        ne uuteen listaan.,
        """
        orderlist = self.database.execute(
            "SELECT highscore FROM Highscores ORDER BY highscore DESC LIMIT 5").fetchall()
        self.database.commit()
        list = []
        for i in orderlist:
            list.append(i[0])
        return list
