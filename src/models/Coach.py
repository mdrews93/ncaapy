class Coach:

    def __init__(self, name, alma_mater="N/A", seasons="N/A", record="N/A"):
        self.name = name
        self.alma_mater = alma_mater
        self.seasons = seasons
        self.record = record

    def __repr__(self):
        return (f"{self.name} ({self.alma_mater}): " 
                f"{self.seasons} season(s) ({self.record})")


def get_coach(team_page_soup):
    coach_div = team_page_soup.find("div", {"id": "head_coaches_div"})
    contents = coach_div.contents[1].contents
    name = contents[5].text
    alma_mater = contents[9].strip()
    seasons = contents[13]
    record = contents[17].strip()

    return Coach(name, alma_mater, seasons, record)
