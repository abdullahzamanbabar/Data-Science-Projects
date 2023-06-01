from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input('Where do you want to go?'))
        bot.select_dates(input("What is check in date? e.g.2023-06-15"), 
                         input("What is check out date? e.g.2023-06-30"))
        bot.select_adults(int(input("How many people?")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()
        bot.report_results()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise

