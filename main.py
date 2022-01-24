from game_stage import *

'''
    To Start The Game, Call the Main Menu Function.
'''
if cacheData.check_cached_data():
    main_menu(constant.SelectOption)
else:
    print("Error While Loading the Game Data From File")
