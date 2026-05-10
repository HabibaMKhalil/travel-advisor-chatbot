DESTINATION_BASE_URLS = [
    "https://en.wikivoyage.org/wiki/Paris",
    "https://en.wikivoyage.org/wiki/Rome",
    "https://en.wikivoyage.org/wiki/Berlin",
    "https://en.wikivoyage.org/wiki/Madrid",
    "https://en.wikivoyage.org/wiki/Tokyo",
    "https://en.wikivoyage.org/wiki/Cairo",
    "https://en.wikivoyage.org/wiki/London",
    "https://en.wikivoyage.org/wiki/New_York_City",
    "https://en.wikivoyage.org/wiki/Sydney",
    "https://en.wikivoyage.org/wiki/Dubai",
]

TRAVEL_TIPS_URLS = [
    "https://en.wikivoyage.org/wiki/Stay_safe",
    "https://en.wikivoyage.org/wiki/Health",
    "https://en.wikivoyage.org/wiki/Get_in"
]

REGION_PAGES = [
    "https://en.wikivoyage.org/wiki/Europe",
    "https://en.wikivoyage.org/wiki/Asia",
    "https://en.wikivoyage.org/wiki/Africa",
    "https://en.wikivoyage.org/wiki/North_America",
    "https://en.wikivoyage.org/wiki/South_America"
]

MAX_DESTINATIONS = 50   # My medium sized dataset ( possibly size up later )
HEADERS = {
    "User-Agent": "TravelAdvisorBot/1.0 (Educational NLP Project)"
}

REQUEST_DELAY = 2
MAX_RETRIES = 2


ALLOWED_TAGS = ["h1", "h2", "h3", "p", "ul", "li"]

EXCLUDED_PATTERNS = [
    "/wiki/File:",
    "/wiki/Category:",
    "/wiki/User:",
    "?action="
]
