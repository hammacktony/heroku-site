def test_sources_import():
    ''' Application should be able to import Masonite modules '''
    from mods.scrape.sources import sources
    if len(sources) > 0:
        assert True 
    else:
        assert False, "Error importing webscraping sources file."

def test_sources_import():
    ''' Application should be able to import Masonite modules '''
    from mods.scrape.search_criterion import criterion
    if len(criterion) > 0:
        assert True 
    else:
        assert False, "Error importing webscraping sources file."

