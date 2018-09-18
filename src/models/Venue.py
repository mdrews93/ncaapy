class Venue:

    def __init__(self, name, capacity, year_built):
        self.name = name
        self.capacity = capacity
        self.year_built = year_built

    def __repr__(self):
        return (f"{self.name} - Capacity: {self.capacity}, "
                f"built in {self.year_built}")


def get_venue(team_page_soup):
    venue_div = team_page_soup.find("div", {"id": "facility_div"})
    venue_div = venue_div.next_element.next_element.next_element.next_element
    contents = venue_div.contents[3].contents
    name = contents[2].strip()
    capacity = contents[6].strip()
    year_built = contents[10].strip()
    return Venue(name, capacity, year_built)
