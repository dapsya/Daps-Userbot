# Β© @JustRex Xa-Userbot
# I took these modules from ultroid and modified them
# Jangan hapus yg ada tanda # kontol!
# Hiroshi Userbot

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import hiro_cmd
import asyncio


@hiro_cmd(pattern="lebaran(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('πΊππππππ π―πππ πΉπππ π°πππ π­ππππ')
    animation_chars = [
        '[Happy Eid Mubarak ](https://telegra.ph/file/f950e09cc4aebcf2abe7f.jpg)',
        '[Β­π](https://telegra.ph/file/506f5aa4870472307f8fd.jpg)',
        '[γ€Β­](https://telegra.ph/file/759966f82f6590a1b8dfa.jpg)',
        '[Β­γ€](https://telegra.ph/file/661ca99916b9cf5a582d6.jpg)',
        '[γ€](https://telegra.ph/file/8bec6bbe35d4bd1587569.jpg)',
        '[π](https://telegra.ph/file/360ce99e861f8efca1ea3.jpg)',
        '[β£οΈ](https://telegra.ph/file/701503c243265b40e3223.jpg)',
        '[β€οΈ](https://telegra.ph/file/9f0f76eeba3e54298d60a.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@hiro_cmd(pattern="hbd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('π»ππππ¦ π΅πππ‘ππππ¦')
    animation_chars = [
        '[π»ππππ¦ ](https://telegra.ph/file/2fbc53ea22ec4471929fa.jpg)',
        '[Β­πππ](https://telegra.ph/file/e4e5729634f5c8c0c9e06.jpg)',
        '[π΅πππ‘ππππ¦ππ](https://telegra.ph/file/d60d1697b9ac267371fd6.jpg)',
        '[Β­ππ πππ’π](https://telegra.ph/file/0a5d688271f8259b43a9f.jpg)',
        '[π»ππππ¦ π΅πππ‘ππππ¦ππ](https://telegra.ph/file/2fd7cf79f3478ee3c9a27.jpg)',
        '[ππ](https://telegra.ph/file/0f39e15093b70d3502bda.jpg)',
        '[ππππ](https://telegra.ph/file/59d6d8e8b1b9d3b112fc3.jpg)',
        '[πππ](https://telegra.ph/file/8021015799addb650f107.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@hiro_cmd(pattern="happyaniv(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('π»ππππ¦ π΄πππ£πππ πππ¦')
    animation_chars = [
        '[π»ππππ¦ ](https://telegra.ph/file/f0c6b06eb041dddd01119.jpg)',
        '[β€οΈβ€οΈβ€οΈ](https://telegra.ph/file/ebc83df798ba99a94bfc3.jpg)',
        '[π΄πππ£πππ πππ¦β€οΈβ€οΈ](https://telegra.ph/file/1a302daf9ac95e931b675.jpg)',
        '[Β­ππ¦ πππππ©ββ€οΈβπβπ¨](https://telegra.ph/file/8a1cba2ab4bbd86609a68.jpg)',
        '[π»ππππ¦ π΄πππ£πππ πππ¦π»ππ](https://telegra.ph/file/88a297c386c0c2f999e9c.jpg)',
        '[β€οΈβ€οΈππ](https://telegra.ph/file/f0c6b06eb041dddd01119.jpg)',
        '[πππβ€οΈ](https://telegra.ph/file/59ca0bbaeb740ee58aa72.jpg)',
        '[πππ](https://telegra.ph/file/3cd166b4057b5b60aa71d.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@hiro_cmd(pattern="papku(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('Aku mau ngasih Pap aku buat kamu')
    animation_chars = [
        '[Ini aku](https://telegra.ph/file/091024e9bb4729426cc44.jpg)',
        '[aku ganteng](https://telegra.ph/file/836ec69a83a81b909e106.jpg)',
        '[Ganteng Banget kan π»](https://telegra.ph/file/597969f9c0783081e523e.jpg)',
        '[Β­Ganteng intinyaπ©ββ€οΈβπβπ¨](https://telegra.ph/file/32fc29f1689be15e20a7d.jpg)',
        '[Kamu Mau jadi pacarku?π»ππ](https://telegra.ph/file/0cdcb0452c89a664dcb98.jpg)',
        '[Mau lagi?](https://telegra.ph/file/10140ec996bfed2b41dc1.jpg)',
        '[Nihhh](https://telegra.ph/file/ba17968cd0fa477e96dc3.jpg)',
        '[Terkahir](https://telegra.ph/file/ed6a84a8b1c315183cc35.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)

CMD_HELP.update(
    {
        "ucapan": f"**Plugin : **`ucapan`\
        \n\n    **Perintah :** `{cmd}hbd`\
        \nβ    **Fungsi : **ucapan selamat ulang tahun.\
        \n\n    **Perintah :** `{cmd}lebaran`\
        \nβ    **Fungsi : **Ucapan Lebaran.\
        \n\n    **Perintah :** `{cmd}happyaniv`\
        \nβ    **Fungsi : **Untuk Mengucapkan Happy Aniversary kepasanganmu (Kalo Punya).\
        \n\n    **Perintah :** `{cmd}papku`\
        \nβ    **Fungsi : **Bonus awoakwoak."
    })
