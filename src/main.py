from src.models.Team import get_team


team = get_team(449711)
print(team)
print(team.get_coach())
print(team.get_venue())
print(team.get_schedule())
