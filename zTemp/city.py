import codecs, json
from memorial.models import City,State

load_citys = codecs.open('zTemp/city.json', encoding='utf-8').read()
citys = json.loads(load_citys)


for ostan in citys:
    try:
        STATE = State.objects.get(state=ostan)
        ostanCitys = citys.get(ostan)
        for city in ostanCitys:
            id = ostanCitys.get(city)
            City.objects.create(state=STATE,city=city,id=id)
    except:
        print("Import ERROR!")
        print(ostan)
        print("Import ERROR!")