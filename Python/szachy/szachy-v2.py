#plansza kod
def create_board():
    """
    Funkcja tworząca planszę gry.

    Returns:
        list: Lista reprezentująca planszę gry.
    """

    board = [
        ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
        ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        ['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
        ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
    ]

    return board
#wyświetl plansze kod

def display_board(board):
    """
    Funkcja wyświetlająca planszę gry.

    Args:
        board (list): Lista reprezentująca planszę gry.
    """

    for row in board:
        for square in row:
            if square is None:
                print('   ', end='')
            else:
                print(square[:2] + ' ', end='')
        print()


#ruch hetmanem
def move_queen(board, start_pos, end_pos):
    """
    Funkcja przesuwająca hetmana na planszy na pole docelowe zgodnie z zasadami ruchu hetmana.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola startowego, na którym znajduje się hetman.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego, na którym ma zostać przesunięty hetman.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy pole docelowe znajduje się na planszy
    if end_pos[0] < 0 or end_pos[0] > 7 or end_pos[1] < 0 or end_pos[1] > 7:
        return False

    # Sprawdź, czy ruch jest wykonywany na przemianę pola białego i czarnego
    if (start_pos[0] + start_pos[1]) % 2 == (end_pos[0] + end_pos[1]) % 2:
        return False

    # Sprawdź, czy ruch jest wykonywany poziomo, pionowo lub po przekątnej
    if start_pos[0] != end_pos[0] and start_pos[1] != end_pos[1] and abs(start_pos[0] - end_pos[0]) != abs(start_pos[1] - end_pos[1]):
        return False

    # Sprawdź, czy nie ma przeszkód na drodze ruchu
    if start_pos[0] == end_pos[0]:
        for col in range(min(start_pos[1], end_pos[1]) + 1, max(start_pos[1], end_pos[1])):
            if board[start_pos[0]][col] is not None:
                return False
    elif start_pos[1] == end_pos[1]:
        for row in range(min(start_pos[0], end_pos[0]) + 1, max(start_pos[0], end_pos[0])):
            if board[row][start_pos[1]] is not None:
                return False
    else:
        dx = 1 if end_pos[0] > start_pos[0] else -1
        dy = 1 if end_pos[1] > start_pos[1] else -1
        x = start_pos[0] + dx
        y = start_pos[1] + dy
        while x != end_pos[0] and y != end_pos[1]:
            if board[x][y] is not None:
                return False
            x += dx
            y += dy

    # Wykonaj ruch
    board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None
    return True

#ruch krolem
def move_king(board, start_pos, end_pos):
    """
    Funkcja przesuwająca króla na planszy na pole docelowe zgodnie z zasadami ruchu króla.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola startowego, na którym znajduje się król.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego, na którym ma zostać przesunięty król.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy pole docelowe znajduje się na planszy
    if end_pos[0] < 0 or end_pos[0] > 7 or end_pos[1] < 0 or end_pos[1] > 7:
        return False

    # Sprawdź, czy ruch jest wykonywany na przemianę pola białego i czarnego
    if (start_pos[0] + start_pos[1]) % 2 == (end_pos[0] + end_pos[1]) % 2:
        return False

    # Sprawdź, czy ruch jest wykonywany o jedno pole w poziomie, pionie lub po przekątnej
    if abs(start_pos[0] - end_pos[0]) > 1 or abs(start_pos[1] - end_pos[1]) > 1:
        return False

    # Wykonaj ruch
    board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None
    return True

#ruch goncem
def move_bishop(board, start_pos, end_pos):
    """
    Funkcja przesuwająca gońca na planszy na pole docelowe zgodnie z zasadami ruchu gońca.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola startowego, na którym znajduje się goniec.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego, na którym ma zostać przesunięty goniec.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy pole docelowe znajduje się na planszy
    if end_pos[0] < 0 or end_pos[0] > 7 or end_pos[1] < 0 or end_pos[1] > 7:
        return False

    # Sprawdź, czy ruch jest wykonywany na przemianę pola białego i czarnego
    if (start_pos[0] + start_pos[1]) % 2 == (end_pos[0] + end_pos[1]) % 2:
        return False

    # Sprawdź, czy ruch jest wykonywany po przekątnej
    if abs(start_pos[0] - end_pos[0]) != abs(start_pos[1] - end_pos[1]):
        return False

    # Sprawdź, czy nie ma przeszkód na drodze ruchu
    dx = 1 if end_pos[0] > start_pos[0] else -1
    dy = 1 if end_pos[1] > start_pos[1] else -1
    x = start_pos[0] + dx
    y = start_pos[1] + dy
    while x != end_pos[0] and y != end_pos[1]:
        if board[x][y] is not None:
            return False
        x += dx
        y += dy

    # Wykonaj ruch
    board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None
    return True

#ruch koniem
def move_knight(board, start_pos, end_pos):
    """
    Funkcja przesuwająca skoczka na planszy na pole docelowe zgodnie z zasadami ruchu skoczka.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola startowego, na którym znajduje się skoczek.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego, na którym ma zostać przesunięty skoczek.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy pole docelowe znajduje się na planszy
    if end_pos[0] < 0 or end_pos[0] > 7 or end_pos[1] < 0 or end_pos[1] > 7:
        return False

    # Sprawdź, czy ruch jest wykonywany na przemianę pola białego i czarnego
    if (start_pos[0] + start_pos[1]) % 2 == (end_pos[0] + end_pos[1]) % 2:
        return False

    # Sprawdź, czy ruch jest wykonywany zgodnie z zasadami ruchu skoczka
    if abs(start_pos[0] - end_pos[0]) == 2 and abs(start_pos[1] - end_pos[1]) == 1:
        pass
    elif abs(start_pos[0] - end_pos[0]) == 1 and abs(start_pos[1] - end_pos[1]) == 2:
        pass
    else:
        return False

    # Wykonaj ruch
    board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None
    return True

#ruch wieza
def move_rook(board, start_pos, end_pos):
    """
    Funkcja przesuwająca wieżę na planszy na pole docelowe zgodnie z zasadami ruchu wieży.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola startowego, na którym znajduje się wieża.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego, na którym ma zostać przesunięta wieża.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy pole docelowe znajduje się na planszy
    if end_pos[0] < 0 or end_pos[0] > 7 or end_pos[1] < 0 or end_pos[1] > 7:
        return False

    # Sprawdź, czy ruch jest wykonywany na przemianę pola białego i czarnego
    if (start_pos[0] + start_pos[1]) % 2 == (end_pos[0] + end_pos[1]) % 2:
        return False

    # Sprawdź, czy ruch jest wykonywany w poziomie lub pionie
    if start_pos[0] != end_pos[0] and start_pos[1] != end_pos[1]:
        return False

    # Sprawdź, czy nie ma przeszkód na drodze ruchu
    if start_pos[0] == end_pos[0]:
        for col in range(min(start_pos[1], end_pos[1]) + 1, max(start_pos[1], end_pos[1])):
            if board[start_pos[0]][col] is not None:
                return False
    else:
        for row in range(min(start_pos[0], end_pos[0]) + 1, max(start_pos[0], end_pos[0])):
            if board[row][start_pos[1]] is not None:
                return False

    # Wykonaj ruch
    board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None
    return True

#ruch pionkiem
def move_pawn(board, start_pos, end_pos):
    """
    Funkcja przesuwająca pionek na planszy na pole docelowe zgodnie z zasadami ruchu pionka.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola startowego, na którym znajduje się pionek.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego, na którym ma zostać przesunięty pionek.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy pole docelowe znajduje się na planszy
    if end_pos[0] < 0 or end_pos[0] > 7 or end_pos[1] < 0 or end_pos[1] > 7:
        return False

    # Sprawdź, czy ruch jest wykonywany na przemianę pola białego i czarnego
    if (start_pos[0] + start_pos[1]) % 2 == (end_pos[0] + end_pos[1]) % 2:
        return False

    # Sprawdź, czy ruch jest wykonywany w poprawnym kierunku
    direction = -1 if board[start_pos[0]][start_pos[1]].color == 'w' else 1
    if end_pos[0] != start_pos[0] + direction:
        return False

    # Sprawdź, czy ruch jest wykonywany do przodu bez bicia
    if end_pos[1] == start_pos[1] and board[end_pos[0]][end_pos[1]] is None:
        board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
        board[start_pos[0]][start_pos[1]] = None
        return True

    # Sprawdź, czy ruch jest wykonywany do przodu z biciem
    if abs(end_pos[1] - start_pos[1]) == 1 and board[end_pos[0]][end_pos[1]] is not None:
        board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
        board[start_pos[0]][start_pos[1]] = None
        return True

    return False

#ruch 
def move_piece(board, start_pos, end_pos):
    """
    Funkcja wykonująca ruch dowolną figurą na planszy.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola, z którego ruch jest wykonywany.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego ruchu.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy na polu startowym znajduje się figura
    if board[start_pos[0]][start_pos[1]] is None:
        return False

    # Sprawdź, czy ruch jest zgodny z zasadami gry szachów
    if not is_valid_move(board, start_pos, end_pos):
        return False

    # Wykonaj ruch
    board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None
    return True

#szoszada
def castle(board, color, side):
    """
    Funkcja wykonująca ruch szachownicą dla króla i wieży podczas szachowania.

    Args:
        board (list): Lista reprezentująca planszę gry.
        color (str): Kolor gracza wykonującego ruch.
        side (str): Strona, po której król ma się przemieścić (może być 'K' lub 'Q').

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy król i wieża są na swoich pozycjach początkowych
    if color == 'white':
        row = 0
    else:
        row = 7
    if side == 'K':
        king_start = (row, 4)
        rook_start = (row, 7)
        king_end = (row, 6)
        rook_end = (row, 5)
    else:
        king_start = (row, 4)
        rook_start = (row, 0)
        king_end = (row, 2)
        rook_end = (row, 3)
    if board[king_start[0]][king_start[1]] != color + '_king' or board[rook_start[0]][rook_start[1]] != color + '_rook':
        return False

    # Sprawdź, czy król nie znajduje się w szachu
    if in_check(board, color):
        return False

    # Sprawdź, czy nie ma pionów ani innych figur na drodze ruchu
    if king_start[1] < king_end[1]:
        start = king_start[1]
        end = king_end[1] + 1
    else:
        start = king_end[1]
        end = king_start[1]
    for col in range(start, end):
        if board[king_start[0]][col] is not None or is_attacked(board, (king_start[0], col), opponent(color)):
            return False

    # Wykonaj ruch
    board[king_end[0]][king_end[1]] = board[king_start[0]][king_start[1]]
    board[king_start[0]][king_start[1]] = None
    board[rook_end[0]][rook_end[1]] = board[rook_start[0]][rook_start[1]]
    board[rook_start[0]][rook_start[1]] = None
    return True

#bicei w przelocie
def en_passant(board, start_pos, end_pos):
    """
    Funkcja wykonująca ruch bicia w przelocie.

    Args:
        board (list): Lista reprezentująca planszę gry.
        start_pos (tuple): Krotka zawierająca współrzędne pola startowego, na którym znajduje się pion.
        end_pos (tuple): Krotka zawierająca współrzędne pola docelowego, na którym ma zostać przesunięty pion.

    Returns:
        bool: Wartość True, jeśli ruch został wykonany pomyślnie, lub False, jeśli ruch był nielegalny.
    """

    # Sprawdź, czy ruch jest wykonywany na skos o jedno pole w lewo lub w prawo
    if abs(start_pos[1] - end_pos[1]) != 1:
        return False

    # Sprawdź, czy pion wykonuje ruch o dwie pola do przodu i czy na końcu ruchu znajduje się pion przeciwnika
    if (board[start_pos[0]][start_pos[1]].startswith('white') and start_pos[0] != 4) or \
       (board[start_pos[0]][start_pos[1]].startswith('black') and start_pos[0] != 3):
        return False
    if board[end_pos[0]][end_pos[1]] is not None:
        return False
    if board[start_pos[0]][end_pos[1]] is None or not board[start_pos[0]][end_pos[1]].startswith(opponent(board[start_pos[0]][start_pos[1]])):
        return False

    # Wykonaj ruch
    board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None
    board[start_pos[0]][end_pos[1]] = None
    return True

#promocja piona
def promote_pawn(board, pawn_pos, promote_to):
    """
    Funkcja wykonująca promocję piona.

    Args:
        board (list): Lista reprezentująca planszę gry.
        pawn_pos (tuple): Krotka zawierająca współrzędne pola, na którym znajduje się pion do promocji.
        promote_to (str): Nazwa figury, na którą ma zostać zamieniony pion.

    Returns:
        bool: Wartość True, jeśli promocja została wykonana pomyślnie, lub False, jeśli promocja była nielegalna.
    """

    # Sprawdź, czy pion znajduje się na końcu planszy
    if (board[pawn_pos[0]][pawn_pos[1]].startswith('white') and pawn_pos[0] != 7) or \
       (board[pawn_pos[0]][pawn_pos[1]].startswith('black') and pawn_pos[0] != 0):
        return False

    # Sprawdź, czy nazwa figury jest poprawna
    if promote_to not in ['queen', 'rook', 'bishop', 'knight']:
        return False

    # Zamień piona na wybraną figurę
    board[pawn_pos[0]][pawn_pos[1]] = board[pawn_pos[0]][pawn_pos[1]].replace('pawn', promote_to)
    return True

#wykrycie szacha 
def in_check(board, color):
    """
    Funkcja sprawdzająca, czy król danego koloru jest w szachu.

    Args:
        board (list): Lista reprezentująca planszę gry.
        color (str): Kolor króla, którego szachownica ma być sprawdzona.

    Returns:
        bool: Wartość True, jeśli król jest w szachu, lub False, jeśli nie jest.
    """

    # Znajdź pozycję króla danego koloru na planszy
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == color + '_king':
                king_pos = (row, col)
                break

    # Sprawdź, czy król jest atakowany przez jakąkolwiek figurę przeciwnika
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is not None and not board[row][col].startswith(color):
                if is_valid_move(board, (row, col), king_pos):
                    return True
    return False

#wykrycie mata
def in_checkmate(board, color):
    """
    Funkcja sprawdzająca, czy król danego koloru jest w matu.

    Args:
        board (list): Lista reprezentująca planszę gry.
        color (str): Kolor króla, którego szachownica ma być sprawdzona.

    Returns:
        bool: Wartość True, jeśli król jest w matu, lub False, jeśli nie jest.
    """

    # Sprawdź, czy król jest w szachu
    if not in_check(board, color):
        return False

    # Sprawdź, czy król może się uciec z szachu
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is not None and board[row][col].startswith(color):
                for move in generate_moves(board, (row, col)):
                    if not is_check_after_move(board, (row, col), move):
                        return False

    # Król jest w matu
    return True

#wykrycie remisu
def is_stalemate(board, color):
    """
    Funkcja sprawdzająca, czy aktualna pozycja na planszy prowadzi do remisu.

    Args:
        board (list): Lista reprezentująca planszę gry.
        color (str): Kolor gracza, którego sytuacja na planszy ma być sprawdzona.

    Returns:
        bool: Wartość True, jeśli aktualna pozycja na planszy prowadzi do remisu, lub False, jeśli nie prowadzi.
    """

    # Sprawdź, czy nie ma możliwych ruchów dla żadnej z figur gracza
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is not None and board[row][col].startswith(color):
                if generate_moves(board, (row, col)):
                    return False

    # Sprawdź, czy król danego koloru nie jest w szachu
    if in_check(board, color):
        return False

    # Jest to remis
    return True

#wykywanie konca gry
def is_game_over(board, color):
    """
    Funkcja sprawdzająca, czy gra się zakończyła.

    Args:
        board (list): Lista reprezentująca planszę gry.
        color (str): Kolor gracza, którego sytuacja na planszy ma być sprawdzona.

    Returns:
        str: Informacja o zakończeniu gry: 'checkmate', 'stalemate', 'insufficient material' lub 'not over'.
    """

    # Sprawdź, czy któryś z graczy jest w matu
    if in_checkmate(board, color):
        return 'checkmate'
    if in_checkmate(board, opponent(color)):
        return 'checkmate'

    # Sprawdź, czy aktualna pozycja na planszy prowadzi do remisu
    if is_stalemate(board, color):
        return 'stalemate'

    # Sprawdź, czy na planszy znajduje się wystarczająco mało figur, aby móc zakończyć grę
    if not has_sufficient_material(board):
        return 'insufficient material'

    # Gra nie jest jeszcze skończona
    return 'not over'

