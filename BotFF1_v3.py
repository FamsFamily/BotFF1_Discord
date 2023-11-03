import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def he(ctx, count_he = 3):
    await ctx.send("he" * count_he)

@bot.command()
async def wk(ctx, count_wk = 3):
    await ctx.send("wk" * count_wk)

@bot.command()
async def hi(ctx, count_hi = 3):
    await ctx.send("hi" * count_hi)

@bot.command()
async def ha(ctx, count_ha = 3):
    await ctx.send("ha" * count_ha)

@bot.command()
async def hiks(ctx, count_hiks = 3):
    await ctx.send("hiks " * count_hiks)

@bot.command()
async def ho(ctx, count_ho = 3):
    await ctx.send("ho" * count_ho)

@bot.command()
async def hu(ctx, count_hu = 3):
    await ctx.send("hu" * count_hu)

@bot.command()
async def uhuk(ctx, count_uhuk = 3):
    await ctx.send("uhuk " * count_uhuk)

@bot.command()
async def prok(ctx, count_prok = 3):
    await ctx.send("prok " * count_prok)

@bot.command()
async def meme1(ctx):
    with open('Slide2.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def meme2(ctx):
    with open('Slide3.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def meme3(ctx):
    with open('Slide4.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def menerapkan_gaya_hidup_ramah_lingkungan(ctx):
    await ctx.send('''
- Kurangi Penggunaan Plastik Sekali Pakai
- Hemat Energi di Rumah
- Gunakan Transportasi Berkelanjutan
- Daur Ulang
- Menghemat Air
- Minimalkan Pemakaian Bahan Kimia yang Berbahaya
- Mengurangi Konsumsi Daging
- Budidaya Tanaman Sendiri
- Menggunakan Produk Ramah Lingkungan
- Mengurangi Pemborosan Makanan
- Mendukung Komunitas Lokal
- Kurangi Penggunaan Air Botol
- Gunakan Produk Keanekaragaman Hayati yang Bertanggung Jawab
- Menggunakan Kertas Secara Bijaksana
- Kurangi Penggunaan Bahan Bakar Fosil
- Mendukung Pengembangan Ramah Lingkungan
- Mengurangi Konsumsi Internet
Pelajari selengkapnya di https://sohib.indonesiabaik.id/article/langkah-gaya-hidup-ramah-lingkungan-ADgsj
                   ''')
    
@bot.command()
async def cara_mengurangi_limbah(ctx):
    await ctx.send('''
- Tidak Menggunakan Sedotan Plastik
- Membawa Tas Belanja Sendiri
- Mempunyai dan Membawa Botol Minum Sendiri
- Membiasakan Diri Untuk Memasak Sendiri di Rumah
- Membeli Barang dalam Kemasan yang Lebih besar Untuk Waktu yang Lama
- Membatasi Penggunaan Microbeads
- Memilih Es Krim Cone dibandingkan Es Krim Cup
- Hindari Mengonsumsi Permen Karet
- Membatasi Penggunaan Plastik dalam Membungkus Paket
- Menggunakan Bahan Bekas yang Bisa Dipakai Lagi
- Membuat Tas Daur Ulang dari Pembungkus Plastik
- Memanfaatkan Botol Plastik Sebagai Pot
- Mengkreasikan Botol Plastik Besar Menjadi Celengan
- Botol Plastik dirubah Menjadi Tempat Pakan Burung
- Merubah Botol Plastik Menjadi Tempat Alat Tulis
Pelajari selengkapnya di https://www.rumah.com/panduan-properti/15-cara-mengurangi-sampah-plastik-rumahan-dan-contoh-daur-ulangnya-27696
                   ''')


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("TOKEN RAHASIA ADA DI SINI")
