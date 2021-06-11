from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.tua(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**EH BOCAH TUA HINA, KALO TUANYA TUA AJA GOBLOK GA COCOK BOCAH TUA KAYA LU MAIN KEK GINIAN TOLOL UDAH BAU TANAH JADINYA GAUSAH BELAGU KONTOL.**")
    sleep(7)
    await typew.edit("**URUSIN AJA BEGO KUBURAN LU ITU BESOK CALON RUMAH LU SEKALI SEKALI YEKAN LU TINGGAL DIRUMAH GA DI RONGSOKAN MULU**")


@register(outgoing=True, pattern='^.stress(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**NI YE GUA KASIH TAU SAMA LU YA BEGO LU BAKAL PUNYA ANAK CUCU LU KASIH TAU AJA KETURUNAN LU TUH KALO UDAH HINA YA HINA BEGO.**")
    sleep(6)
    await typew.edit("**GUA SARANIN JUGA LU SURUH ANAK LU NYEKOLAHIN CUCU LU BESOK BIAR PINTER GA KEK LU DONGO GOBLOK IDIOT YEKAN.ANAK LU SURUH KERJA BIAR PUNYA DUIT BIAR BISA MAKAN JANGAN BERGANTUNG SAMA BANSOS MULU.NIH YA KALO KOSA KATA MASIH NYURI DARI ORANG LAINAPA LAGI COPY PASTE GAUSAH BELAGU KONTOL.MAKANYA OTAKNYA DIPAKE TOLOL JANGAN DITARO DI DENGKUL MULU.**")
    sleep(14)
    await typew.edit("**KEBANYAKAN COLI SIH MAKANYA JADI KOPONG TUH DENGKUL ISI OTAK LU AJA CUMA DEBU SAMA SARANG LABA LABA BEGO**")
    sleep(6)
    await typew.edit("**GA USAH SO MANTEP BEGO KALO LEHER MASIH BEDAKI SELANGKANGAN BEJAMUR KONTOL NANAHAN MAKANYA KALO MANDI PAKE AIR BUKAN PAKE PASIR.**")
    sleep(6)
    await typew.edit("**GUA JAGO GA KAYA LU YG SOSOAN JADI JAGOAN KOSA KATA CUMA 1-10 TERUS DIBALIKIN 10-1 SAMA KAYA HIDUP LU MUNDAR MANDIR SANA SINI CARI PINJEMAN BUAT MAKAN SEHARI HARI YEKAN**")
    sleep(7)
    await typew.edit("**MAU SAMPE KAPAN PUN GUA BAKALAN LADENIN LU GOBLOK, LADENIN MANUSIA PURBA JELEK KEK LU GABAKALAN BERENTI GUA TOLOL NI YE GUA SARANIN MENDING LU APUS TELE DAH KONTOL.**")


@register(outgoing=True, pattern='^.gajelas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**YA AMPUN LU NGOMONG APA? GA NYAMBUNG KONTOL KAYA KEHIDUPAN LU MAKANYA ORG ORG KAYA LU GABAKALN MAJU HIDUPNYA APA LAGI ORG ORG BAWAHAN KAYA LU.**")


@register(outgoing=True, pattern='^.caper(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**CAPER BET LU NAJIS, MAU DI RESPON KAH? GUA TAU LU DIKACANGIN JADI LU CAPER KYK GINI. DAPET APA SI GITU? DI GAJI GA? NGACA + MIKIR LU UDAH GEDE KONTOL.**")


CMD_HELP.update({
    "nyindir1":
    "•🗿CMD🗿: `.tua`\
    \n•Penjelasan: Gatau cek sendiri asu\
    \n\n•🗿CMD🗿: `.stress`\
    \n•Penjelasan: Gatau cek sendiri asu\
    \n\n•🗿CMD🗿: `.gajelas`\
    \n•Penjelasan: Nyindir orang Goblok.\
    \n\n•🗿CMD🗿: `.caper`\
    \n•Penjelasan: Buat Orang Caper."


})
