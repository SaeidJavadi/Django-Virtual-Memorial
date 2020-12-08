


ostans = (
    'تهران',
    'گیلان',
    'آذربایجان شرقی',
    'خوزستان',
    'فارس',
    'اصفهان',
    'خراسان رضوی',
    'قزوین',
    'سمنان',
    'قم',
    'مرکزی',
    'زنجان',
    'مازندران',
    'گلستان',
    'اردبیل',
    'آذربایجان غربی',
    'همدان',
    'کردستان',
    'کرمانشاه',
    'لرستان',
    'بوشهر',
    'کرمان',
    'هرمزگان',
    'چهارمحال و بختیاری',
    'یزد',
    'سیستان و بلوچستان',
    'ایلام',
    'کهگلویه و بویراحمد',
    'خراسان شمالی',
    'خراسان جنوبی',
    'البرز',
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
# exec(codecs.open('zTemp/ostans.py', encoding='utf-8').read())