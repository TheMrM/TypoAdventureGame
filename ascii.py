#ascii art for the game

castle = """
   /\                                                        /\\
  |  |                                                      |  |
 /----\\                  Lord Dark's Keep                  /----\\
[______]             Where Brave Knights Tremble          [______]
 |    |         _____                        _____         |    |
 |[]  |        [     ]                      [     ]        |  []|
 |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
 |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
 |             |     |/'    ____..____    '\\|     |             |
  \\  []        |     |    /'    ||    '\\    |     |        []  //
   |      []   |     |   |o     ||     o|   |     |  []       |
   |           |  _  |   |     _||_     |   |  _  |           |
   |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
   |           |     |   |     (||)     |   |     |           |
   |           |     |   |      ||      |   |     |           |
 /''           |     |   |o     ||     o|   |     |           ''\\
[_____________[_______]--'------''------'--[_______]_____________]
"""

map = """
+-----------------------+
|                       |
|                       |
|                       |
|                       |
|                       |
|                       |
|                       |
|     You are here      |
|          X            |
+-----------------------+
"""
map_forest = """
+-----------------------+
|                       |
|                       |
|                       |
|                       |
|                       |
|Forest___              |
|         Y             |
|         |             |
|         X             |
+-----------------------+
"""
map_cemetery = """
+-----------------------+
|                       |
|                       |
|                       |
|                       |
|               cemetery|
|          _____x x x x |
|         Y             |
|         |             |
|         X             |
+-----------------------+
"""
map_forest_1 = """
+-----------------------+
|    |Dragon Laire|     |
|      /                |
|     |                 |
|     |                 |
|Forest                 |
| ? ? ?___              |
|         Y             |
|         |             |
|         X             |
+-----------------------+
"""
map_cemetery_1 = """
+-----------------------+
|    |Dragon Laire|     |
|                \      |
|                 |     |
|                 |     |
|               Cemetery|
|          _____x x x x |
|         Y             |
|         |             |
|         X             |
+-----------------------+
"""
map_finish = """
+-----------------------+
|    |Dragon Laire|     |
|      /         \      |
|     |           |     |
|     |           |     |
|Forest         Cemetery|
| ? ? ?___ _____x x x x |
|         Y             |
|         |             |
|         X             |
+-----------------------+
"""

import time

dragon = '''
            \||/
            |  @___oo
  /\  /\   / (__,,,,|
 ) /^\) ^\/ _)
 )   /^\/   _)
 )   _ /  / _)
/\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\\
 | \____(      )___) )___)
  \______(_______;;; __;;;
'''

fire = '''
                              .
                            \ | /
                          '-.;;;.-'
                        -==; _ ;==-
                          / | \\
                            ' '
'''

ghost = '''
       .-^-.
      /_/_\_\\
'\\'\\)     (/ /'/' 
        '-`-'  
'''

sword = '''
    () 
   __)(__
   '-<>-'
     )(   __
     ||  / \\
     || (  ||)
     || ]_(\,|
     || ]-->/|
     || (  ||)
     ||  \_//
     ||
     ||  
     \/

'''


bow = '''
    (
     )
 ##-------->
     )
    /
   (
'''
forest = '''
     ^  ^  ^   ^    ^  ^   ^  ^  ^   ^  ^
    /|\/|\/|\ /|\  /|\/|\ /|\/|\/|\ /|\/|
    /|\/|\/|\ /|\  /|\/|\ /|\/|\/|\ /|\/|
    /|\/|\/|\ /|\  /|\/|\ /|\/|\/|\ /|\/|
'''
skull = '''
|     '       /  |    |             /  |
     /__      ___ (  /     /__   Y  __  (  _/
     \\--`-'-|`---\\ |     \`--`-'-|`---\\/
      |' _/   ` __/ /       |'__/   ` __/ |
      '._  W    ,--'        '-.   w   ,--/
         |_:_._/              |'_._._/  /
                              |________/
'''

spider = '''
    .  .
   .|  |.
   ||  ||
   \\\()//
   .={}=.
  / /`'\ \\
  ` \  /  '
     `'
'''