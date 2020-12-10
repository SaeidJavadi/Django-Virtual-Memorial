import codecs, json
from memorial.models import City, State

load_citys = codecs.open('zTemp/stateCity.json', encoding='utf-8').read()
citys = json.loads(load_citys)

o = 0
c = 0
e = 0
for ostan in citys:
    try:
        STATE = State.objects.create(state=ostan)
        ostanCitys = citys.get(ostan)
        o += 1
        for city in ostanCitys:
            id = ostanCitys.get(city)
            City.objects.create(state=STATE, city=city, id=id)
            c += 1
            print(f"State={o} | City={c}", end="\r")
    except:
        e += 1
        print("Import ERROR!")
        print(ostan)
        print("Import ERROR!")
print("Finish.\n")
print(f"\nState={o} | City={c}\nError={e}")

# import codecs
# exec(open('zTemp/stateCity_Import.py').read())
# exec(codecs.open('zTemp/stateCity_Import.py', encoding='utf-8').read())
