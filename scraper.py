from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


search_url = "https://opendata.arcgis.com/api/v2/datasets?filter%5Bcatalogs%5D=data-moray.opendata.arcgis.com&include=organizations%2Cgroups&page%5Bnumber%5D=1&page%5Bsize%5D=10&q=polling&sort=-updatedAt"
stations_url = "https://opendata.arcgis.com/datasets/65e731a73f384fadad25bef39fdcc342_0.geojson"
districts_url = "https://opendata.arcgis.com/datasets/bd878bfec39f4a659c2d016f1b3bc920_1.geojson"
council_id = 'S12000020'


search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape()
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
