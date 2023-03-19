import datetime

class OM:
    def __init__(self, nume, prenume, data_nasterii):
        self.nume = nume
        self.prenume = prenume
        self. data_nasterii = datetime.datetime.strptime(data_nasterii, "%d-%m-%Y")

    def __str__(self):
        return f"Numele omului este {self.nume} , prenumele este {self.prenume} si are varsta{self.data_nasterii}"

    def varsta(self):
        today = datetime.date.today()
        age = today.year - self.data_nasterii.year - (
                    (today.month, today.day) < (self.data_nasterii.month, self.data_nasterii.day))
        return f"{self.nume} {self.prenume} are varsta de {age} ani."


class Student(OM):
    def __init__(self, nume, prenume, data_nasterii, facultate, an_inmatriculare):
        super().__init__(nume, prenume, data_nasterii)
        self.facultate = facultate
        self.an_inmatriculare = an_inmatriculare

    def ani_de_studiu(self):
        an_curent = datetime.datetime.now().year
        ani_studiu = an_curent - self.an_inmatriculare
        return ani_studiu

class Profesor(OM):
    def __init__(self, nume, prenume, data_nasterii, materie_predata):
        super().__init__(nume, prenume, data_nasterii)
        self.materie_predata = materie_predata

    def numar_materii(self):
        return f"Profesorul {self.nume} {self.prenume} preda {len(self.materie_predata)}"

    def profesor_materii(self):
        return f"Profesorul {self.nume} {self.prenume} preda{self.materie_predata}"

    @property
    def materia_cu_cel_mai_lung_nume(self):
        materie_lunga = ""
        for materie in self.materie_predata:
            if len(materie) > len(materie_lunga):
                materie_lunga = materie
        return materie_lunga


class Director_de_liceu(Profesor):
    def __init__(self, nume, prenume, data_nasterii, materie_predata, nume_liceu):
        super().__init__(nume, prenume, data_nasterii, materie_predata)
        self.nume_liceu = nume_liceu

    def litere_unice(self):
        litere = set(self.nume.replace(" ", "")+self.prenume.replace(" ", ""))
        return f"Directorul liceului {self.nume} {self.prenume} are urmatoarele litere unice in nume: {''.join(litere)}"


om1 = OM("Popescu", "Ion", "01-01-1980")
om2 = OM("Marinescu", "Madalina", "15-10-1997")
print(om1.varsta())
print(om2.varsta())


student1 = Student("Popescu", "Ion", "01-01-2000", "Informatica", 2020)
student2 = Student("Ionescu", "Maria", "02-02-2001", "Matematica", 2022)
print(student1.ani_de_studiu())
print(student2.ani_de_studiu())

profesor1 = Profesor("Popa", "Rares", "10-10-1970", ["Istorie", "Sociologie"])
profesor2 = Profesor("Ionita", "Analisa", "20-12-1985", ["Geografie", "Geologie", "Biologie"])
print(profesor1.numar_materii())
print(profesor1.profesor_materii())
print(profesor1.materia_cu_cel_mai_lung_nume)

print(profesor2.numar_materii())
print(profesor2.profesor_materii())
print(profesor2.materia_cu_cel_mai_lung_nume)

director1 = Director_de_liceu("Georgescu", "Mihai", "01-01-1965", "Fizica", "Liceul Mihai Eminescu")
director2 = Director_de_liceu("Paraschivescu", "Irina", "05-05-1975", "Chimie", "Liceul Stefan cel Mare")
print(director2.litere_unice())
print(director1.litere_unice())


with open("nume_prenume.txt", "w") as f:
    f.write(f"Studenti:\n{student1.nume} {student1.prenume}\n{student2.nume} {student2.prenume}\n")
    f.write(f"Profesori:\n{profesor1.nume} {profesor1.prenume}\n{profesor2.nume} {profesor2.prenume}\n")
    f.write(f"Directori de liceu:\n{director1.nume} {director1.prenume}\n{director2.nume} {director2.prenume}\n")

with open("nume_prenume.txt", "r") as f:
    print(f.read())
