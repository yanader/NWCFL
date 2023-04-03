
def dictionary_processor(gameday:dict):
    daily_fixtures_list = []
    for k, v in gameday.items():
        for match in v:
            teams = match.split(' - ')
            daily_fixtures_list.append([k, teams[0], teams[1], []])
    return daily_fixtures_list

def formatted_list(gameday: dict):
    formatted_return_list = []
    for k, v in gameday.items():
        for match in v:
            teams = match.split(' - ')
            formatted_return_list.append([teams[0], ' - ', teams[1]])
    return formatted_return_list


    ##this needs to receive a dictionary and format it so that it contains info on:
    # 1 Home Team
    # 2 Away Team
    # 3 Space for a list of reported scores
    # 4 do I also want to have a note for which league it's in?