#kullanacağım kütüphaneleri import ettim
import math
from operator import itemgetter

#4 tane değişken tanımladım bunlar noktaların koordinatlarını oluşturacak olan değerler
#değişkenlere kafama göre değer verdim bunun yerine kullanıcıdan alınarak da yapılabilirdi 
x1=1
y1=1
x2=4
y2=5

#tanımlanan değişkenleri tuple da birleştirerek noktaların koordinatlarını oluşturdum sonra hepsini points list inde tuttum
points = [(x1,y1),(x2,y1),(x2,y2)]

#euclideanDistance adında bir fonksiyon oluşturdum bu fonksiyon iki noktanın koordinatlarını aldıktan sonra aralarındaki mesafeyi hesaplıyıp döndürüyor
def euclideanDistance(point1,point2):
   return math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)


#noktaların arasındaki mesafenin tutulması için liste oluşturdum
distances=[]

#points listesinin içinde bulunan iki ögeyi karşılaştırmak için iki tane for döngüsü oluşturdum 
#döngüler sırayla 1. 2. , 1. 3. , 2. 3.  noktaları karşılaştırıyor 
for i in range(len(points)):
   for j in range(i+1,len(points)):
      distance = euclideanDistance(points[i],points[j])
      distances.append((points[i],points[j],distance))


#itemgetter kullanarak tuple içinden min ve max veriyi çektik
min_distance = min(distances, key=itemgetter(2))
EF_distance = max(distances, key=itemgetter(2))
print("verilen noktalarda iki tanesi arasında ki en kısa mesafe:",min_distance[2])
print("E ve F arasındaki mesafe:",EF_distance[2])
