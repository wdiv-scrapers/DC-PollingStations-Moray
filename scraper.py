from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


search_url = "https://opendata.arcgis.com/api/v3/datasets?q=polling&filter%5Bowner%5D=gis_moray"
stations_url = "https://opendata.arcgis.com/datasets/65e731a73f384fadad25bef39fdcc342_0.geojson"
districts_url = "https://opendata.arcgis.com/datasets/bd878bfec39f4a659c2d016f1b3bc920_1.geojson"
council_id = 'MRY'

search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape(exclude_keys=['meta'])
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
