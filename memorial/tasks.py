


def quranCount(marhom):
    quran = marhom.deadquran
    jozs = {}
    jozs['j1'] = quran.j1.count()
    jozs['j2'] = quran.j2.count()
    jozs['j3'] = quran.j3.count()
    jozs['j4'] = quran.j4.count()
    jozs['j5'] = quran.j5.count()
    jozs['j6'] = quran.j6.count()
    jozs['j7'] = quran.j7.count()
    jozs['j8'] = quran.j8.count()
    jozs['j9'] = quran.j9.count()
    jozs['j10'] = quran.j10.count()
    jozs['j11'] = quran.j11.count()
    jozs['j12'] = quran.j12.count()
    jozs['j13'] = quran.j13.count()
    jozs['j14'] = quran.j14.count()
    jozs['j15'] = quran.j15.count()
    jozs['j16'] = quran.j16.count()
    jozs['j17'] = quran.j17.count()
    jozs['j18'] = quran.j18.count()
    jozs['j19'] = quran.j19.count()
    jozs['j20'] = quran.j20.count()
    jozs['j21'] = quran.j21.count()
    jozs['j22'] = quran.j22.count()
    jozs['j23'] = quran.j23.count()
    jozs['j24'] = quran.j24.count()
    jozs['j25'] = quran.j25.count()
    jozs['j26'] = quran.j26.count()
    jozs['j27'] = quran.j27.count()
    jozs['j28'] = quran.j28.count()
    jozs['j29'] = quran.j29.count()
    jozs['j30'] = quran.j30.count()
    # max_j = sorted(jozs, key=(lambda key:jozs[key]), reverse=True)
    min_j = sorted(jozs, key=(lambda key:jozs[key]))
    offer = min_j[0]
    khatmCount = jozs.get(offer)
    offer = int(offer.replace('j',''))
    return khatmCount, offer