from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery

START_MESSAGE_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton('🎷 ℂ𝔸ℕ𝔸𝕃 🎻', url='https://t.me/maxUpload')],
    [InlineKeyboardButton("💳 𝔸ℂℂ𝔼𝕊𝕆 🔐", url="https://t.me/catDev01")]
])

DOWN = ReplyKeyboardMarkup([
	[("❌ ℂ𝔸ℕℂ𝔼𝕃𝔸ℝ ❌"),
	("📥 𝔻𝔼𝕊ℂ𝔸ℝ𝔾𝔸ℝ 📥")]
],one_time_keyboard=True,resize_keyboard=True)

root = InlineKeyboardMarkup(
	[
		[InlineKeyboardButton("༒⩔៩Ʀ ♬Ʀ¢Ϧɨ⩔០ន༒",callback_data='root')]
	]
)
tutos = InlineKeyboardMarkup(
	[
		[InlineKeyboardButton("👨🏼‍💻 ₮Ʉ₮Ø$ 👨🏼‍💻",url='https://t.me/+iEX64u7itJMzOGY5')]
	]
)

cancelar = InlineKeyboardMarkup(
	[
		[InlineKeyboardButton("༒€₳₦€ɆⱠ₳Ɍ༒",callback_data='cancelar')]
	]
)

MENU = InlineKeyboardMarkup(
	[	[InlineKeyboardButton("👑𝔼𝔻𝕌ℂ𝔸👑", callback_data = "EDUCA")],		[InlineKeyboardButton("༒ℝ𝕖𝕧𝔸𝕡𝕪𝕖༒", callback_data="APYE"),InlineKeyboardButton("༒ℝ𝕖𝕧𝔼𝕕𝕚𝕔༒", callback_data="EDIC")],
		[InlineKeyboardButton("༒ℝ𝕖𝕧ℂ𝕚𝕟𝕗𝕠༒", callback_data="CINFO"),InlineKeyboardButton("༒ℝ𝕖𝕧𝕊𝕥𝕘𝕠༒", callback_data="STGO")],
		[InlineKeyboardButton("༒ℝ𝕖𝕧ℝ𝕖𝕘𝕦༒", callback_data="REGU"),InlineKeyboardButton("༒ℝ𝕖𝕧𝕌𝕔𝕚𝕖༒", callback_data="UCIE")],
		[InlineKeyboardButton("༒ℝ𝕖𝕧𝕋𝕖𝕔𝕖༒", callback_data="TECE")],
		[InlineKeyboardButton("❌",callback_data="del")]
	]
)

APYE = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📖 ℝ𝕖𝕧𝕚𝕤𝕥𝕒𝕤 𝕒𝕡𝕪𝕖.📕", callback_data="REVISTAS.apye")],
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5")
        ],
        [InlineKeyboardButton("⬅️",callback_data="back")]
    ]
)

EDIC = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📖 ℝ𝕖𝕧𝕚𝕤𝕥𝕒𝕤 𝔼𝕕𝕚𝕔𝕚𝕠𝕟𝕖𝕤📕", callback_data="REVISTAS.edic")],
        [InlineKeyboardButton("1", callback_data="01"),
            InlineKeyboardButton("2", callback_data="02"),
            InlineKeyboardButton("3", callback_data="03"),
            InlineKeyboardButton("4", callback_data="04"),
            InlineKeyboardButton("5", callback_data="05")],
            [InlineKeyboardButton("⬅️", callback_data="back")]
        ]
)

CINFO = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📖 ℝ𝕖𝕧𝕚𝕤𝕥𝕒𝕤 ℂ𝕚𝕟𝕗𝕠.📕", callback_data="REVISTAS.cinfo")],
        [InlineKeyboardButton("1", callback_data="001"),
            InlineKeyboardButton("2", callback_data="002"),
            InlineKeyboardButton("3", callback_data="003"),
            InlineKeyboardButton("4", callback_data="004"),
            InlineKeyboardButton("5", callback_data="005")],
            [InlineKeyboardButton("⬅️", callback_data="back")]
        ]
)

STGO = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📖 ℝ𝕖𝕧𝕚𝕤𝕥𝕒𝕤 𝕊𝕥𝕘𝕠.📕", callback_data="REVISTAS.santiago")],
        [InlineKeyboardButton("1", callback_data="0001")],
            [InlineKeyboardButton("2", callback_data="0002")],
            [InlineKeyboardButton("⬅️", callback_data="back")]
        ]
)

ZIPSTGO = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📦 𝕊𝕖𝕝𝕖𝕔𝕔𝕚𝕠𝕟𝕖 𝕥𝕒𝕞𝕒𝕟̃𝕠 𝕕𝕖𝕝 𝕫𝕚𝕡 🗜️", callback_data="ZIPS.santiago")],
        [InlineKeyboardButton("20", callback_data="z2"),
            InlineKeyboardButton("30", callback_data="z3"),
            InlineKeyboardButton("40", callback_data="z4"),
            InlineKeyboardButton("50", callback_data="z5")],
            [InlineKeyboardButton("⬅️", callback_data="back")]
        ]
)

REGU = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📖 ℝ𝕖𝕧𝕚𝕤𝕥𝕒𝕤 ℝ𝕖𝕘𝕦.📕", callback_data="REVISTAS.regu")],
        [InlineKeyboardButton("1", callback_data="r1"),
            InlineKeyboardButton("2", callback_data="r2"),
            InlineKeyboardButton("3", callback_data="r3"),
            InlineKeyboardButton("4", callback_data="r4"),
            InlineKeyboardButton("5", callback_data="r5")],
            [InlineKeyboardButton("⬅️", callback_data="back")]
        ]
)

UCIE = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📖 ℝ𝕖𝕧𝕚𝕤𝕥𝕒𝕤 𝕌𝕔𝕚𝕖𝕟𝕔𝕚𝕒.📕", callback_data="REVISTAS.uciencia")],
        [InlineKeyboardButton("1", callback_data="r01"),
            InlineKeyboardButton("2", callback_data="r02"),
            InlineKeyboardButton("3", callback_data="r03"),
            InlineKeyboardButton("4", callback_data="r04"),
            InlineKeyboardButton("5", callback_data="r05")],
            [InlineKeyboardButton("⬅️", callback_data="back")]
        ]
)

TECE = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📖 ℝ𝕖𝕧𝕚𝕤𝕥𝕒𝕤 𝕋𝕖𝕔𝕖𝕕𝕦.📕", callback_data="REVISTAS.tecedu")],
        [InlineKeyboardButton("1", callback_data="t1"),
            InlineKeyboardButton("2", callback_data="t2"),
            InlineKeyboardButton("3", callback_data="t3"),
            InlineKeyboardButton("4", callback_data="t4"),
            InlineKeyboardButton("5", callback_data="t5")],
            [InlineKeyboardButton("⬅️", callback_data="back")]
        ]
)