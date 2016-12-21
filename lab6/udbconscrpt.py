import MySQLdb
import configparser


config = configparser.RawConfigParser()
config.read('config.ini')


class Event():
    id = 0
    name = ""
    address = ""
    time = ""
    desc = ""
    imageUrl = ""

    def get(self, connection, id):
        cur = connection.cursor()
        cur.execute("SELECT * FROM main_event WHERE id=%d" % (id,))
        res = cur.fetchall()[0]
        self.id = res[0]
        self.name = res[1]
        self.address = res[2]
        self.time = res[3]
        self.desc = res[4]
        self.imageUrl = res[5]
        cur.close()
        return self

    def __str__(self):
        return "Id=%d, Name=%s, time=%s, address=%s"\
            % (self.id, self.name, self.time, self.address)


if __name__ == "__main__":
    con = MySQLdb.connect(
        host=config["DATABASES"]["HOST"],
        user=config["DATABASES"]["USER"],
        passwd=config["DATABASES"]["PASSWORD"],
        db=config["DATABASES"]["NAME"]
    )

    ev = Event()
    print(ev.get(con, 5))
    con.close()
