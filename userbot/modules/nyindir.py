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


@register(outgoing=True, pattern='^.tobat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**TOBAT NJENG TOBATTT, KIAMAT BENTAR LAGI DAN LU MASIH GINI?**")
    sleep(3)
    await typew.edit("**TOBAT NYED BIAR APA SI LU GITU? GA ADA FAEDAHNYA. BIAR APA COBA?**")
    sleep(3)
    await typew.edit("**BIAR TERKENAL?**")
    sleep(3)
    await typew.edit("**BIAR VIRAL?**")
    sleep(3)
    await typew.edit("**TOBAT YA NYED TOBAT IBADAH JANGAN MAKSIAT MULU TOD**")


@register(outgoing=True, pattern='^.berlin(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Hai gaes nama gua Berlin.**")
    sleep(4)
    await typew.edit("**Gua asal Jogja,tapi asli Brebes,**")
    sleep(3)
    await typew.edit("**umur gua baru 16,salam kenal yaa ajg**")


@register(outgoing=True, pattern='^.wibutlol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**APASIH NGATAIN WIBU²,BIAR NGAPA NGATAIN ORA WIBU KEK GITU ANJG?,CUMA PAKE PP ANIME DIKATAIN WIBU KONTOL,NONTON ANIME AJA KAGA GUA ASYU..**")


CMD_HELP.update(
    {
        "nyindir": "**Modules** `nyindir`\
        \n\n•🗿CMD🗿: `.tua`\
        \n•Penjelasan: Gatau cek sendiri asu\
        \n\n•🗿CMD🗿: `.stress`\
        \n•Penjelasan: Gatau cek sendiri asu\
        \n\n•🗿CMD🗿: `.gajelas`\
        \n•Penjelasan: Nyindir orang Goblok\
        \n\n•🗿CMD🗿: `.caper`\
        \n•Penjelasan: Buat Orang Caper\
        \n\n•🗿CMD🗿: `.tobat`\
        \n•Penjelasan: Tobat Nyed Tobat\
        \n\n•🗿CMD🗿: `.wibutlol`\
        \n•Penjelasan: Gas Katain Balik Wibu\
    "
    }
)
