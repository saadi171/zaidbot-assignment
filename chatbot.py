import random

# ===============================
# Character Building Responses
# ===============================

character_brain = {

    "happy":[

        "😊 Alhamdulillah! Happiness is a blessing from Allah. Remember to thank Him.",

        "😊 Spread your smile. The Prophet ﷺ said that smiling at your brother is charity.",

        "😊 Share your happiness with others.",

        "😊 Gratitude increases blessings.",

        "😊 Always remain humble."
    ],

    "sad":[

        "😔 Allah says:\n\n'Indeed, with hardship comes ease.'\n(Quran 94:5-6)",

        "😔 Never lose hope in Allah's mercy.\n(Quran 39:53)",

        "😔 Every difficulty is temporary.",

        "😔 Make dua and trust Allah.",

        "😔 Better days are coming."
    ],

    "angry":[

        "😠 Prophet Muhammad ﷺ said:\n\n'The strong man is not the one who defeats others, but the one who controls himself when angry.'\n(Sahih al-Bukhari)",

        "😠 Sit down if you are standing.",

        "😠 Make Wudu.",

        "😠 Remain silent until you calm down.",

        "😠 Ask Allah for patience."
    ],

    "stressed":[

        "😰 Take a deep breath and remember Allah.",

        "😰 Read Surah Ash-Sharh (94).",

        "😰 Allah never burdens a soul beyond its capacity.\n(Quran 2:286)",

        "😰 Perform two Rak'ah of Salah.",

        "😰 Trust Allah's plan."
    ]

}

# ===============================
# Islamic Knowledge
# ===============================

islamic_brain = {

    "what is the goal of my life":

"""
📖 Allah says:

'I did not create jinn and mankind except to worship Me.'

(Quran 51:56)

Your purpose is to worship Allah, obey Him, develop good character, help others and prepare for the Hereafter.
""",

    "why did allah create us":

"""
Allah created us to worship Him sincerely.

(Quran 51:56)

Life is a test, and our deeds determine our success in the Hereafter.
""",

    "who is prophet muhammad":

"""
Prophet Muhammad ﷺ is the final Messenger of Allah.

Allah says:

'And We have not sent you except as a mercy to the worlds.'

(Quran 21:107)
""",

    "importance of parents":

"""
Allah says:

'Be grateful to Me and to your parents.'

(Quran 31:14)

Respecting parents is among the greatest acts of worship.
""",

    "importance of prayer":

"""
The Prophet ﷺ said:

'The first matter that the slave will be brought to account for on the Day of Judgment is the prayer.'

(Reported in the major hadith collections)

Never miss your Salah.
""",

    "how can i control anger":

"""
The Prophet ﷺ said:

'Do not become angry.'

(Sahih al-Bukhari)

Practical advice:

• Make Wudu
• Stay silent
• Change your position
• Remember Allah
""",

    "what is honesty":

"""
The Prophet ﷺ said:

'Truthfulness leads to righteousness, and righteousness leads to Paradise.'

(Sahih al-Bukhari & Sahih Muslim)
""",

    "who was abu bakr":

"""
Abu Bakr As-Siddiq (RA)

• First Caliph
• Closest friend of Prophet ﷺ
• Known for truthfulness
• Supported Islam with his wealth
""",

    "who was umar":

"""
Umar ibn Al-Khattab (RA)

• Second Caliph
• Symbol of justice
• Courageous leader
• Expanded the Muslim state
""",

    "who was uthman":

"""
Uthman ibn Affan (RA)

• Third Caliph
• Extremely generous
• Oversaw the standardization of the written Quran
• Known for modesty
""",

    "who was ali":

"""
Ali ibn Abi Talib (RA)

• Fourth Caliph
• Cousin and son-in-law of Prophet ﷺ
• Known for wisdom, courage and justice
"""

}

# ===============================
# Default Responses
# ===============================

default_reply = [

"I'm still learning that topic.",

"Can you ask another Character Building question?",

"Try asking about happiness, anger, honesty, parents, Salah or the purpose of life.",

"I specialize in Character Building and Islamic guidance."

]

# ===============================
# Main Function
# ===============================

def get_response(message):

    message = message.lower().strip()

    if message in character_brain:

        return random.choice(character_brain[message])

    if message in islamic_brain:

        return islamic_brain[message]

    return random.choice(default_reply)