from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from MatrixMusic import app

app = Client("xo_game")

# Dictionary to store game data for each chat
games = {}

# Function to check for a winner
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Function to display the game board
def display_board(board):
    return "\n".join([" | ".join(row) for row in board])

@app.on_message(filters.command("startgame", [".", "/"]))
async def start_game(client, message):
    chat_id = message.chat.id
    games[chat_id] = {
        "board": [[" " for _ in range(3)] for _ in range(3)],
        "player": "X",
        "turn": message.from_user.id,
    }
    await message.reply_text(f"Game started! {message.from_user.first_name} goes first.\n{display_board(games[chat_id]['board'])}")

@app.on_callback_query(filters.regex(r'^xo \d$'))
async def play(client, callback_query):
    chat_id = callback_query.message.chat.id
    game = games.get(chat_id)
    if not game or game['turn'] != callback_query.from_user.id:
        await callback_query.answer("It's not your turn!")
        return
    move = int(callback_query.data.split()[1])
    row, col = (move-1) // 3, (move-1) % 3
    if game['board'][row][col] == " ":
        game['board'][row][col] = game['player']
        winner = check_winner(game['board'])
        if winner:
            await callback_query.message.reply_text(f"{game['player']} wins!\n{display_board(game['board'])}")
            del games[chat_id]
            return
        if all(all(cell != " " for cell in row) for row in game['board']):
            await callback_query.message.reply_text("It's a draw!\nGame over.")
            del games[chat_id]
            return
        game['player'] = "O" if game['player'] == "X" else "X"
        game['turn'] = callback_query.from_user.id
        await callback_query.message.edit_text(f"{game['player']}'s turn.\n{display_board(game['board'])}")
    else:
        await callback_query.answer("Invalid move!")

@app.on_message(filters.command("اكس او", [".", "/"]))
async def xo_command(client, message):
    buttons = [
        [
            InlineKeyboardButton("1", callback_data="xo 1"),
            InlineKeyboardButton("2", callback_data="xo 2"),
            InlineKeyboardButton("3", callback_data="xo 3"),
        ],
        [
            InlineKeyboardButton("4", callback_data="xo 4"),
            InlineInlineKeyboardButton("5", callback_data="xo 5"),
            InlineKeyboardButton("6", callback_data="xo 6"),
        ],
        [
            InlineKeyboardButton("7", callback_data="xo 7"),
            InlineKeyboardButton("8", callback_data="xo 8"),
            InlineKeyboardButton("9", callback_data="xo 9"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text("≭︰اهلا بك في لعبة X - O .\n≭︰اول شخص سيقوم بالضغط على زر بدأ اللعب سوف يلعب مع", reply_markup=reply_markup)
