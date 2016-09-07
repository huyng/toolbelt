# install https://github.com/huyng/foogle
from foogle import google
results = google.search_images("celebrities")
for r in results:
        print r.link
