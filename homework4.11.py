class book:
    def __init__(self, id, name, muallifi, miqdori, narxi):
        self.id = id
        self.name = name
        self.muallifi = muallifi
        self.miqdori = miqdori
        self.narxi = narxi

        try:
            with open('kitoblar.txt', 'a', encoding='utf-8') as file:
                file.write(f"{self.id}-{self.name}-{self.muallifi}-{self.miqdori}-{self.narxi}\n")
        except FileNotFoundError:
            print("Xatolik: Fayl topilmadi!")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")

    def read_file(self):
        with open('kitoblar.txt', encoding='utf-8') as file:
            qatorlar = file.readlines()
            for i in qatorlar:
                if i.strip():
                    data = i.strip().split("-")
                    print(f"""{"-"*30}
ID: {data[0]}
Kitob nomi: {data[1]}
Muallifi: {data[2]}
Miqdori: {data[3]}
Narxi: {data[4]}
""")

    def choose_book(self, id_book):
        
        with open('kitoblar.txt', 'r+', encoding='utf-8') as file:
            qatorlar = file.readlines()
            
            file.seek(0)
            file.truncate()

            for i in qatorlar:
                if i.strip():
                    data = i.strip().split("-")
                    if id_book == data[0]:
                        data[3] = str(int(data[3]) - 1)
                        print(f"ID:{data[0]} raqamli kitob miqdori bittaga kamaydi.")

                    file.write(f"{data[0]}-{data[1]}-{data[2]}-{data[3]}-{data[4]}\n")
                    
    def delete_book(self, id_book):
        
        with open('kitoblar.txt', 'r+', encoding='utf-8') as file:
            qatorlar = file.readlines()
            
            file.seek(0)
            file.truncate()

            for i in qatorlar:
                if i.strip():
                    data = i.strip().split("-")
                    if id_book == data[0]:
                        print(f"ID: {data[0]} raqamli kitob fayldan ochirildi!")
                        continue

                    file.write(f"{data[0]}-{data[1]}-{data[2]}-{data[3]}-{data[4]}\n")

lst = [[206, "O'tgan kunlar", "Abdulla Qodiriy", 22, 45000],
        [207, "JImjitlik", "Said Ahmad", 15, 50000],
            [208,"Oq kema","Ch.aytmatov",20,20500],
            [209,"Chinor","A.Muxtor",10,35000]]

for i in lst:
    kitob = book(i[0],i[1],i[2],i[3],i[4])

# for i in range(int(input("Nechta kitob kiritmoqchisiz: "))):
#     kitob = book(input("ID: "),input("Nomi: "),input("Muallifi: "),input("Miqdori: "),input("Narxi: "))
    
kitob.read_file()

kitob.choose_book("206")
# kitob.read_file()
kitob.delete_book("208")
# kitob.read_file()

