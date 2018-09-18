from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from src.models.Coach import get_coach
from src.models.Venue import get_venue
from src.models.Schedule import get_schedule


class Team:

    def __init__(self, team_id, name, coach, venue, schedule):
        self.team_id = team_id
        self.name = name
        self.coach = coach
        self.venue = venue
        self.schedule = schedule

    def get_coach(self):
        return self.coach

    def get_venue(self):
        return self.venue

    def get_schedule(self):
        return self.schedule

    def __repr__(self):
        return f"{self.name} ({self.team_id})"


def get_team(team_id):
    req = Request(f"https://stats.ncaa.org/teams/{team_id}",
                  headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req).read()
    soup = BeautifulSoup(resp, "lxml")

    team = Team(team_id=team_id,
                name=get_team_name(soup),
                coach=get_coach(soup),
                venue=get_venue(soup),
                schedule=get_schedule(soup))

    return team


def get_team_name(team_page_soup):
    return team_page_soup.find("legend").a.text
