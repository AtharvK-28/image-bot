from duckduckgo_search import DDGS

class ImageSearch:
    def search_images(self, query, max_results=5):
        results = []
        with DDGS() as ddgs:
            for r in ddgs.images(query):
                if 'image' in r:
                    results.append(r['image'])
                if len(results) >= max_results:
                    break
        return results