BOT_TOKEN = ""

START_MESSAGE = """Qripplex Airdrop and Referrals
As we are celebrating the launch of the Qripplex project, we have decided to reward our community
for their loyalty and their belief with airdrop and referrals..
Get 2000 PPL (~ $12 ) when you follow the rules + 100 PPL per referral (Unlimited).
You must complete all tasks to receive bounty.
Any cheating or manipulation of the system and you will be disqualified.
The Bounty will end on November 30 2018.
Join Our <a href='http://t.me/Qripplex_community'>Telegram channel</a> (1000 PPL)
Follow Us on <a href='http://twitter.com/QRIPPLEX_PPL'>Twitter</a> (1000 PPL)"""

ADMIN_ID = 0

EMAIL_REGEX = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
ERC20_REGEX = r"0[xX][a-fA-F0-9]{40}"
USERNAME_REGEX = r"^@?(\w){1,15}$"

REGISTRATION_BONUS = 5
REFERER_BONUS = 1

WRONG_CAPTCHA_MESSAGE = "Wrong captcha."
WRONG_EMAIL_MESSAGE = "Wrong email format."
WRONG_USERNAME_MESSAGE = "Wrong twitter username format."
WRONG_ERC20_MESSAGE = "Wrong erc20 format."

CONFIRM_EMAIL_MESSAGE = "Do you confirm %s as your email address?"
CONFIRM_USERNAME_MESSAGE = "Do you confirm %s as your twitter username?"
CONFIRM_ERC20_MESSAGE = "Do you confirm %s as your ERC20 address?"

ASK_EMAIL_MESSAGE = "Send me your e-mail address:"
ASK_CAPTCHA_MESSAGE = "Enter the characters you see in the image"
ASK_USERNAME_MESSAGE = "Nice, now send me your Twitter username"
ASK_ERC20_MESSAGE = "Just one more step! Send me your ERC20 wallet address"

REGISTRATION_SUCCESS_MESSAGE = "Congratulations! You're registered!\nIncrease your balance by sharing this link: %s"
REGISTRATION_ABORTED_MESSAGE = "Registration aborted."
NOT_REGISTERED_MESSAGE = "You're not registered!"
BALANCE_MESSAGE = "Ref link: %s\nYour balance: %s points"
ALREADY_REGISTERED_MESSAGE = "You're already registered!"