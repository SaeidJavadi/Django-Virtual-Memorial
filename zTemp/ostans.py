


ostans = (
    'تهران',
    'گیلان',
    'خوزستان',
    'فارس',
    'اصفهان',
    'البرز',
    'ایلام',
    'خراسان رضوی',
    'خراسان شمالی',
    'خراسان جنوبی',
    'قزوین',
    'سمنان',
    'قم',
    'مرکزی',
    'زنجان',
    'مازندران',
    'گلستان',
    'اردبیل',
    'آذربایجان شرقی',
    'آذربایجان غربی',
    'همدان',
    'کردستان',
    'کرمانشاه',
    'لرستان',
    'بوشهر',
    'کرمان',
    'هرمزگان',
    'یزد',
    'چهارمحال و بختیاری',
    'سیستان و بلوچستان',
    'کهگلویه و بویراحمد',

)

from memorial.models import State

i=0
for ostan in ostans:
    State.objects.create(state=ostan)
    i+=1
    print(i)
print('Finish')

# import codecs
# exec(open('zTemp/ostans.py').read())
# exec(codecs.open('zTemp/stateCity_Import.py.py', encoding='utf-8').read())