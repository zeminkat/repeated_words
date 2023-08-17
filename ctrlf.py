import operator
baglaclar = ['ve', 'ile', 'ya da', 'veya', 'ancak', 'fakat', 'ama', 'veya', 'veyahut', 'yahut', 'hem',
             'de', 'ile beraber', 'beraber', 'artı', 'kadar', 'ise', 'ki', 'çünkü', 'zira', 'oysa',
             'yani', 'demek ki', 'ama', 'fakat',"daha","gibi","da","de","her","şey", 'hâlbuki', 'oysaki',
             'şayet', 'eğer', 'madem', 'rağmen', 'dolayı', 'için', 'diye',"bir","ne","bu","o", 'açısından', 'bakımından']
edatlar = ['a', 'acaba', 'altında', 'anında', 'aşağıda', 'başında', 'belki', 'beri', 'bile', 'boyunca',
           'bu arada', 'dair', 'dolu', 'döneminde', 'doğru', 'dışında', 'e', 'elinde', 'göre', 'göreli',
           'hakkında', 'hariç', 'hep', 'içeri', 'içinde', 'için', 'ilgili', 'ilimine göre', 'karşın', 'karşı',
          'karşılığında', 'kat', 'kaynaklı', 'kıyasla', 'kadar', 'lütfen', 'mahiyetinde', 'mekte', 'meğer',
           'meğerki', 'nasıl', 'nasılsa', 'nerede', 'nereden', 'niçin', 'o', 'olduğunda', 'oldukça',
           'olduğu gibi', 'olduğunu', 'orada', 'pek', 'rağmen', 'sayesinde', 'sanki', 'sonra',
           'süresince', 'tahminen', 'tarafından', 'tümüyle', 'vardı', 'vardır', 'vardırlar',
           'veya', 'yakın', 'yakınında', 'yani', 'yönünde', 'üzerinde', 'üzerine']


kaynak="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ";hedef="abcçdefgğhıijklmnoöprsştuüvyz";translator=str.maketrans(kaynak,hedef)
path=r"C:\Users\Sedat\PycharmProjects\pythonProject\CTRL+F Mantığı\tarama.txt"
sozluk={};liste=[];liste2=[];siralama=list()
with open(path,"r",encoding="UTF-8") as dosya:

    liste+=(i.translate(translator) for i in dosya.read().split())
for i in liste:
    if not str(i).isalpha() or (str(i) in baglaclar or str(i) in edatlar):
        liste2.append(i)
for i in liste2:
    liste.remove(i)
for i in liste:
    if i not in sozluk.keys():
        sozluk[i]=1
    else:
        sozluk[i]+=1
progress_start=0
for i in sozluk:
    progress=float((100*(progress_start+1))/len(sozluk));print("İlerleme durumu %{} ||| {} Kelime tarandı".format(progress,progress_start+1))
    progress_start += 1
    if sozluk[i]==sorted(sozluk.values(),reverse=True)[0]:
        siralama.append([i,sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[1]:
        siralama.append([i,sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[2]:
        siralama.append([i, sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[3]:
        siralama.append([i, sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[4]:
        siralama.append([i, sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[5]:
        siralama.append([i, sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[6]:
        siralama.append([i, sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[7]:
        siralama.append([i, sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[8]:
        siralama.append([i, sozluk[i]])
    elif sozluk[i]==sorted(sozluk.values(),reverse=True)[9]:
        siralama.append([i, sozluk[i]])
siralama.sort(key=operator.itemgetter(1),reverse=True)
for i in range(10):
    print("{}. Sıra >>Metinde geçen {} kelimesi toplamda {} kere kullanılmış".format(i+1,siralama[i][0],siralama[i][1]))









