import pandas as pd

from src.ncaa_site import BASE_URL


class Schedule:

    def __init__(self, schedule_df):
        self.schedule = schedule_df

    def get_game_links(self):
        return self.schedule["Game links"].tolist()

    def get_team_links(self):
        return self.schedule["Team links"].tolist()

    def __str__(self):
        return f"{self.schedule[['Date', 'Opponent', 'Result']]}"


def get_schedule(team_page_soup):
    full_table = team_page_soup.find("table")
    schedule_table = full_table.find("td").find("table")
    schedule = pd.read_html(str(schedule_table), header=1)[0]
    schedule = add_game_links(schedule, schedule_table)
    schedule = add_team_links(schedule, schedule_table)
    return Schedule(schedule)


def add_game_links(schedule, schedule_table):
    links = [link_tag["href"] for link_tag
             in schedule_table.find_all("a", class_="skipMask")]
    links.extend(["" for _ in range(len(schedule)-len(links))])
    links_series = pd.Series(links)
    schedule['Game links'] = links_series.values
    return schedule


def add_team_links(schedule, schedule_table):
    links = []
    for tr in schedule_table.find_all("tr"):
        a_tag = tr.find("a")
        if links and not a_tag:
            links.append("")
        elif a_tag:
            links.append(a_tag["href"])

    links_series = pd.Series(links)
    schedule["Team links"] = links_series.values
    return schedule
